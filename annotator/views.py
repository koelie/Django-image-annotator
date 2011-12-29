from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
import glob
from django.conf import settings
import random

def index(request):
    num_images = Image.objects.count()
    labels = {}
    for label in Label.objects.all():
        labels[label.name] = label.annotation_set.count()

    return render_to_response('index.html', {'num_images': num_images, 'labels': labels}, context_instance=RequestContext(request))


def annotate(request, labelname):
    label = get_object_or_404(Label, name=labelname)
    message = ''
    if request.method == 'POST':

        try:
            img = get_object_or_404(Image, pk=request.POST.get('image_id',-1))

            if Annotation.objects.filter(image=img).filter(label=label).count() > 0:
                message = "Error storing annotation, image already annotated for the label " + label.name
            else:
                area = [int(request.POST.get(c)) for c in ['x1','x2','y1','y2']]
                value = label.labelvalue_set.get(value=request.POST.get('value'))

                annotation = Annotation()
                annotation.image = img
                annotation.label = label
                annotation.area_x1 = area[0]
                annotation.area_x2 = area[1]
                annotation.area_y1 = area[2]
                annotation.area_y2 = area[3]
                annotation.value = value
                annotation.save()
                message = "Annotation saved succesfully"
        except:
            message = "Error storing the annotation"        

    unannotated = Image.objects.exclude(annotation__label=label)
    if unannotated.count() == 0:
        return render_to_response('done.html', {}, context_instance=RequestContext(request))
        
    image = random.sample(unannotated, 1)[0]
    return render_to_response('annotate.html', {'image': image, 'label':label, 'msg':message,
        'num_left': unannotated.count()}, context_instance=RequestContext(request))

def scan(request):
    path = settings.MEDIA_ROOT + settings.IMAGE_PATH
    files = glob.glob("%s/*.jpg" % path)
    for f in files:
        fn = f.replace(settings.MEDIA_ROOT, '')
        num=Image.objects.filter(image = fn).count()
        if num == 0:
            img = Image()
            img.image = fn
            img.save()

    return index(request)
