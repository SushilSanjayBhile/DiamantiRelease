from django.urls import path

from .views import (TCSTATUSGETPOSTVIEW, USER_INFO_GET_POST_VIEW,
        USER_INFO_SPECIFIC_BY_ID, USER_INFO_SPECIFIC_BY_NAME, LOG,
        GETSETUPWISETCINFO, RELEASEINFO, RELEASEINFOPOST,
        TCAGGREGATE, USER_LOGIN_VIEW)

#from .views import (TCSTATUSGETPOSTVIEW, USER_INFO_GET_POST_VIEW,
#        USER_INFO_SPECIFIC_BY_ID, USER_INFO_SPECIFIC_BY_NAME, LOG,
#        GETSETUPWISETCINFO, RELEASEINFO, GETPLATFORMWISETCINFO, RELEASEINFOPOST,
#        GETPLATFORMANDSETUPWISETCINFO, TCAGGREGATE, USER_LOGIN_VIEW)

from .guiviews import GUITCSTATUSGETPOSTVIEW

#from .views import DOMAINWISETCINFO, DOMAINWISETCSTATUS 
from .tcinfo import (TC_INFO_GET_POST_VIEW, GET_TC_INFO_BY_ID, WHOLE_TC_INFO,
	MULTIPLE_TC_UPDATION, UPDATE_TC_INFO_BY_ID, TcCountByFilter, WHOLE_GUI_TC_INFO)
from .createDB import createDB
from .sanity import SANITY_VIEW

#from .tcinfo import TC_INFO_GET_POST_VIEW, TC_INFO_BY_ID, WHOLE_TC_INFO, MULTIPLE_TC_UPDATION, TC_INFO_BY_ID, TcCountByFilter, WHOLE_GUI_TC_INFO

urlpatterns = [
    path('tcstatus/<str:Release>', TCSTATUSGETPOSTVIEW),
    path('guitcstatus/<str:Release>', GUITCSTATUSGETPOSTVIEW),
    #path('<str:Release>/tcstatus/domain/<str:Domain>', DOMAINWISETCSTATUS),

    path('tcinfo/<str:Release>', TC_INFO_GET_POST_VIEW),
    path('tccount/<str:Release>', TcCountByFilter),
    #path('<str:Release>/tcinfo/domain/<str:Domain>', DOMAINWISETCINFO),
    path('tcupdate/<str:Release>', MULTIPLE_TC_UPDATION),

    path('tcinfo/<str:Release>/id/<str:id>/card/<str:card>', GET_TC_INFO_BY_ID),
    path('tcinfoput/<str:Release>/id/<str:id>/card/<str:card>', UPDATE_TC_INFO_BY_ID),
    #path('tcinfo/<str:Release>/id/<str:id>/card/<str:card>', TC_INFO_BY_ID),

    path('wholetcinfo/<str:Release>', WHOLE_TC_INFO),
    path('wholeguitcinfo/<str:Release>', WHOLE_GUI_TC_INFO),

    path('sanity/<str:SanityType>/<str:Release>', SANITY_VIEW),

    path('user/login', USER_LOGIN_VIEW),
    path('userinfo/', USER_INFO_GET_POST_VIEW),
    path('user/id/<int:id>/', USER_INFO_SPECIFIC_BY_ID),
    path('user1/name/<str:email>/', USER_INFO_SPECIFIC_BY_NAME),

    path('logs/<str:Release>', LOG),

    path('tcinfosetupwise/<str:SetupName>/', GETSETUPWISETCINFO),
    #path('tcinfoplatformwise/<str:OrchestrationPlatform>/', GETPLATFORMWISETCINFO),
    #path('platformandsetupwise/<str:OrchestrationPlatform>/<str:SetupName>/', GETPLATFORMANDSETUPWISETCINFO),

    path('release/<str:Release>', RELEASEINFO),
    path('release', RELEASEINFOPOST),
]
