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
from BeautifulSoup import BeautifulSoup
import urllib2
import re

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
    msg = GridLayout(cols=1, padding=15, spacing=20, size_hint_y=None)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    
    Cm = Label(text="[b][color=#32D1D1][size=20]CyanogenMod[/color][/size][/b]", markup=True)
    stable = CustomButton(text='STABLE', size=(560, 45), size_hint=(None, None))
    stable.bind(on_press=load_cm_s)
    
    rc = CustomButton(text='RELEASE CANDIDATE', size=(560, 45), size_hint=(None, None))
    rc.bind(on_release=load_cm_r)
    night = CustomButton(text='NIGHTLY', size=(560, 45), size_hint=(None, None))
    night.bind(on_release=load_cm_n)
    
    msg.add_widget(Cm)
    msg.add_widget(stable)
    msg.add_widget(rc)
    msg.add_widget(night)
        
    root = ScrollView(size_hint=(None, None),bar_margin=-22, size=(575, 350), do_scroll_x=False)
    root.add_widget(msg)
    Box.add_widget(root)
    Box.add_widget(btn_layout)
    
    popup = Popup(background='atlas://images/eds/pop', title='Download Rom',content=Box, auto_dismiss=True,
    size_hint=(None, None), size=(620, 460))
    done.bind(on_release=popup.dismiss)
    popup.open()
    

def load_cm_s(self):
    Box = BoxLayout(orientation="vertical", spacing=10)
    panel = SettingsPanel(title="CyanogenMod", settings=self)  
    msg = GridLayout(cols=1, size_hint=(None, 8.8), width=750)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    try:
        html_page = urllib2.urlopen(cyan_s)
        soup = BeautifulSoup(html_page)
        for link in soup.findAll('a'):
            if "/get/jenkins/" in link.get('href'):
                name = link.get('href').split(".html")[0]
                
                re1='((?:[a-z][a-z]+))'    # Word 1
                re2='(.)'    # Any Single Character 1
                re3='(.)'    # Any Single Character 2
                re4='(.)'    # Any Single Character 3
                re5='((?:[a-z][a-z]+))'    # Word 2
                re6='(.)'    # Any Single Character 4
                re7='((?:[a-z][a-z]+))'    # Word 3
                re8='(.)'    # Any Single Character 5
                re9='((?:[a-z][a-z]+))'    # Word 4
                re10='(.)'    # Any Single Character 6
                re11='((?:[a-z][a-z]+))'    # Word 5
                re12='(.)'    # Any Single Character 7
                re13='(\\d+)'    # Integer Number 1
                re14='(.)'    # Any Single Character 8
                re15='((?:[a-z][a-z]+))'    # Word 6
                re16='(.)'    # Any Single Character 9
                re17='(\\d+)'    # Integer Number 2
                re18='(.)'    # Any Single Character 10
                re19='(\\d+)'    # Integer Number 3
                re20='(.)'    # Any Single Character 11
                re21='(\\d+)'    # Integer Number 4
                re22='(.)'    # Any Single Character 12
                re23='(\w+)'    # Alphanum 1
                re24='(.)'    # Any Single Character 13
                re25='((?:[a-z][a-z]+))'    # Word 7
                
                rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15+re16+re17+re18+re19+re20+re21+re22+re23+re24+re25,re.IGNORECASE|re.DOTALL)
                m = rg.search(name)
                if m:
                    word1=m.group(1)
                    c1=m.group(2)
                    c2=m.group(3)
                    c3=m.group(4)
                    word2=m.group(5)
                    c4=m.group(6)
                    word3=m.group(7)
                    c5=m.group(8)
                    word4=m.group(9)
                    c6=m.group(10)
                    word5=m.group(11)
                    c7=m.group(12)
                    int1=m.group(13)
                    c8=m.group(14)
                    word6=m.group(15)
                    c9=m.group(16)
                    int2=m.group(17)
                    c10=m.group(18)
                    int3=m.group(19)
                    c11=m.group(20)
                    int4=m.group(21)
                    c12=m.group(22)
                    alphanum1=m.group(23)
                    c13=m.group(24)
                    word7=m.group(25)
                    url = c7+int1+c8+word6+c9+int2+c10+int3+c11+int4+c12+alphanum1+c13+word7
                    ver = word6+c9+int2+c10+int3+c11+int4
                    device = alphanum1
                    
                    stable = SettingItem(panel = panel, title = "%s" % device.upper(), disabled=False, desc = "Build: %s" % ver)
                    stable_btn = CustomButton(text="%s" % url, size_hint=(None, None),width=330, height=40)
                    stable_b2 = CustomButton(text="%s" % url)
                    stable.add_widget(stable_btn)
                    msg.add_widget(stable) 
                    
                    def cm_stable(self):
                        webbrowser.open('http://get.cm/get/jenkins%s' % self.text)
                    stable_btn.bind(on_release=cm_stable)
            
        root = ScrollView(size_hint=(None, None), size=(730, 390), do_scroll_x=False)
        root.add_widget(msg)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
        
        popup = Popup(background='atlas://images/eds/pop', title='CyanogenMod (STABLE)',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(750, 500))
        done.bind(on_release=popup.dismiss)
        popup.open()

    except:
        EdsNotify().run("'Url Not Found", 'Error Loading: http://get.cm')


def load_cm_r(self):
    Box = BoxLayout(orientation="vertical", spacing=10)
    panel = SettingsPanel(title="CyanogenMod", settings=self)  
    msg = GridLayout(cols=1, size_hint=(None, 8.8), width=750)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    try:
        html_page = urllib2.urlopen(cyan_r)
        soup = BeautifulSoup(html_page)
        for link in soup.findAll('a'):
            if "/get/jenkins/" in link.get('href'):
                name = link.get('href').split(".html")[0]
                               
                re1='(http)'
                re2='(:)'   
                re3='(\\/)' 
                re4='(\\/)' 
                re5='(get)' 
                re6='(\\.)'
                re7='(cm)'
                re8='(\\/)' 
                re9='(get)'
                re10='(\\/)'
                re11='((?:[a-z][a-z]+))'
                re12='(\\/)'
                re13='(\\d+)'
                re14='(\\/)'
                re15='(cm)'
                re16='(-)'
                re17='(\\d+)'
                re18='(\\.)'
                re19='(\\d+)'
                re20='(\\.)'
                re21='(\\d+)'
                re22='(-)' 
                re23='((?:[a-z][a-z]*[0-9]+[a-z0-9]*))'
                re24='(-)' 
                re25='(\w+)' 
                re26='(\\.)'
                re27='(zip)'
                
                rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15+re16+re17+re18+re19+re20+re21+re22+re23+re24+re25+re26+re27,re.IGNORECASE|re.DOTALL)
                m = rg.search(name)
                if m:
                    var1=m.group(1)
                    c1=m.group(2)
                    c2=m.group(3)
                    c3=m.group(4)
                    word1=m.group(5)
                    c4=m.group(6)
                    word2=m.group(7)
                    c5=m.group(8)
                    word3=m.group(9)
                    c6=m.group(10)
                    word4=m.group(11)
                    c7=m.group(12)
                    int1=m.group(13)
                    c8=m.group(14)
                    word5=m.group(15)
                    c9=m.group(16)
                    int2=m.group(17)
                    c10=m.group(18)
                    int3=m.group(19)
                    c11=m.group(20)
                    int4=m.group(21)
                    c12=m.group(22)
                    alphanum1=m.group(23)
                    c13=m.group(24)
                    alphanum2=m.group(25)
                    c14=m.group(26)
                    word6=m.group(27)

                    url = int1+c8+word5+c9+int2+c10+int3+c11+int4+c12+alphanum1+c13+alphanum2+c14+word6
                    ver = word5+c9+int2+c10+int3+c11+int4
                    device = alphanum2

                    stable = SettingItem(panel = panel, title = "%s" % device.upper(), disabled=False, desc = "Build: %s" % ver)
                    stable_btn = CustomButton(text="%s" % url, size_hint=(None, None),width=330, height=40)
                    stable_b2 = CustomButton(text="%s" % url)
                    stable.add_widget(stable_btn)
                    msg.add_widget(stable) 
                    
                    def cm_stable(self):
                        webbrowser.open('http://get.cm/get/jenkins'+c7+'%s' % self.text)
                    stable_btn.bind(on_release=cm_stable)
            
        root = ScrollView(size_hint=(None, None), size=(730, 390), do_scroll_x=False)
        root.add_widget(msg)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
        
        popup = Popup(background='atlas://images/eds/pop', title='CyanogenMod (RELEASE CANDIDATE)',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(750, 500))
        done.bind(on_release=popup.dismiss)
        popup.open()
        
    except:
        EdsNotify().run("'Url Not Found", 'Error Loading: http://get.cm')
      
          
def load_cm_n(self):
    Box = BoxLayout(orientation="vertical", spacing=10)
    panel = SettingsPanel(title="CyanogenMod", settings=self)  
    msg = GridLayout(cols=1, size_hint=(None, 8.8), width=750)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    try:
        html_page = urllib2.urlopen(cyan_n)
        soup = BeautifulSoup(html_page)
        for link in soup.findAll('a'):
            if "/get/jenkins/" in link.get('href'):
                name = link.get('href').split(".html")[0]
                
                re1='(http)'    # Variable Name 1
                re2='(:)'    # Any Single Character 1
                re3='(\\/)'    # Any Single Character 2
                re4='(\\/)'    # Any Single Character 3
                re5='(get\\.cm)'    # Fully Qualified Domain Name 1
                re6='(\\/)'    # Any Single Character 4
                re7='(get)'    # Word 1
                re8='(\\/)'    # Any Single Character 5
                re9='((?:[a-z][a-z]+))'    # Word 2
                re10='(\\/)'    # Any Single Character 6
                re11='(\\d+)'    # Integer Number 1
                re12='(\\/)'    # Any Single Character 7
                re13='(cm)'    # Word 3
                re14='([-+]\\d+)'    # Integer Number 1
                re15='(-)'    # Any Single Character 8
                re16='((?:(?:[1]{1}\\d{1}\\d{1}\\d{1})|(?:[2]{1}\\d{3}))(?:[0]?[1-9]|[1][012])(?:(?:[0-2]?\\d{1})|(?:[3][01]{1})))(?![\\d])'    # YYYYMMDD 1
                re17='(-)'    # Any Single Character 9
                re18='(NIGHTLY)'    # Word 4
                re19='(-)'    # Any Single Character 10
                re20='(\w+)'    # Alphanum 1
                re21='(\\.)'    # Any Single Character 11
                re22='(zip)'    # Word 5
                
                rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15+re16+re17+re18+re19+re20+re21+re22,re.IGNORECASE|re.DOTALL)
                m = rg.search(name)
                if m:
                    var1=m.group(1)
                    c1=m.group(2)
                    c2=m.group(3)
                    c3=m.group(4)
                    fqdn1=m.group(5)
                    c4=m.group(6)
                    word1=m.group(7)
                    c5=m.group(8)
                    word2=m.group(9)
                    c6=m.group(10)
                    int1=m.group(11)
                    c7=m.group(12)
                    word3=m.group(13)
                    signed_int1=m.group(14)
                    c8=m.group(15)
                    yyyymmdd1=m.group(16)
                    c9=m.group(17)
                    word4=m.group(18)
                    c10=m.group(19)
                    alphanum1=m.group(20)
                    c11=m.group(21)
                    word5=m.group(22)

                    url = int1+c7+word3+signed_int1+c8+yyyymmdd1+c9+word4+c10+alphanum1
                    ver = word3+signed_int1
                    device = alphanum1
                    
                    night = SettingItem(panel = panel, title = "%s" % device.upper(), disabled=False, desc = "Build: %s" % ver + "\nBuild Date: %s" % yyyymmdd1)
                    night_btn = CustomButton(text="%s" % url ,size_hint=(None, None),width=330, height=40)
                    night.add_widget(night_btn)
                    msg.add_widget(night) 
                    
                    def cm_nightly(self):
                        webbrowser.open('http://get.cm/get/jenkins%s' % c6+self.text+c11+word5)
                    night_btn.bind(on_release=cm_nightly)
            
        root = ScrollView(size_hint=(None, None), size=(730, 390), do_scroll_x=False)
        root.add_widget(msg)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
        
        popup = Popup(background='atlas://images/eds/pop', title='CyanogenMod (NIGHTLY)',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(750, 500))
        done.bind(on_release=popup.dismiss)
        popup.open()
        
    except:
        EdsNotify().run("'Url Not Found", 'Error Loading: http://get.cm')


def boot_scripts(self):
    self.panel_layout.clear_widgets()
    title = Label(text='[b][color=#22A0D6][size=20]Init.d Scripts[/size][/color][/b]', markup = True, pos_hint={'x':.0, 'y':.20})
    grid_layout = GridLayout(cols=3, row_force_default=True, row_default_height=40, spacing=10, pos_hint={'x':.0, 'y':-.35})
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

    
