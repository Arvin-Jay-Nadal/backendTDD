from django.test import TestCase
from .models import RentalModel, ReservationModel
import json
import datetime 
# Create your tests here.

class TestCase1(TestCase):
    @classmethod
    def setUpTestData(test):
        RentalModel.objects.create(name="Rental-1")
        RentalModel.objects.create(name="Rental-2")

        #Rental1
        #Reservation1
        ReservationModel.objects.create(rental_name=RentalModel.objects.get(name="Rental-1"), checkin=datetime.date(2022,1,1), checkout=datetime.date(2022,1,13))
        #Reservation2
        ReservationModel.objects.create(rental_name=RentalModel.objects.get(name="Rental-1"), checkin=datetime.date(2022,1,20), checkout=datetime.date(2022,2,10))
        #Reservation3
        ReservationModel.objects.create(rental_name=RentalModel.objects.get(name="Rental-1"), checkin=datetime.date(2022,2,20), checkout=datetime.date(2022,3,10))

        #Rental2
        #Reservation1
        ReservationModel.objects.create(rental_name=RentalModel.objects.get(name="Rental-2"), checkin=datetime.date(2022,1,2), checkout=datetime.date(2022,1,20))
        #Reservation2
        ReservationModel.objects.create(rental_name=RentalModel.objects.get(name="Rental-2"), checkin=datetime.date(2022,1,20), checkout=datetime.date(2022,2,11))

    def test_reservation1(self):
        id=1
        previous_reservation='-'
        Rental_name='Rental-1'
        checkin="2022-01-01"
        checkout="2022-01-13"

        resp = self.client.get("/reservations/1/")

        self.assertEqual(resp.data['id'], id)
        self.assertEqual(resp.data['Rental_name'], Rental_name)
        self.assertEqual(resp.data['checkin'], checkin)
        self.assertEqual(resp.data['checkout'], checkout)
        self.assertEqual(resp.data['previous_reservation'], previous_reservation)

    def test_reservation2(self):
        id=2
        previous_reservation='Res-1 ID'
        Rental_name='Rental-1'
        checkin="2022-01-20"
        checkout="2022-02-10"

        resp = self.client.get("/reservations/2/")

        self.assertEqual(resp.data['id'], id)
        self.assertEqual(resp.data['Rental_name'], Rental_name)
        self.assertEqual(resp.data['checkin'], checkin)
        self.assertEqual(resp.data['checkout'], checkout)
        self.assertEqual(resp.data['previous_reservation'], previous_reservation)

    def test_reservation3(self):
        id=3
        previous_reservation='Res-2 ID'
        Rental_name='Rental-1'
        checkin="2022-02-20"
        checkout="2022-03-10"

        resp = self.client.get("/reservations/3/")

        self.assertEqual(resp.data['id'], id)
        self.assertEqual(resp.data['Rental_name'], Rental_name)
        self.assertEqual(resp.data['checkin'], checkin)
        self.assertEqual(resp.data['checkout'], checkout)
        self.assertEqual(resp.data['previous_reservation'], previous_reservation)

    def test_reservation4(self):
        id=4
        previous_reservation='-'
        Rental_name='Rental-2'
        checkin="2022-01-02"
        checkout="2022-01-20"

        resp = self.client.get("/reservations/4/")

        
        self.assertEqual(resp.data['id'], id)
        self.assertEqual(resp.data['Rental_name'], Rental_name)
        self.assertEqual(resp.data['checkin'], checkin)
        self.assertEqual(resp.data['checkout'], checkout)
        self.assertEqual(resp.data['previous_reservation'], previous_reservation)

    def test_reservation5(self):
        id=5
        previous_reservation='Res-4 ID'
        Rental_name='Rental-2'
        checkin="2022-01-20"
        checkout="2022-02-11"

        resp = self.client.get("/reservations/5/")

        self.assertEqual(resp.data['id'], id)
        self.assertEqual(resp.data['Rental_name'], Rental_name)
        self.assertEqual(resp.data['checkin'], checkin)
        self.assertEqual(resp.data['checkout'], checkout)
        self.assertEqual(resp.data['previous_reservation'], previous_reservation)