import datetime as dt

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main import models

DATA = [
    [70, "2016-02-29T12:00:00Z", "2016-02-29T14:00:00Z"],
    [71, "2017-12-11T15:07:13Z", "2017-12-11T15:14:56Z"],
    [72, "2017-12-12T22:47:56Z", "2017-12-12T22:50:56Z"],
    [73, "2017-12-12T21:57:13Z", "2017-12-12T22:10:56Z"],
    [74, "2017-12-12T04:57:13Z", "2017-12-12T06:10:56Z"],
    [75, "2017-12-13T21:57:13Z", "2017-12-14T22:10:56Z"],
    [76, "2017-12-12T15:07:58Z", "2017-12-12T15:12:56Z"],
    [77, "2018-02-28T21:57:13Z", "2018-03-01T22:10:56Z"]
]

SOURCE = "99988526423"

DESTINATION = "9933468278"

class AccountTests(APITestCase):
    def test_create_call_meta(self):
        url = reverse('call-meta-list')

        for call_meta in DATA:
            response = self.client.post(url, {
                "rtype": models.CallMeta.RegistryType.BEGIN,
                "call_id": call_meta[0],
                "timestamp": dt.datetime.fromisoformat(call_meta[1]),
                "source": SOURCE,
                "destination": DESTINATION
            })
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            response = self.client.post(url, {
                "rtype": models.CallMeta.RegistryType.END,
                "call_id": call_meta[0],
                "timestamp": dt.datetime.fromisoformat(call_meta[2]),
            })
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
