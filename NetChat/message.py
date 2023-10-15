import json

class Message():
    time = 0
    text = ''
    type = ''
    senderName = ''
    senderIp = ''
    receiverName = ''
    receiverIp = ''

    def __init__(self, jsonstring): # '{"time": "03-10-2023", ....}'
        data = json.loads(jsonstring)
        self.time = data.get('time', 0)
        if 'senderIp' in data:
            self.senderIp = data['senderIp']
        if "senderName" in data:
            self.senderName = data['senderName']
        if "text" in data:
            self.text = data['text']
        if "receiverName" in data:
            self.receiverName = data['receiverName']
        if 'receiverIp' in data:
            self.receiverIp = data['receiverIp']
        if "type" in data:
            self.type = data['type']
    
    def toJson(self):
        data = {}
        data['time'] = self.time
        data['text'] = self.text
        data['type'] = self.type
        data['senderIp'] = self.senderIp
        data['senderName'] = self.senderName
        data['receiverName'] = self.receiverName
        data['receiverIp'] = self.receiverIp
        return json.dumps(data)
    
if '__main__' == __name__:
    msg = Message('{"text":"sender_name","time":50}')
    print(msg.toJson())