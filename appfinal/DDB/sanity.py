from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.db.models.functions import Trunc
import json, time

from .serializers import TC_INFO_SERIALIZER, TC_STATUS_SERIALIZER, LOG_SERIALIZER, E2E_SERIALIZER, STRESS_SERIALIZER, LONGEVITY_SERIALIZER
from .models import E2E, LONGEVITY, STRESS, LOGS
from .forms import TcInfoForm, E2EForm, StressForm, LongevityForm
from .views import GenerateLogData
from django.db.models import Q

@csrf_exempt
def E2EView(request, Release):
    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        fd = E2EForm(req)
        if fd.is_valid():
            data = fd.save(commit = False)
            data.save(using = Release)
        else:
            print(req)
            print(fd.errors)
            return JsonResponse({'Error': fd.errors}, status = 400)
        # GenerateLogData(1, 'POST', 'specificuserbyid/' + str(id) + " => " + json.dumps(req))
        return HttpResponse("SUCCESS")
        # return JsonResponse({'Success': "Record added successfully"}, status = 200)
    elif request.method == "GET":
        data = E2E.objects.using(Release).all()
        serializer = E2E_SERIALIZER(data, many = True)
        return HttpResponse(json.dumps(serializer.data))
        # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)

@csrf_exempt
def StressView(request, Release):
    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        fd = StressForm(req)
        if fd.is_valid():
            data = fd.save(commit = False)
            data.save(using = Release)
        else:
            print(req)
            print(fd.errors)
            return JsonResponse({'Error': fd.errors}, status = 400)
        # GenerateLogData(1, 'POST', 'specificuserbyid/' + str(id) + " => " + json.dumps(req))
        return HttpResponse("SUCCESS")
        # return JsonResponse({'Success': "Record added successfully"}, status = 200)
    elif request.method == "GET":
        data = STRESS.objects.using(Release).all()
        serializer = TC_STATUS_GUI_SERIALIZER(data, many = True)
        return HttpResponse(json.dumps(serializer.data))
        # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)

@csrf_exempt
def LongevityView(request, Release):
    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        fd = LongevityForm(req)
        if fd.is_valid():
            data = fd.save(commit = False)
            data.save(using = Release)
        else:
            print(req)
            print(fd.errors)
            return JsonResponse({'Error': fd.errors}, status = 400)
        # GenerateLogData(1, 'POST', 'specificuserbyid/' + str(id) + " => " + json.dumps(req))
        return HttpResponse("SUCCESS")
        # return JsonResponse({'Success': "Record added successfully"}, status = 200)
    elif request.method == "GET":
        data = TC_STATUS_GUI.objects.using(Release).all()
        serializer = TC_STATUS_GUI_SERIALIZER(data, many = True)
        return HttpResponse(json.dumps(serializer.data))
        # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)

