from Utilities.mqttClient import MQTT
from Utilities.modbusRS485 import ModbusRS485
from Scheduler.scheduler import Scheduler
from PrivateTasks.private_handleDevice import HandleDevice
# from private_handleDevice import HandleDevice
import time
import schedule
class HandleAuto:
    def __init__(self, _client : MQTT, _ser : ModbusRS485, _scheduler : Scheduler, _device : HandleDevice):
        self.client = _client
        self.ser = _ser
        self.scheduler = _scheduler
        self.device = _device
        self.topicV12 = self.client.username + self.client.topics[8]
        self.topicV13 = self.client.username + self.client.topics[9]
        self.topicV14 = self.client.username + self.client.topics[10]
        self.topic = None
        self.payload = ""
        self.taskID_daily_mixer1 = None
        self.taskID_weekly_mixer1 = None

        self.area = None

    def start(self):
        if self.client.isHaveDataFromServer():
            self.topic = self.client.getTopicServer()
            self.payload = self.client.getPayloadServer()
            if self.topic == self.topicV12:
                self.setAutoMixer1()
            if self.topic == self.topicV13:
                self.setAutoMixer2()
            if self.topic == self.topicV14:
                self.setAutoMixer3()

    def setAutoMixer1(self):
        split_list = self.payload.split(",")
        type_sch = split_list[0]
        time_sch = split_list[1]
        self.area = split_list[2]
        if type_sch == "once":
            schedule.every().day.at(time_sch).do(self.runAutoMixer1)
            schedule.run_pending()
        
        if type_sch == "daily":
            schedule.every().day.at(time_sch).do(self.runAutoMixer1)
            self.taskID_daily_mixer1 = self.scheduler.SCH_Add_Task(schedule.run_pending, 1, 1000)
        else:
            self.endlAutoMixer1()

        if type_sch == "weekly":
            schedule.every().week.at(time_sch).do(self.runAutoMixer1)
            self.taskID_weekly_mixer1 = self.scheduler.SCH_Add_Task(schedule.run_pending, 1, 1000)
        else:
            self.endlAutoMixer1()

    def runAutoMixer1(self):
        if self.device.getStateMixer1() == False:
            self.client.client.publish(self.client.username + self.client.topics[0], "1")
            if self.area == "1":
                self.client.client.publish(self.client.username + self.client.topics[4], "1")
            if self.area == "2":
                self.client.client.publish(self.client.username + self.client.topics[5], "1")
            if self.area == "3":
                self.client.client.publish(self.client.username + self.client.topics[6], "1")
            self.scheduler.SCH_Add_Task(self.device.start, 1, 1000)

    def setAutoMixer2(self):
        split_list = self.payload.split(",")
        type_sch = split_list[0]
        time_sch = split_list[1]
        self.area = split_list[2]
        if type_sch == "once":
            schedule.every().day.at(time_sch).do(self.runAutoMixer2)
            schedule.run_pending()
        
        if type_sch == "daily":
            schedule.every().day.at(time_sch).do(self.runAutoMixer2)
            self.taskID_daily_mixer2 = self.scheduler.SCH_Add_Task(schedule.run_pending, 1, 1000)
        else:
            self.endlAutoMixer2()

        if type_sch == "weekly":
            schedule.every().week.at(time_sch).do(self.runAutoMixer2)
            self.taskID_weekly_mixer2 = self.scheduler.SCH_Add_Task(schedule.run_pending, 1, 1000)
        else:
            self.endlAutoMixer2()
        
    def runAutoMixer2(self):
        if self.device.getStateMixer2() == False:
            self.client.client.publish(self.client.username + self.client.topics[1], "1")
            if self.area == "1":
                self.client.client.publish(self.client.username + self.client.topics[4], "1")
            if self.area == "2":
                self.client.client.publish(self.client.username + self.client.topics[5], "1")
            if self.area == "3":
                self.client.client.publish(self.client.username + self.client.topics[6], "1")
            self.scheduler.SCH_Add_Task(self.device.start, 1, 1000)

    def setAutoMixer3(self):
        split_list = self.payload.split(",")
        type_sch = split_list[0]
        time_sch = split_list[1]
        self.area = split_list[2]
        if type_sch == "once":
            schedule.every().day.at(time_sch).do(self.runAutoMixer3)
            schedule.run_pending()
        
        if type_sch == "daily":
            schedule.every().day.at(time_sch).do(self.runAutoMixer3)
            self.taskID_daily_mixer3 = self.scheduler.SCH_Add_Task(schedule.run_pending, 1, 1000)
        else:
            self.endlAutoMixer3()

        if type_sch == "weekly":
            schedule.every().week.at(time_sch).do(self.runAutoMixer3)
            self.taskID_weekly_mixer3 = self.scheduler.SCH_Add_Task(schedule.run_pending, 1, 1000)
        else:
            self.endlAutoMixer3()

    def runAutoMixer3(self):
        if self.device.getStateMixer3() == False:
            self.client.client.publish(self.client.username + self.client.topics[2], "1")
            if self.area == "1":
                self.client.client.publish(self.client.username + self.client.topics[4], "1")
            if self.area == "2":
                self.client.client.publish(self.client.username + self.client.topics[5], "1")
            if self.area == "3":
                self.client.client.publish(self.client.username + self.client.topics[6], "1")
            self.scheduler.SCH_Add_Task(self.device.start, 1, 1000)

    def autoSet(self):
        if self.device.getStateMixer1() == True:
            self.client.client.publish(self.client.username + self.client.topics[6], "1")
            self.device.done_mixer1 = False
        if self.device.getStateMixer2() == True:
            self.client.client.publish(self.client.username + self.client.topics[6], "1")
            self.device.done_mixer2 = False
        if self.device.getStateMixer3() == True:
            self.client.client.publish(self.client.username + self.client.topics[6], "1")
            self.device.done_mixer3 = False

    def endlAutoMixer1(self):
        check = self.scheduler.SCH_Delete(self.taskID_daily_mixer1)
        if check == True:
            print("End auto mixer1 successfully")

    def endlAutoMixer2(self):
        check = self.scheduler.SCH_Delete(self.taskID_daily_mixer2)
        if check == True:
            print("End auto mixer2 successfully")

    def endlAutoMixer3(self):
        check = self.scheduler.SCH_Delete(self.taskID_daily_mixer3)
        if check == True:
            print("End auto mixer3 successfully")