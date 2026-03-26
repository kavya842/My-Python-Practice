class Whatsapp:
    def send(self):
        print('send')
class Text(Whatsapp):
    def send(self,msg):
        print(msg)
class Image(Whatsapp):
    def send(self,image):
        print('sending',image)
class Video(Whatsapp):
    def send(self):
        print('sending video')
obj1=Text()
obj1.send('hello kavya')
obj2=Image()
obj2.send(' image')



