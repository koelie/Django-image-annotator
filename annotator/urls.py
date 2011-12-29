from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'annotator.views.index', name='annotator_index'),
    url(r'^annotate/(?P<labelname>.*)/', 'annotator.views.annotate', name='annotator_annotate'),
    url(r'^scan/', 'annotator.views.scan', name='annotator_scan'),
    
    # Examples:
    # url(r'^$', 'django_annotator.views.home', name='home'),
    # url(r'^django_annotator/', include('django_annotator.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


