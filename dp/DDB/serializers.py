from rest_framework import serializers
from .models import TC_INFO, TC_STATUS, USER_INFO, LOGS, RELEASES

class TC_INFO_SERIALIZER(serializers.ModelSerializer):
    class Meta:
        model = TC_INFO
        fields = '__all__'

class TC_STATUS_SERIALIZER(serializers.ModelSerializer):
    # tcinfo1 = TC_INFO_SERIALIZER(many = True)

    class Meta:
        model = TC_STATUS
        # fields = ['TcID', 'tcinfo1']
        fields = '__all__'

class USER_SERIALIZER(serializers.ModelSerializer):
    class Meta:
        model = USER_INFO
        fields = '__all__'

class LOG_SERIALIZER(serializers.ModelSerializer):
    class Meta:
        model = LOGS
        fields = '__all__'

class RELEASE_SERIALIZER(serializers.ModelSerializer):
    class Meta:
        model = RELEASES
        fields = '__all__'