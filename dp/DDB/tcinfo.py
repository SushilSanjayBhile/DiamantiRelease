from django.views.decorators.csrf import csrf_exempt
from .models import TC_INFO
from .forms import TcInfoForm
import json
from django.http import HttpResponse, JsonResponse
from DDB.serializers import TC_INFO_SERIALIZER

@csrf_exempt
def TC_INFO_GET_POST_VIEW(request, Release):
    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        fd = TcInfoForm(req)

        if fd.is_valid():
            data = fd.save(commit = False)
            data.save(using = Release)
            return HttpResponse("SUCCESSFULLY SAVED")
        else:
            try:
                data = TC_INFO.objects.using(Release).get(TcID = req['TcID'])
                data.CardType.append(req['CardType'])
                data.OrchestrationPlatform.append(req['OrchestrationPlatform'])
                data = data.save(commit = False)
                data.save(using = Release)
                return HttpResponse("SUCCESSFULLY UPDATED")
            except:
                return HttpResponse("ERROR OCCURED")

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


@csrf_exempt
def SPECIFIC_TC_INFO_BY_NAME(request, name):
    print("COMING")
    data = TC_INFO.objects.get(TcName=name)
    serializer = TC_INFO_SERIALIZER(data)
    return HttpResponse(json.dumps(serializer.data))

@csrf_exempt
def SPECIFIC_TC_INFO_BY_ID(request, id):
    data = TC_INFO.objects.get(TcID=id)
    serializer = TC_INFO_SERIALIZER(data)
    return HttpResponse(json.dumps(serializer.data))
