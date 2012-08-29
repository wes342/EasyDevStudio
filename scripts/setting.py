#Copyright 2012 EasyDevStdio , wes342
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.


import urllib2
import re
from scripts.GI import *
from kivy.uix.textinput import TextInput

config = ConfigParser()
config.read('%s/eds.ini' % Usr)


def invalid(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=1, row_force_default=True, row_default_height=50, spacing=25)
    cancel = Button(text='Cancel', size_hint_x=None, width=375)
    root.add_widget(Label(text='\n\n** Serial Numbers Are Case Sensitive **\nYou Have Entered An Invalid Serial Number\n'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(cancel)
    
    def bad_ser(self):
        print "Bad Serial"
        config.set('Register', 'reg_key', '')
        config.write() 
    cancel.bind(on_release=bad_ser)
    
    popup = Popup(background='atlas://images/eds/pop', title='Register',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(400, 200))
    cancel.bind(on_release=popup.dismiss)
    popup.open()
         
    
def valid(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=1, row_force_default=True, row_default_height=50, spacing=25)
    ok = Button(text='ok', size_hint_x=None, width=375)
    root.add_widget(Label(text='\n\nThank You For Registering\nEasy Development Studio\n'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(ok)
    popup = Popup(background='atlas://images/eds/pop', title='Register',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(400, 200))
    ok.bind(on_release=popup.dismiss)
    popup.open()

def reg2(self, value):
    serial = value
    html_content = urllib2.urlopen('http://www.easydevstudio.com/ser').read()
    matches = re.findall(serial, html_content);
    if len(matches) == 0: 
        invalid(self)
    else:
        if len(serial) < 13:
            invalid(self)
        else:
            if len(serial) > 13:
                invalid(self)
            else:
                if serial[0:3].isalpha():
                    invalid(self)
                else:
                    if serial[3:4].islower():
                        invalid(self)
                    else:
                        if serial[3:5].isdigit():
                            invalid(self)
                        else:
                            if serial[5:7].isalpha():
                                invalid(self)
                            else:
                                if serial[7:10].isdigit():
                                    invalid(self)
                                else:
                                    if serial[10:13].isdigit():
                                        valid(self)
                                        config.set('Register', 'reg_key', value)
                                        config.write()

def demo(dt):
    get_device = config.get("Register", "reg_key")
    if get_device == '':
        root = BoxLayout(orientation='vertical',padding=25, spacing=60)
        btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=40, spacing=10)
        agree = Button(text='Exit', width=150)
        root.add_widget(Label(markup=True, halign="center", text='The Trial time period is over\nPlease register\n'))
        root.add_widget(btn_layout)
        btn_layout.add_widget(agree)
        popup = Popup(background='atlas://images/eds/pop', title='Demo Complete',content=root, auto_dismiss=False,
        size_hint=(None, None), size=(425, 250))
        agree.bind(on_release=go_away)
        popup.open()
    else:
        value = config.get("Register", "reg_key")
        serial = value
        html_content = urllib2.urlopen('http://www.easydevstudio.com/ser').read()
        matches = re.findall(serial, html_content);
        if len(matches) == 0: 
            root = BoxLayout(orientation='vertical',padding=25, spacing=60)
            btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=40, spacing=10)
            agree = Button(text='Exit', width=150)
            root.add_widget(Label(markup=True, halign="center", text='The Trial time period is over\nPlease register\n'))
            root.add_widget(btn_layout)
            btn_layout.add_widget(agree)
            popup = Popup(background='atlas://images/eds/pop', title='Demo Complete',content=root, auto_dismiss=False,
            size_hint=(None, None), size=(425, 250))
            agree.bind(on_release=go_away)
            popup.open()
        else:
            if len(serial) < 13:
                popup.open()
            else:
                if len(serial) > 13:
                    popup.open()
                else:
                    if serial[0:3].isalpha():
                        popup.open()
                    else:
                        if serial[3:4].islower():
                            popup.open()
                        else:
                            if serial[3:5].isdigit():
                                popup.open()
                            else:
                                if serial[5:7].isalpha():
                                    popup.open()
                                else:
                                    if serial[7:10].isdigit():
                                        popup.open()
                                    else:
                                        if serial[10:13].isdigit():
                                            print "Your Are Registered"
Clock.schedule_once(demo, 6000)
def go_away(self):
    webbrowser.open('http://easydevstudio.com/home/Store.html')
    exit()