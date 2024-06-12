from Utilities.mqttClient import MQTT
from Utilities.modbusRS485 import ModbusRS485
import time

TEMP_TOPIC = "btl_iot_server/feeds/V18"
HUMI_TOPIC = "btl_iot_server/feeds/V19"

class HandleTempHumi:
    def __init__(self, client: MQTT, ser: ModbusRS485):
        self.client = client
        self.ser = ser

    def readValue(self):
        self.ser.readTempAndHumi()
        temp_value = self.ser.getTemp() / 100
        print("Temp: ", temp_value)
        self.client.client.publish(TEMP_TOPIC, temp_value)
        time.sleep(1)
        humi_value = self.ser.getHumi()
        print("Humi:", humi_value)
        self.client.client.publish(HUMI_TOPIC, humi_value)