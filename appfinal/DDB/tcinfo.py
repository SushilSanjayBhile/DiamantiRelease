from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.db.models.functions import Trunc
import json, time

from .serializers import TC_INFO_SERIALIZER, TC_STATUS_SERIALIZER, LOG_SERIALIZER
from .models import TC_INFO, TC_STATUS, LOGS
from .forms import TcInfoForm
from .views import GenerateLogData
from django.db.models import Q

@csrf_exempt
def WHOLE_TC_INFO(request, Release):
    if request.method == "GET":
        AllInfoData = []
        statusDict = {}

        index = int(request.GET.get('index', 0))

        Domain = str(request.GET.get('Domain', None))
        SubDomain = str(request.GET.get('SubDomain', None))
        CardType = str(request.GET.get('CardType', None))

        statusdata = TC_STATUS.objects.using(Release).all().order_by('Date')
        infodata = TC_INFO.objects.all().using(Release).filter(~Q(Domain = "GUI"))

        if Domain != 'None':
            infodata = infodata.filter(Domain = Domain)
        if SubDomain != 'None':
            infodata = infodata.filter(SubDomain = SubDomain)
        if CardType != 'None':
            infodata = infodata.filter(CardType = CardType)

        count = int(request.GET.get('count', len(infodata)))
        try:
            infodata = infodata[index : (index + count)]
        except:
            allDataCount = info.count()
            if index < allDataCount and count < allDataCount:
                infodata = infodata[index:count]
            elif index < allDataCount:
                infodata = infodata[index:]
            else:
                infodata = TC_INFO.objects.using(Release).all()

        infoserializer = TC_INFO_SERIALIZER(infodata, many = True)
        statusserializer = TC_STATUS_SERIALIZER(statusdata, many=True)

        data = json.dumps(statusserializer.data)
        data = json.loads(data)

        for rec in data:
            tcid = rec['TcID']
            card = rec['CardType'].strip('][').strip('\'')

            if card not in statusDict:
                statusDict[card]= {}
            else:
                if tcid in statusDict[card]: 
                    statusDict[card][tcid].append(rec)
                else:
                    statusDict[card][tcid] = []
                    statusDict[card][tcid].append(rec)
        
        for info in infoserializer.data:
            #del info['Description']
            info['StautsList'] = {"id": "", "TcID": info['TcID'], "TcName": info['TcName'], "Build": "", "Result": "", "Bugs": "", "Date": "", "Domain": info['Domain'], "SubDomain": info['SubDomain'], "CardType": info['CardType']}
            info['CurrentStauts'] = {"id": "", "TcID": info['TcID'], "TcName": info['TcName'], "Build": "", "Result": "", "Bugs": "", "Date": "", "Domain": info['Domain'], "SubDomain": info['SubDomain'], "CardType": info['CardType']}

            card = info['CardType']
            tcid = info['TcID']

            try:
                info['StatusList'] = statusDict[card][tcid]
                info['CurrentStatus'] = statusDict[card][tcid][-1]
            except:
                pass

            AllInfoData.append(info)

        print("total filtered test cases count: ", len(AllInfoData))
        return HttpResponse(json.dumps(AllInfoData))


@csrf_exempt
def TC_INFO_GET_POST_VIEW(request, Release):
    master = "master"
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
            	print(card)
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
            		    #data.save(using = master)
            		    
            		    if "Activity" in req:
            		        AD = req['Activity']
            		        GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], card, AD['Release'])
                
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

def updateData(updatedData, data, Release):
     try:
         data.TcID = updatedData['TcID']
         data.id = updatedData['id']
         data.TcName = updatedData['TcName']
         data.Domain = updatedData['Domain']
         data.SubDomain = updatedData['SubDomain']
         data.Scenario = updatedData['Scenario']
         data.Description = updatedData['Description']
         #data.Steps = updatedData['Steps']
         data.ExpectedBehavior = updatedData['ExpectedBehaviour']
         data.Notes = updatedData['Notes']
         data.CardType = updatedData['CardType']
         data.ServerType = updatedData['ServerType']
         #data.OrchestrationPlatform = updatedData['OrchestrationPlatform']
         data.WorkingStatus = updatedData['WorkingStatus']
         data.Date = updatedData['Date']
         data.Assignee = updatedData['Assignee']
         data.Creator = updatedData['Creator']
         data.Tag = updatedData['Tag']
         data.Priority = updatedData['Priority']
    
         data.save(using = Release)
         return 1
     except:
         return 0

def TcCountByFilter(request, Release):
        print("COMING")
        countDict = {}
        replaceDict = {'ManagementTestcases': "Management", "MultizoneCluster":"Multizone Cluster",  "NetworkTestCases":"Network", "Rbac":"RBAC", "Rbac":"RBAC","StorageMirrored-Tests":"Storage-Mirrored","Additionaltests":"Additional", "HelmTestCases":"Helm","Interfacetestcases":"Interface","Kubernetes-tests": "Kubernetes", "ManagementTestcases":"Management", "MultizoneCluster":"Multizone Cluster", "NetworkTestCases":"Network","QOSTestcases":"QOS","StorageMirrored-Tests":"Storage-Mirrored","StorageRemote-Tests":"Storage-Remote","StorageSnapshot-Tests":"Storage-Snapshot","Upgradetests":"Upgrade", "Storage-Tests":"Storage"}
        for i in replaceDict:
            data = TC_INFO.objects.filter(Domain = i).using(Release)
            serializer = TC_INFO_SERIALIZER(data, many = True)

            for d in serializer.data:
                card = d['CardType']
                tcid = d['TcID']
                dat = TC_INFO.objects.using(Release).filter(TcID = tcid).get(CardType = card)
                d = json.dumps(d)
                d = json.loads(d)
                updatedData = d

                updatedData['Domain'] = replaceDict[i]
                print(dat.Domain)
                #print(updatedData, "\n",dat)
                #updateData(updatedData, dat, Release)
        return HttpResponse(json.dumps(countDict))

def TcCountByFilter2(request, Release):
        print("COMING")
        countDict = {}
        data = TC_INFO.objects.filter(Domain = "RBAC").using(Release)
        serializer = TC_INFO_SERIALIZER(data, many = True)

        for d in serializer.data:
            card = d['CardType']
            tcid = d['TcID']
            dat = TC_INFO.objects.using(Release).filter(TcID = tcid).get(CardType = card)
            d = json.dumps(d)
            d = json.loads(d)
            updatedData = d

            if "-" not in d['TcID']:
                print(d['TcID'], d['CardType'])
                dat.delete()
        return HttpResponse(json.dumps(countDict))

@csrf_exempt
def MULTIPLE_TC_UPDATION(request, Release):
    print("COMING to update multiple TCs")
    if request.method == "PUT":
        requests = json.loads(request.body.decode("utf-8"))
        errRecords = []
        print("total requests: ", len(requests))

        for req in requests:
            print(req)
            card = req['CardType']
            tcid = req['TcID']

            data = TC_INFO.objects.using(Release).filter(TcID = tcid).get(CardType = card)
            serializer = TC_INFO_SERIALIZER(data)
            updatedData = serializer.data
        
            for key in req:
                updatedData[key] = req[key]

            res = updateData(updatedData, data, Release)
            if res == 0:
                print("error", req)
                errRecords.append(req)
            elif "Activity" in requests:
                AD = requests['Activity']
                GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
        
        if len(errRecords) > 0:
            return HttpResponse(json.dumps(errRecords))

        return HttpResponse({"SUCCESS": "Record Successfully updated"})

    elif request.method == "DELETE":
        requests = json.loads(request.body.decode("utf-8"))
        errRecords = []

        for req in requests:
            card = req['CardType']
            tcid = req['TcID']

            data = TC_INFO.objects.using(Release).filter(TcID = tcid).get(CardType = card)
            serializer = TC_INFO_SERIALIZER(data)
            updatedData = serializer.data
            updatedData['WorkingStatus'] = "SKIP"

            res = updateData(updatedData, data, Release)
            if res == 0:
                errRecords.append(req)
            elif "Activity" in req:
                AD = requests['Activity']
                GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
        
        if len(errRecords) > 0:
            return HttpResponse(json.dumps(errRecords))
        return HttpResponse({"SUCCESS": "SOFT DELETED ALL RECORDS"})

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
            tcdata['Activity'] = activitySerializer.data
            tcdata['StatusList'] = []
            for status in statusSerializer.data:
                tcdata['StatusList'].append(status)
        except:
            return HttpResponse({"ERROR": "NO RECORD FOUND"})
            
        return HttpResponse(json.dumps(tcdata))

@csrf_exempt
def UPDATE_TC_INFO_BY_ID(request, Release, id, card):
    if request.method == "PUT":
        errRecords = []
        req = json.loads(request.body.decode("utf-8"))

        data = TC_INFO.objects.using(Release).filter(TcID = id)
        serializer = TC_INFO_SERIALIZER(data, many = True)
        newData = serializer.data

        for d in serializer.data:
            singleData = TC_INFO.objects.using(Release).filter(TcID = id).get(CardType = d['CardType'])
            singleSerializer = TC_INFO_SERIALIZER(singleData)
            updatedData = singleSerializer.data

            for key in req:
                if key != "CardType" and key != "TcID" and key != "Activity":
                    updatedData[key] = req[key]

            res = updateData(updatedData, singleData, Release)
            #res = updateData(updatedData, singleData, "master")
            if res == 0:
                errRecords.append(req)
            elif "Activity" in req:
                AD = req['Activity']
                GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
        
        if len(errRecords) > 0:
            return HttpResponse(json.dumps(errRecords))
        return HttpResponse({"SUCCESS": "Record Successfully updated"})

