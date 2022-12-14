from rest_framework import serializers
from .models import RentalModel, ReservationModel
from django.utils.timezone import now

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationModel
        #fields = "__all__"
        exclude = ["rental_name"]

    previous_reservation = serializers.SerializerMethodField()
    Rental_name = serializers.SerializerMethodField()
        
    def get_previous_reservation(self, obj):
        ctr = ReservationModel.objects.filter(rental_name=obj.rental_name, id__lt=obj.id).order_by('-id').first()
        
        if ctr:
            return f"Res-{ctr.id} ID"
        else:
            return '-'

    def get_Rental_name(self, obj):
        return f"{obj.rental_name.name}"

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalModel
        fields = "__all__"