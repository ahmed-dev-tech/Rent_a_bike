"""
helper_builder= 
ScreenManager:    
    AddBike2:
<AddBike2>:
    name:
        'hey'
    MDRoundFlatButton:
        text:"Ride A bike"
        font_style : 'H1'
        text_color: 0, 0, 1, 1
        md_bg_color: 1, 1, 0, 1
        pos_hint: {"center_x": .5, "center_y": .6}   

helper_builder1= 
ScreenManager:    
    AddBike1:
<AddBike1>:
    name:
        'hello'
    MDRoundFlatButton:
        text:"Ride A bike"
        font_style : 'H1'
        text_color: 0, 0, 1, 1
        md_bg_color: 1, 1, 0, 1
        pos_hint: {"center_x": .5, "center_y": .5}    

class AddBike1(Screen):
    pass
class AddBike2(Screen):
    pass

sm=ScreenManager()

#sm.add_widget(AddBike(name='hello'))
sm.add_widget(AddBike2(name='hey'))
sm1=ScreenManager()
sm1.add_widget(AddBike1(name='hello'))
class Demo(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        hs=Builder.load_string(helper_builder)
        screen.add_widget(hs)
        hs1=Builder.load_string(helper_builder1)
        screen.add_widget(hs1)
        return screen

Demo().run()
"""