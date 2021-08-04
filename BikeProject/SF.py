from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2
from kivy.core.window import Window
import pyzbar.pyzbar as pyzbar
from kivy.properties import NumericProperty 
from kivy.clock import Clock
import qrcode

screen_helper = """
ScreenManager:
    HomeScreen:
    ScanScreen:
    FareScreen:
    AddBikeScreen:
    FileSaveScreen:
<HomeScreen>:
    name: 'home'
    MDRectangleFlatButton:
        text: 'Ride A Bike'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'scan'
        on_press:app.stop()
        on_press:app.back()
    MDRectangleFlatButton:
        text: 'Add A Bike'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'add bike'
<ScanScreen>:
    name: 'scan'
    MDLabel:
        id:num
        text: str(round(app.number)) 
		text_size: self.size 
		halign: 'center' 
		valign: 'middle'      
    MDRectangleFlatButton:
        text: 'Scan Here'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: root.camera()
        on_press:app.Start1()
    MDRectangleFlatButton:
        text: 'Finish The Ride'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_release: root.manager.current = 'fare'
        on_press: app.stop()
        on_release: app.FareCal()
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_release:root.manager.current = 'home'
        on_release:app.stop()
        on_release:app.back()

    
<FareScreen>:
    name: 'fare'
    MDLabel:
        text: 'Your Calculated fare is '
        valign: 'center'
        halign:'center'
    MDRectangleFlatButton:
        id:fc
        text: str(round(app.number))
        pos_hint: {'center_x':0.5,'center_y':0.3}
        #on_press:app.FareCal()

<AddBikeScreen>
    name: 'add bike'
    MDTextField:
        id: qr
        hint_text: "Enter Your Bike"
        helper_text: "This will do something"
        helper_text_mode:"on_focus"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        size_hint_x: None
        width:300
    MDRectangleFlatButton:
        text: 'Generate QR Code'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_release:app.qrGenerator()
        on_release:root.manager.current = 'save screen'

<FileSaveScreen>
    name: 'save screen'
    MDLabel
        text:"You have Add bike's QR Code"
        valign: 'center'
        halign:'center'
    MDRectangleFlatButton:
        text: 'Add Another Bike!!!'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_release:root.manager.current = 'add bike'
    MDRectangleFlatButton:
        text: 'Back To Home Screen'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_release:root.manager.current = 'home'
        #on_release: yahan "add bike ka text null krna hy "
"""


class ScanScreen(Screen):
    
    def __init__(self, **kwargs):                                  #super(name,id,address)
        super(ScanScreen, self).__init__(**kwargs)
    def camera(self):
        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_PLAIN
        file = open("data.txt", "r")
        check = file.read().split(',')
        print(check)
        flag=True
        while flag:
            _, frame = cap.read()
            decodedObjects = pyzbar.decode(frame)
            i=''
            print(check)
            for obj in decodedObjects:
                i=str(obj.data)
                cv2.putText(frame, str(obj.data), (50, 50), font, 2, (255, 0, 0), 3)
                print(i[2:-1])
                print(check)
                for itr in range(len(check)):
                    if  check[itr] == str(i[2:-1]):
                        print("andar")
                        cv2.putText(frame, str(i), (50, 50), font, 2, (255, 0, 0), 3)
                        flag=False
                        break
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == 27:
                cap.release()
                cv2.destroyAllWindows()
                self.manager.current='home'
                break
        cap.release()
        cv2.destroyAllWindows()
class HomeScreen(Screen):
    pass
class FareScreen(Screen):
    pass
class AddBikeScreen(Screen):
    pass
class FileSaveScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(ScanScreen(name='scan'))
sm.add_widget(FareScreen(name='fare'))

Window.size = (360, 600)


class Bike(MDApp):
    count=0
    number = NumericProperty()
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(screen_helper)
        return self.screen
    def clock(self):
        
        Clock.schedule_interval(self.increment_time, .1)
        self.increment_time(0)

    def increment_time(self, interval):
        self.number += .1

    def start(self):
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, .1)

    # To stop the count / time
    def stop(self):
        Clock.unschedule(self.increment_time)
    def Start1(self):
        self.start()
    def back(self):
        self.number=0
        self.screen.get_screen('scan').ids.num.text=str(self.number)
    def FareCal(self):
        self.number+=100
        self.screen.get_screen('fare').ids.fc.text=str(round(self.number))
    def qrGenerator(self):
        self.qr=qrcode.QRCode(version=1,box_size=10,border=5)
        self.data=self.screen.get_screen('add bike').ids.qr.text
        file = open('data.txt', 'a')
        file.write(self.data)
        file.write(",")
        file.close()
        self.count+=1
        print(self.count)
        self.qr.add_data(self.data)
        self.img=self.qr.make_image(fill="black",back_color="white")
        file = open("namefile.txt", "a")
        file.write("\n")
        file.write(str(self.count))
        file.close()
        file = open("namefile.txt", "r")
        lines = file.read().splitlines()
        last_line = lines[-1]
        print(last_line)
        self.img.save("{}.png".format(last_line))



Bike().run()