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
screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'upload'
    
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Profile'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = app.hello
        
<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
        
"""