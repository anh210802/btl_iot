import paho.mqtt.client as mqtt


class MQTT:
    def __init__(self, host, port, username, password, topics):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.topics = topics
        self.client = mqtt.Client()
        self.client.username_pw_set(self.username, self.password)
        self.client.on_connect = self.mqtt_connect
        self.client.on_message = self.mqtt_message
        self.payload_server = ""
        self.topic_server = ""
        self.flag = 0

    def start(self):
        try:
            print(f"Connecting to server...")
            self.client.connect(self.host, self.port, 60)
            self.client.loop_forever()
        except Exception as e:
            print("An error occurred:", str(e))
    
    def mqtt_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to server successfully")
            for topic_name in self.topics:
                self.client.subscribe(self.username + topic_name)
                print(f"Subscribed to {topic_name}")
        else:
            print(f"Failed to connect, return code {rc}\n")

    def mqtt_message(self, client, userdata, message):
        print(f"Topic: {message.topic} :sent data: {message.payload.decode('utf-8')}")
        self.topic_server = message.topic
        self.payload_server = message.payload.decode('utf-8')
        self.flag = 1

    def isHaveDataFromServer(self):
         if self.flag == 1:
            self.flag = 0
            return 1
         return 0
                
    def getTopicServer(self):
        return self.topic_server
    
    def getPayloadServer(self):
        return self.payload_server
    