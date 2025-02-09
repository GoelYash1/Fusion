from rest_framework import serializers
from applications.central_mess.models import *

class MessinfoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Messinfo
        fields=('__all__')

class Mess_regSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mess_reg
        fields=('__all__')

class MessBillBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessBillBase
        fields=('__all__')

class Monthly_billSerializer(serializers.ModelSerializer):
    class Meta:
        model=Monthly_bill
        fields=('__all__')

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payments
        fields=('__all__')

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields=('__all__')

class RebateSerializer(serializers.ModelSerializer):

    class Meta:
        model=Rebate
        fields=('__all__')

class Vacation_foodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation_food
        fields=('__all__')

# class Nonveg_menuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Nonveg_menu
#         fields=('__all__')

# class Nonveg_dataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Nonveg_data
#         fields=('__all__')

class Special_requestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Special_request
        fields=('__all__')

class Mess_meetingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mess_meeting
        fields=('__all__')        
    
class Mess_minutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mess_minutes
        fields=('__all__')

class Menu_change_requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu_change_request
        fields=('__all__')

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields=('__all__')

