from rest_framework import serializers

from mainapp.models import CarMaker


class CarMakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarMaker
        fields = ['make_id', 'make_display', 'make_is_common', 'make_country']
