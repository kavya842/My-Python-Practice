class Whatsapp:
    phcall="voicecall"
    messages="whatsapp messages"
    camera="photos"
    def __init__(self,messages,voicecall,videocall,status):
        self.messages=messages
        self.voicecall=voicecall
        self.videocall=videocall
        self.status=status
    def disp(self):
        print(self.messages,self.voicecall,self.videocall,self.status)
class Update_whatsapp(Whatsapp):
    def __init__(self,messages,voicecall,videocall,status,songforstatus,screenshare,onetapimagesorviedos):
        super(). __init__(messages,voicecall,videocall,status)
        self.songforstatus=songforstatus
        self.screenshare=screenshare
        self.onetapimagesorviedos=onetapimagesorviedos
    def disp(self):
        super().disp()
        print(self.songforstatus,self.screenshare,self.onetapimagesorviedos)
Up=Update_whatsapp("end to end messages :","voice call:","viedocall:","images:","song for image:","sharing the screen:","sending images for once:")
Up.disp()
