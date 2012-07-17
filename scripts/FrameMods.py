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

from scripts.GI import *
from kivy.uix.switch import Switch
from kivy.uix.settings import SettingItem, SettingsPanel

def frame_mods(self):
    FramePop(self)
    
def FramePop(self):
    layout = GridLayout(cols=1, size_hint=(None, 2.5), width=700)
    layout.bind(minimum_height=layout.setter('height'))
    panel = SettingsPanel(title="Framework Mods", settings=self)   
    main = BoxLayout(orientation = 'vertical')
    root = ScrollView(size_hint=(None, None),bar_margin=-11, bar_color=(47 / 255., 167 / 255., 212 / 255., 1.), do_scroll_x=False)
    root.size = (600, 400)
    root.add_widget(layout)
    main.add_widget(root)
    done = Button(text ='Done Choosing Options')
    main.add_widget(done) 
    
    
    
    popup = Popup(background='atlas://images/eds/pop', title='Framework Mods', content=main, auto_dismiss=True, size_hint=(None, None), size=(630, 500))
    popup.open()
