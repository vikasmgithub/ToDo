from django.conf.urls import url
from .views import TM_List,TM_Detail
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


urlpatterns = [
	url(r'^api-token-auth/', obtain_jwt_token), 
	url(r'^api-token-refresh/', refresh_jwt_token),
	url(r'^api-token-verify/', verify_jwt_token),	
    url(r'^taskmanager/$', TM_List.as_view()),
    url(r'^taskmanager/(?P<pk>[0-9]+)/$',TM_Detail.as_view()),
]



urlpatterns = format_suffix_patterns(urlpatterns)