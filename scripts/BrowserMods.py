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
from scripts.EdsNotify import EdsNotify

    
def browse_mods(self):
    try:
        shutil.rmtree('%s/apktool' % Home)
        os.chdir(Apktool)
        output = os.popen('java -jar apktool.jar if %s/framework-res.apk' % (Rom_Frame))
        print output
    except:
        EdsNotify().run("Could Not Find Framework-res.apk", "Framework-res.apk must be in EDS_WORKING Directory" )
    try:
        os.chdir(Apktool)
        output = os.popen('java -jar apktool.jar if %s/com.htc.resources.apk' % (Rom_Frame))
        print output
    except: 
        print "No Htc Resources Found.... Skipping"
    os.chdir(Apktool)
    if os.path.exists('%s/Browser.apk' % SystemApp) == True:
        output = os.popen('java -jar apktool.jar d -f %s/Browser.apk' % (SystemApp) + ' %s/out' % (SystemApp)).read()
        print output
        check_smali(self)
    else:
        print 'Cant find Browser.apk'

def check_smali(self):
    if  os.path.exists("%s/BrowserSettings.smali" % (Browser)) == True:
        print 'Smali Found'
        BrowserPop(self)
        
def BrowserPop(self):
    layout = GridLayout(cols=1, size_hint=(None, 1.0), width=700)
    layout.bind(minimum_height=layout.setter('height'))
    panel = SettingsPanel(title="Browser Mods", settings=self)   
    main = BoxLayout(orientation = 'vertical')
    root = ScrollView(size_hint=(None, None),bar_margin=-11, bar_color=(47 / 255., 167 / 255., 212 / 255., 1.), do_scroll_x=False)
    root.size = (600, 400)
    root.add_widget(layout)
    main.add_widget(root)
    done = Button(text ='Done Choosing Options')
    main.add_widget(done)
    if 'const/4 v0, 0x4' in open("%s/BrowserSettings.smali" % (Browser)).read():
        fp = open("%s/BrowserSettings.smali" % (Browser), "r")
        lines = fp.readlines()
        fp.close()
        tabs = SettingItem(panel = panel, title = "Unlimited Browser Tabs",disabled=False, desc = "Allows Unlimited number of browser tabs to be open")
        for i in range(len(lines)):
            if 'const/4 v0, 0x4' in open("%s/BrowserSettings.smali" % (Browser)).read():
                tabs_switch = Switch(active=False)
                continue
            if 'const/4 v0, 0x4' in open("%s/BrowserSettings.smali" % (Browser)).read():
                tabs_switch = Switch(active=True)
        tabs.add_widget(tabs_switch)
        layout.add_widget(tabs)
    
        def callback(instance, value):
            tabs_state(instance, value)
        tabs_switch.bind(active=callback)
    
    popup = Popup(background='atlas://images/eds/pop', title='Browser Mods', content=main, auto_dismiss=False, size_hint=(None, None), size=(630, 500))
    popup.open()

    def finish(self):
        finish_browser(self)
        popup.dismiss()
    done.bind(on_release=finish)
    
def tabs_state(instance, value):
    if value == True:
        os.chdir(Browser)
        for i, line in enumerate(fileinput.input('%s/BrowserSettings.smali' % Browser, inplace = 1)):
            sys.stdout.write(line.replace('const/4 v0, 0x4', 'const v0, 0xf'))
    elif value == False:
        os.chdir(Browser)
        for i, line in enumerate(fileinput.input('%s/BrowserSettings.smali' % Browser, inplace = 1)):
            sys.stdout.write(line.replace('const v0, 0xf', 'const/4 v0, 0x4'))
        
        
def finish_browser(self):
    try:
        os.chdir(Apktool)
        if os.path.exists('%s/Browser.apk' % SystemApp) == True:
            os.rename('%s/Browser.apk' % SystemApp, '%s/Browser.apk.bak' % SystemApp)
            output = os.popen('java -jar apktool.jar b -f %s/out' % (SystemApp) + ' %s/Browser.apk' % (SystemApp)).read()
            print output
            pass
        else:
            print 'NO Browser ERROR'
    except:
        'NO FILES FOUND'
    os.remove('%s/Browser.apk.bak' % SystemApp)
    shutil.rmtree('%s/out' % SystemApp) 