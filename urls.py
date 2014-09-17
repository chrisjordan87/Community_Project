from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('apps.jobs.urls', namespace='jobs')),
                       # url(r'^blog/', include('blog.urls')),

)
