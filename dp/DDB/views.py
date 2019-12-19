from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json, datetime
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from django.db.models import ProtectedError

from DDB.serializers import TC_INFO_SERIALIZER, TC_STATUS_SERIALIZER, USER_SERIALIZER, LOG_SERIALIZER, \
    RELEASE_SERIALIZER
from .models import TC_INFO, TC_STATUS, USER_INFO, LOGS, RELEASES
from .forms import TcInfoForm, TcStatusForm, UserInfoForm, LogForm, ReleaseInfoForm
from django.views.generic import UpdateView



@csrf_exempt
def TCSTATUSGETPOSTVIEW(request):

    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        fd = TcStatusForm(req)
        if fd.is_valid():
            fd.save()
        else:
            print(req, fd.errors)
        return HttpResponse(fd.errors)

    elif request.method == "GET":

        dict = {}
        list1 = []
        data = TC_STATUS.objects.all()
        serializer = TC_STATUS_SERIALIZER(data, many=True)
        for i in serializer.data:
            a = TC_STATUS.data.all()
            print(a)
            d = json.dumps(i)
            d = json.loads(d)

            data = TC_INFO.objects.filter(TcID = d['TcID'])
            s = TC_INFO_SERIALIZER(data,many = True)
            s = json.dumps(s.data)
            s = json.loads(s)
            domain = s[0]['Domain']
            subdomain = s[0]['SubDomain']
            d['Domain'] = domain
            d['SubDomain'] = subdomain
            list1.append(d)
        return HttpResponse(json.dumps(list1))

@csrf_exempt
def USER_INFO_GET_POST_VIEW(request):
    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        fd = UserInfoForm(req)
        if fd.is_valid():
            fd.save()
        else:
            print(req)
            print(fd.errors())
        GenerateLogData(1, 'POST', 'specificuserbyid/' + str(id) + " => " + json.dumps(req))
        return HttpResponse(fd.errors)
    else:
        data = USER_INFO.objects.all()
        serializer = USER_SERIALIZER(data, many = True)
        return HttpResponse(json.dumps(serializer.data))

def USER_INFO_SPECIFIC_BY_ID(request, id):
    data = USER_INFO.objects.using('users').get(UserId = id)
    serializer = USER_SERIALIZER(data)
    GenerateLogData(6, 'GET', 'specificuserbyid/' + str(id) + " => " + json.dumps(serializer.data))
    return HttpResponse(json.dumps(serializer.data))

def USER_INFO_SPECIFIC_BY_NAME(request, uname):
    data = USER_INFO.objects.filter(UserName__icontains = uname)
    serializer = USER_SERIALIZER(data, many=True)
    return HttpResponse(json.dumps(serializer.data))


@require_http_methods(["GET"])
@csrf_exempt
def LOG(request):
    data = LOGS.objects.all()
    serializer = LOG_SERIALIZER(data, many = True)
    return HttpResponse(json.dumps(serializer.data))

def GenerateLogData(UserID, RequestType, logData):
    Logs = json.dumps(logData)
    Timestamp = datetime.datetime.now()
    data = {'UserID': UserID, 'RequestType': RequestType, 'Logs': logData, 'Timestamp': Timestamp}
    fd = LogForm(data)
    if fd.is_valid():
        fd.save()
    else:
        print("INVALID", fd.errors)


# class CategoryFilter(filters.FilterSet):
#     category = filters.CharFilter(lookup_expr='icontains')

#     class Meta:
#         model = TC_INFO
#         fields = '__all__'

list1 = {}
list2 = {}

def GETSETUPWISETC(request, SetupName):
    global list1
    tccounter = 0
    c = 0

    data = TC_INFO.objects.filter(Setup__icontains = SetupName)
    serializer = TC_INFO_SERIALIZER(data, many=True)
    d = json.dumps(serializer.data)
    d = json.loads(d)
    for i in range(len(d)):
        co = (d[i]['Setup']).count(SetupName)
        c += co
    print(SetupName, c)

    tccounter = 0
    data = TC_INFO.objects.all()
    serializer = TC_INFO_SERIALIZER(data, many=True)
    d = json.dumps(serializer.data)
    d = json.loads(d)
    print("row count of tc in db",len(d))
    for i in range(len(d)):
        tccounter += len(d[i]['Setup'])
    print("all tcs with addded setups", tccounter)

    return HttpResponse(json.dumps(serializer.data))

@csrf_exempt
def RELEASEINFOPOST(request):
    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        fd = ReleaseInfoForm(req)
        if fd.is_valid():
            fd.save()
        else:
            print(fd.errors)
        # GenerateLogData(1, 'POST', 'specificuserbyid/' + str(id) + " => " + json.dumps(req))
        return HttpResponse(fd.errors)


@csrf_exempt
def RELEASEINFO(request, Release):
    if request.method == "GET":
        if(Release == 'all'):
            data = RELEASES.objects.all()
            serializer = RELEASE_SERIALIZER(data, many = True)
            return HttpResponse(json.dumps(serializer.data))
        else:
            data = RELEASES.objects.filter(ReleaseNumber__icontains = Release)
            serializer = RELEASE_SERIALIZER(data, many = True)
            return HttpResponse(json.dumps(serializer.data))

    elif request.method == "DELETE":
        try:
            data = RELEASES.objects.get(ReleaseNumber__icontains = Release).delete()
            return HttpResponse("DELETED SUCCESSFULLY")
        except RELEASES.DoesNotExist:
            error_message = "OBJECT NOT PRESENT CANNOT BE DELETED!!"
            return HttpResponse(error_message)

    elif request.method == "PUT":
        try:
            req = json.loads(request.body.decode("utf-8"))
            data = RELEASES.objects.get(ReleaseNumber__icontains = Release)
            serializer = RELEASE_SERIALIZER(data, data=req)
            print(req, serializer)
            if serializer.is_valid():
                print("VALID")
                serializer.save()
            else:
                print("INVALID")
                print(serializer.errors)
            print("SUCCESS")
            return HttpResponse("SUCCESS")
        except:
            print("FAILURE")
            return HttpResponse("SOME ERROR OCCURED")

    # elif request.method == "POST":
    #     try:
    #         data = RELEASES.objects.get(ReleaseNumber__icontains = Release)
    #         serializer = RELEASE_SERIALIZER(data, data=request.data)

    #         if serializer.is_valid():
    #             serializer.save()
    #         return HttpResponse(json.dumps(serializer))
    #     except:
    #         pass

            
def GETPLATFORMWISETC(request, OrchestrationPlatform):
    data = TC_INFO.objects.filter(OrchestrationPlatform__icontains = OrchestrationPlatform)
    serializer = TC_INFO_SERIALIZER(data, many=True)
    print("orchestartion platform name: ", OrchestrationPlatform, "number of TCs: ", len(serializer.data))
    return HttpResponse(json.dumps(serializer.data))


def GETPLATFORMANDSETUPWISETC(request, OrchestrationPlatform, SetupName):
    data = TC_INFO.objects.filter(CardType__icontains = SetupName, OrchestrationPlatform__icontains = OrchestrationPlatform)
    serializer = TC_INFO_SERIALIZER(data, many=True)
    print("Setupname: ", SetupName, "orchestartion platform name: ", OrchestrationPlatform, "number of TCs: ", len(serializer.data))
    return HttpResponse(json.dumps(serializer.data))
