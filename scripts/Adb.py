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
    try:
        import pynotify
        if pynotify.init(NAME):
            n = pynotify.Notification("File Pushed Successfully", output)
            n.set_urgency(pynotify.URGENCY_NORMAL)
            n.show()
        else:
            print "there was a problem initializing the 'pynotify' module"
    except:
        print "you don't seem to have 'pynotify' installed"

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
    try:
        import pynotify
        if pynotify.init(NAME):
            n = pynotify.Notification("Shell Command Output", output)
            n.set_urgency(pynotify.URGENCY_NORMAL)
            n.show()
        else:
            print "there was a problem initializing the 'pynotify' module"
    except:
        print "you don't seem to have 'pynotify' installed"
        
 
    
def adb_comm(self):
    
    layout = GridLayout(cols=1, spacing=10, size_hint=(None, None), width=300)
    layout.bind(minimum_height=layout.setter('height'))
    
    blank_lbl = Label()
    general_lbl = Label(text='[b][color=#2AE309][size=20]General[/color][/size][/b]', markup = True)
    shell_lbl = Label(text='[b][color=#2AE309][size=20]Shell[/color][/size][/b]', markup = True)
    remounts_lbl = Label(text='[b][color=#E30918][size=20]Remount[/color][/size][/b]', markup = True)
    reboot_lbl = Label(text='[b][color=#E30918][size=20]Reboot[/color][/size][/b]', markup = True)


    kill = Button(text='Adb kill-server -- (stops adb server)', size=(500, 40), size_hint=(None, None))
    kill.bind(on_release=kill_server)
    start = Button(text='Adb start-server -- (starts adb server)', size=(500, 40), size_hint=(None, None))
    start.bind(on_release=start_server)
    
    devices = Button(text='Adb Devices -- (List of Devices)', size=(500, 40), size_hint=(None, None))
    devices.bind(on_release=check_device)
    state = Button(text='Adb State -- (Gets Current Device State)', size=(500, 40), size_hint=(None, None))
    state.bind(on_press=check_state)
    logcat = Button(text='Adb Logcat -- (Gets Logcat)', size=(500, 40), size_hint=(None, None))
    logcat.bind(on_press=adb_logcat)
    bugreport = Button(text='Adb Bug report -- (Gets Bugreport)', size=(500, 40), size_hint=(None, None))
    bugreport.bind(on_press=adb_bugreport)

    dmesg = Button(text='Adb shell dmesg -- (Gets dmesg)', size=(500, 40), size_hint=(None, None))
    dmesg.bind(on_press=adb_dmesg)
    getprop = Button(text='Adb shell getprop -- (Gets build.prop)', size=(500, 40), size_hint=(None, None))
    getprop.bind(on_press=adb_getprop)
    dumpstate = Button(text='Adb shell dumpstate -- (Gets dump of full system)', size=(500, 40), size_hint=(None, None))
    dumpstate.bind(on_press=adb_dumpstate)
    dumpactivity = Button(text='Adb shell dumpsys activity -- (Gets dump of current activities)', size=(500, 40), size_hint=(None, None))
    dumpactivity.bind(on_press=adb_dumpactivity)
    
    remount = Button(text='Adb Remount -- (Remount /system partition)', size=(500, 40), size_hint=(None, None))
    remount.bind(on_press=adb_remount)
    
    reboot = Button(text='Adb Reboot -- (Reboots Device)', size=(500, 40), size_hint=(None, None))
    reboot.bind(on_press=adb_reboot)
    recovery = Button(text='Adb Recovery -- (Reboots Into Recovery)', size=(500, 40), size_hint=(None, None))
    recovery.bind(on_press=adb_recovery)
    bootloader = Button(text='Adb Bootloader -- (Reboots Into Bootloader)', size=(500, 40), size_hint=(None, None))
    bootloader.bind(on_press=adb_bootloader)
    
    layout.add_widget(kill)
    layout.add_widget(start)
    layout.add_widget(blank_lbl)
    layout.add_widget(general_lbl)
    layout.add_widget(blank_lbl)
    layout.add_widget(devices)
    layout.add_widget(state)
    layout.add_widget(logcat)
    layout.add_widget(bugreport)
    layout.add_widget(blank_lbl)
    layout.add_widget(shell_lbl)
    layout.add_widget(blank_lbl)
    layout.add_widget(dmesg)
    layout.add_widget(getprop)
    layout.add_widget(dumpstate)
    layout.add_widget(dumpactivity)
    layout.add_widget(blank_lbl)
    layout.add_widget(remounts_lbl)
    layout.add_widget(blank_lbl)
    layout.add_widget(remount)
    layout.add_widget(blank_lbl)
    layout.add_widget(reboot_lbl)
    layout.add_widget(blank_lbl)
    layout.add_widget(reboot)
    layout.add_widget(recovery)
    layout.add_widget(bootloader)


    root = ScrollView(size_hint=(None, None),bar_margin=-11, bar_color=(47 / 255., 167 / 255., 212 / 255., 1.), do_scroll_x=False)
    root.size = (500, 420)
    root.add_widget(layout)

    popup = Popup(background='atlas://images/eds/pop', title='Adb Commands', content=root, size_hint=(None, None), size=(530, 500))
    popup.open()

# Adb General Commands
def kill_server(self):
    os.chdir(Tools)
    comm = './adb kill_server'
    output = os.popen(comm).read()
    try:
        import pynotify
        if pynotify.init(NAME):
            n = pynotify.Notification("Adb Server Killed", output)
            n.set_urgency(pynotify.URGENCY_NORMAL)
            n.show()
        else:
            print "there was a problem initializing the 'pynotify' module"
    except:
        print "you don't seem to have 'pynotify' installed"

def start_server(self):
    os.chdir(Tools)
    comm = './adb start_server'
    output = os.popen(comm).read()
    try:
        import pynotify
        if pynotify.init(NAME):
            n = pynotify.Notification("Adb Server Resurrected", output)
            n.set_urgency(pynotify.URGENCY_NORMAL)
            n.show()
        else:
            print "there was a problem initializing the 'pynotify' module"
    except:
        print "you don't seem to have 'pynotify' installed"

def check_device(self):
    os.chdir(Tools)
    comm = './adb devices'
    output = os.popen(comm).read()
    print output
    try:
        import pynotify
        if pynotify.init(NAME):
            n = pynotify.Notification("Adb Devices", output)
            n.set_urgency(pynotify.URGENCY_NORMAL)
            n.show()
        else:
            print "there was a problem initializing the 'pynotify' module"
    except:
        print "you don't seem to have 'pynotify' installed"
        
        
def check_state(self):
    os.chdir(Tools)
    comm = './adb get-state'
    output = os.popen(comm).read()
    print output
    try:
        import pynotify
        if pynotify.init(NAME):
            n = pynotify.Notification("Adb State", output)
            n.set_urgency(pynotify.URGENCY_NORMAL)
            n.show()
        else:
            print "there was a problem initializing the 'pynotify' module"
    except:
        print "you don't seem to have 'pynotify' installed"
        
        
def adb_logcat(self):
    os.chdir(Tools)
    comm = './adb logcat -d > %s/logcat.txt' % (Desktop)
    os.popen(comm)
    try:
        import pynotify
        if pynotify.init(NAME):
            n = pynotify.Notification("Logcat successful", 'logcat.txt is located on desktop')
            n.set_urgency(pynotify.URGENCY_NORMAL)
            n.show()
        else:
            print "there was a problem initializing the 'pynotify' module"
    except:
        print "you don't seem to have 'pynotify' installed"


def adb_bugreport(self):
    os.chdir(Tools)
    comm = './adb bugreport -d > %s/bugreport.txt' % (Desktop)
    os.popen(comm)
    try:
        import pynotify
        if pynotify.init(NAME):
            n = pynotify.Notification("Bug report successful", 'bugreport.txt is located on desktop')
            n.set_urgency(pynotify.URGENCY_NORMAL)
            n.show()
        else:
            print "there was a problem initializing the 'pynotify' module"
    except:
        print "you don't seem to have 'pynotify' installed"      

# Adb Shell Commands

def adb_dmesg(self):
    os.chdir(Tools)
    comm = './adb shell dmesg -d > %s/dmesg.txt' % (Desktop)
    os.popen(comm)
    try:
        import pynotify
        if pynotify.init(NAME):
            n = pynotify.Notification("dmesg successful", 'dmesg.txt is located on desktop')
            n.set_urgency(pynotify.URGENCY_NORMAL)
            n.show()
        else:
            print "there was a problem initializing the 'pynotify' module"
    except:
        print "you don't seem to have 'pynotify' installed"
        
def adb_getprop(self):
    os.chdir(Tools)
    comm = './adb shell getprop -d > %s/getprop.txt' % (Desktop)
    os.popen(comm)
    try:
        import pynotify
        if pynotify.init(NAME):
            n = pynotify.Notification("getprop successful", 'getprop.txt is located on desktop')
            n.set_urgency(pynotify.URGENCY_NORMAL)
            n.show()
        else:
            print "there was a problem initializing the 'pynotify' module"
    except:
        print "you don't seem to have 'pynotify' installed" 

def adb_dumpstate(self):
    os.chdir(Tools)
    comm = './adb shell dumpstate -d > %s/dumpstate.txt' % (Desktop)
    os.popen(comm)
    try:
        import pynotify
        if pynotify.init(NAME):
            n = pynotify.Notification("dumpstate successful", 'dumpstate.txt is located on desktop')
            n.set_urgency(pynotify.URGENCY_NORMAL)
            n.show()
        else:
            print "there was a problem initializing the 'pynotify' module"
    except:
        print "you don't seem to have 'pynotify' installed" 
        
def adb_dumpactivity(self):
    os.chdir(Tools)
    comm = './adb shell dumpsys activity -d > %s/dumpsys_activity.txt' % (Desktop)
    os.popen(comm)
    try:
        import pynotify
        if pynotify.init(NAME):
            n = pynotify.Notification("dumpsys activity successful", 'dumpsys_activity.txt is located on desktop')
            n.set_urgency(pynotify.URGENCY_NORMAL)
            n.show()
        else:
            print "there was a problem initializing the 'pynotify' module"
    except:
        print "you don't seem to have 'pynotify' installed"

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

    
