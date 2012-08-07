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
import subprocess


def clean_working(self):
    if os.path.exists(Mod_File) == True:
        shutil.rmtree(Mod_File)
        shutil.rmtree(Sign_Apk)
        os.mkdir(Mod_File)
        os.mkdir(Sign_Apk)
        EdsNotify().run("Working Directory Cleaned", "\nFiles From:\n'Mod_A_File'\n'Sign_A_File'\nHave Been Cleaned Out")
    else: 
        print 'Cant Find %s' % (Mod_File)
        os.mkdir(Mod_File)

def install_framework(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=1, row_force_default=True, row_default_height=50, spacing=15, padding=20)
    rom = Button(text='From Rom', size_hint_x=None, width=300)
    mod_file = Button(text='From EDS_WORKING Dir', size_hint_x=None, width=300)
    cancel = Button(text='Cancel', size_hint_x=None, width=300)
    root.add_widget(btn_layout)
    btn_layout.add_widget(rom)
    btn_layout.add_widget(mod_file)
    btn_layout.add_widget(cancel)
    popup = Popup(background='atlas://images/eds/pop', title='Install Framework files',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(360, 265))
    cancel.bind(on_release=popup.dismiss)
    popup.open()
    
    def frame_rom(self):
        from_rom(self)
    rom.bind(on_release=frame_rom)
    rom.bind(on_release=popup.dismiss)
    
    def frame_mod(self):
        from_mod(self)
    mod_file.bind(on_release=frame_mod)
    mod_file.bind(on_release=popup.dismiss)
  

def from_mod(self):
    if os.path.exists('%s/framework-res.apk' % (EdsWorking)) == True:
        try:
            shutil.rmtree('%s/apktool' % (Home))
            os.chdir(Apktool)
            output = os.popen(Framework).read()
            print output
            EdsNotify().run("'Framework Install Complete", "\nYou can now  modify an apk file")
            if os.path.exists('%s/com.htc.resources.apk' % (EdsWorking)) == True:
                os.chdir(Apktool)
                output2 = os.popen(Resources).read()
                print output2
            else:
                print 'com.htc.resources.apk Not Found: Skipping....'
         
        except:
            print 'apktool dir not found: Moving on....'
            os.chdir(Apktool)
            output = os.popen(Framework).read()
            print output
            EdsNotify().run("'Framework Install Complete", "\nYou can now work with modify an apk file")
            if os.path.exists('%s/com.htc.resources.apk' % (EdsWorking)) == True:
                os.chdir(Apktool)
                output2 = os.popen(Resources).read()
                print output2
            else:
                print 'com.htc.resources.apk Not Found: Skipping....'
        print 'hello'
    else:
        EdsNotify().run("'framework-res.apk' NOT FOUND", "'\nframework-res.apk'\nNeeds To Be In:\n" + '%s/' % (EdsWorking))          
            
def from_rom(self):
    if os.path.exists('%s/framework-res.apk' % (Rom_Frame)) == True:
        try:
            os.remove('%s/framework-res.apk' % (EdsWorking))
            os.remove('%s/com.htc.resources.apk' % (EdsWorking))
        except:
            print 'cant remove old framework files'
        try:
            shutil.copy('%s/framework-res.apk' % (Rom_Frame),'%s/framework-res.apk' % (EdsWorking))
            shutil.copy('%s/com.htc.resources.apk' % (Rom_Frame),'%s/com.htc.resources.apk' % (EdsWorking))
            from_mod(self)
        except:
            print 'No Framework Files Found'

      

def Decompile_Apk(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=1, row_force_default=True, row_default_height=50, spacing=15, padding=20)
    rom = Button(text='From Rom', size_hint_x=None, width=300)
    mod_file = Button(text='From Mod_A_File Dir', size_hint_x=None, width=300)
    cancel = Button(text='Cancel', size_hint_x=None, width=300)
    root.add_widget(btn_layout)
    btn_layout.add_widget(rom)
    btn_layout.add_widget(mod_file)
    btn_layout.add_widget(cancel)
    popup = Popup(background='atlas://images/eds/pop', title='Decompile An Apk',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(360, 265))
    cancel.bind(on_release=popup.dismiss)
    popup.open()
    
    def dec_from_rom(self):
        dec_rom(self)
    rom.bind(on_release=dec_from_rom)
    rom.bind(on_release=popup.dismiss)
    
    def dec_from_mod(self):
        dec_apk(self)
    mod_file.bind(on_release=dec_from_mod)
    mod_file.bind(on_release=popup.dismiss)
           

def dec_apk(self):
        if os.listdir(Mod_File):
            os.chdir(Apktool)
            output = os.popen(DecApk).read()
            print output
            if os.path.exists('%s/out/apktool.yml' % (Mod_File)):
                EdsNotify().run('Decompile Complete', "\nYour Apk Decompiled Successfully")
            else:
                EdsNotify().run('Decompile Failed', "\nCheck Your Framework Files")                
        else:
            EdsNotify().run('No Apk Found', "\nAn APk Needs To Be In:\n" + '%s/' % (Mod_File))           

def dec_rom(self):
    Box = BoxLayout(orientation="vertical", spacing=10)
    msg = GridLayout(cols=1, padding=15, spacing=10, size_hint_y=None)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    popup = Popup(background='atlas://images/eds/pop', title='Decompile An Apk',content=Box, auto_dismiss=True,        
    size_hint=(None, None), size=(400, 400))
    try:
        file_listing = os.listdir(SystemApp)
        file_listing.sort()
        for item in file_listing:
            btnname = (CustomButton(text='%s' % item, font_size=10, size_hint_y=None, height=40))
            msg.add_widget(btnname)
            btnname.bind(on_release=do_button)
            btnname.bind(on_release=popup.dismiss)
        root = ScrollView(size_hint=(None, None), size=(375, 290), do_scroll_x=False)
        root.add_widget(msg)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
        done.bind(on_release=popup.dismiss)
        popup.open()
    except:
        EdsNotify().run("'system/app Directory Not Found", 'Cant Find:\n' + SystemApp)    

def do_button(self):
    filepath = "%s/%s" % (SystemApp, self.text)
    if os.path.exists(Mod_File) == True:
        shutil.rmtree(Mod_File)
        os.mkdir(Mod_File)
        shutil.copy(filepath , Mod_File)
        dec_apk(self)
    else:
        EdsNotify().run("'Mod_A_File Directory Not Found", 'Cant Find:\n' + Mod_File)
      
def rec_apk(self):
    if os.path.exists('%s/out/apktool.yml' % (Mod_File)) == True:
            os.chdir(Apktool)
            output = os.popen(RecApk).read()
            print output
            EdsNotify().run('Recompile Complete', "\nYour Apk Recompiled Successfully")
    else:
        EdsNotify().run("Error: Recompile Failed", "\nbrut.directory.PathNotExitst: apktool.yml")        
            
def sign(self):
    if os.path.exists('%s/repackaged-unsigned.apk' % (Mod_File)) == True:
        os.chdir(Signapk)
        output = os.popen(Sign).read()
        print output
        os.remove('%s/repackaged-unsigned.apk' % (Mod_File))
        EdsNotify().run("Apk Has Been Signed", "Your File is in:\n" + '%s/' % (Mod_File))   
    else:
        EdsNotify().run("File Not Found", "An 'repackaged-unsigned.apk' Needs To Be In:\n" + '%s/' % (Mod_File))
    
def source(self):
    if os.listdir(Mod_File):
        os.chdir(Dex2jar)
        output = os.popen(Dex2j).read()
        print output
        os.chdir(Jdgui)
        output = os.popen(Jd).read()
        print output
        for filename in glob.glob('%s/*_dex2jar.jar' % (Mod_File)) :
            os.remove(filename) 
        #os.remove('%s/dex2jar.jar' % (Mod_File))
    else:
        EdsNotify().run("File Error", "A File Could Not Be Found In:\n" + '%s/\n' % (Mod_File) + 'Or Could Not View Source For That File')
        
def sign_misc(self):
    if os.listdir(Sign_Apk):
        os.chdir(Signapk)
        output = os.popen(Sign_Other)
        print output
        EdsNotify().run("Apk Has Been Signed", "Your File is in:\n" + '%s/' % (Sign_Apk))
    else:
            EdsNotify().run("File Error", "A File Could Not Be Found In:\n" + '%s/\n' % (Sign_Apk))

def dec_dex(self):
        if os.listdir(Mod_File):
            try:
                os.rmdir('%s/out' % (Mod_File))
                os.chdir(Baksmali)
                output = os.popen(DecDex).read()
                print output
                
            except:
                print 'No out directory detected: Skipping... '
                os.chdir(Baksmali)
                output = os.popen(DecDex).read()
                print output
                if os.path.exists('%s/out' % (Mod_File)) == True:
                    EdsNotify().run('Decompile Complete', "Your Dex File Decompiled Successfully")
                else:
                    EdsNotify().run('Decompile Error', "Check Integrity of Dex File")
        else:
            EdsNotify().run('No Dex Found', "A Dex Needs To Be In:\n" + '%s/' % (Mod_File))     
        
def rec_dex(self):
    if os.path.exists('%s/out' % (Mod_File)) == True:
        os.chdir(Baksmali)
        output = os.popen(RecDex).read()
        print output
        if os.path.exists('%s/new_classes.dex' % (Mod_File)) == True:
            EdsNotify().run('Recompile Complete', "Your Dex File Recompiled Successfully")
        else:
            EdsNotify().run('Recompile Error', "Check Integrity of Dex File")
    else:
        EdsNotify().run("No 'out' Directory Found", '\nYou Must Decompile a Dex file first')

def draw9_patch(self):
    print 'Implimented In Future'


def apk_run(self):
    comm = self.text_input.text
    output = os.popen(comm).read()
    print output
    self.text_input.text = ''
    EdsNotify().run("Shell Command Output", output)

def apk_help(self):
    print 'Future Help Implementation'
