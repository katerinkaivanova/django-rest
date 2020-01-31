from django.urls import path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.CarMakerListView.as_view(), name='car_makers'),
]
