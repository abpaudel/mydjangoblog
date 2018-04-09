from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
	 url(r'^locate/$', views.LocationList.as_view()),
	 url(r'^locate/district/(?P<district>.+)/$', views.LocationSpecific.as_view()),
	 url(r'^locate/zone/(?P<zone>.+)/$', views.LocationSpecific.as_view()),
	 url(r'^locate/region/(?P<region>.+)/$', views.LocationSpecific.as_view()),
	 url(r'^adtobs/$', views.AD_BS.as_view()),
	 url(r'^bstoad/$', views.BS_AD.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)