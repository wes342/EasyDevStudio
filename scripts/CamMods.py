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

    
def cam_mods(self):
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
    if os.path.exists('%s/HTCCamera.apk' % SystemApp) == True:
        output = os.popen('java -jar apktool.jar d -f %s/HTCCamera.apk' % (SystemApp) + ' %s/out' % (SystemApp)).read()
        print output
        check_smali(self)
    else:
        print 'Cant find HTCCamera.apk. Now Looking for Camera.apk'
        
        if os.path.exists('%s/Camera.apk' % SystemApp) == True:
            output = os.popen('java -jar apktool.jar d -f %s/Camera.apk' % (SystemApp) + ' %s/out' % (SystemApp)).read()
            print output
            check_smali(self)
        else:
            print 'Cant open Camera.apk'
            EdsNotify().run("No Camera found", "Please check Mod_A_File Directory for a Camera apk" )

def check_smali(self):
    if  os.path.exists("%s/DisplayDevice.smali" % (Camera)) == True:
        print 'Smali Found'
        CamPop(self)
        
def CamPop(self):
    layout = GridLayout(cols=1, size_hint=(None, 2.5), width=700)
    layout.bind(minimum_height=layout.setter('height'))
    panel = SettingsPanel(title="Camera Mods", settings=self)   
    main = BoxLayout(orientation = 'vertical')
    root = ScrollView(size_hint=(None, None),bar_margin=-11, bar_color=(47 / 255., 167 / 255., 212 / 255., 1.), do_scroll_x=False)
    root.size = (600, 400)
    root.add_widget(layout)
    main.add_widget(root)
    done = Button(text ='Done Choosing Options')
    main.add_widget(done)
    if '.method public static EnableGeoTagByDefault()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        geo = SettingItem(panel = panel, title = "Enable Geo Tagging",disabled=False, desc = "add geo tagging to photos")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                geo_switch = Switch(active=False)
                #value = False
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                geo_switch = Switch(active=True)
                #value = True
            elif ".method public static EnableGeoTagByDefault()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        geo.add_widget(geo_switch)
        layout.add_widget(geo)
        
        def callback(instance, value):
            geo_state(instance, value)
        geo_switch.bind(active=callback)
        
    if '.method public static canCancelFocus()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        focus = SettingItem(panel = panel, title = "Can Cancel Focus",disabled=False, desc = "Ability To Cancel Focus")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                focus_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                focus_switch = Switch(active=True)
            elif ".method public static canCancelFocus()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        focus.add_widget(focus_switch)
        layout.add_widget(focus)
        
        def callback(instance, value):
            focus_state(instance, value)
        focus_switch.bind(active=callback)
        
    if '.method public static captrueFullSize()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        full = SettingItem(panel = panel, title = "Capture Full Size",disabled=False, desc = "Captures Pictures At Full Size")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                full_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                full_switch = Switch(active=True)
            elif ".method public static captrueFullSize()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        full.add_widget(full_switch)
        layout.add_widget(full)
        
        def callback(instance, value):
            full_state(instance, value)
        full_switch.bind(active=callback)
            
    if '.method public static forceSutterSound()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        shutter = SettingItem(panel = panel, title = "Force Shutter Sound",disabled=False, desc = "Forces Shutter Sound To Always On")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                shutter_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                shutter_switch = Switch(active=True)
            elif ".method public static forceSutterSound()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        shutter.add_widget(shutter_switch)
        layout.add_widget(shutter)
        
        def callback(instance, value):
            shutter_state(instance, value)
        shutter_switch.bind(active=callback)

    if '.method public static hasAutoFocus()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        auto_focus = SettingItem(panel = panel, title = "Has Auto Focus",disabled=False, desc = "Allows Auto Focus")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                auto_focus_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                auto_focus_switch = Switch(active=True)
            elif ".method public static hasAutoFocus()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        auto_focus.add_widget(auto_focus_switch)
        layout.add_widget(auto_focus)
        
        def callback(instance, value):
            auto_focus_state(instance, value)
        auto_focus_switch.bind(active=callback)

    if '.method public static hasLimit250KB()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        has_limit = SettingItem(panel = panel, title = "Has 250KB Limit",disabled=False, desc = "Limits File Size to 250KB")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                has_limit_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                has_limit_switch = Switch(active=True)
            elif ".method public static hasLimit250KB()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        has_limit.add_widget(has_limit_switch)
        layout.add_widget(has_limit)
        
        def callback(instance, value):
            has_limit_state(instance, value)
        has_limit_switch.bind(active=callback)   
        
    if '.method public static removeMMS()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        no_mms = SettingItem(panel = panel, title = "Remove MMS",disabled=False, desc = "Removes MMS Option")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                no_mms_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                no_mms_switch = Switch(active=True)
            elif ".method public static removeMMS()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        no_mms.add_widget(no_mms_switch)
        layout.add_widget(no_mms)
        
        def callback(instance, value):
            no_mms_state(instance, value)
        no_mms_switch.bind(active=callback)  
        
    if '.method public static support128kBitrate()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        s_128 = SettingItem(panel = panel, title = "Support 128k Bitrate",disabled=False, desc = "Supports 128k Bitrate")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                s_128_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                s_128_switch = Switch(active=True)
            elif ".method public static support128kBitrate()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        s_128.add_widget(s_128_switch)
        layout.add_widget(s_128)
        
        def callback(instance, value):
            s_128_state(instance, value)
        s_128_switch.bind(active=callback) 

    if '.method public static supportAutoUpload()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        auto_up= SettingItem(panel = panel, title = "Support Auto Upload",disabled=False, desc = "Allows Auto Upload")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                auto_up_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                auto_up_switch = Switch(active=True)
            elif ".method public static supportAutoUpload()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        auto_up.add_widget(auto_up_switch)
        layout.add_widget(auto_up)
        
        def callback(instance, value):
            auto_up_state(instance, value)
        auto_up_switch.bind(active=callback)

    if '.method public static supportFaceDetection()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        face= SettingItem(panel = panel, title = "Support Face Detection",disabled=False, desc = "Allows Face Detection")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                face_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                face_switch = Switch(active=True)
            elif ".method public static supportFaceDetection()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        face.add_widget(face_switch)
        layout.add_widget(face)
        
        def callback(instance, value):
            face_state(instance, value)
        face_switch.bind(active=callback)

    if '.method public static supportGpuEffect()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        gpu= SettingItem(panel = panel, title = "Support GPU Effect",disabled=False, desc = "Allows GPU Effect")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                gpu_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                gpu_switch = Switch(active=True)
            elif ".method public static supportGpuEffect()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        gpu.add_widget(gpu_switch)
        layout.add_widget(gpu)
        
        def callback(instance, value):
            gpu_state(instance, value)
        gpu_switch.bind(active=callback)

    if '.method public static supportHVGARecording()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        hvga= SettingItem(panel = panel, title = "Support HVGA Recording",disabled=False, desc = "Allows HVGA Recording")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                hvga_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                hvga_switch = Switch(active=True)
            elif ".method public static supportHVGARecording()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        hvga.add_widget(hvga_switch)
        layout.add_widget(hvga)
        
        def callback(instance, value):
            hvga_state(instance, value)
        hvga_switch.bind(active=callback)

    if '.method public static supportISO()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        iso= SettingItem(panel = panel, title = "Support ISO Format",disabled=False, desc = "Allows ISO Format")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                iso_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                iso_switch = Switch(active=True)
            elif ".method public static supportISO()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        iso.add_widget(iso_switch)
        layout.add_widget(iso)
        
        def callback(instance, value):
            iso_state(instance, value)
        iso_switch.bind(active=callback)

    if '.method public static supportMMSVedioRecording()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        mms= SettingItem(panel = panel, title = "Support MMS Video Recording",disabled=False, desc = "Allows Video Recording Format For MMS Messages")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                mms_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                mms_switch = Switch(active=True)
            elif ".method public static supportMMSVedioRecording()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        mms.add_widget(mms_switch)
        layout.add_widget(mms)
        
        def callback(instance, value):
            mms_state(instance, value)
        mms_switch.bind(active=callback)

    if '.method public static supportOnlyMP4VideoFormat()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        mp4= SettingItem(panel = panel, title = "Support Only MP4 Format",disabled=False, desc = "Only Allows MP4 Video Format")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                mp4_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                mp4_switch = Switch(active=True)
            elif ".method public static supportOnlyMP4VideoFormat()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        mp4.add_widget(mp4_switch)
        layout.add_widget(mp4)
        
        def callback(instance, value):
            mp4_state(instance, value)
        mp4_switch.bind(active=callback)

    if '.method public static supportTapScreenCapture()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        tap= SettingItem(panel = panel, title = "Support Tap Screen To Capture",disabled=False, desc = "Allows For Tapping On Screen To Take Pictures")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                tap_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                tap_switch = Switch(active=True)
            elif ".method public static supportTapScreenCapture()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        tap.add_widget(tap_switch)
        layout.add_widget(tap)
        
        def callback(instance, value):
            tap_state(instance, value)
        tap_switch.bind(active=callback)

    if '.method public static contactsNoStorage()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        contacts= SettingItem(panel = panel, title = "Contacts No Storage",disabled=False, desc = "Contacts No Storage")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                contacts_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                contacts_switch = Switch(active=True)
            elif ".method public static contactsNoStorage()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        contacts.add_widget(contacts_switch)
        layout.add_widget(contacts)
        
        def callback(instance, value):
            contacts_state(instance, value)
        contacts_switch.bind(active=callback)

    if '.method public static forceFocusSound()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        focus_sound= SettingItem(panel = panel, title = "Force Focus Sound",disabled=False, desc = "Force Focus Sounds")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                focus_sound_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                focus_sound_switch = Switch(active=True)
            elif ".method public static forceFocusSound()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        focus_sound.add_widget(focus_sound_switch)
        layout.add_widget(focus_sound)
        
        def callback(instance, value):
            focus_sound_state(instance, value)
        focus_sound_switch.bind(active=callback)

    if '.method public static supportFastFrameRecording()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        fast_frame= SettingItem(panel = panel, title = "Support Fast Frame Recording",disabled=False, desc = "Enable Fast Frame Recording")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                fast_frame_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                fast_frame_switch = Switch(active=True)
            elif ".method public static supportFastFrameRecording()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        fast_frame.add_widget(fast_frame_switch)
        layout.add_widget(fast_frame)
        
        def callback(instance, value):
            fast_frame_state(instance, value)
        fast_frame_switch.bind(active=callback)

    if '.method public static supportVideoFormatChoosing()Z' in open("%s/DisplayDevice.smali" % (Camera)).read():
        fp = open("%s/DisplayDevice.smali" % (Camera), "r")
        lines = fp.readlines()
        fp.close()
        vid_format= SettingItem(panel = panel, title = "Support Fast Frame Recording",disabled=False, desc = "Enable Fast Frame Recording")
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                vid_format_switch = Switch(active=False)
                continue
            elif inFunc and 'const/4 v0, 0x1' in lines[i]:
                vid_format_switch = Switch(active=True)
            elif ".method public static supportVideoFormatChoosing()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        vid_format.add_widget(vid_format_switch)
        layout.add_widget(vid_format)
        
        def callback(instance, value):
            vid_format_state(instance, value)
        vid_format_switch.bind(active=callback)

    popup = Popup(background='atlas://images/eds/pop', title='Camera Mods', content=main, auto_dismiss=True, size_hint=(None, None), size=(630, 500))
    popup.open()

    def finish(self):
        finish_cam(self)
        popup.dismiss()
    done.bind(on_release=finish)

def geo_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static EnableGeoTagByDefault()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static EnableGeoTagByDefault()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()

def focus_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static canCancelFocus()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static canCancelFocus()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
        
def full_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static captrueFullSize()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static captrueFullSize()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()

def shutter_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static forceSutterSound()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static forceSutterSound()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()

def auto_focus_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static hasAutoFocus()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static hasAutoFocus()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()

def has_limit_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static hasLimit250KB()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static hasLimit250KB()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()

def no_mms_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static removeMMS()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static removeMMS()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()

def s_128_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static support128kBitrate()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static support128kBitrate()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()

def auto_up_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static supportAutoUpload()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static supportAutoUpload()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()

def face_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static supportFaceDetection()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static supportFaceDetection()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()

def gpu_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static supportGpuEffect()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static supportGpuEffect()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()

def hvga_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static supportHVGARecording()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static supportHVGARecording()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()

def iso_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static supportISO()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static supportISO()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()     

def mms_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static supportMMSVedioRecording()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static supportMMSVedioRecording()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()        

def mp4_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static supportOnlyMP4VideoFormat()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static supportOnlyMP4VideoFormat()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close() 

def tap_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static supportTapScreenCapture()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static supportTapScreenCapture()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close() 

def contacts_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static contactsNoStorage()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static contactsNoStorage()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close() 

def focus_sound_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static forceFocusSound()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static forceFocusSound()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close() 
        
def fast_frame_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static supportFastFrameRecording()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static supportFastFrameRecording()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close() 

def vid_format_state(instance, value):
    if value == True:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x0" in lines[i]:
                lines[i] = lines[i].replace("0x0", "0x1")
                continue
            elif ".method public static supportVideoFormatChoosing()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close()
    elif value == False:
        os.chdir(Camera)
        fp = open("DisplayDevice.smali", "r")
        lines = fp.readlines()
        fp.close()
        inFunc = False
        for i in range(len(lines)):
            if inFunc and "const/4 v0, 0x1" in lines[i]:
                lines[i] = lines[i].replace("0x1", "0x0")
                continue
            elif ".method public static supportVideoFormatChoosing()Z" in lines[i]:
                inFunc = True
                continue
            elif ".end method" in lines[i]:
                inFunc = False
        
        fp = open("DisplayDevice.smali", "w")
        fp.write("".join(lines))
        fp.close() 

def finish_cam(self):
    try:
        os.chdir(Apktool)
        if os.path.exists('%s/HTCCamera.apk' % SystemApp) == True:
            os.rename('%s/HTCCamera.apk' % SystemApp, '%s/HTCCamera.apk.bak' % SystemApp)
            output = os.popen('java -jar apktool.jar b -f %s/out' % (SystemApp) + ' %s/HTCCamera.apk' % (SystemApp)).read()
            print output
        else:
            print 'NO HTC CAM ERROR'
        
        if os.path.exists('%s/Camera.apk' % SystemApp) == True:
            os.rename('%s/Camera.apk' % SystemApp, '%s/Camera.apk.bak' % SystemApp)
            output = os.popen('java -jar apktool.jar b -f %s/out' % (SystemApp) + ' %s/Camera.apk' % (SystemApp)).read()
            print output
        else:
            print 'NO CAM ERROR'
    except:
        'NO FILES FOUND'
    os.remove('%s/HTCCamera.apk.bak' % SystemApp)
    shutil.rmtree('%s/out' % SystemApp)    


def sys_mods(self):
    print 'system mods'
    
def sett_mods(self):
    print 'Settings Mods'
    
def browse_mods(self):
    print 'browser mods'   

def audio_mods(self):
    print 'sound mods'
    
def mms_mods(self):
    print 'MMS mods'
    
def misc_mods(self):
    print 'misc mods'
