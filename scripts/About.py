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

#!/usr/bin/env python
#import kivy
from GI import *
import webbrowser
from kivy.uix.image import Image, AsyncImage
from kivy.uix.settings import SettingItem, SettingsPanel


def show_site(self):
    webbrowser.open(Site) 
      
def show_twitter(self):
    webbrowser.open(Twitter)  
    
def show_forum(self):
    webbrowser.open(Forum)
       
def show_bugs(self):
    webbrowser.open(Bugs)

    
def credits_popup(self):
    layout = GridLayout(cols=1, size_hint=(None, 1.4), width=700)
    layout.bind(minimum_height=layout.setter('height'))
    panel = SettingsPanel(title="Credits", settings=self)   
    main = BoxLayout(orientation = 'vertical')
    root = ScrollView(size_hint=(None, None),bar_margin=-11, bar_color=(47 / 255., 167 / 255., 212 / 255., 1.), do_scroll_x=False)
    root.size = (600, 400)
    root.add_widget(layout)
    main.add_widget(root)
    done = Button(text ='Close')
    main.add_widget(done)

    wes_btns = GridLayout(cols=3, spacing=10, padding=5)
    wes_twit = CustomButton(text='Twitter', size_hint_x=None, size_hint_y=30, width=60)
    wes_btns.add_widget(wes_twit)
    wes_contact = CustomButton(text='Gmail', size_hint_x=None, size_hint_y=30, width=60)
    wes_btns.add_widget(wes_contact)
    wes_site = CustomButton(text='Site', size_hint_x=None, size_hint_y=30, width=60)
    wes_btns.add_widget(wes_site)

    wes = SettingItem(panel = panel, title = "Wes342",disabled=False, desc = "Lead Developer:  -  Python,  xml,  java,  smali,  json\nLead Site Maintainer: - Html,  Xml,  Php")
    wes.add_widget(wes_btns)
    layout.add_widget(wes)

    sac_btns = GridLayout(cols=3, spacing=10, padding=5)
    sac_twit = CustomButton(text='Twitter',size_hint_x=None, size_hint_y=60, width=60)
    sac_btns.add_widget(sac_twit)
    sac_contact = CustomButton(text='Gmail',size_hint_x=None, size_hint_y=60, width=60)
    sac_btns.add_widget(sac_contact)
    sac_site = CustomButton(text='Site',size_hint_x=None, size_hint_y=60, width=60)
    sac_btns.add_widget(sac_site)
    
    zar_btns = GridLayout(cols=3, spacing=10, padding=5)
    zar_twit = CustomButton(text='Twitter',size_hint_x=None, size_hint_y=60, width=60)
    zar_btns.add_widget(zar_twit)
    zar_contact = CustomButton(text='Gmail',size_hint_x=None, size_hint_y=60, width=60)
    zar_btns.add_widget(zar_contact)
    zar_site = CustomButton(text='Site',size_hint_x=None, size_hint_y=60, width=60)
    zar_btns.add_widget(zar_site)

    sac = SettingItem(panel = panel, title = "Sac23",disabled=False, desc = "Lead Developer:  -  Android,  xml,  smali")
    sac.add_widget(sac_btns)
    layout.add_widget(sac)

    zar = SettingItem(panel = panel, title = "Zarboz",disabled=False, desc = "Kernel Development:  -  Source, Make, Github")
    zar.add_widget(zar_btns)
    layout.add_widget(zar)
   
   
    thanks = SettingItem(panel = panel, title = "Credits",disabled=True, desc = Credits)
    layout.add_widget(thanks)
    
    donors = SettingItem(panel = panel, title = "Donors",disabled=True, desc = Donors)
    layout.add_widget(donors)

    popup = Popup(background='atlas://images/eds/pop', title='Credits', content=main, auto_dismiss=True, size_hint=(None, None), size=(630, 500))
    popup.open()
    done.bind(on_release=popup.dismiss)

    def wes_twitter(self):
        webbrowser.open('http://twitter.com/wes342')
    wes_twit.bind(on_press=wes_twitter)
    
    def wes_gtalk(self):
        webbrowser.open("mailto:wes342@gmail.com")
    wes_contact.bind(on_press=wes_gtalk)
    
    def wes_website(self):
        webbrowser.open('http://easydevstudio.com/home')
    wes_site.bind(on_press=wes_website)
       
    def sac_twitter(self):
        webbrowser.open('http://twitter.com/sac232')
    sac_twit.bind(on_press=sac_twitter)

    def sac_gtalk(self):
        webbrowser.open("mailto:sarkisdx@gmail.com")
    sac_contact.bind(on_press=sac_gtalk)
    
    def sac_website(self):
        webbrowser.open('http://citycollisioncenter.com')
    sac_site.bind(on_press=sac_website)
    
    def zar_twitter(self):
        webbrowser.open('http://twitter.com/zarboz')
    zar_twit.bind(on_press=zar_twitter)

    def zar_gtalk(self):
        webbrowser.open("mailto:zarboz@gmail.com")
    zar_contact.bind(on_press=zar_gtalk)
    
    def zar_website(self):
        webbrowser.open('https://github.com/zarboz')
    zar_site.bind(on_press=zar_website)
