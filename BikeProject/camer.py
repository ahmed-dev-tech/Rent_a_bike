from kivymd.app import MDApp
#from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2
from kivy.core.window import Window
import pyzbar.pyzbar as pyzbar
from kivy.properties import NumericProperty 
from kivy.clock import Clock
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRectangleFlatButton

screen_helper = """
ScreenManager:
    HomeScreen:
    ProfileScreen:
    UploadScreen:
<HomeScreen>:
    name: 'home'
    MDRectangleFlatButton:
        text: 'Ride A Bike'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        #on_press: root.manager.current = 'profile'
        on_press: root.camera()
        on_press: root.start() 
    MDLabel:
        text: str(round(root.number)) 
	    text_size: self.size 
	    halign: 'center' 
	    valign: 'middle'
    MDRectangleFlatButton:
        text: 'Add A Bike'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'profile'
<ProfileScreen>:
    name: 'profile'
    # MDLabel:
    #     text: str(round(root.number)) 
		# text_size: self.size 
		# halign: 'center' 
		# valign: 'middle' 
    # MDRectangleFlatButton:
    #     text: 'Start'
    #     pos_hint: {'center_x':0.5,'center_y':0.1}
    #     on_press:root.start()
    #     
    # MDRectangleFlatButton:
    #     text: 'Stop'
    #     pos_hint: {'center_x':0.5,'center_y':0.2}
    #     on_press: root.stop()
    # MDRectangleFlatButton:
    #     text: 'Fare Calculation'
    #     pos_hint: {'center_x':0.5,'center_y':0.3}
    #     on_press: root.manager.current = 'upload'


<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Your Calculated fare is '
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'home'

"""


class ProfileScreen(Screen):
    # number = NumericProperty()
    # def _init_(self, **kwargs):
    #     # The super() builtin
    #     # returns a proxy object that
    #     # allows you to refer parent class by 'super'.
    #     super(ProfileScreen, self)._init_(**kwargs)
    #
    #     # Create the clock and increment the time by .1 ie 1 second.
    #     Clock.schedule_interval(self.increment_time, .1)
    #
    #     self.increment_time(0)
    #
    # def increment_time(self, interval):
    #     self.number += .1
    #
    # def start(self):
    #     Clock.unschedule(self.increment_time)
    #     Clock.schedule_interval(self.increment_time, .1)
    #
    # # To stop the count / time
    # def stop(self):
    #     Clock.unschedule(self.increment_time)
    pass
class HomeScreen(Screen):
    number = NumericProperty()
    def __init__(self, **kwargs):                                  #super(name,id,address)
        super(HomeScreen, self).__init__(**kwargs)
        Clock.schedule_interval(self.increment_time, .1)
        self.increment_time(0)
    def camera(self):
        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_PLAIN
        while True:
            _, frame = cap.read()
            decodedObjects = pyzbar.decode(frame)
            i=''
            for obj in decodedObjects:
                # print("Data", obj.data)
                i+=str(obj.data)
                cv2.putText(frame, str(obj.data), (50, 50), font, 2, (255, 0, 0), 3)
                print(i)
            if i==str(b'rafiq'):
                cv2.putText(frame, str(i), (50, 50), font, 2, (255, 0, 0), 3)
                break
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == 27:
                 break
        cap.release()
        cv2.destroyAllWindows()

    def increment_time(self, interval):
        self.number += .1

    def start(self):
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, .1)

        # To stop the count / time
    def stop(self):
        Clock.unschedule(self.increment_time)

        #DemoApp.star(self)
class UploadScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))

Window.size = (360, 600)


class Bike(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_helper)
        return screen
    # def on_start(self):
    #     HomeScreen().camera()

Bike().run()