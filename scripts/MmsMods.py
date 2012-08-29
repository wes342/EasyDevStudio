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


def mms_mods(self):
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
            
        if os.path.exists('%s/Mms.apk' % SystemApp) == True:
            output = os.popen('java -jar apktool.jar d -f %s/Mms.apk' % (SystemApp) + ' %s/out' % (SystemApp)).read()
            print output
            check_smali(self)
        else:
            print 'Cant find Mms.apk. Now Looking for Message+CRC_1.apk'
            
            if os.path.exists('%s/Message+CRC_1.apk' % SystemApp) == True:
                output = os.popen('java -jar apktool.jar d -f %s/Message+CRC_1.apk' % (SystemApp) + ' %s/out' % (SystemApp)).read()
                print output
                check_smali(self)
            else:
                print 'Cant open Message+CRC_1.apk Looking for Message+CRC_2.apk'               
                            
            if os.path.exists('%s/Message+CRC_2.apk' % SystemApp) == True:
                output = os.popen('java -jar apktool.jar d -f %s/Message+CRC_2.apk' % (SystemApp) + ' %s/out' % (SystemApp)).read()
                print output
                check_smali(self)
            else:
                print 'Cant open Message+CRC_2.apk'
                EdsNotify().run("No Mms Files found", "Please check Base Rom Directory for a Mms Files" )

def check_smali(self):
    if  os.path.exists("%s/ImageModel.smali" % (Mms)) == True:
        print 'Smali Found'
        MmsPop(self)

def MmsPop(self):
    layout = GridLayout(cols=1, size_hint=(None, 1.0), width=700)
    layout.bind(minimum_height=layout.setter('height'))
    panel = SettingsPanel(title="Mms Mods", settings=self)   
    main = BoxLayout(orientation = 'vertical')
    root = ScrollView(size_hint=(None, None),bar_margin=-11, bar_color=(47 / 255., 167 / 255., 212 / 255., 1.), do_scroll_x=False)
    root.size = (600, 400)
    root.add_widget(layout)
    main.add_widget(root)
    done = Button(text ='Done Choosing Options')
    main.add_widget(done)
    if """    .line 77
    const/4 v0, 0x1

    sput-boolean v0, Lcom/android/mms/model/ImageModel;->mCheckResolution:Z""" in open("%s/ImageModel.smali" % (Mms)).read():
        fp = open("%s/ImageModel.smali" % (Mms), "r")
        lines = fp.readlines()
        fp.close()
        comp = SettingItem(panel = panel, title = "Remove Mms Compression",disabled=False, desc = "Disables Compression of Mms Messages")
        for i in range(len(lines)):
            if """    .line 77
    const/4 v0, 0x1

    sput-boolean v0, Lcom/android/mms/model/ImageModel;->mCheckResolution:Z""" in open("%s/ImageModel.smali" % (Mms)).read():
                comp_switch = Switch(active=False)
                continue
            if """    .line 77
    const/4 v0, 0x1

    sput-boolean v0, Lcom/android/mms/model/ImageModel;->mCheckResolution:Z""" in open("%s/ImageModel.smali" % (Mms)).read():
                comp_switch = Switch(active=True)
        comp.add_widget(comp_switch)
        layout.add_widget(comp)
    
        def callback(instance, value):
            comp_state(instance, value)
        comp_switch.bind(active=callback)

    popup = Popup(background='atlas://images/eds/pop', title='Mms Mods', content=main, auto_dismiss=False, size_hint=(None, None), size=(630, 500))
    popup.open()

    def finish(self):
        finish_comp(self)
        popup.dismiss()
    done.bind(on_release=finish)
    
def comp_state(instance, value):
    if value == True:
        lines = open("%s/ImageModel.smali" % Mms, 'r').readlines()
        lines[51] = "    #const/4 v0, 0x1\n"
        lines[53] = "    #sput-boolean v0, Lcom/android/mms/model/ImageModel;->mCheckResolution:Z\n"
        out = open("%s/ImageModel.smali" % Mms, 'w')
        out.writelines(lines)
        out.close()

    elif value == False:
        lines = open("%s/ImageModel.smali" % Mms, 'r').readlines()
        lines[51] = "    const/4 v0, 0x1\n"
        lines[53] = "    sput-boolean v0, Lcom/android/mms/model/ImageModel;->mCheckResolution:Z\n"
        out = open("%s/ImageModel.smali" % Mms, 'w')
        out.writelines(lines)
        out.close()

def finish_comp(self):
    try:
        os.chdir(Apktool)
        if os.path.exists('%s/Mms.apk' % SystemApp) == True:
            os.rename('%s/Mms.apk' % SystemApp, '%s/Mms.apk.bak' % SystemApp)
            output = os.popen('java -jar apktool.jar b -f %s/out' % (SystemApp) + ' %s/Mms.apk' % (SystemApp)).read()
            print output
            pass
        else:
            print 'NO Mms ERROR'
        if os.path.exists('%s/Message+CRC_1.apk' % SystemApp) == True:
            os.rename('%s/Message+CRC_1.apk' % SystemApp, '%s/Message+CRC_1.apk.bak' % SystemApp)
            output = os.popen('java -jar apktool.jar b -f %s/out' % (SystemApp) + ' %s/Message+CRC_1.apk' % (SystemApp)).read()
            print output
        else:
            print 'NO Message+CRC_1 ERROR'
        if os.path.exists('%s/Message+CRC_2.apk' % SystemApp) == True:
            os.rename('%s/Message+CRC_2.apk' % SystemApp, '%s/Message+CRC_2.apk.bak' % SystemApp)
            output = os.popen('java -jar apktool.jar b -f %s/out' % (SystemApp) + ' %s/Message+CRC_2.apk' % (SystemApp)).read()
            print output
        else:
            print 'NO Message+CRC_2 ERROR'
            
        try:
            if os.path.exists("%s/Mms.apk" % SystemApp) == True:
                os.remove('%s/Mms.apk.bak' % SystemApp)
                shutil.rmtree('%s/out' % SystemApp)
            else:
                os.rename('%s/Mms.apk.bak' % SystemApp, '%s/Mms.apk' % SystemApp)
                shutil.rmtree('%s/out' % SystemApp)
        except:
            try:
                if os.path.exists("%s/Message+CRC_1.apk" % SystemApp) == True:
                    os.remove('%s/Message+CRC_1.apk.bak' % SystemApp)
                    shutil.rmtree('%s/out' % SystemApp)
                else:
                    os.rename('%s/Message+CRC_1.apk.bak' % SystemApp, '%s/Message+CRC_1.apk' % SystemApp)
                    shutil.rmtree('%s/out' % SystemApp)
            except:
                try:
                    if os.path.exists("%s/Message+CRC_2.apk" % SystemApp) == True:
                        os.remove('%s/Message+CRC_2.apk.bak' % SystemApp)
                        shutil.rmtree('%s/out' % SystemApp)
                    else:
                        os.rename('%s/Message+CRC_2.apk.bak' % SystemApp, '%s/Message+CRC_2.apk' % SystemApp)
                        shutil.rmtree('%s/out' % SystemApp)
                        
                except:
                    print "I Dont know what went wrong"
    except:
        print "something"

    
    
    