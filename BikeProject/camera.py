from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2
from kivy.core.window import Window
import pyzbar.pyzbar as pyzbar

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
        on_press: root.camera()
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'profile'

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Profile'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'home'


<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Finish Ride!!!'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'home'

"""


class HomeScreen(Screen):
    def __init__(self, **kwargs):                                  #super(name,id,address)
        super(HomeScreen, self).__init__(**kwargs)
        self.cap = cv2.VideoCapture(0)
    # def clock(self):
    #     screen=UploadScreen()
    # def cont(self):
    #     a=self.camera() #b1
    #     bytearra=['b1','b2']
    #     for i in bytearra:
    #         if(a==i):
    #             self.clock()

    def camera(self):
        # if kivy-opencv works then import settings of that here
        # isi ko bana na hy proper
        # pages bhi isi main define hongy
        font = cv2.FONT_HERSHEY_PLAIN
        while True:
            _, frame = self.cap.read()
            decodedObjects = pyzbar.decode(frame)

            for obj in decodedObjects:
                # print("Data", obj.data)
                cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                            (255, 0, 0), 3)
                self.cap.release()
                cv2.destroyAllWindows()
                ret=str(obj.data)
                print(ret)
                # return ret


            cv2.imshow("Frame", frame)

            key = cv2.waitKey(1)
            if key == 27:
                break
            #return ret
        # When everything done, release the capture

        # self.manager.current = self.manager.current('home')


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))

Window.size = (360, 600)


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()