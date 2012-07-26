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
        try:  
            Box = BoxLayout(orientation="vertical", spacing=10, size_hint=(1.0, 0.75), pos_hint= {'x':.0, 'y':.12})
            self.main_layout.add_widget(Box)
            msg = GridLayout(cols=3, padding=15, spacing=10, size_hint_y=None)
            msg.bind(minimum_height=msg.setter('height'))
            for name in os.listdir(SystemApp):
                btnname = (CustomButton(text='%s' % name, font_size=10, size_hint_y=None, height=40))
                msg.add_widget(btnname)
                btnname.bind(on_release=do_button)
            root = ScrollView(size=(800, 450), do_scroll_x=False)
            root.add_widget(msg)
            Box.add_widget(root)
        except:
            EdsNotify().run("'system/app Directory Not Found", 'Cant Find:\n' + SystemApp)

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
