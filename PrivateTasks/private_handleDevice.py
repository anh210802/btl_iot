from Utilities.mqttClient import MQTT
from Utilities.modbusRS485 import ModbusRS485
from Scheduler.scheduler import Scheduler


class HandleDevice:
    def __init__(self, client: MQTT, ser: ModbusRS485, scheduler: Scheduler):
        self._client = client
        self.ser = ser
        self.scheduler = scheduler
        self.topic = ""
        self.payload = ""
        self.topicV1 = self._client.username + self._client.topics[0]
        self.topicV2 = self._client.username + self._client.topics[1]
        self.topicV3 = self._client.username + self._client.topics[2]
        self.topicV4 = self._client.username + self._client.topics[3]
        self.topicV5 = self._client.username + self._client.topics[4]
        self.topicV6 = self._client.username + self._client.topics[5]
        self.topicV7 = self._client.username + self._client.topics[6]
        self.topicV8 = self._client.username + self._client.topics[7]
        
        self.count_mixer1 = 0
        self.state_mixer1 = None
        self.taskID_mixer1 = None
        self.done_mixer1 = False
        
        self.count_mixer2 = 0
        self.state_mixer2 = None
        self.taskID_mixer2 = None
        self.done_mixer2 = False
        
        self.count_mixer3 = 0
        self.state_mixer3 = None
        self.taskID_mixer3 = None
        self.done_mixer3 = False

        self.count_area1 = 0
        self.state_area1 = None
        self.taskID_area1 = None
        
        self.count_area2 = 0
        self.state_area2 = None
        self.taskID_area2 = None
        
        self.count_area3 = 0
        self.state_area3 = None
        self.taskID_area3 = None
        
        self.count_pump_in = 0
        self.state_pump_in = None
        self.taskID_pump_in = None
        self.done_pump_in = False
        
        self.count_pump_out = 0
        self.state_pump_out = None
        self.taskID_pump_out = None
        self.done_pump_out = False
        
    def start(self):
        if self._client.isHaveDataFromServer():
            self.topic = self._client.getTopicServer()
            self.payload = self._client.getPayloadServer()
            self.setDevice()

    def setDevice(self):
        try:
            if self.topic == self.topicV1:
                if self.payload == "1":
                    self.state_mixer1 = True
                    self.taskID_mixer1 = self.scheduler.SCH_Add_Task(self.mixer1Run, 1, 1000)
                else:
                    self.state_mixer1 = False

            if self.topic == self.topicV2:
                if self.payload == "1":
                    self.state_mixer2 = True
                    self.taskID_mixer2 = self.scheduler.SCH_Add_Task(self.mixer2Run, 1, 1000)
                else:
                    self.state_mixer2 = False

            if self.topic == self.topicV3:
                if self.payload == "1":
                    self.state_mixer3 = True
                    self.taskID_mixer3 = self.scheduler.SCH_Add_Task(self.mixer3Run, 1, 1000)
                else:
                    self.state_mixer3 = False

            if self.topic == self.topicV4:
                if self.payload == "1":
                    self.state_area1 = True
                    self.taskID_area1 = self.scheduler.SCH_Add_Task(self.selectArea1, 3, 1000)
                else:
                    self.state_area1 = False

            if self.topic == self.topicV5:
                if self.payload == "1":
                    self.state_area2 = True
                    self.taskID_area2 = self.scheduler.SCH_Add_Task(self.selectArea2, 3, 1000)
                else:
                    self.state_area2 = False

            if self.topic == self.topicV6:
                if self.payload == "1":
                    self.state_area3 = True
                    self.taskID_area3 = self.scheduler.SCH_Add_Task(self.selectArea3, 3, 1000)
                else:
                    self.state_area3 = False
            
            if self.topic == self.topicV7:
                if self.payload == "1":
                    self.state_pump_in = True
                    self.taskID_pump_in = self.scheduler.SCH_Add_Task(self.pumpIn, 2, 1000)
                else:
                    self.state_pump_in = False
            
            if self.topic == self.topicV8:
                if self.payload == "1":
                    self.state_pump_out = True
                    self.taskID_pump_out = self.scheduler.SCH_Add_Task(self.pumpOut, 4, 1000)
                else:
                    self.state_pump_out = False
        except Exception as e:
            print(f"Error in setDevice: {e}")

    def mixer1Run(self):
        if self.state_mixer1 == True:
            if self.count_mixer1 == 0:
                print(f"SYSTEM: Run mixer1")
                self._client.client.publish("btl_iot_server/feeds/V15", "Run")  
                value = self.ser.setDevice1(True)
                self._client.client.publish("btl_iot_server/feeds/V9", value)
            self.count_mixer1 += 1
            # if self.count_mixer1 >= 10 or value >= 20:
            if self.count_mixer1 >= 10:
                self.state_mixer1 = False
                self._client.client.publish(self.topicV1, "0")
        else:
            check = self.scheduler.SCH_Delete(self.taskID_mixer1)
            if check == True:
                print(f"SYSTEM: Stop mixer1")
                self.taskID_mixer1 = None
                self.count_mixer1 = 0
                self.done_mixer1 = True
                value = self.ser.setDevice1(False)
                self._client.client.publish("btl_iot_server/feeds/V9", value)
                self._client.client.publish("btl_iot_server/feeds/V15", "Done")
    
    def mixer2Run(self):
        if self.state_mixer2 == True:
            if self.count_mixer2 == 0:
                print(f"SYSTEM: Run mixer2")
                self._client.client.publish("btl_iot_server/feeds/V16", "Run")
                value = self.ser.setDevice2(True)
                self._client.client.publish("btl_iot_server/feeds/V10", value)
            self.count_mixer2 += 1
            # if self.count_mixer2 >= 10 or value >= 20:
            if self.count_mixer2 >= 10:
                self.state_mixer2 = False
                self._client.client.publish(self.topicV2, "0")
        else:
            check = self.scheduler.SCH_Delete(self.taskID_mixer2)
            if check == True:
                print(f"SYSTEM: Stop mixer2")
                self.taskID_mixer2 = None
                self.count_mixer2 = 0
                self.done_mixer2 = True
                value = self.ser.setDevice2(False)
                self._client.client.publish("btl_iot_server/feeds/V10", value)
                self._client.client.publish("btl_iot_server/feeds/V16", "Done")

    def mixer3Run(self):
        if self.state_mixer3 == True:
            if self.count_mixer3 == 0:
                print(f"SYSTEM: Run mixer3")
                self._client.client.publish("btl_iot_server/feeds/V17", "Run") 
                value = self.ser.setDevice3(True)
                self._client.client.publish("btl_iot_server/feeds/V11", value)
            self.count_mixer3 += 1 
            # if self.count_mixer3 >= 10 or value >= 20:
            if self.count_mixer3 >= 10:
                self.state_mixer3 = False
                self._client.client.publish(self.topicV3, "0")
        else:
            check = self.scheduler.SCH_Delete(self.taskID_mixer3)
            if check == True:
                print(f"SYSTEM: Stop mixer3")
                self.taskID_mixer3 = None
                self.count_mixer3 = 0
                self.done_mixer3 = True
                value = self.ser.setDevice3(False)
                self._client.client.publish("btl_iot_server/feeds/V11", value)
                self._client.client.publish("btl_iot_server/feeds/V17", "Done")

    def selectArea1(self):
        if self.state_area1 == True:
            if self.count_area1 == 0:
                print("SYSTEM: Selected area 1")
                self.ser.setDevice4(True)
            self.count_area1 += 1
        else:
            check = self.scheduler.SCH_Delete(self.taskID_area1)
            if check == True:
                self.count_area1 = 0
                self.ser.setDevice6(False)
                print("SYSTEM: Cancel selection area 1")
                self._client.client.publish(self.topicV4, "0")
    
    def selectArea2(self):
        if self.state_area2 == True:
            if self.count_area2 == 0:
                print("SYSTEM: Selected area 2")
                self.ser.setDevice5(True)
            self.count_area2 += 1
        else:
            check = self.scheduler.SCH_Delete(self.taskID_area2)
            if check == True:
                self.count_area2 = 0
                self.ser.setDevice6(False)
                print("SYSTEM: Cancel selection area 2")
                self._client.client.publish(self.topicV5, "0")

    def selectArea3(self):
        if self.state_area3 == True:
            if self.count_area3 == 0:
                print("SYSTEM: Selected area 3")
                self.ser.setDevice6(True)
            self.count_area3 += 1
        else:
            check = self.scheduler.SCH_Delete(self.taskID_area3)
            if check == True:
                self.count_area3 = 0
                self.ser.setDevice6(False)
                print("SYSTEM: Cancel selection area 3")
                self._client.client.publish(self.topicV6, "0")

    def pumpIn(self):
        if self.state_pump_in == True:
            if self.state_pump_in == 0:
                print("SYSTEM: Pump in is start")
                self.ser.setDevice7(True)
            self.count_pump_in += 1
            if self.count_pump_in >= 20:
                self.state_pump_in = False
                self._client.client.publish(self.topicV7, "0")
        else:
            check = self.scheduler.SCH_Delete(self.taskID_pump_in)
            if check == True:
                print(f"SYSTEM: Pump in from tank is stop")
                self.taskID_pump_in = None
                self.count_pump_in = 0
                self.done_pump_in = True
                self.ser.setDevice7(False)

    def pumpOut(self):
        if self.state_pump_out == True:
            if self.state_pump_out == 0:
                print("SYSTEM: Pump out is start")
                self.ser.setDevice8(True)
            self.count_pump_out += 1
            if self.count_pump_out >= 30:
                self.state_pump_out = False
                self._client.client.publish(self.topicV8, "0")
        else:
            check = self.scheduler.SCH_Delete(self.taskID_pump_in)
            if check == True:
                print(f"SYSTEM: Pump in from tank is stop")
                self.taskID_pump_out = None
                self.count_pump_out = 0
                self.ser.setDevice8(False)
                if self.state_area1 == True:
                    self.state_area1 = False
                if self.state_area2 == True:
                    self.state_area2 = False
                if self.state_area3 == True:
                    self.state_area3 = False
                if self.done_mixer1 == True:
                    self.done_mixer1 = False
                if self.done_mixer2 == True:
                    self.done_mixer2 = False
                if self.done_mixer3 == True:
                    self.done_mixer3 = False
                self.done_pump_out = True
    
    def getStateMixer1(self):
        return self.done_mixer1
    
    def getStateMixer2(self):
        return self.done_mixer2
    
    def getStateMixer3(self):
        return self.done_mixer3
    
    def getStatePumpIn(self):
        return self.done_pump_in
    
    def getStatePumpOut(self):
        return self.done_pump_out