from rest_framework import viewsets

from mainapp.models import CarMaker

from restapp.serializers import CarMakerSerializer


class CarMakerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CarMaker.objects.all()
    serializer_class = CarMakerSerializer
