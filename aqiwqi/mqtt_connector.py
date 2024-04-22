# myapp/mqtt_connector.py
import paho.mqtt.client as mqtt
import django
from django.conf import settings


def start_mqtt_client():
    # Configure Django settings (if not already configured)
    if not settings.configured:
        django.setup()
        
    from aqiwqi.models import PMSData, MQ7Data, GPSData, PhSensor, TempSensor, TDSSensor

    MQTT_BROKER_HOST = "broker.hivemq.com"
    MQTT_BROKER_PORT = 1883
    MQTT_TOPICS = [
        "project2024gpsdata",
        "project2024pmsdata",
        "project2024mq7sensor",
        "project2024phsensor",
        "project2024tempsensor",
        "project2024tdssensor"
    ]

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
            for topic in MQTT_TOPICS:
                client.subscribe(topic)
        else:
            print("Failed to connect to MQTT broker with error code", rc)

    def on_message(client, userdata, msg):
        topic_name = msg.topic
        payload_value = msg.payload.decode()

        # Handle MQTT messages based on topic
        if topic_name == "project2024gpsdata":
            # Parse GPS data (assuming it's in format "longitude,latitude")
            gps_values = payload_value.split(',')
            if len(gps_values) >= 2:
                longitude = float(gps_values[0].strip())
                latitude = float(gps_values[1].strip())
                GPSData.objects.create(longitude=longitude, latitude=latitude)

        elif topic_name == "project2024pmsdata":
            # Parse PMS data (assuming it's in format "pm_1.0,pm_2.5,pm_10.0")
            pm_values = payload_value.split(',')
            if len(pm_values) >= 3:
                pm_1_0 = float(pm_values[0].strip())
                pm_2_5 = float(pm_values[1].strip())
                pm_10_0 = float(pm_values[2].strip())
                PMSData.objects.create(pm_1_0=pm_1_0, pm_2_5=pm_2_5, pm_10_0=pm_10_0)

        elif topic_name == "project2024mq7sensor":
            # Parse MQ7 sensor data
            mq7_data = float(payload_value.strip())
            MQ7Data.objects.create(mq7_data=mq7_data)

        elif topic_name == "project2024phsensor":
            # Parse pH sensor data
            ph_data = float(payload_value.strip())
            PhSensor.objects.create(ph_data=ph_data)

        elif topic_name == "project2024tempsensor":
            # Parse temperature sensor data
            temp = float(payload_value.strip())
            TempSensor.objects.create(temp=temp)

        elif topic_name == "project2024tdssensor":
            # Parse TDS sensor data
            tds = float(payload_value.strip())
            TDSSensor.objects.create(tds=tds)

        else:
            print(f"Ignored unknown topic: {topic_name}")

        print(f"Added new data entry for topic='{topic_name}', value='{payload_value}'")

    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)
    mqtt_client.loop_start()


