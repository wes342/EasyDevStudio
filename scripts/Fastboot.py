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
from scripts.EdsNotify import EdsNotify

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    
def dismiss(self):
    self._popup.dismiss()

def show_fb_browse(self):
    content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
    self._popup = Popup(title="EDS File Browser", background='atlas://images/eds/pop', content=content, size_hint=(0.9, 0.9))
    self._popup.open()


def select_fb_file(self, path, filename):
    try:
        global fileb
        fileb = os.path.join(path, filename[0])
        self.dismiss_popup()
    except: 
        print 'no file selected'   
        self.dismiss_popup()
        
def fastboot_comm(self):
    
    layout = GridLayout(cols=1, spacing=10, size_hint=(None, None), width=300)
    layout.bind(minimum_height=layout.setter('height'))

    blank_lbl = Label()
    general_lbl = Label(text='[b][color=#E30918][size=20]General[/color][/size][/b]', markup = True)

    devices = Button(text='Fastboot Devices -- (List of Devices)', size=(500, 40), size_hint=(None, None))
    devices.bind(on_press=check_device)
    bootloader = Button(text='Fastboot Bootloader -- (Reboots The Bootloader)', size=(500, 40), size_hint=(None, None))
    bootloader.bind(on_press=fastboot_bootloader)
    reboot = Button(text='Fastboot Reboot -- (Reboots The Device)', size=(500, 40), size_hint=(None, None))
    reboot.bind(on_press=fastboot_reboot)

    layout.add_widget(blank_lbl)
    layout.add_widget(general_lbl)
    layout.add_widget(blank_lbl)
    layout.add_widget(devices)
    layout.add_widget(bootloader)
    layout.add_widget(reboot)



    root = ScrollView(size_hint=(None, None),bar_margin=-11, bar_color=(47 / 255., 167 / 255., 212 / 255., 1.), do_scroll_x=False)
    root.size = (500, 220)
    root.add_widget(layout)

    popup = Popup(title='Fastboot Commands',background='atlas://images/eds/pop', content=root, size_hint=(None, None), size=(530, 300))
    popup.open()

def check_device(self):
    os.chdir(Tools)
    comm = './fastboot devices'
    output = os.popen(comm).read()
    print output
    EdsNotify().run("Fastboot Devices", output)

# Misc Fastboot Commands
def fastboot_reboot(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
    restart = Button(text='Reboot', size_hint_x=None, width=150)
    cancel = Button(text='Cancel', size_hint_x=None, width=150)
    root.add_widget(Label(text='Reboot The Device Now?'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(restart)
    btn_layout.add_widget(cancel)
    popup = Popup(background='atlas://images/eds/pop', title='Fastboot Reboot',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    cancel.bind(on_press=popup.dismiss)
    popup.open()  
    
    def callback(instance, value):
        os.chdir(Tools)
        comm = './fastboot reboot'
        os.popen(comm)
    restart.bind(state=callback)


def fastboot_bootloader(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
    restart = Button(text='Reboot', size_hint_x=None, width=150)
    cancel = Button(text='Cancel', size_hint_x=None, width=150)
    root.add_widget(Label(text='Reboot The Bootloader Now?'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(restart)
    btn_layout.add_widget(cancel)
    popup = Popup(background='atlas://images/eds/pop', title='Fastboot Reboot',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    cancel.bind(on_press=popup.dismiss)
    popup.open()  
    
    def callback(instance, value):
        os.chdir(Tools)
        comm = './fastboot reboot-bootloader'
        os.popen(comm)
    restart.bind(state=callback)
    
 
def go_fastboot(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
    restart = Button(text='Reboot', size_hint_x=None, width=150)
    cancel = Button(text='Cancel', size_hint_x=None, width=150)
    root.add_widget(Label(text='Boot Into Fastboot Now?\nDevice needs to be connected'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(restart)
    btn_layout.add_widget(cancel)
    popup = Popup(background='atlas://images/eds/pop', title='Reboot to Fastboot',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    cancel.bind(on_press=popup.dismiss)
    popup.open()  
    
    def callback(instance, value):
        os.chdir(Tools)
        comm = './adb reboot bootloader'
        os.popen(comm)
    restart.bind(state=callback) 

# Main Fastboot Commands
def flash_boot(self):
    comm = './fastboot flash boot'
    os.chdir(Tools) 
    output = os.popen(comm + ' ' + fileb).read()
    print output
    EdsNotify().run("'Boot.img flashed", output)   

def boot_recovery(self):
    os.chdir(Tools)
    comm = './fastboot boot'
    output = os.popen(comm + ' ' + fileb).read()
    print output
    EdsNotify().run("'Booted Recovery.img", output)

def fastboot_run(self):
    comm = self.text_input.text
    output = os.popen(comm).read()
    print output
    self.text_input.text = ''
    EdsNotify().run("Shell Command Output", output)

def fastboot_help(self):
    print 'For Future Help'
