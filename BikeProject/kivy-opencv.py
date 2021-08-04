from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.lang import Builder
import cv2
import pyzbar.pyzbar as pyzbar
from kivy.core.window import Window

Kv='''
Screen:
    MDRoundFlatButton:
        text:"Add A bike"
        text_color: 0, 0, 1, 1
        md_bg_color: 1, 1, 0, 0.95
        pos_hint: {"center_x": .5, "center_y": .7}
        on_press:app.reader()
    MDRoundFlatButton:
        name:"rb"
        text:"Ride A bike"
        text_color: 0, 0, 1, 1
        md_bg_color: 1, 1, 0, 0.95
        pos_hint: {"center_x": .5, "center_y": .5}
    
'''
Window.size=(360,600)
class CamApp(App):

    def build(self):
        self.img1=Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        #add_button for clock start / add another button from layout
        layout.add_widget(Builder.load_string(Kv))
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.reader, 1.0/33.0)
        return layout
    def reader(self):
        self.capture = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_PLAIN
        while True:
            _, frame = self.capture.read()

            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                cv2.putText(frame, str("SucessFuly Unlock"), (50, 50), font, 2,(255, 0, 0), 3)
                #True for Timer 
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == 27:
                break


    # def update(self, dt):
    #     # display image from cam in opencv window
    #     ret, frame = self.capture.read()
    #     cv2.imshow("CV2 Image", frame)
    #     # convert it to texture
    #     buf1 = cv2.flip(frame, 0)
    #     buf = buf1.tostring()
    #     texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr') 
    #     #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer. 
    #     texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
    #     # display image from the texture
    #     self.img1.texture = texture1
CamApp().run()
cv2.destroyAllWindows()