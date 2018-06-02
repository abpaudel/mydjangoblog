from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
	 url(r'^locate/$', views.Locate.as_view()),
	 url(r'^adtobs/$', views.AD_BS.as_view()),
	 url(r'^bstoad/$', views.BS_AD.as_view()),
	 url(r'^sudoku/$', views.SudokuSolver.as_view()),
	 url(r'^dump/$', views.Dump.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)