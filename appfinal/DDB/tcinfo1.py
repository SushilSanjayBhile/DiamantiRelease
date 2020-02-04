from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.db.models.functions import Trunc
import json, time

from .serializers import TC_INFO_SERIALIZER, TC_STATUS_SERIALIZER, LOG_SERIALIZER
from .models import TC_INFO, TC_STATUS, LOGS
from .forms import TcInfoForm
from .views import GenerateLogData

@csrf_exempt
def WHOLE_TC_INFO(request, Release):
    if request.method == "GET":
        index = int(request.GET.get('index', 0))
        count = int(request.GET.get('count', 100))
        AllInfoData = []
        statusDict = {}

        try:
            if count == 0:
                infodata = TC_INFO.objects.using(Release).all()[index : ]
            else:
                infodata = TC_INFO.objects.using(Release).all()[index : (index + count)]
        except:
            infodata = TC_INFO.objects.using(Release).all()
        statusdata = TC_STATUS.objects.using(Release).all().order_by('Date')

        infoserializer = TC_INFO_SERIALIZER(infodata, many = True)
        statusserializer = TC_STATUS_SERIALIZER(statusdata, many=True)

        d = json.dumps(statusserializer.data)
        d = json.loads(d)

        for i in d:
            card = i['CardType']
            tcid = i['TcID']

            if card not in statusDict:
                statusDict[card]= {}
            else:
                if tcid in statusDict[card]: 
                    statusDict[card][tcid].append(i)
                else:
                    statusDict[card][tcid] = []
                    statusDict[card][tcid].append(i)
        
        for info in infoserializer.data:
            info['StautsList'] = {"id": "", "TcID": info['TcID'], "TcName": info['TcName'], "Build": "", "Result": "", "Bugs": "", "Date": "", "Domain": info['Domain'], "SubDomain": info['SubDomain'], "CardType": info['CardType']}
            info['CurrentStauts'] = {"id": "", "TcID": info['TcID'], "TcName": info['TcName'], "Build": "", "Result": "", "Bugs": "", "Date": "", "Domain": info['Domain'], "SubDomain": info['SubDomain'], "CardType": info['CardType']}

            card = info['CardType']
            tcid = info['TcID']

            if len(statusDict) > 0:
                if card in statusDict and tcid in statusDict[card]:
                    info['StatusList'] = statusDict[card][tcid]
                    if len(statusDict[card][tcid]) > 0:
                        info['CurrentStatus'] = statusDict[card][tcid][-1]

            AllInfoData.append(info)

        return HttpResponse(json.dumps(AllInfoData))


@csrf_exempt
def TC_INFO_GET_POST_VIEW(request, Release):
    master = "master"
    coflictFlag = False
    errorMsg = {}
    errorMsg[Release] = []
    errorMsg[master] = []

    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        cards = req['CardType']

        for card in cards:
            # post request for current release
            data = TC_INFO.objects.using(Release).filter(TcID = req['TcID']).filter(CardType = card)
            #if len(data) != 1 and len(data) != 0:
            if len(data) != 0:
                errorMsg[Release].append('Duplicate: ' + req['TcID'] + ' with ' + card)
                conflictFlag = True
                #return JsonResponse({'message': 'Duplicate TcID'}, status = 409)
            else:
            	serializer = TC_INFO_SERIALIZER(data, many = True)
            	newData  = req
            	newData = json.dumps(newData)
            	newData = json.loads(newData)
            	newData['CardType'] = card
            	
            	fd = TcInfoForm(newData)

            	if fd.is_valid():
            	    data = fd.save(commit = False)
            	    data.save(using = Release)
            	    
            	    if "Activity" in req:
            	        AD = req['Activity']
            	        GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], card, AD['Release'])

            # post request for master release
            if Release != master:
            	data = TC_INFO.objects.using(master).filter(TcID = req['TcID']).filter(CardType = card)
            	#if len(data) != 1 and len(data) != 0:
            	if len(data) != 0:
            	    errorMsg[master].append('Duplicate: ' + req['TcID'] + ' with ' + card)
            	    conflictFlag = True
            	    #return JsonResponse({'message': 'Duplicate TcID in Master Database'}, status = 409)
            	else:
            		serializer = TC_INFO_SERIALIZER(data, many = True)
            		newData  = req
            		newData = json.dumps(newData)
            		newData = json.loads(newData)
            		newData['CardType'] = card
            		
            		fd = TcInfoForm(newData)

            		if fd.is_valid():
            		    data = fd.save(commit = False)
            		    data.save(using = master)
            		    
            		    if "Activity" in req:
            		        AD = req['Activity']
            		        GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], card, AD['Release'])
                
        if conflictFlag:
            return JsonResponse({"Conflict": json.dumps(errorMsg)}, status = 409)
        return HttpResponse("SUCCESSFULLY UPDATED")

    elif request.method == "GET":
        index = int(request.GET.get('index', 0))
        count = int(request.GET.get('count', 100))

        try:
            if count == 0:
                data = TC_INFO.objects.using(Release).all()[index : ]
            else:
                data = TC_INFO.objects.using(Release).all()[index : (index + count)]
        except:
            return JsonResponse({'message': 'Unknown error occured'}, status = 400)

        if len(data) == 0:
            return JsonResponse({'message': 'Records no found at given index'}, status = 400)

        serializer = TC_INFO_SERIALIZER(data, many=True)
        return HttpResponse(json.dumps(serializer.data))
    """
    elif request.method == "DELETE":
        req = json.loads(request.body.decode("utf-8"))
        data = TC_INFO.objects.filter(TcID = req['TcID'])
        serializer = TC_INFO_SERIALIZER(data,many = True)
        d = json.dumps(serializer.data)
        d = json.loads(d)        
        
        if(len(d[0]['Setup']) > 1):
            print(d[0]['Setup'])
            return HttpResponse("PLEASE PROVIDE SETUP ALSO NAME ALSO AS THERE ARE MULTIPLE SETUPS")
        if(len(d[0]['OrchestrationPlatform']) > 1):
            print(d[0]['OrchestrationPlatform'])
            return HttpResponse("PLEASE PROVIDE ORCHESTRATION PLATFORM NAME AS THERE ARE MULTIPLE PLATFORMS")

        return HttpResponse(json.dumps(d))
    """

@csrf_exempt
def MULTIPLE_TC_UPDATION(request, Release):
    if request.method == "PUT":
        requests = json.loads(request.body.decode("utf-8"))

        for req in requests:
            card = req['CardType']
            tcid = req['TcID']

            data = TC_INFO.objects.using(Release).filter(TcID = tcid).get(CardType = card)
            serializer = TC_INFO_SERIALIZER(data)
            updatedData = serializer.data
        
            for key in req:
                updatedData[key] = req[key]
            #result = data.delete()

            fd = TcInfoForm(updatedData)
            if fd.is_valid():
                data = fd.save(commit = False)
                data.save(using = Release)
                
                if "Activity" in requests:
                    AD = requests['Activity']
                    GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
                
                result = data.delete()
            else:
                HttpResponse({"ERROR": fd.errors})
        
        return HttpResponse({"SUCCESS": "Record Successfully updated"})

    elif request.method == "DELETE":
        requests = json.loads(request.body.decode("utf-8"))

        for req in requests:
            card = req['CardType']
            tcid = req['TcID']

            data = TC_INFO.objects.using(Release).filter(TcID = tcid).get(CardType = card)
            serializer = TC_INFO_SERIALIZER(data)
        
            updatedData = serializer.data
            updatedData['Status'] = "SKIP"
        
            fd = TcInfoForm(updatedData)
            if fd.is_valid():
                data = fd.save(commit = False)
                data.save(using = Release)
                
                if "Activity" in req:
                    AD = requests['Activity']
                    GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
                
                result = data.delete()
            else:
                HttpResponse({"ERROR": fd.errors})
        
        return HttpResponse({"SUCCESS": "SOFT DELTED ALL RECORDS"})

@csrf_exempt
def GET_TC_INFO_BY_ID(request, Release, id, card):
    if request.method == "GET":
        infoData = TC_INFO.objects.using(Release).filter(TcID = id).get(CardType = card)
        activityData = LOGS.objects.using(Release).filter(TcID = id).filter(CardType = card)

        activitySerializer = LOG_SERIALIZER(activityData, many = True)
        infoSerializer = TC_INFO_SERIALIZER(infoData)
    
        try:
            statusData = TC_STATUS.objects.using(Release).filter(TcID = id).filter(CardType = card).order_by('Date')
            statusSerializer = TC_STATUS_SERIALIZER(statusData, many=True)
    
            tcdata = infoSerializer.data
            tcdata['Activity'] = activityData.data
            tcdata['StatusList'] = []
            for status in statusSerializer.data:
                tcdata['StatusList'].append(status)
        except:
            return HttpResponse({"ERROR": "NO RECORD FOUND"})
            
        return HttpResponse(json.dumps(tcdata))

@csrf_exempt
def UPDATE_TC_INFO_BY_ID(request, Release, id, card):
    if request.method == "PUT":
        req = json.loads(request.body.decode("utf-8"))

        data = TC_INFO.objects.using(Release).filter(TcID = id)
        serializer = TC_INFO_SERIALIZER(data, many = True)
        newData = serializer.data

        for d in serializer.data:
            singleData = TC_INFO.objects.using(Release).filter(TcID = id).get(CardType = d['CardType'])
            singleSerializer = TC_INFO_SERIALIZER(singleData)
            newData = singleSerializer.data

            for key in req:
                if key != "CardType" and key != "TcID" and key != "Activity":
                    newData[key] = req[key]


            fd = TcInfoForm(newData)
            if fd.is_valid():
                data = fd.save(commit = False)
                data.save(using = Release)
                singleData.delete()
                if "Activity" in req:
                    AD = req['Activity']
                    GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
            else:
                HttpResponse({"ERROR": fd.errors})
        return HttpResponse({"SUCCESS": "Record Successfully updated"})
