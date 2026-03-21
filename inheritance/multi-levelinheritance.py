class Whatsapp:
    def __init__(self,messages,voicecall,videocall,status):
        self.messages=messages
        self.voicecall=voicecall
        self.videocall=videocall
        self.status=status
    def disp(self):
        print(self.messages,self.voicecall,self.videocall,self.status)

class Update_whatsapp(Whatsapp):
    def __init__(self,messages,voicecall,videocall,status,songforstatus,screenshare,onetapimages):
        super(). __init__(messages,voicecall,videocall,status)
        self.songforstatus=songforstatus
        self.screenshare=screenshare
        self.onetapimages=onetapimages
    def disp(self):
        super().disp()
        print("Updated Features:")
        print(self.songforstatus,self.screenshare,self.onetapimages)

class Latest_whatsapp(Update_whatsapp):
    def __init__(self,messages,voicecall,videocall,status,songforstatus,screenshare,onetapimages,ai_chat):
        super().__init__(messages,voicecall,videocall,status,songforstatus,screenshare,onetapimages)
        self.ai_chat = ai_chat
    def disp(self):
        super().disp()
        print("Latest Features")
        print(self.ai_chat)
Up=Latest_whatsapp("end to end messages","voice call","viedocall","images","song for image","sharing the screen","sending images for once","ai_chat")
Up.disp()