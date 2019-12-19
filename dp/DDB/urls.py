from django.urls import path
from .views import TCSTATUSGETPOSTVIEW, USER_INFO_GET_POST_VIEW, USER_INFO_SPECIFIC_BY_ID, USER_INFO_SPECIFIC_BY_NAME, LOG, \
    GETSETUPWISETC, RELEASEINFO, GETPLATFORMWISETC, RELEASEINFOPOST, GETPLATFORMANDSETUPWISETC

from .tcinfo import TC_INFO_GET_POST_VIEW, SPECIFIC_TC_INFO_BY_NAME, SPECIFIC_TC_INFO_BY_ID

urlpatterns = [
    path('tcinfo/', TC_INFO_GET_POST_VIEW),
    path('tcstatus/', TCSTATUSGETPOSTVIEW),
    path('tcinfo/name/<str:name>/', SPECIFIC_TC_INFO_BY_NAME),
    path('tcinfo/id/<str:id>/', SPECIFIC_TC_INFO_BY_ID),
    path('userinfo/', USER_INFO_GET_POST_VIEW),
    path('user/id/<int:id>/', USER_INFO_SPECIFIC_BY_ID),
    path('user/name/<str:uname>/', USER_INFO_SPECIFIC_BY_NAME),
    path('logs/', LOG),
    path('setupwise/<str:SetupName>/', GETSETUPWISETC),
    path('platformwise/<str:OrchestrationPlatform>/', GETPLATFORMWISETC),
    path('platformandsetupwise/<str:OrchestrationPlatform>/<str:SetupName>/', GETPLATFORMANDSETUPWISETC),
    path('release/<str:Release>', RELEASEINFO),
    path('release', RELEASEINFOPOST),
]
