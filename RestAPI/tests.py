# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from rest_framework.test import RequestsClient

BASE_URL = 'http://localhost:8000/'


class RestTestCase(TestCase):

    def setUp(self):
       self.location1 ={
           'lat': 36.1189,
           'lon': -86.6892,
           'city': 'Nashville',
           'state': 'Tennessee'
       }
       self.location2 = {
           'lat': 36.1189,
           'lon': -86.6892,
           'city': 'Monroe',
           'state': 'Tennessee'
       }
       self.location3 = {
           'lat': 35.1189,
           'lon': -16.6892,
           'city': 'Monroe',
           'state': 'Louisiana'
       }
       self.location4 = {
           'lat': 'wrong',
           'lon': -86.6892,
           'city': 'Nashville',
           'state': 'Tennessee'
       }
       self.location5 = {
           'lat': 36.1189,
           'lon': 'wrong',
           'city': 'Nashville',
           'state': 'Tennessee'
       }
       self.weather1= {
           'id': 1,
           'date': '1985-01-01',
           'location': self.location1,
           'temperature': [42.2, 42.2, 41.7, 41.1, 40.5, 40.4, 40.2, 39.8, 40.7, 43.6, 46.3, 48.8, 50.5, 52.0, 53.1,
                           53.5, 53.2, 51.3, 48.7, 46.9, 45.9, 44.7, 44.3, 43.7]
       }
       self.weather2 = {
           'id': 2,
           'date': '1985-01-02',
           'location': self.location2,
           'temperature': [42.2, 42.2, 2.7, 41.1, 40.5, 40.4, 40.2, 39.8, 40.7, 43.6, 46.3, 48.8, 50.5, 52.0, 53.1,
                           53.5, 53.2, 91.3, 48.7, 46.9, 45.9, 44.7, 44.3, 43.7]
       }
       self.weather3 = {
           'id': 3,
           'date': '1985-01-04',
           'location': self.location3,
           'temperature': [42.2, 42.2, 41.7, 41.1, 40.5, 40.4, 40.2, 39.8, 40.7, 43.6, 46.3, 48.8, 50.5, 52.0, 53.1,
                           53.5, 53.2, 51.3, 48.7, 46.9, 45.9, 44.7, 44.3, 43.7]
       }
       self.weather4 = {
           'id': 'ascas',
           'date': '1985-01-01',
           'location': self.location1,
           'temperature': [42.2, 42.2, 41.7, 41.1, 40.5, 40.4, 40.2, 39.8, 40.7, 43.6, 46.3, 48.8, 50.5, 52.0, 53.1,
                           53.5, 53.2, 51.3, 48.7, 46.9, 45.9, 44.7, 44.3, 43.7]
       }
       self.weather5 = {
           'id': 1,
           'date': 'asaa',
           'location': self.location1,
           'temperature': [42.2, 42.2, 41.7, 41.1, 40.5, 40.4, 40.2, 39.8, 40.7, 43.6, 46.3, 48.8, 50.5, 52.0, 53.1,
                           53.5, 53.2, 51.3, 48.7, 46.9, 45.9, 44.7, 44.3, 43.7]
       }
       self.weather6 = {
           'id': 1,
           'date': '1985-01-01',
           'location': self.location4,
           'temperature': [42.2, 42.2, 41.7, 41.1, 40.5, 40.4, 40.2, 39.8, 40.7, 43.6, 46.3, 48.8, 50.5, 52.0, 53.1,
                           53.5, 53.2, 51.3, 48.7, 46.9, 45.9, 44.7, 44.3, 43.7]
       }

       self.weather7 = {
           'id': 1,
           'date': '1985-01-01',
           'location': self.location5,
           'temperature': [42.2, 42.2, 41.7, 41.1, 40.5, 40.4, 40.2, 39.8, 40.7, 43.6, 46.3, 48.8, 50.5, 52.0, 53.1,
                           53.5, 53.2, 51.3, 48.7, 46.9, 45.9, 44.7, 44.3, 43.7]
       }
       self.weather8 = {
           'id':'wrong',
           'date': 'wrong',
           'location': {
               'lat': 'wrong',
               'lon': 'ascac',
               'city': 'Nashville',
               'state': 'Tennessee'
            },
           'temperature': [42.2, 42.2, 41.7, 41.1, 40.5, 40.4, 40.2, 39.8, 40.7, 43.6, 46.3, 48.8, 50.5, 52.0, 53.1,
                           53.5, 53.2, 51.3, 48.7, 46.9, 45.9, 44.7, 44.3, 43.7]
       }

    def test_wrong_post_request(self):
        client = RequestsClient()
        res = client.get(BASE_URL + 'weather/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), [])
        res = client.post(BASE_URL + 'weather/', json=self.weather4)
        self.assertEqual(res.status_code, 400, 'Id should be a whole number')
        self.assertEqual(res.json()['id'], ['Enter a whole number.'])
        res = client.post(BASE_URL + 'weather/', json=self.weather5)
        self.assertEqual(res.status_code, 400, 'Date should be in given format')
        self.assertEqual(res.json()['date'], ['Enter a valid date/time.'])

        res = client.post(BASE_URL + 'weather/', json=self.weather6)
        self.assertEqual(res.status_code, 400, 'Latitude should be in given format')
        self.assertEqual(res.json()['lat'], ['Enter a number.'])
        res = client.post(BASE_URL + 'weather/', json=self.weather7)
        self.assertEqual(res.status_code, 400, 'longitude should be in given format')
        self.assertEqual(res.json()['lon'],['Enter a number.'])
        res = client.post(BASE_URL + 'weather/', json=self.weather8)
        self.assertEqual(res.status_code, 400, 'Bad request data')
        self.assertEqual(res.json()['lat'], ['Enter a number.'])
        self.assertEqual(res.json()['lon'], ['Enter a number.'])
        self.assertEqual(res.json()['id'],  ['Enter a whole number.'])
        self.assertEqual(res.json()['date'],  ['Enter a valid date/time.'])
        res = client.post(BASE_URL + 'weather/', json=self.weather1)
        self.assertEqual(res.status_code, 201)

    def test_valid_request(self):
        client = RequestsClient()
        res = client.get(BASE_URL + 'weather/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), [])
        res = client.post(BASE_URL + 'weather/', json=self.weather2)
        self.assertEqual(res.status_code, 201)
        res = client.post(BASE_URL + 'weather/', json=self.weather2)
        self.assertEqual(res.status_code, 400, 'Weather with this id already exist')
        self.assertEqual(res.json()['id'], ['Weather with this Id already exists.'])
        res = client.post(BASE_URL + 'weather/', json=self.weather1)
        self.assertEqual(res.status_code, 201)
        res = client.post(BASE_URL + 'weather/', json=self.weather3)
        self.assertEqual(res.status_code, 201)
        res = client.get(BASE_URL + 'weather/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), [self.weather1, self.weather2, self.weather3])

    def test_weather_filter_request(self):
        client = RequestsClient()
        client.get(BASE_URL + 'weather/')
        client.post(BASE_URL + 'weather/', json=self.weather2)
        client.post(BASE_URL + 'weather/', json=self.weather1)
        client.post(BASE_URL + 'weather/', json=self.weather3)
        res = client.get(BASE_URL + 'weather?lat=36.1189&lon=-86.6892')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), [self.weather1, self.weather2])
        res = client.get(BASE_URL + 'weather?lat=35.1189&lon=-16.6892')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), [self.weather3])
        res = client.get(BASE_URL + 'weather?lat=12.3232&lon=-34.1234')
        self.assertEqual(res.status_code, 404, 'There is no weather data with given lat and lon')

    def test_weather_temperature_filter_request(self):
        client = RequestsClient()
        client.get(BASE_URL + 'weather/')
        client.post(BASE_URL + 'weather/', json=self.weather2)
        client.post(BASE_URL + 'weather/', json=self.weather1)
        client.post(BASE_URL + 'weather/', json=self.weather3)
        res = client.get(BASE_URL + 'weather/temperature?start=1985-02-01&end=1985-02-02')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), [])
        self.assertEqual(len(res.json()), 0)
        res = client.get(BASE_URL + 'weather/temperature?start=1985-01-01&end=1985-01-02')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 2)
        self.assertEqual(res.json()[0]['lowest'], 2.7)
        self.assertEqual(res.json()[0]['highest'], 91.3)
        self.assertEqual(res.json()[1]['lowest'], 39.8)
        self.assertEqual(res.json()[1]['highest'], 53.5)
        res = client.get(BASE_URL + 'weather/temperature?start=1985-01-01&end=1985-01-04')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 3)
        self.assertEqual(res.json()[0]['city'], 'Monroe')
        self.assertEqual(res.json()[0]['state'], 'Louisiana')
        self.assertEqual(res.json()[1]['city'], 'Monroe')
        self.assertEqual(res.json()[1]['state'], 'Tennessee')
        self.assertEqual(res.json()[2]['city'], 'Nashville')
        self.assertEqual(res.json()[2]['state'], 'Tennessee')

    def test_weathe_delete_request(self):
        client = RequestsClient()
        client.get(BASE_URL + 'weather/')
        client.post(BASE_URL + 'weather/', json=self.weather2)
        client.post(BASE_URL + 'weather/', json=self.weather1)
        client.post(BASE_URL + 'weather/', json=self.weather3)
        res = client.get(BASE_URL + 'weather/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 3)
        res = client.delete(BASE_URL + 'erase/2')
        self.assertEqual(res.status_code, 200)
        res = client.delete(BASE_URL + 'erase/2')
        self.assertEqual(res.status_code, 404, 'There is no weather data with id 2')
        res = client.get(BASE_URL + 'weather/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 2)
        self.assertEqual(res.json(), [self.weather1, self.weather3])
        res = client.delete(BASE_URL + 'erase?start=1985-01-04&end=1985-01-04&lat=35.1189&lon=-16.6892')
        self.assertEqual(res.status_code, 200)
        res = client.get(BASE_URL + 'weather/')
        self.assertEqual(res.json(), [self.weather1])
