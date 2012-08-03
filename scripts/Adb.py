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
from kivy.logger import LoggerHistory
from scripts.EdsNotify import EdsNotify

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    
def dismiss(self):
    self._popup.dismiss()

def show_adb_browse(self):
    content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
    self._popup = Popup(background='atlas://images/eds/pop',title="EDS File Browser", content=content, size_hint=(0.9, 0.9))
    self._popup.open()


def select_adb_file(self, path, filename):
    try:
        global fileb
        fileb = os.path.join(path, filename[0])
        self.dismiss_popup()
    except: 
        print 'no file selected'   
        self.dismiss_popup()
    

def push_path(self):
    pass

def adb_push(self):
    os.chdir(Tools)
    f = self.push_text.text
    comm = './adb push'
    output = os.popen(comm + ' ' + fileb + ' ' + f).read()
    EdsNotify().run("File Pushed Successfully", output)

def adb_pull(self):
    os.chdir(Tools)
    f = self.pull_text.text
    comm = './adb pull'
    output = os.popen(comm + ' ' + f + ' ' + Pulled).read()
    print output

def adb_run(self):
    comm = self.text_input.text
    output = os.popen(comm).read()
    self.text_input.text = ''
    EdsNotify().run("Shell Command Output", output)
    
def adb_comm(self):
    
    Box = BoxLayout(orientation="vertical", spacing=10)
    msg = GridLayout(cols=1, padding=15, spacing=10, size_hint_y=None)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    
    general_lbl = Label(text='[b][color=#2AE309][size=20]General[/color][/size][/b]', markup = True)
    shell_lbl = Label(text='[b][color=#2AE309][size=20]Shell[/color][/size][/b]', markup = True)
    remounts_lbl = Label(text='[b][color=#E30918][size=20]Remount[/color][/size][/b]', markup = True)
    reboot_lbl = Label(text='[b][color=#E30918][size=20]Reboot[/color][/size][/b]', markup = True)


    kill = CustomButton(text='Adb kill-server -- (stops adb server)', size=(350, 40), size_hint=(None, None))
    kill.bind(on_release=kill_server)
    start = CustomButton(text='Adb start-server -- (starts adb server)', size=(350, 40), size_hint=(None, None))
    start.bind(on_release=start_server)
    
    devices = CustomButton(text='Adb Devices -- (List of Devices)', size=(350, 40), size_hint=(None, None))
    devices.bind(on_release=check_device)
    state = CustomButton(text='Adb State -- (Gets Current Device State)', size=(350, 40), size_hint=(None, None))
    state.bind(on_press=check_state)
    logcat = CustomButton(text='Adb Logcat -- (Gets Logcat)', size=(350, 40), size_hint=(None, None))
    logcat.bind(on_press=adb_logcat)
    bugreport = CustomButton(text='Adb Bug report -- (Gets Bugreport)', size=(350, 40), size_hint=(None, None))
    bugreport.bind(on_press=adb_bugreport)

    dmesg = CustomButton(text='Adb shell dmesg -- (Gets dmesg)', size=(350, 40), size_hint=(None, None))
    dmesg.bind(on_press=adb_dmesg)
    getprop = CustomButton(text='Adb shell getprop -- (Gets build.prop)', size=(350, 40), size_hint=(None, None))
    getprop.bind(on_press=adb_getprop)
    dumpstate = CustomButton(text='Adb shell dumpstate -- (Gets dump of full system)', size=(350, 40), size_hint=(None, None))
    dumpstate.bind(on_press=adb_dumpstate)
    dumpactivity = CustomButton(text='Adb shell dumpsys activity -- (Gets dump of current activities)', size=(500, 40), size_hint=(None, None))
    dumpactivity.bind(on_press=adb_dumpactivity)
    
    remount = CustomButton(text='Adb Remount -- (Remount /system partition)', size=(350, 40), size_hint=(None, None))
    remount.bind(on_press=adb_remount)
    
    reboot = CustomButton(text='Adb Reboot -- (Reboots Device)', size=(350, 40), size_hint=(None, None))
    reboot.bind(on_press=adb_reboot)
    recovery = CustomButton(text='Adb Recovery -- (Reboots Into Recovery)', size=(350, 40), size_hint=(None, None))
    recovery.bind(on_press=adb_recovery)
    bootloader = CustomButton(text='Adb Bootloader -- (Reboots Into Bootloader)', size=(350, 40), size_hint=(None, None))
    bootloader.bind(on_press=adb_bootloader)
    
    msg.add_widget(kill)
    msg.add_widget(start)
    msg.add_widget(general_lbl)
    msg.add_widget(devices)
    msg.add_widget(state)
    msg.add_widget(logcat)
    msg.add_widget(bugreport)
    msg.add_widget(shell_lbl)
    msg.add_widget(dmesg)
    msg.add_widget(getprop)
    msg.add_widget(dumpstate)
    msg.add_widget(dumpactivity)
    msg.add_widget(remounts_lbl)
    msg.add_widget(remount)
    msg.add_widget(reboot_lbl)
    msg.add_widget(reboot)
    msg.add_widget(recovery)
    msg.add_widget(bootloader)

    root = ScrollView(size_hint=(None, None),bar_margin=-22, size=(475, 390), do_scroll_x=False)
    root.add_widget(msg)
    Box.add_widget(root)
    Box.add_widget(btn_layout)
    
    popup = Popup(background='atlas://images/eds/pop', title='Adb Commands',content=Box, auto_dismiss=True,
    size_hint=(None, None), size=(520, 500))
    done.bind(on_release=popup.dismiss)
    popup.open()

# Adb General Commands
def kill_server(self):
    os.chdir(Tools)
    comm = './adb kill_server'
    output = os.popen(comm).read()
    EdsNotify().run("Adb Server Killed", output)

def start_server(self):
    os.chdir(Tools)
    comm = './adb start_server'
    output = os.popen(comm).read()
    EdsNotify().run("Adb Server Resurrected", output)

def check_device(self):
    os.chdir(Tools)
    comm = './adb devices'
    output = os.popen(comm).read()
    print output
    EdsNotify().run("Adb Devices", output)    
        
def check_state(self):
    os.chdir(Tools)
    comm = './adb get-state'
    output = os.popen(comm).read()
    print output
    EdsNotify().run("Adb State", output)        
        
def adb_logcat(self):
    os.chdir(Tools)
    comm = './adb logcat -d > %s/logcat.txt' % (Desktop)
    os.popen(comm)
    EdsNotify().run("Logcat successful", 'logcat.txt is located on desktop')

def adb_bugreport(self):
    os.chdir(Tools)
    comm = './adb bugreport -d > %s/bugreport.txt' % (Desktop)
    os.popen(comm)
    EdsNotify().run("Bug report successful", 'bugreport.txt is located on desktop')  

# Adb Shell Commands

def adb_dmesg(self):
    os.chdir(Tools)
    comm = './adb shell dmesg -d > %s/dmesg.txt' % (Desktop)
    os.popen(comm)
    EdsNotify().run("dmesg successful", 'dmesg.txt is located on desktop')
        
def adb_getprop(self):
    os.chdir(Tools)
    comm = './adb shell getprop -d > %s/getprop.txt' % (Desktop)
    os.popen(comm)
    EdsNotify().run("getprop successful", 'getprop.txt is located on desktop') 

def adb_dumpstate(self):
    os.chdir(Tools)
    comm = './adb shell dumpstate -d > %s/dumpstate.txt' % (Desktop)
    os.popen(comm)
    EdsNotify().run("dumpstate successful", 'dumpstate.txt is located on desktop')
        
def adb_dumpactivity(self):
    os.chdir(Tools)
    comm = './adb shell dumpsys activity -d > %s/dumpsys_activity.txt' % (Desktop)
    os.popen(comm)
    EdsNotify().run("dumpsys activity successful", 'dumpsys_activity.txt is located on desktop')

# Adb Remount Commands
def adb_remount(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
    restart = Button(text='Remount', size_hint_x=None, width=150)
    cancel = Button(text='Cancel', size_hint_x=None, width=150)
    root.add_widget(Label(text='Remount /system Partition Now?'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(restart)
    btn_layout.add_widget(cancel)
    popup = Popup(background='%s/pop.png' % Images, title='Adb Remount',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    cancel.bind(on_press=popup.dismiss)
    popup.open()  
    
    def callback(instance, value):
        os.chdir(Tools)
        comm = './adb remount'
        os.popen(comm)
    restart.bind(state=callback) 

# ADB Reboot Commands
def adb_reboot(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
    restart = Button(text='Reboot', size_hint_x=None, width=150)
    cancel = Button(text='Cancel', size_hint_x=None, width=150)
    root.add_widget(Label(text='Reboot Your Device Now?'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(restart)
    btn_layout.add_widget(cancel)
    popup = Popup(background='%s/pop.png' % Images, title='Adb Reboot',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    cancel.bind(on_press=popup.dismiss)
    popup.open()  
    
    def callback(instance, value):
        os.chdir(Tools)
        comm = './adb reboot'
        os.popen(comm)
    restart.bind(state=callback)
 
    
def adb_recovery(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
    restart = Button(text='Reboot', size_hint_x=None, width=150)
    cancel = Button(text='Cancel', size_hint_x=None, width=150)
    root.add_widget(Label(text='Reboot To Recovery Now?'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(restart)
    btn_layout.add_widget(cancel)
    popup = Popup(background='%s/pop.png' % Images, title='Adb Reboot',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    cancel.bind(on_press=popup.dismiss)
    popup.open()  
    
    def callback(instance, value):
        os.chdir(Tools)
        comm = './adb reboot recovery'
        os.popen(comm)
    restart.bind(state=callback)
    
def adb_bootloader(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
    restart = Button(text='Reboot', size_hint_x=None, width=150)
    cancel = Button(text='Cancel', size_hint_x=None, width=150)
    root.add_widget(Label(text='Reboot to bootloader now?'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(restart)
    btn_layout.add_widget(cancel)
    popup = Popup(background='%s/pop.png' % Images, title='Adb Reboot',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    cancel.bind(on_press=popup.dismiss)
    popup.open()  
    
    def callback(instance, value):
        os.chdir(Tools)
        comm = './adb reboot bootloader'
        os.popen(comm)
    restart.bind(state=callback)
    
# TODO Impliment Help System

def adb_help(self):
    pass

    
