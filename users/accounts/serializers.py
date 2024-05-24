from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    is_new_account = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined', 'is_new_account']

    def get_is_new_account(self, obj):
        # Define "new" account criteria, e.g., account created in the last 7 days
        from datetime import timedelta
        from django.utils import timezone
        return timezone.now() - obj.date_joined < timedelta(days=7)
