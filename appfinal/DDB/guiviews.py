from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from DDB.serializers import TC_STATUS_GUI_SERIALIZER
from .models import TC_STATUS_GUI 
from .forms import GuiTcInfoForm
from .forms import GuiTcInfoForm
from .views import GenerateLogData

@csrf_exempt
def GUITCSTATUSGETPOSTVIEW(request, Release):
    if request.method == "POST":
        req = json.loads(request.body.decode("utf-8"))
        fd = GuiTcInfoForm(req)
        if fd.is_valid():
            data = fd.save(commit = False)
            data.save(using = Release)
            if "Activity" in req:
                AD = req['Activity']
                GenerateLogData(AD['UserName'], AD['RequestType'], AD['URL'], AD['LogData'], AD['TcID'], AD['CardType'], AD['Release'])
        else:
            print(req, fd.errors)
            return JsonResponse({'Error': fd.errors}, status = 400)
        return HttpResponse("SUCCESS")
        # return JsonResponse({'Success': "Record added successfully"}, status = 200)
    elif request.method == "GET":
        data = TC_STATUS_GUI.objects.using(Release).all()
        serializer = TC_STATUS_GUI_SERIALIZER(data, many = True)
        return HttpResponse(json.dumps(serializer.data))
        # return JsonResponse({'data': json.dumps(serializer.data)}, status = 200)
