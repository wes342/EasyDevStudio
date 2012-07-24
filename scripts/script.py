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

from GI import *
import webbrowser

        
def initd(instance):
    Box = BoxLayout(orientation="vertical", spacing=10)
    msg = GridLayout(cols=1, spacing=5, size_hint_y=None)
    btn_layout = GridLayout(cols=1)
    done = CustomButton(text="Done")
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    for root, dirs, files in os.walk(Rom_Initd):
        for name in files:       
            fname = name
            btnname = (CustomButton(text='%s' % fname, font_size=10, size_hint_y=None, height=40))
            msg.add_widget(btnname)
            btnname.bind(on_release=do_button)
    root = ScrollView(size_hint=(None, None), size=(375, 290), do_scroll_x=False)
    root.add_widget(msg)
    Box.add_widget(root)
    Box.add_widget(btn_layout)

    popup = Popup(background='atlas://images/eds/pop', title='Needed packages',content=Box, auto_dismiss=True,
    size_hint=(None, None), size=(400, 400))
    done.bind(on_release=popup.dismiss)
    popup.open()
    
def do_button(self):
    for root, dirs, files in os.walk(Rom_Initd):
        for name in files:       
            fname = name
            btnname = (CustomButton(text='%s' % fname, font_size=10, size_hint_y=None, height=40))
            print btnname.text



def buildprop(self):
    webbrowser.open(BuildProp)

def uscript(self):
    webbrowser.open(UScript)

def changes(self):
    webbrowser.open(Change)
    
def aroma_config(self):
    webbrowser.open(Aroma)

def rom_terms(self):
    webbrowser.open(Terms)
    
    
    
    