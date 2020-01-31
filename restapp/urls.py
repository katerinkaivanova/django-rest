from django.urls import path, include
from rest_framework import routers
from restapp import views


app_name = 'restapp'

router = routers.DefaultRouter()
router.register(r'car_makers', views.CarMakerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
