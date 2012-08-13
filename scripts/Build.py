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

def build_options(self):
    Box = BoxLayout(orientation="vertical", spacing=10)
    msg = GridLayout(cols=1, padding=15, spacing=10, size_hint_y=None)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    
    pack=CustomButton(text="Package Rom",size=(475, 40), size_hint=(None, None))
    pack_sign=CustomButton(text="Package + Sign Rom",size=(475, 40), size_hint=(None, None))
    pack_sign_align=CustomButton(text="Package + Sign + Zipalign Rom",size=(475, 40), size_hint=(None, None))

    msg.add_widget(pack)
    msg.add_widget(pack_sign)
    msg.add_widget(pack_sign_align)
    
    root = ScrollView(size_hint=(None, None),bar_margin=-22, size=(475, 190), do_scroll_x=False)
    root.add_widget(msg)
    Box.add_widget(root)
    Box.add_widget(btn_layout)
    
    popup = Popup(background='atlas://images/eds/pop', title='Build Options',content=Box, auto_dismiss=True,
    size_hint=(None, None), size=(520, 300))
    done.bind(on_release=popup.dismiss)
    pack.bind(on_release=pack_rom)
    pack_sign.bind(on_release=pack_sign_rom)
    pack_sign_align.bind(on_release=pack_sign_align_rom)
    popup.open()
    
def pack_rom(self):
    for line in fileinput.input(BuildProp):
        try:
            if 'ro.build.description=' in line:
                output=line.strip("ro.build.description=")
                try:
                    os.remove('%s/Desktop/' % Home + output + '.zip' )
                except:
                    pass    
                shutil.make_archive(output, "zip", Rom)
                shutil.move(output + '.zip' , '%s/Desktop' % Home)
                EdsNotify().run("Rom Packaging Complete",'%s/Desktop/' % Home + output + '.zip' )
            else:
                if 'ro.build.version=' in line:
                    output=line.strip("ro.build.version=") 
                    try:
                        os.remove('%s/Desktop/' % Home + output + '.zip' )
                    except:
                        pass    
                    shutil.make_archive(output, "zip", Rom)
                    shutil.move(output + '.zip' , '%s/Desktop' % Home)
                    EdsNotify().run("Rom Packaging Complete", '%s/Desktop/' % Home + output + '.zip' )
        except:
            print "Packaging Error"

    
def pack_sign_rom(self):
    print 'Package + Sign Rom'

def pack_sign_align_rom(self):
    print 'Package + Sign + Zipalign Rom'    
    
    