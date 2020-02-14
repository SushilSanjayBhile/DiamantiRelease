from .serializers import TC_INFO_SERIALIZER, TC_STATUS_SERIALIZER, LOG_SERIALIZER
from .models import TC_INFO, TC_STATUS, LOGS
from .forms import TcInfoForm
from .views import GenerateLogData
import json

def updateStatusData(updatedData, data, Release):
     try:
         data.TcID = updatedData['TcID']
         data.TcName = updatedData['TcName']
         data.Build = updatedData['Build']
         data.Result = updatedData['Result']
         data.Bugs = updatedData['Bugs']
         data.Date = updatedData['Date']
         data.Domain = updatedData['Domain']
         data.SubDomain = updatedData['SubDomain']
         data.CardType = updatedData['CardType']

         data.save(using = Release)
         return 1
     except:
         return 0

def updateStatusID(oldTcID, newTcID, Release):
	statusInfo = TC_STATUS.objects.using(Release).filter(TcID = oldTcID)
	serializer = TC_STATUS_SERIALIZER(statusInfo, many = True)

	for status in serializer.data:
		statusData = TC_STATUS.objects.using(Release).get(id = status['id'])
		updatedData = status

		for key in status:
			if key == 'TcID':
				updatedData[key] = newTcID
			else:
				updatedData[key] = status[key]
		updateStatusData(updatedData, statusData, Release)

def updateStatusName(TcID, newTcName, Release):
	statusInfo = TC_STATUS.objects.using(Release).filter(TcID = TcID)
	serializer = TC_STATUS_SERIALIZER(statusInfo, many = True)

	for status in serializer.data:
		statusData = TC_STATUS.objects.using(Release).get(id = status['id'])
		updatedData = status

		for key in status:
			if key == 'TcName':
				updatedData[key] = newTcName
			else:
				updatedData[key] = status[key]
		print(updatedData)
		#updateStatusData(updatedData, statusData, Release)

def updateStatusDomain(TcID, newDomain, Release):
	statusInfo = TC_STATUS.objects.using(Release).filter(TcID = TcID)
	serializer = TC_STATUS_SERIALIZER(statusInfo, many = True)

	for status in serializer.data:
		statusData = TC_STATUS.objects.using(Release).get(id = status['id'])
		updatedData = status

		for key in status:
			if key == 'Domain':
				updatedData[key] = newDomain
			else:
				updatedData[key] = status[key]
		#updateStatusData(updatedData, statusData, Release)

def updateStatusSubDomain(TcID, newSubDomain, Release):
	statusInfo = TC_STATUS.objects.using(Release).filter(TcID = TcID)
	serializer = TC_STATUS_SERIALIZER(statusInfo, many = True)

	for status in serializer.data:
		statusData = TC_STATUS.objects.using(Release).get(id = status['id'])
		updatedData = status

		for key in status:
			if key == 'SubDomain':
				updatedData[key] = newSubDomain
			else:
				updatedData[key] = status[key]
		#updateStatusData(updatedData, statusData, Release)
