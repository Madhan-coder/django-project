from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    (r'^', include('prajact.project.urls')),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
