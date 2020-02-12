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
def SANITY_VIEW(request, SanityType, Release):
    if "delete" not in SanityType.lower():
        return SanityView(request, Release, SanityType)
    else:
        return SanityDeleteView(request, Release, SanityType)

def SanityDeleteView(request, Release, SanityType):
    if request.method == "POST":
        requests = json.loads(request.body.decode("utf-8"))

        for req in requests:
            if "e2e" in SanityType.lower():
                data = E2E.objects.using(Release).get(id = req['id']).delete()
            if "stress" in SanityType.lower():
                data = STRESS.objects.using(Release).get(id = req['id']).delete()
            if "longevity" in SanityType.lower():
                data = LONGEVITY.objects.using(Release).get(id = req['id']).delete()

            if "Activity" in req:
                AD = req['Activity']
                GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
        return HttpResponse("SUCCESS")
        # return JsonResponse({'Success': "Record added successfully"}, status = 200)


def SanityView(request, Release, SanityType):
    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        req['CardType'] = req['CardType'][0]
        print(req)

        if SanityType.lower() == "e2e":
            fd = E2EForm(req)
        if SanityType.lower() == "stress":
            fd = StressForm(req)
        if SanityType.lower() == "longevity":
            fd = LongevityForm(req)

        if fd.is_valid():
            data = fd.save(commit = False)
            data.save(using = Release)
            if "Activity" in req:
                AD = req['Activity']
                GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
        else:
            print(fd.errors)
            return JsonResponse({'Error': fd.errors}, status = 400)
        return HttpResponse("SUCCESS")
        # return JsonResponse({'Success': "Record added successfully"}, status = 200)


    elif request.method == "GET":
        if SanityType.lower() == "e2e":
            data = E2E.objects.using(Release).all()
            serializer = E2E_SERIALIZER(data, many = True)
        if SanityType.lower() == "stress":
            data = STRESS.objects.using(Release).all()
            serializer = STRESS_SERIALIZER(data, many = True)
        if SanityType.lower() == "longevity":
            data = LONGEVITY.objects.using(Release).all()
            serializer = LONGEVITY_SERIALIZER(data, many = True)

        return HttpResponse(json.dumps(serializer.data))
        # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)

    elif request.method == "DELETE":
        req = json.loads(request.body.decode("utf-8"))
        req['CardType'] = req['CardType'][0]
        print(req)
