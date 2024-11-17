from django.core.management.base import BaseCommand, CommandError
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

class Command(BaseCommand):
    # help = "Populate database with mocked data"

    def handle(self, *args, **kwargs):
        for row in DATA:
            models.CallMeta.objects.create(
                call_id=row[0],
                timestamp=row[1],
                rtype=models.CallMeta.RegistryType.BEGIN,
                source=SOURCE,
                destination=DESTINATION
            )
            models.CallMeta.objects.create(
                call_id=row[0],
                timestamp=row[2],
                rtype=models.CallMeta.RegistryType.END
            )
