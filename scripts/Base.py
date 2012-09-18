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
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch
from kivy.uix.settings import SettingItem, SettingsPanel, SettingOptions
from scripts.EdsNotify import EdsNotify
import BeautifulSoup

config = ConfigParser()
config.read('%s/eds.ini' % Usr)


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    
def dismiss(self):
    self._popup.dismiss()

def show_base_browse(self):
    content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
    self._popup = Popup(background='atlas://images/eds/pop',title="EDS File Browser", content=content, size_hint=(0.9, 0.9))
    self._popup.open()


def select_base_file(self, path, filename):
    try:
        shutil.rmtree(Rom)
        os.mkdir(Rom)
        global fileb
        fileb = os.path.join(path, filename[0])
        self.dismiss_popup()
    except: 
        print 'no file selected'
    destpath = '%s/' % (Rom)
    z = zipfile.ZipFile(fileb)
    z.extractall(destpath)
    if config.getint('Config', 'changelog'):
        text_file = open(Changelog, "w")
        text_file.write("######## Changelog #########\n")
        text_file.write("Created: %s\n" % timestamp)
        text_file.close()
    else:
        print "Auto Changelog Disabled"

    EdsNotify().run("Base Rom Extracted Successfully", 'Selected file was:\n' + fileb)   
    self.dismiss_popup()


def select_base(self):   
    self.panel_layout.clear_widgets()
    title = Label(text='[b][color=#22A0D6][size=20]Base Rom Selection[/size][/color][/b]', markup = True, pos_hint={'x':-.05, 'y':.20})
    browse = CustomButton(text='BROWSE', pos_hint={'x':.0, 'y':.550}, size_hint=(.90, .06))
    download = CustomButton(text='Download', pos_hint={'x':.0, 'y':.450}, size_hint=(.90, .06))
    extract = CustomButton(text='Extract From RUU', pos_hint={'x':.0, 'y':.250}, size_hint=(.90, .06))
    port = CustomButton(text='Rom Porting (Experimental)', pos_hint={'x':.0, 'y':.150}, size_hint=(.90, .06))
    clean = Button(text='Clean Out Old Rom Files', pos_hint={'x':.0, 'y':-.05}, size_hint=(.90, .06), background_color=(1.4, 0, 0, 0.6))
    self.panel_layout.add_widget(title)
    self.panel_layout.add_widget(browse)
    self.panel_layout.add_widget(download)
    download.bind(on_release=dl_base_type)

    self.panel_layout.add_widget(extract)
    self.panel_layout.add_widget(port)
    self.panel_layout.add_widget(clean)
        
    def browse_files(instance):
        show_base_browse(self)
    browse.bind(on_release=browse_files)  

    def clean_files(instance):
        root = BoxLayout(orientation='vertical', spacing=20)
        btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
        remove = Button(text='Clean', size_hint_x=None, width=150)
        cancel = Button(text='Cancel', size_hint_x=None, width=150)
        root.add_widget(Label(text='Are You Sure You Want To\nClean Out Current Rom Files?'))
        root.add_widget(btn_layout)
        btn_layout.add_widget(remove)
        btn_layout.add_widget(cancel)
        popup = Popup(background='atlas://images/eds/pop', title='Add Option',content=root, auto_dismiss=False,
        size_hint=(None, None), size=(350, 200))
        cancel.bind(on_release=popup.dismiss)
        popup.open()
        
        def clean_now(self):
            shutil.rmtree(Rom)
            os.mkdir(Rom)
            EdsNotify().run("Clean Successful", 'Rom Files Have Been Removed')
        remove.bind(on_press=clean_now)
        remove.bind(on_release=popup.dismiss)
    clean.bind(on_release=clean_files)

def dl_base_type(self):
    Box = BoxLayout(orientation="vertical", spacing=10)
    msg = GridLayout(cols=1, padding=15, spacing=10, size_hint_y=None)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    
    over = CustomButton(text='CyanogenMod', size=(475, 40), size_hint=(None, None))
    over.bind(on_release=load_cm)
    
    msg.add_widget(over)
    
    root = ScrollView(size_hint=(None, None),bar_margin=-22, size=(475, 390), do_scroll_x=False)
    root.add_widget(msg)
    Box.add_widget(root)
    Box.add_widget(btn_layout)
    
    popup = Popup(background='atlas://images/eds/pop', title='Download Rom',content=Box, auto_dismiss=True,
    size_hint=(None, None), size=(520, 500))
    done.bind(on_release=popup.dismiss)
    popup.open()

def load_cm(self):
    Box = BoxLayout(orientation="vertical", spacing=10)
    panel = SettingsPanel(title="Stock HTC Kernels", settings=self)  
    msg = GridLayout(cols=1, size_hint=(None, 50.8), width=700)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    adv = Button(text='Show Custom Kernels',size_hint_y=(None), height=25)
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    try:
        from BeautifulSoup import BeautifulSoup
        import urllib2
        import re
        html_page = urllib2.urlopen(cyan)
        soup = BeautifulSoup(html_page)
        for link in soup.findAll('a'):
            if "/get/jenkins/" in link.get('href'):
                print link.get('href').split(".html")[0]
                name = link.get('href').split(".html")[0]
    
                item = SettingItem(panel = panel, title = "%s" % name, disabled=False, desc = "%s" % name)
                item_btn = CustomButton(text="%s" % name ,size_hint=(None, None),width=290, height=40)
                item.add_widget(item_btn)
                msg.add_widget(item) 
            
        root = ScrollView(size_hint=(None, None), size=(675, 350), do_scroll_x=False)
        root.add_widget(msg)
        Box.add_widget(adv)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
        
        popup = Popup(background='atlas://images/eds/pop', title='Stock HTC Kernels',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(700, 500))
        done.bind(on_release=popup.dismiss)
        adv.bind(on_release=popup.dismiss)
        popup.open()
        
    except:
        EdsNotify().run("'system/app Directory Not Found", 'Cant Find:\n' + SystemApp)
    
def boot_scripts(self):
    self.panel_layout.clear_widgets()
    title = Label(text='[b][color=#22A0D6][size=20]Init.d Scripts[/size][/color][/b]', markup = True, pos_hint={'x':-.05, 'y':.20})
    grid_layout = GridLayout(cols=3, row_force_default=True, row_default_height=40, spacing=10, pos_hint={'x':-.05, 'y':-.35})
    ext = CustomButton(text='Ext4 Tweak', pos_hint={'x':.0, 'y':.550}, size_hint=(.90, .06))
    sd = CustomButton(text='Sd Card Speed Fix', pos_hint={'x':.0, 'y':.550}, size_hint=(.90, .06))
    zip = CustomButton(text='Zipalign', pos_hint={'x':.0, 'y':.550}, size_hint=(.90, .06))
    self.panel_layout.add_widget(title)
    self.panel_layout.add_widget(grid_layout)
    grid_layout.add_widget(ext)
    grid_layout.add_widget(sd)
    grid_layout.add_widget(zip)
    
    def cp_ext(self):
        shutil.copy('%s/00ext4'% (Initd), (Rom_Initd))
        if config.getint('Config', 'changelog'):
            text_file = open(Changelog, "a") 
            text_file.write("\n%s -- Added ext4 tweak\n" % timestamp)
            text_file.close()
        EdsNotify().run("Script Added Successfully", '')   
    ext.bind(on_release=cp_ext)
    
    def cp_sd(self):
        shutil.copy('%s/05sdcardspeedfix'% (Initd), (Rom_Initd))
        if config.getint('Config', 'changelog'):
            text_file = open(Changelog, "a")
            text_file.write("\n%s -- Added Sd Card Speed Fix\n" % timestamp)
            text_file.close()
        EdsNotify().run("Added Successfully", '')   
    sd.bind(on_release=cp_sd)
    
    def cp_zip(self):
        shutil.copy('%s/06zipalign'% (Initd), (Rom_Initd))
        if config.getint('Config', 'changelog'):
            text_file = open(Changelog, "a")
            text_file.write("\n%s -- Added Zipalign on boot\n" % timestamp)
            text_file.close()
        EdsNotify().run("Added Successfully", '')   
    zip.bind(on_release=cp_zip)
    
    
    
def trans_scripts(self):
    print 'Hello Transitions'
    
def boot_anims(self):
    print 'Doing boot animations'


    
