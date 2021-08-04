from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import cv2
from kivy.core.window import Window
import pyzbar.pyzbar as pyzbar
from kivy.properties import NumericProperty 
from kivy.clock import Clock
import qrcode
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
import json

screen_helper = """
ScreenManager:
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    SignupScreen:
    HomeScreen:
    ScanScreen:
    FareScreen:
    AddBikeScreen:
    FileSaveScreen:

<WelcomeScreen>:
    name:'welcomescreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDLabel:
        text:'&'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.7}
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.5}
    MDRaisedButton:
        text:'Login'
        pos_hint : {'center_x':0.4,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press: 
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        text:'Signup'
        pos_hint : {'center_x':0.6,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'left'
        
<LoginScreen>:
    name:'loginscreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        
        id:login_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Login'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.login()
            #root.manager.current= 'home'

            # app.username_changer() 
            
        
    MDTextButton:
        text: 'Create an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'up'
<SignupScreen>:
    name:'signupscreen'
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.75,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()
    MDTextButton:
        text: 'Already have an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'
    
    
<MainScreen>:
    name: 'mainscreen'
    MDLabel:
        id:username_info
        text:'Hello Main'
        font_style:'H1'
        halign:'center'
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
class WelcomeScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(ScanScreen(name='scan'))
sm.add_widget(FareScreen(name='fare'))
sm.add_widget(WelcomeScreen(name = 'loginscreen'))
sm.add_widget(MainScreen(name = 'mainscreen'))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))
Window.size = (360, 600)


class Bike(MDApp):
    count=0
    number = NumericProperty()
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(screen_helper)
    #1    self.url = "https://bike-a3965.firebaseio.com/.json"
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
    def signup(self):
        signupEmail = self.screen.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.screen.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.screen.get_screen('signupscreen').ids.signup_username.text
        #make a field for Wallet here and in Help_str
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split())>1:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Username',text = 'Please enter username without space',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail,signupPassword)
            signup_info = str({f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".","-")
            signup_info = signup_info.replace("\'","")
            self.to_database = json.loads(signup_info)
        #2  requests.patch(url = self.url,json = self.to_database)
            self.screen.get_screen('loginscreen').manager.current= 'loginscreen'
        auth='H9aTijr46WRCPbXVYYPC7JDIT6lKL2OvwY0lJy1z'
    def login(self):
        loginEmail = self.screen.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.screen.get_screen('loginscreen').ids.login_password.text
        self.login_check = False
        supported_loginEmail = loginEmail.replace('.','-')
        supported_loginPassword = loginPassword.replace('.','-')
        print(supported_loginEmail,supported_loginPassword)
    #3  request  = requests.get(self.url+'?auth='+self.auth)
    #4  data = request.json()      
        data= self.to_database
        emails=set()
        for key,value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check=True
            self.screen.get_screen('home').manager.current = 'home'
        else:
            print("user no longer exists")
    def close_username_dialog(self,obj):
        self.dialog.dismiss()
    def username_changer(self):
        if self.login_check:
            self.strng.get_screen('home').manager.current = 'home'

'''
design changes iss main copy kr dyna 
User login ky variables use kr sakty ho or wallet bhi bana lyna 
line 322,386,396,397 ko uncomment for fireBase user auth
'''
Bike().run()