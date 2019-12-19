from django.views.decorators.csrf import csrf_exempt
from .models import TC_INFO
from .forms import TcInfoForm
import json
from django.http import HttpResponse
from DDB.serializers import TC_INFO_SERIALIZER

@csrf_exempt
def TC_INFO_GET_POST_VIEW(request):
    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        fd = TcInfoForm(req)

        if fd.is_valid():
            fd.save()
        else:
            try:
                data = TC_INFO.objects.using('default').get(TcID = req['TcID'])
                data.Setup.append(req['Setup'])
                data.OrchestrationPlatform.append(req['OrchestrationPlatform'])
                data.save()
            except:
                pass
            print(req, fd.errors)
        return HttpResponse(fd.errors)

    elif request.method == "GET":
        data = TC_INFO.objects.all()
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