from django.forms import ModelForm
from .models import TC_INFO, TC_STATUS, USER_INFO, LOGS, RELEASES


class TcInfoForm(ModelForm):
    class Meta:
        model = TC_INFO
        fields = "__all__"

class TcStatusForm(ModelForm):
    class Meta:
        model = TC_STATUS
        fields = "__all__"

class UserInfoForm(ModelForm):
    class Meta:
        model = USER_INFO
        fields = "__all__"

class LogForm(ModelForm):
    class Meta:
        model = LOGS
        fields = '__all__'

class ReleaseInfoForm(ModelForm):
    class Meta:
        model = RELEASES
        fields = '__all__'