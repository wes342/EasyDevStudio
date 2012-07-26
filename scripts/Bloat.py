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
from EdsNotify import EdsNotify


def load_apps(self):
    Box = BoxLayout(orientation="vertical", spacing=10)
    msg = GridLayout(cols=2, padding=15, spacing=10, size_hint_y=None)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    try:
        for name in os.listdir(SystemApp):
            btnname = (CustomButton(text='%s' % name, font_size=10, size_hint_y=None, height=40))
            msg.add_widget(btnname)
            btnname.bind(on_release=do_button)
        root = ScrollView(size_hint=(None, None), size=(675, 390), do_scroll_x=False)
        root.add_widget(msg)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
    
        popup = Popup(background='atlas://images/eds/pop', title='Removable Apps',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(700, 500))
        done.bind(on_release=popup.dismiss)
        popup.open()
    except:
        EdsNotify().run("'Init.d Directory Not Found", 'Cant Find:\n' + SystemApp)


def do_button(self):

    filepath = "%s/%s" % (SystemApp, self.text)
    
    if sys.platform.startswith('darwin'):
        #subprocess.call(('open', filepath))
        print filepath
    elif os.name == 'nt':
        #os.startfile(filepath)
        print filepath
    elif os.name == 'posix':
        #subprocess.call(('xdg-open', filepath))
        print filepath

def restore_removed(self):
    print "Restore Removed"
    
def clean_removed(self):
    print "Clean Removed"