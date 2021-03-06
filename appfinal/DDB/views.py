# Django packages
from django.db.models import Q
from django.shortcuts import render
# # from django.http import HttpResponse, JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# imports from django app
from .models import TC_INFO, TC_STATUS, USER_INFO, LOGS, RELEASES, AGGREGATE_TC_STATE
from .forms import TcInfoForm, TcStatusForm, UserInfoForm, LogForm, ReleaseInfoForm, AggregationForm
from DDB.serializers import TC_INFO_SERIALIZER, TC_STATUS_SERIALIZER, USER_SERIALIZER, LOG_SERIALIZER, \
    RELEASE_SERIALIZER, AGGREGATION_SERIALIZER
from .aggregation import TCAGGREGATE

# Third party softwares / libraries
import gzip
import psycopg2
from sh import pg_dump
from psycopg2 import sql
import json, datetime, os, time
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

@csrf_exempt
def TCSTATUSGETPOSTVIEW(request, Release):
    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        if "Activity" in req:
            AD = req['Activity']
            GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])

        data = TC_INFO.objects.using(Release).filter(TcID = req['TcID'])
        serializer = TC_INFO_SERIALIZER(data, many = True)
        data = json.dumps(serializer.data)
        data = json.loads(data)
        try:
            req['TcName'] = data[0]['TcName']
        except:
            req['TcName'] = data['TcName']

        fd = TcStatusForm(req)
        if fd.is_valid():
            data = fd.save(commit = False)
            data.save(using = Release)
        else:
            print(req, fd.errors)
        # return JsonResponse({'Error': fd.errors}, status = 400)
        return HttpResponse(fd.errors)

    elif request.method == "GET":
        data = TC_STATUS.objects.using(Release).all().order_by('TcID')
        serializer = TC_STATUS_SERIALIZER(data, many=True)
        # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)
        return HttpResponse(json.dumps(serializer.data))

"""
@csrf_exempt
def DOMAINWISETCSTATUS(request, Release, Domain):
    if request.method == "GET":
        AllInfoData = []

        infodata = TC_INFO.objects.using(Release).filter(Domain = Domain)
        if Domain == "GUI":
            statusdata = TC_STATUS_GUI.objects.using(Release).filter(Domain = Domain)
            statusserializer = TC_STATUS_GUI_SERIALIZER(statusdata, many=True)
        else:
            statusdata = TC_STATUS.objects.using(Release).filter(Domain = Domain)
            statusserializer = TC_STATUS_SERIALIZER(statusdata, many=True)

        infoserializer = TC_INFO_SERIALIZER(infodata, many = True)

        d = json.dumps(statusserializer.data)
        d = json.loads(d)

        for info in infoserializer.data:
            stat = {}
            stat['TcID'] = info['TcID']
            stat['TcName'] = info['TcName']
            stat['Build'] = ''
            stat['Result'] = 'Not Tested'
            stat['Bugs'] = ''
            stat['Date'] = ''
            stat['Domain'] = info['Domain']
            stat['SubDomain'] = info['SubDomain']
            stat['CardType'] = info['CardType']

            try:
                for status in d:
                    if status['TcID'] == info['TcID'] and status['CardType'] == info['CardType']:
                        stat = status
                        d.remove(status)
                        AllInfoData.append(stat)
            except:
                pass
            AllInfoData.append(stat)
        return HttpResponse(json.dumps(AllInfoData))

@csrf_exempt
def DOMAINWISETCINFO(request, Release, Domain):
    if request.method == "GET":
        data = TC_INFO.objects.using(Release).filter(Domain = Domain)
        serializer = TC_INFO_SERIALIZER(data, many=True)
        # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)
        return HttpResponse({len(serializer.data), json.dumps(serializer.data)})
"""

# @csrf_exempt
# def DEFAULT_VALUE_SETTER_GETTER(request):
#     if request.method == "POST":
        

@csrf_exempt
def USER_INFO_GET_POST_VIEW(request):
    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        fd = UserInfoForm(req)
        if fd.is_valid():
            fd.save()
            if "Activity" in req:
                AD = req['Activity']
                GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
        else:
            print(req)
            print(fd.errors)
        # GenerateLogData(1, 'POST', 'specificuserbyid/' + str(id) + " => " + json.dumps(req))
        # return JsonResponse({'Error': fd.errors}, status = 400)
        return HttpResponse(fd.errors)
    else:
        # data = USER_INFO.objects.using(req['ReleaseNumber']).all()
        data = USER_INFO.objects.all()
        serializer = USER_SERIALIZER(data, many = True)
        # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)
        return HttpResponse(json.dumps(serializer.data))

def USER_INFO_SPECIFIC_BY_ID(request, id):
    data = USER_INFO.objects.using('users').get(UserId = id)
    serializer = USER_SERIALIZER(data)
    #GenerateLogData(6, 'GET', 'specificuserbyid/' + str(id) + " => " + json.dumps(serializer.data))
    # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)
    return HttpResponse(json.dumps(serializer.data))

@csrf_exempt
def USER_INFO_SPECIFIC_BY_NAME(request, email):
    if request.method == "GET":
    	data = USER_INFO.objects.filter(email__icontains = email)
    	serializer = USER_SERIALIZER(data, many=True)
    	# return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)
    	return HttpResponse(json.dumps(serializer.data))
    elif request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        data = USER_INFO.objects.get(email__icontains = email)
        serializer = USER_SERIALIZER(data)

        req['role'] = "ENGG"
        data.role = req['role']
        #data.PreviousCompany = req["PreviousCompany"]
        data.save()
        if "Activity" in req:
            AD = req['Activity']
            GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])

        #if fd.is_valid():
        #     data = fd.save(commit = False)
        #     data.save()
        #else:
        #     print("INVALID")
        #     print(fd.errors)
    return HttpResponse("ASDASD")

@require_http_methods(["GET"])
@csrf_exempt
def LOG(request, Release):
    data = LOGS.objects.using(Release).all()
    serializer = LOG_SERIALIZER(data, many = True)
    # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)
    return HttpResponse(json.dumps(serializer.data))

def GenerateLogData(UserName, RequestType, url, logData, tcid, card, Release):
    Logs = json.dumps(logData)
    Timestamp = datetime.datetime.now()
    data = {'UserName': UserName, 'RequestType': RequestType, 'LogData': logData, 'Timestamp': Timestamp, 'URL': url, 'TcID': tcid, 'CardType': card}
    fd = LogForm(data)
    if fd.is_valid():
        print(data)
        data = fd.save(commit = False)
        data.save(using = Release)
    else:
        print("INVALID", fd.errors)

def GETSETUPWISETCINFO(request, SetupName):
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

    # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)
    return HttpResponse(json.dumps(serializer.data))

@csrf_exempt
def RELEASEINFOPOST(request):
    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        req.pop('TcAggregate', None)

        fd = ReleaseInfoForm(req)
        if fd.is_valid():
            res = createDB(req['ReleaseNumber'])
            if res == 0:
                print("Database already exists")
            else:
                print("Created Database succesfully")
            fd.save()
            if "Activity" in req:
                AD = req['Activity']
                GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
            # return JsonResponse({'Sucess': 'SUCCESSFULLY ADDED NEW RELEASE'}, status = 200)
            print("SUCCESSFULLY ADDED NEW RELEASE")
            return HttpResponse("SUCCESSFULLY ADDED NEW RELEASE")
        else:
            print(fd.errors)
            # GenerateLogData(1, 'POST', 'specificuserbyid/' + str(id) + " => " + json.dumps(req))
            # return JsonResponse({'Error': fd.errors}, status = 400)
            return HttpResponse(fd.errors)


@csrf_exempt
def RELEASEINFO(request, Release):
    if request.method == "GET":
        list = []
        
        if(Release == 'all'):
            data = RELEASES.objects.all()
            serializer = RELEASE_SERIALIZER(data, many = True)

            for i in serializer.data:
                data = json.dumps(i)
                data = json.loads(data)
    
                if(i['ReleaseNumber'] != "universal"):
                    a = TCAGGREGATE(i['ReleaseNumber'])
                    data['TcAggregate'] = a
                list.append(data)

            # return JsonResponse(json.dumps(list), status = 200)
            return HttpResponse(json.dumps(list))
        else:
            data = RELEASES.objects.using('universal').filter(ReleaseNumber__icontains = Release)
            serializer = RELEASE_SERIALIZER(data, many = True)
            # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)
            return HttpResponse(json.dumps(serializer.data))

    elif request.method == "DELETE":
        try:
            data = RELEASES.objects.get(ReleaseNumber__icontains = Release).delete()
            if "Activity" in req:
               AD = request['Activity']
               GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
            # return JsonResponse({'Success': "DELETED SUCCESSFULLY"}, status = 200)
            return HttpResponse("DELETED SUCCESSFULLY")
        except RELEASES.DoesNotExist:
            error_message = "OBJECT NOT PRESENT CANNOT BE DELETED!!"
            # return JsonResponse({'Error': error_message}, status = 400)
            return HttpResponse(error_message)

    elif request.method == "PUT":
        try:
            req = json.loads(request.body.decode("utf-8"))
            data = RELEASES.objects.get(ReleaseNumber__icontains = Release)
            serializer = RELEASE_SERIALIZER(data, data = req)
            print("new aratI", req)
            if serializer.is_valid():
                serializer.save()
                if "Activity" in req:
                    AD = req['Activity']
                    GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
            else:
                print(serializer.errors)
            # return JsonResponse({'Success': "RECORD UPDATED SUCCESSFULLY"}, status = 200)
            return HttpResponse("SUCCESS")
        except:
            # return JsonResponse({'error': "SOME ERROR OCCURED"}, status = 400)
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

"""
def GETPLATFORMWISETCINFO(request, OrchestrationPlatform):
    data = TC_INFO.objects.filter(OrchestrationPlatform__icontains = OrchestrationPlatform)
    serializer = TC_INFO_SERIALIZER(data, many=True)
    print("orchestartion platform name: ", OrchestrationPlatform, "number of TCs: ", len(serializer.data))
    # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)
    return HttpResponse(json.dumps(serializer.data))


def GETPLATFORMANDSETUPWISETCINFO(request, OrchestrationPlatform, SetupName):
    data = TC_INFO.objects.filter(CardType__icontains = SetupName, OrchestrationPlatform__icontains = OrchestrationPlatform)
    serializer = TC_INFO_SERIALIZER(data, many=True)
    print("Setupname: ", SetupName, "orchestartion platform name: ", OrchestrationPlatform, "number of TCs: ", len(serializer.data))
    # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)
    return HttpResponse(json.dumps(serializer.data))
"""

@csrf_exempt
def USER_LOGIN_VIEW(request):
    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        print(req)

        try:
            data = USER_INFO.objects.get(UserName = req['email'])
            serializer = USER_SERIALIZER(data)
            #GenerateLogData(serializer.data['UserName'], 'POST', 'user/login', json.dumps(req))
            return JsonResponse({'role': serializer.data['Role']}, status = 200)
        except:
            print("except")
            data ={}
            data['Designation'] = "UNKNOWN"
            data['UserName'] = req['email']
            if 'Role' not in req:
                data['Role'] = "ADMIN"
            else:
                data['Role'] = req['Role']

            fd = UserInfoForm(data)
            if fd.is_valid():
                fd.save()
                if "Activity" in req:
                    AD = req['Activity']
                    GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
                return JsonResponse({'role': data['Role']}, status = 200)
            else:
                return JsonResponse({'error': fd.errors}, status = 400)
            #GenerateLogData(data['UserName'], 'POST', 'user/login', json.dumps(req))

        return JsonResponse({'role': data['Role']}, status = 200)

