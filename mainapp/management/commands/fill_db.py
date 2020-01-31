import os
import json

from django.core.management.base import BaseCommand
from mainapp.models import CarMaker


JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        car_makers = load_from_json('car_makers')

        CarMaker.objects.all().delete()

        for car_maker in car_makers:
            new_car_maker = CarMaker(**car_maker)
            new_car_maker.save()
