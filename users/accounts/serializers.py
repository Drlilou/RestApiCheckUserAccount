from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    is_new_account = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ['id', 'email', 'username', 'date_joined', 'is_active', 'is_new_account']

    def get_is_new_account(self, obj):
        from datetime import timedelta
        from django.utils import timezone
        return timezone.now() - obj.date_joined < timedelta(days=7)
