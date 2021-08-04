from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatButton
from KV import Kv
from kivy.core.window import Window
import cv2
Window.size = (360,600)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style="Dark"
        s=Screen()
        s.add_widget(Builder.load_string(Kv))
        s.add_widget(MDRoundFlatButton(name='rb',on_release=self.hello,text="Ride A bike"
        ,pos_hint={"center_x": .5, "center_y": .5},text_color= (0, 0, 1, 1),
        md_bg_color= (1, 1, 0, 0.95)))
        s.add_widget(MDRoundFlatButton(name='ab',on_release=self.hello1,text="Add A bike"
        ,pos_hint={"center_x": .5, "center_y": .7},text_color= (0, 0, 1, 1),
        md_bg_color= (1, 1, 0, 0.95)))

        return s
    def hello1(self,obj):
        print("hello world")
    def hello(self,obj):
        screen2= Screen()
        cap = cv2.VideoCapture(0)
        screen2.add_widget(cap)
       

        while(True):
        # Capture frame-by-frame
            ret, frame = cap.read()

        # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
            cv2.imshow('frame',gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
MainApp().run()