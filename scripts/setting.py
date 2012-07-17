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

def invalid(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=1, row_force_default=True, row_default_height=50, spacing=25)
    cancel = Button(text='Cancel', size_hint_x=None, width=375)
    root.add_widget(Label(text='\n\n** Serial Numbers Are Case Sensitive **\nYou Have Entered An Invalid Serial Number\n'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(cancel)
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
                                        try:
                                            processing_change = False
                                            for line in fileinput.input(Reg, inplace=1):
                                                if line.startswith('Serial:'):
                                                    processing_change = True
                                                else:
                                                    if processing_change:
                                                        print 'Serial:' + value
                                                        processing_change = False
                                                    print line,
                                        except:
                                            print 'cant write'
