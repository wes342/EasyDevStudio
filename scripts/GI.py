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

################## IMPORTS ###################

import os
import sys
import pwd
import glob
import kivy
import urllib
import shutil
import tarfile
import zipfile
import time
import platform
import fileinput
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.config import ConfigParser
from scripts.EdsNotify import EdsNotify
from kivy.uix.spinner import Spinner


######################## MISC FUNCTIONS ######################################
VERSION = ('1.0.0')
NAME = ('Easy Development Studio')

## Detects Os To Determine What Method to use to find user name
if (os.name == "posix"):
    You = pwd.getpwuid(os.getuid())[0]
elif (os.name == "win32"):
    You = os.environ['USERNAME']
else:
    print "os undetected"
    
## Timestamp
timestamp = time.strftime('%Y-%m-%d %H:%M:%S', (time.localtime(time.time())))


# Tests users system to find Cpu Info
numprocs = [ int(line.strip()[-1]) for line in open('/proc/cpuinfo', 'r') if line.startswith('processor') ][-1] + 1

############## GLOBAL PATH VARS ######################

Home = os.path.expanduser('~')
Working = os.getcwd()
Root = '/usr/share/eds'
Scripts = '%s/scripts' % (Root)
Desktop = '%s/Desktop' % (Home)
Usr = '%s/.easydevstudio' % (Home)
Themes = '%s/Themes' % (Usr)
Conf = '%s/config' % (Root)
Logs = '%s/Logs' % (Usr)

#################### IMAGE PATHS ######################

Images = '%s/images' % (Root)

#################### GLOBAL IMAGES ####################
Bg = '%s/background.jpg' % (Usr)
Wall = '%s/background.jpg' % (Images)
ukv = '%s/eds.kv' % (Usr)
kv = '%s/eds.kv' % (Root)
Icon = '%s/icon.png' % (Images)

################# TOOLS DIRECTORIES ####################

Tools = '%s/Tools' % (Usr)
Apktool = '%s/Apktool' % (Tools)
Baksmali = '%s/Baksmali' % (Tools)
Dex2jar = '%s/Dex2jar' % (Tools)
Jdgui = '%s/Jd_gui' % (Tools)
Odex = '%s/Odex' % (Tools)
Signapk = '%s/Signapk' % (Tools)
Zipalign = '%s/Zipalign' % (Tools)
Initd = '%s/Initd' % (Tools)

############## EDS WORKING DIRECTORIES ##################

EdsWorking = '%s/EDS_WORKING' % (Home)
Rom = '%s/Custom_Rom' % (EdsWorking)
Mod_File = '%s/Mod_A_File' % (EdsWorking)
Pulled = '%s/Pulled_Files' % (EdsWorking)
Removed = '%s/Removed_Apps' % (EdsWorking)
Sign_Apk = '%s/Sign_An_Apk' % (EdsWorking)

############### CUSTOM_ROM DIRECTORIES ###################

System = '%s/system' % (Rom)
DataApp = '%s/data/app' % (Rom)
SystemApp = '%s/system/app' % (Rom)
Update = '%s/META-INF/com/google/android' % (Rom)
Camera = '%s/out/smali/com/android/camera' % (SystemApp)
Browser = '%s/out/smali/com/android/browser' % (SystemApp)
Rom_Frame = '%s/system/framework' % (Rom)
Rom_Initd = '%s/etc/init.d' % (System)

#################### FILES #################################

BuildProp = '%s/build.prop' % (System)
Aroma = '%s/aroma-config' % (Update)
UScript = '%s/updater-script' % (Update)
Terms = '%s/aroma/terms.txt' % (Update)
EdsIni = '%s/eds.ini' % (Usr)
Reg = '%s/Usr.txt' % (Usr)
Change = '%s/aroma/change.txt' % (Update)
Changelog = '%s/change.txt' % (Rom)
################## FASTBOOT COMMANDS ########################

Boot = '%s/boot.img' % (EdsWorking)
Recovery = '%s/recovery.img' % (EdsWorking)
FlashBoot = './fastboot flash boot %s/boot.img' % (EdsWorking)
BootRec = './fastboot boot %s/recovery.img' % (EdsWorking)

##################### APK COMMANDS #################################3

Framework = 'java -jar apktool.jar if %s/framework-res.apk' % (EdsWorking)
Resources = 'java -jar apktool.jar if %s/com.htc.resources.apk' % (EdsWorking)
DecApk = 'java -jar apktool.jar d -f %s/*.apk' % (Mod_File) + ' %s/out' % (Mod_File)
RecApk = 'java -jar apktool.jar b %s/out' % (Mod_File) + ' %s/repackaged-unsigned.apk' % (Mod_File)
Sign = 'java -jar signapk.jar testkey.x509.pem testkey.pk8 %s/repackaged-unsigned.apk' % (Mod_File) + ' %s/repackaged-signed.apk' % (Mod_File)
Jd = './jd-gui %s/*.jar' % (Mod_File)
Dex2j = './dex2jar.sh %s/*' % (Mod_File)
Sign_Other = 'java -jar signapk.jar testkey.x509.pem testkey.pk8 %s/*.apk' % (Sign_Apk) + ' %s/signed.apk' % (Sign_Apk)
RecDex = 'java -jar smali.jar -o %s/new_classes.dex' % (Mod_File) + ' %s/out' % (Mod_File)
DecDex = 'java -jar baksmali.jar -o %s/out' % (Mod_File) + ' %s/*.dex' % (Mod_File)

########################### URL's ######################################
Site = 'http://easydevstudio.com'
Forum = 'http://easydevstudio.com/forum'
Twitter = 'http://twitter.com/easydevstudio'
Bugs = 'http://code.google.com/p/easy-development-studio/issues/list'

eds_git = 'https://raw.github.com/wes342'
Cm7 = '%s/EdsLive/master/Devices_Cm7.list' % (eds_git)
Cm9 = '%s/EdsLive/master/Devices_Cm9.list' % (eds_git)
Cm10 = '%s/EdsLive/master/Devices_Cm10.list' % (eds_git)


################## about icons (Need to remove) #######################

#Images for About Team links 
#TODO fix so they can be reused and not needing set per team member	  	

B = Image(source='atlas://images/eds/site', size_hint_x=None, width=50)
T = Image(source='atlas://images/eds/contact', size_hint_x=None, width=50)  	
Tw = Image(source='atlas://images/eds/twit', size_hint_x=None, width=50)
B2 = Image(source='atlas://images/eds/site', size_hint_x=None, width=50)
T2 = Image(source='atlas://images/eds/contact', size_hint_x=None, width=50)
Tw2 = Image(source='atlas://images/eds/twit', size_hint_x=None, width=50)
B3 = Image(source='atlas://images/eds/site', size_hint_x=None, width=50)
T3 = Image(source='atlas://images/eds/contact', size_hint_x=None, width=50)
Tw3 = Image(source='atlas://images/eds/twit', size_hint_x=None, width=50)

#################### CREDITS AND CONTRIBUTORS ########################

Credits = '''\nTommyTomatoe,  Armenian6000,  GNU/Linux\n
bruit.all,  jesusfreke,  Emmanuel Dupuy,  Panxiaobo,\n
Google,  AOSP,  Open Handset Alliance\n''' 

# People who have made donations to the project
# TODO change list to $10+ only make to the list 
# If donations list becomes too large
Donors = '''Neil Faulkner, Ward Seabrook, WiLL Morehead,  Kenneth Soares'''

######################## GLOBAL LISTS ##############################

devices = []


# Custom Button Is a global button defined in eds.kv file
# All buttons Should be CustomButton not Button 
# This will make themes work when themeing eds.kv
class CustomButton(Button):
    pass

####################### GLOBAL FUNCTIONS ############################

# Makes EDS_WORKING dir to hold all users files
def mkworking(self):
    if os.path.exists(EdsWorking) == False:
        try:   
            os.mkdir(EdsWorking)
            os.mkdir(Rom)
            os.mkdir(Mod_File)
            os.mkdir(Pulled)
            os.mkdir(Removed)
            os.mkdir(Sign_Apk)
        except:
            print 'Error Making File System'
    else:
        print 'EDS_WORKING Directory Exists'

# Makes .easydevstudio folder in users home folder
# This dir holds:
#background.jpg (so themes can replace background.jpg with themes background image)
# eds.ini (Which is just the config file)
# eds.kv (this is so eds.kv can be used in a theme which will
# be loaded with "Builder.load_file('%s/eds.kv' % (Usr))" from main app class    
def mkusr_fs(self):
    if os.path.exists(Usr) == False:
        try:
            os.mkdir(Usr)
            os.mkdir('%s/Themes' % (Usr))
            shutil.copy(kv, '%s/eds.kv' % (Usr))
            shutil.copy(Wall, Usr)
            stock = '%s/Themes/Eds_stock_theme.zip' % (Root)
            dest = '%s/Themes' % (Usr)
            shutil.copy(stock, dest)
            red = '%s/Themes/Eds_red_theme.zip' % (Root)
            dest = '%s/Themes' % (Usr)
            shutil.copy(red, dest)
            os.mkdir('%s/Tools' % Usr)
            tzip = '%s/Tools/Tools.tar.gz' % (Root)
            tools = '%s/Tools' % (Usr)
            shutil.copy(tzip, tools)
            os.chdir('%s/Tools' % Usr)
            tar = tarfile.open('Tools.tar.gz')
            for item in tar:
                tar.extract(item)
            os.remove('Tools.tar.gz')
        except:
            print 'Cant make .easydevstudio Directory'
    else:
        print '.easydevstudio Directory Exists'


# Global restart function for applying themes, wallpapers etc..
# TODO fix so this works when changing file browser style
# which hangs for a long time will be used when figure out why its having issues   
def restart(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
    restart = Button(text='Restart', size_hint_x=None, width=150)
    cancel = Button(text='Cancel', size_hint_x=None, width=150)
    root.add_widget(Label(text='Would you like to restart now to apply changes?'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(restart)
    btn_layout.add_widget(cancel)
    popup = Popup(background='atlas://images/eds/pop', title='Restart',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    cancel.bind(on_press=popup.dismiss)
    popup.open()  

# This is the actual restart command   
    def callback(instance, value):
        python = sys.executable
        os.execl(python, python, * sys.argv)
    restart.bind(state=callback)
      

    
    
    
    
    
