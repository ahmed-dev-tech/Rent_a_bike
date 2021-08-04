from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatButton
from KV import Kv
import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np 
Kv='''
Screen:
    MDRoundFlatButton:
        text:"Add A bike"
        text_color: 0, 0, 1, 1
        md_bg_color: 1, 1, 0, 0.95
        pos_hint: {"center_x": .5, "center_y": .7}
    MDRoundFlatButton:
        name:"rb"
        text:"Ride A bike"
        text_color: 0, 0, 1, 1
        md_bg_color: 1, 1, 0, 0.95
        pos_hint: {"center_x": .5, "center_y": .5}
    
'''
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style="Dark"
        s=Screen()
        s.add_widget(Builder.load_string(Kv))
        s.add_widget(MDRoundFlatButton(name='rb',on_release=self.reader,text="Ride A bike"
        ,pos_hint={"center_x": .5, "center_y": .5},text_color= (0, 0, 1, 1),
        md_bg_color= (1, 1, 0, 0.95)))
        s.add_widget(MDRoundFlatButton(name='ab',on_release=self.hello1,text="Add A bike"
        ,pos_hint={"center_x": .5, "center_y": .7},text_color= (0, 0, 1, 1),
        md_bg_color= (1, 1, 0, 0.95)))

        return s
    def reader(self,obj):
        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_PLAIN
        while True:
            _, frame = cap.read()

            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                cv2.putText(frame, str("SucessFuly Unlock"), (50, 50), font, 2,(255, 0, 0), 3)
                #True for Timer 
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
    def hello1(self,obj):
        print("Run a QR code generator")
MainApp().run()