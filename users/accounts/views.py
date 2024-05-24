from rest_framework import generics
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer

class AccountDetailView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        account = self.get_object()
        serializer = self.get_serializer(account)
        return Response(serializer.data)
