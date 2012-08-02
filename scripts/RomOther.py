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
import datetime
from kivy.uix.textinput import TextInput
from EdsNotify import EdsNotify

def add_aroma(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
    add = Button(text='Add', size_hint_x=None, width=150)
    cancel = Button(text='Cancel', size_hint_x=None, width=150)
    root.add_widget(Label(text='Are You Sure You Want To\nAdd Aroma Inastaller?'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(add)
    btn_layout.add_widget(cancel)
    popup = Popup(background='atlas://images/eds/pop', title='Add Option',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    cancel.bind(on_release=popup.dismiss)
    popup.open()
 
    
    def callback(instance):
        try:
            pathtofile = '%s/Aroma/Aroma.zip' % (Tools)
            destpath = '%s/META-INF/com/google/android' % (Rom)
            z = zipfile.ZipFile(pathtofile)
            z.extractall(destpath)
            f = open(UScript)
            text = f.read()
            f.close()
            f = open(UScript, 'w')
            f.write('''ui_print("");
    #
    # WIPE = config.prop => selected.1=2
    #
    if
      file_getprop("/tmp/aroma-data/config.prop","selected.1") == "2"
    then
    sleep(3);\n''')
            f.write(text)
            f.close()
            aroma(self)
            dev_name(self)
            device(self)
            today(self)
            contact(self) 
        except:
            EdsNotify().run("'Custom Rom Not Found", "'\nPlease Select Base Rom Then Try Again\n")          
    add.bind(on_press=callback)
    add.bind(on_release=popup.dismiss) 


def aroma(self):
    self.panel_layout.clear_widgets()
    title = Label(text='[b][color=#22A0D6][size=20]Custom Aroma Configuration[/size][/color][/b]', markup = True, pos_hint={'x':-.05, 'y':.20})
    name_lbl = Label(text='[b][color=ffffff][size=12]Set Rom Name :[/size][/color][/b]', markup = True, pos_hint={'x':-.30, 'y':.08})
    ver_lbl = Label(text='[b][color=ffffff][size=12]Rom Version Number :[/size][/color][/b]', markup = True, pos_hint={'x':-.30, 'y':-.02})  
    dev_lbl = Label(text='[b][color=ffffff][size=12]Developer Name :[/size][/color][/b]', markup = True, pos_hint={'x':-.30, 'y':-.12})  
    name = TextInput(text='', multiline=False, pos_hint={'x':.400, 'y':.550}, size_hint=(.50, .05))
    ver = TextInput(text='', multiline=False, pos_hint={'x':.400, 'y':.450}, size_hint=(.50, .05))
    dev = TextInput(text='', multiline=False, pos_hint={'x':.400, 'y':.350}, size_hint=(.50, .05))
    self.panel_layout.add_widget(title)
    self.panel_layout.add_widget(name_lbl)
    self.panel_layout.add_widget(name)
    self.panel_layout.add_widget(ver_lbl)
    self.panel_layout.add_widget(ver)
    self.panel_layout.add_widget(dev_lbl)
    self.panel_layout.add_widget(dev)

    
    
    def name_enter(self):
        processing_change = False
        for line in fileinput.input(Aroma, inplace=1):
            if line.startswith('ini_set("rom_name",             "'):
                processing_change = True
            else:
                if processing_change:
                    print r'ini_set("rom_name",             "' + name.text + r'");'
                    processing_change = False
                print line,
                
        for line in fileinput.input(Aroma, inplace=1):
            if line.startswith('  "You are about to Install <b>'):
                processing_change = True
            else:
                if processing_change:
                    print r'  "You are about to Install <b>' + name.text + r'</b>. \n\n"+'
                    processing_change = False
                print line,

        for line in fileinput.input(Aroma, inplace=1):
            if line.startswith('  "Please read carefully <b>'):
                processing_change = True
            else:
                if processing_change:
                    print r'  "Please read carefully <b>' + name.text + r'</b> Terms of Use Below...",'
                    processing_change = False
                print line,
                
        for line in fileinput.input(Terms, inplace=1):
            if line.startswith('Rom: '):
                processing_change = True
            else:
                if processing_change:
                    print r'Rom: ' + name.text + r''
                    processing_change = False
                print line,
                
        for line in fileinput.input(BuildProp, inplace=1):
            if line.startswith(r'ro.build.description='):
                processing_change = True
            else:
                if processing_change:
                    print r'ro.build.description=' + name.text + r''
                    processing_change = False
                print line, 

    name.bind(on_text_validate=name_enter)
    
    
    def ver_enter(self):
        processing_change = False
        
        for line in fileinput.input(Aroma, inplace=1):
            if line.startswith(r'ini_set("rom_version",'):
                processing_change = True
            else:
                if processing_change:
                    print r'ini_set("rom_version",          "' + ver.text + r'");'
                    processing_change = False
                print line,
                
        for line in fileinput.input(Aroma, inplace=1):
            if line.startswith(r'    "\t\tVERSION\t: <#080>'):
                processing_change = True
            else:
                if processing_change:
                    print r'    "\t\tVERSION\t: <#080>' + ver.text + r'\n"+'
                    processing_change = False
                print line,
                
        for line in fileinput.input(Terms, inplace=1):
            if line.startswith(r'Build: '):
                processing_change = True
            else:
                if processing_change:
                    print r'Build: ' + ver.text + r''
                    processing_change = False
                print line,
                
        for line in fileinput.input(BuildProp, inplace=1):
            if line.startswith('ro.product.version='):
                processing_change = True
            else:
                if processing_change:
                    print r'ro.product.version=' + ver.text + r''
                    processing_change = False
                print line, 
                          
    ver.bind(on_text_validate=ver_enter)
    
    
    def dev_enter(self):
        processing_change = False
        for line in fileinput.input(Aroma, inplace=1):
            if line.startswith(r'ini_set("rom_author",           "'):
                processing_change = True
            else:
                if processing_change:
                    print 'ini_set("rom_author",           "' + dev.text + '");'
                    processing_change = False
                print line,

        for line in fileinput.input(Terms, inplace=1):
            if line.startswith(r'Developer: '):
                processing_change = True
            else:
                if processing_change:
                    print r'Developer: ' + dev.text + r''
                    processing_change = False
                print line,

        for line in fileinput.input(BuildProp, inplace=1):
            if line.startswith(r'ro.build.host='):
                processing_change = True
            else:
                if processing_change:
                    print r'ro.build.host=' + dev.text + r''
                    processing_change = False
                print line,
                
    dev.bind(on_text_validate=dev_enter)


def dev_name(self):
    fin = open(EdsIni)
    for line in fin:
        if line.startswith("uname ="):
            l = line[7:-1].rstrip('\r\n')
    processing_change=False

    for line in fileinput.input(Aroma, inplace=1):
        if line.startswith(r'ini_set("rom_author",           "'):
            processing_change = True
        else:
            if processing_change:
                print 'ini_set("rom_author",           "' + l + '");'
                processing_change = False
            print line,

    for line in fileinput.input(Terms, inplace=1):
        if line.startswith(r'Developer: '):
            processing_change = True
        else:
            if processing_change:
                print r'Developer: ' + l + r''
                processing_change = False
            print line,
            
  
def device(self):
    fin = open(BuildProp)
    for line in fin:
        if line.startswith("ro.product.device="):
            l = line[18:-1].rstrip('\r\n')
    processing_change=False
    for line in fileinput.input(Aroma, inplace=1):
        if line.startswith(r'ini_set("rom_device",           "'):
            processing_change = True
        else:
            if processing_change:
                print r'ini_set("rom_device",           "' + l + '");'
                processing_change = False
            print line,

                             
def today(self):
    today = datetime.date.today()
    processing_change = False
    for line in fileinput.input(Aroma, inplace=1):
        if line.startswith(r'    "\t\tUPDATED\t: <#080>'):
            processing_change = True
        else:
            if processing_change:
                print r'    "\t\tUPDATED\t: <#080>' + today.strftime("%Y/%m/%d") +r'</#>\n\n\n"+'
                processing_change = False
            print line,

def contact(self):
    fin = open(EdsIni)
    for line in fin:
        if line.startswith("email ="):
            l = line[7:-1].rstrip('\r\n')
    processing_change=False
    for line in fileinput.input(Terms, inplace=1):
        if line.startswith(r'Contact: '):
            processing_change = True
        else:
            if processing_change:
                print r'Contact: ' + l + r''
                processing_change = False
            print line,


def boot_img(self):
    self.panel_layout.clear_widgets()
    title = Label(text='[b][color=#22A0D6][size=20]Boot.img Tools[/size][/color][/b]', markup = True, pos_hint={'x':-.05, 'y':.20})
    unpack = CustomButton(text='Unpack Boot.img', pos_hint={'x':.05, 'y':.550}, size_hint=(.40, .06))
    build = CustomButton(text='Build Boot.img', pos_hint={'x':.50, 'y':.550}, size_hint=(.40, .06))
    self.panel_layout.add_widget(title)
    self.panel_layout.add_widget(unpack)
    self.panel_layout.add_widget(build)
 
            
def deodex(self):
    self.panel_layout.clear_widgets()
    deodex_lbl = Label(text='[b][color=#22A0D6][size=20]Deodex Options[/size][/color][/b]', markup = True, pos_hint={'x':-.05, 'y':.20})
    self.panel_layout.add_widget(deodex_lbl)
    
def odex(self):
    self.panel_layout.clear_widgets()
    push_layout = GridLayout(cols=2, row_force_default=True, row_default_height=40, spacing=10, pos_hint={'x':-.05, 'y':-.525})
    shell_layout = GridLayout(cols=2, row_force_default=True, row_default_height=40, spacing=10, pos_hint={'x':-.05, 'y':-.825})
    odex_lbl = Label(text='[b][color=#22A0D6][size=20]Odex Options[/size][/color][/b]', markup = True, pos_hint={'x':-.0, 'y':.20})
    easy = CustomButton(text='One Step Odex', pos_hint={'x':.0, 'y':.575}, size_hint=(.90, .08))
    remount = CustomButton(text='1. Remount', pos_hint={'x':.25, 'y':.500}, size_hint=(.40, .06))
    pdexo = CustomButton(text='2. Push dexo',  size_hint=(.40, .06))
    pdexopt = CustomButton(text='3. Push dexopt-wrapper ',  size_hint=(.40, .06))
    pzip = CustomButton(text='4. Push zip', size_hint=(.40, .06))
    pzipalign = CustomButton(text='5. Push zipalign', size_hint=(.40, .06))
    pbusybox = CustomButton(text='6. Push busybox', size_hint=(.40, .06))
    perms = CustomButton(text='7. Set Permissions to 755', pos_hint={'x':.25, 'y':.225}, size_hint=(.40, .06))
    sbusybox = CustomButton(text='8. Install busybox', size_hint=(.40, .06))
    sdexo = CustomButton(text='9. Run dexo', size_hint=(.40, .06))
    frame = CustomButton(text='10. Pull /Framework', size_hint=(.40, .06))
    app = CustomButton(text='11. Pull /App', size_hint=(.40, .06))
    self.panel_layout.add_widget(odex_lbl)
    self.panel_layout.add_widget(push_layout)
    self.panel_layout.add_widget(shell_layout)
    self.panel_layout.add_widget(easy)
    self.panel_layout.add_widget(remount)
    push_layout.add_widget(pdexo)
    push_layout.add_widget(pdexopt)
    push_layout.add_widget(pzip)
    push_layout.add_widget(pzipalign)
    push_layout.add_widget(pbusybox)
    push_layout.add_widget(perms)
    shell_layout.add_widget(sbusybox)
    shell_layout.add_widget(sdexo)
    shell_layout.add_widget(frame)
    shell_layout.add_widget(app)
    
    def odex_now(self):
            os.chdir(Tools)
            comm = "./adb remount"
            output = os.popen(comm).read()
            print output
            comm = "./adb push " + Odex + '/dexo ' + '/system/bin'
            output = os.popen(comm).read()
            print output
            comm = "./adb push " + Odex + '/dexopt-wrapper ' + '/system/bin'
            output = os.popen(comm).read()
            print output
            comm = "./adb push " + Odex + '/zip' + '/system/xbin'
            output = os.popen(comm).read()
            print output
            comm = "./adb push " + Odex + '/zipalign' + '/system/xbin'
            output = os.popen(comm).read()
            print output
            comm = "./adb push " + Odex + '/busybox ' + '/system/xbin'
            output = os.popen(comm).read()
            print output
            comm = "./adb shell chmod 755 /system/bin/dexo /system/bin/dexopt-wrapper /system/xbin/zip /system/xbin/zipalign /system/xbin/busybox"
            output = os.popen(comm).read()
            print output
            comm = "./adb shell busybox --install /system/xbin"
            output = os.popen(comm).read()
            print output
            comm = "./adb shell dexo"
            output = os.popen(comm).read()
            print output
            os.chdir(Home)
            os.mkdir('%s/Desktop/framework' % Home)
            os.chdir('%s/Desktop/framework' % Home)
            os.chdir(Tools)
            comm = "./adb pull /system/framework %s/framework" % Home
            output = os.popen(comm).read()
            print output
            os.chdir(Home)
            os.mkdir('%s/Desktop/app' % Home)
            os.chdir('%s/Desktop/app' % Home)
            os.chdir(Tools)
            comm = "./adb pull /system/app %s/app" % Home
            output = os.popen(comm).read()
            print output
    easy.bind(on_release=odex_now)
    
    def sys_remount(self):
            os.chdir(Tools)
            comm = "./adb remount"
            output = os.popen(comm).read()
            print output
    remount.bind(on_release=sys_remount)
    
    def push_dexo(self):
            os.chdir(Tools)
            comm = "./adb push " + Odex + '/dexo ' + '/system/bin'
            output = os.popen(comm).read()
            print output
    pdexo.bind(on_release=push_dexo)
    
    def push_dexopt(self):
            os.chdir(Tools)
            comm = "./adb push " + Odex + '/dexopt-wrapper ' + '/system/bin'
            output = os.popen(comm).read()
            print output
    pdexopt.bind(on_release=push_dexopt)
    
    def push_zip(self):
            os.chdir(Tools)
            comm = "./adb push " + Odex + '/zip' + '/system/xbin'
            output = os.popen(comm).read()
            print output
    pzip.bind(on_release=push_zip)
    
    def push_zipalign(self):
            os.chdir(Tools)
            comm = "./adb push " + Odex + '/zipalign' + '/system/xbin'
            output = os.popen(comm).read()
            print output
    pzipalign.bind(on_release=push_zipalign)
    
    def push_busybox(self):
            os.chdir(Tools)
            comm = "./adb push " + Odex + '/busybox ' + '/system/xbin'
            output = os.popen(comm).read()
            print output
    pbusybox.bind(on_release=push_busybox)
    
    def change_perms(self):
            os.chdir(Tools)
            comm = "./adb shell chmod 755 /system/bin/dexo /system/bin/dexopt-wrapper /system/xbin/zip /system/xbin/zipalign /system/xbin/busybox"
            output = os.popen(comm).read()
            print output
    perms.bind(on_release=change_perms)

    def ins_busybox(self):
            os.chdir(Tools)
            comm = "./adb shell busybox --install /system/xbin"
            output = os.popen(comm).read()
            print output
    sbusybox.bind(on_release=ins_busybox)
         
    def run_dexo(self):
            os.chdir(Tools)
            comm = "./adb shell dexo"
            output = os.popen(comm).read()
            print output
    sdexo.bind(on_release=run_dexo)
            
    def pull_frame(self):
            os.chdir(Home)
            os.mkdir('%s/Desktop/framework' % Home)
            os.chdir('%s/Desktop/framework' % Home)
            os.chdir(Tools)
            comm = "./adb pull /system/framework %s/Desktop/framework" % Home
            output = os.popen(comm).read()
            print output
    frame.bind(on_release=pull_frame)
    
    def pull_app(self):
            os.chdir(Home)
            os.mkdir('%s/Desktop/app' % Home)
            os.chdir('%s/Desktop/app' % Home)
            os.chdir(Tools)
            comm = "./adb pull /system/app %s/Desktop/app" % Home
            output = os.popen(comm).read()
            print output
    app.bind(on_release=pull_app)
    
