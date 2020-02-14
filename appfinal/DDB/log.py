from .serializers import TC_INFO_SERIALIZER, TC_STATUS_SERIALIZER, LOG_SERIALIZER
from .models import TC_INFO, TC_STATUS, LOGS
from .forms import TcInfoForm
from .views import GenerateLogData
import json

def updateLogData(updatedData, data, Release):
    try:
        data.logNo = updatedData['logNo']
        data.UserName = updatedData['UserName']
        data.Timestamp = updatedData['Timestamp']
        data.RequestType = updatedData['RequestType']
        data.LogData = updatedData['LogData']
        data.URL = updatedData['URL']
        data.TcID = updatedData['TcID']
        data.CardType = updatedData['CardType']

        data.save(using = Release)
    except:
        pass

def updateLogID(TcID, CardType, newTcID, Release):
	logData = LOGS.objects.using(Release).filter(TcID = TcID).filter(CardType = CardType)
	logSerializer = LOG_SERIALIZER(logData, many = True)

	for log in logSerializer.data:
		log = LOGS.objects.using(Release).get(logNo = log['logNo'])
		updatedData = log

		for key in log:
			if key == 'TcID':
				updatedData[key] = newTcID
			else:
				updatedData[key] = log[key]
		updateLogData(updatedData, log, Release)
			
