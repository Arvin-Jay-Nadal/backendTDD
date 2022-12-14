from rest_framework import viewsets
from .models import RentalModel, ReservationModel
from .serializers import RentalSerializer, ReservationSerializer

# Create your views here.

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = ReservationModel.objects.all()
    serializer_class = ReservationSerializer

class RentalViewSet(viewsets.ModelViewSet):
    queryset = RentalModel.objects.all()
    serializer_class = RentalSerializer
