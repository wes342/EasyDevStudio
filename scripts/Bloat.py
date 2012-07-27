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
from scripts.GI import *
from EdsNotify import EdsNotify
 
check = ["Rosie.apk","AccountSyncManager.apk", "ApplicationsProvider.apk", "AudioEffectService.apk", "Bluetooth.apk"]
                   
def load_apps(self):
    Box = BoxLayout(orientation="vertical", spacing=10)
    msg = GridLayout(cols=2, padding=15, spacing=10, size_hint_y=None)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    adv = Button(text='Advanced',size_hint_y=(None), height=20, background_color=(1,0,0,0.9))
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    try:
        for name in os.listdir(SystemApp):
            btnname = (CustomButton(text='%s' % name, font_size=10, size_hint_y=None, height=40))
            if not name in check:
                msg.add_widget(btnname)
                btnname.bind(on_release=do_button)
            
        root = ScrollView(size_hint=(None, None), size=(675, 350), do_scroll_x=False)
        root.add_widget(msg)
        Box.add_widget(adv)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
        adv.bind(on_release=load_adv_apps)
    
        popup = Popup(background='atlas://images/eds/pop', title='Removable Apps',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(700, 500))
        done.bind(on_release=popup.dismiss)
        popup.open()
    except:
        EdsNotify().run("'Init.d Directory Not Found", 'Cant Find:\n' + SystemApp)

def load_adv_apps(self):
    Box = BoxLayout(orientation="vertical", spacing=10)
    msg = GridLayout(cols=2, padding=15, spacing=10, size_hint_y=None)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    adv = Button(text='Easy Mode',size_hint_y=(None), height=20, background_color=(1,0,0,0.9))
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    try:
        for name in os.listdir(SystemApp):
            btnname = (CustomButton(text='%s' % name, font_size=10, size_hint_y=None, height=40))
            if name in check:
                msg.add_widget(btnname)
                btnname.bind(on_release=do_adv_button)
            
        root = ScrollView(size_hint=(None, None), size=(675, 350), do_scroll_x=False)
        root.add_widget(msg)
        Box.add_widget(adv)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
    
        popup = Popup(background='atlas://images/eds/pop', title='Removable Apps',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(700, 500))
        done.bind(on_release=popup.dismiss)
        popup.open()
    except:
        EdsNotify().run("'Init.d Directory Not Found", 'Cant Find:\n' + SystemApp) 
        
              
def do_button(self):
    filepath = "%s/%s" % (SystemApp, self.text)        
    check = ["Rosie.apk","AccountSyncManager.apk", "ApplicationsProvider.apk", "AudioEffectService.apk", "Bluetooth.apk"]
    if not self.text in check:
        root = BoxLayout(orientation='vertical', spacing=20)
        btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
        remove = Button(text='Remove', size_hint_x=None, width=150)
        cancel = Button(text='Cancel', size_hint_x=None, width=150)
        root.add_widget(Label(text='Are You Sure You Want To Remove This\nApp This could Cause Issues with your rom.'))
        root.add_widget(btn_layout)
        btn_layout.add_widget(remove)
        btn_layout.add_widget(cancel)
        popup = Popup(background='atlas://images/eds/pop', title='NOTICE',content=root, auto_dismiss=False,
        size_hint=(None, None), size=(350, 200))
        cancel.bind(on_release=popup.dismiss)
        popup.open()
        
        def remove_now(self):
            shutil.move(filepath, Removed)
        remove.bind(on_release=remove_now)
        remove.bind(on_release=popup.dismiss)
    else:
        shutil.move(filepath, Removed)

def do_adv_button(self):
    filepath = "%s/%s" % (SystemApp, self.text)        
    check = ["Rosie.apk","AccountSyncManager.apk", "ApplicationsProvider.apk", "AudioEffectService.apk", "Bluetooth.apk"]
    if self.text in check:
        root = BoxLayout(orientation='vertical', spacing=20)
        btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
        remove = Button(text='Remove', size_hint_x=None, width=150)
        cancel = Button(text='Cancel', size_hint_x=None, width=150)
        root.add_widget(Label(text='Are You Sure You Want To Remove This\nApp This could Cause Issues with your rom.'))
        root.add_widget(btn_layout)
        btn_layout.add_widget(remove)
        btn_layout.add_widget(cancel)
        popup = Popup(background='atlas://images/eds/pop', title='NOTICE',content=root, auto_dismiss=False,
        size_hint=(None, None), size=(350, 200))
        cancel.bind(on_release=popup.dismiss)
        popup.open()
        
        def remove_now(self):
            shutil.move(filepath, Removed)
        remove.bind(on_release=remove_now)
        remove.bind(on_release=popup.dismiss)
    else:
        shutil.move(filepath, Removed) 
    
def restore_removed(self):
    for name in os.listdir(Removed):
        shutil.move(Removed + "/" + name, SystemApp)
    
def clean_removed(self):
    for name in os.listdir(Removed):
        os.remove(Removed + "/" + name)
        
        