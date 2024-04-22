from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .mqtt_connector import start_mqtt_client
from .models import PMSData, MQ7Data, GPSData, PhSensor, TempSensor, TDSSensor
from .utils import calculate_wqi,calculate_aqi,predict_aqi,predict_wqi
from django.http import HttpResponse

# Create your views here.
@csrf_exempt 
def front_page(request):

    return render(request,'front_page.html')


def home_page(request):
    start_mqtt_client()
    
    # Fetch the latest sensor data for air quality
    last_pms_data = PMSData.objects.last()
    last_mq7_data = MQ7Data.objects.last()
    
    # Calculate Air Quality Index (AQI)
    last_aqi = None
    predicted_aqi = None
    if last_pms_data and last_mq7_data:
        last_aqi = calculate_aqi(last_pms_data.pm_2_5, last_pms_data.pm_10_0, last_mq7_data.mq7_data)
        predicted_aqi = predict_aqi(last_pms_data.pm_2_5, last_pms_data.pm_10_0, last_mq7_data.mq7_data)
    
    # Fetch the latest sensor data for water quality
    last_ph_sensor = PhSensor.objects.last()
    last_temp_sensor = TempSensor.objects.last()
    last_tds_sensor = TDSSensor.objects.last()
    
    # Calculate Water Quality Index (WQI)
    last_wqi = None
    predicted_wqi = None
    if last_tds_sensor and last_temp_sensor and last_ph_sensor:
        last_wqi = calculate_wqi(last_tds_sensor.tds, last_temp_sensor.temp, last_ph_sensor.ph_data)
        predicted_wqi = predict_wqi(last_ph_sensor.ph_data, last_temp_sensor.temp, last_tds_sensor.tds)
    
    context = {
        'last_pms_data': last_pms_data,
        'last_mq7_data': last_mq7_data,
        'last_aqi': last_aqi,
        'predicted_aqi': predicted_aqi,
        'last_gps_data': GPSData.objects.last(),
        'last_ph_sensor': last_ph_sensor,
        'last_temp_sensor': last_temp_sensor,
        'last_tds_sensor': last_tds_sensor,
        'last_wqi': last_wqi,
        'predicted_wqi': predicted_wqi,
    }
    
    return render(request, 'home_page.html', context)

