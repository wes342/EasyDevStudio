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
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch
from kivy.uix.settings import SettingItem, SettingsPanel, SettingOptions
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.config import ConfigParser
from scripts.EdsNotify import EdsNotify
import commands
import platform
import urllib

devices = []

config = ConfigParser()
config.read('%s/eds.ini' % Usr)

try:
    get_device = config.get("Source", "device")
except:
    get_device = "none"
    
try:
    get_branch = config.get("Source", "branch")
except:
    get_branch = "none"

try:
    make_jobs = config.get("Source", "make")
except:
    make_jobs = numprocs

try:
    sync_jobs = config.get("Source", "sync")
except:
    sync_jobs = 4

try:
    repo_path = config.get("Source", "repo_dir")
except:
    repo_path = "%s/build" % Usr


if "none" in get_branch:
    chk_config = 0
    
elif "cm-gb" in get_branch:
    useBranch = Cm7
    chk_config = 1
    
elif "cm-ics" in get_branch:
    useBranch = Cm9
    chk_config = 1
    
elif "cm-jb" in get_branch:
    useBranch = Cm10
    chk_config = 1
    
else:
    useBranch = "null"
    chk_config = 0

if chk_config == True:
    try:
        filehandle = urllib.urlopen(useBranch)
    except IOError:
        print "Failed to grab url: %s" % useBranch
    
    for lines in filehandle.readlines():
    
        x = lines.strip()
        devices.extend([x])
    
    filehandle.close()

def no_os(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=1, row_force_default=True, row_default_height=40, spacing=25)
    cancel = Button(text='Cancel', size_hint_x=None, width=325)
    root.add_widget(Label(halign="center", text='You Must Be Running Linux to Build from source.\nCurrent Supported Distros are:\n"Ubuntu" Or "Linux Mint"'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(cancel)
    popup = Popup(background='atlas://images/eds/pop', title='Unsupported OS',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    cancel.bind(on_release=popup.dismiss)
    popup.open()

def dismiss(self):
    self._popup.dismiss()


# Function to check if packages are installed
def chkInstalled(arg):

    p = False

    cmd = "dpkg --get-selections " + arg
    p = commands.getoutput(cmd)
    p = p.split("\t")
    p = p[-1]
    if p == "install":
        p = True
    else:
        p = False

    return p

# Function to return and check installed packages per version. Currently Ubuntu & Mint supported.
def getPackages():
    
        # Start an array called "L" to hold the packages we find.
        L = []

        # This is just a package count, mainly to see if we return anything at the end.
        pcount = 0
    
        plat_list = platform.dist() # ('Ubuntu', '12.04', 'precise')
        plat_d = plat_list[0]
        plat_v = plat_list[1]
        plat_n = plat_list[2]
                
        if plat_d == "Ubuntu" or plat_d == "LinuxMint":
            pcount += 1
            P = ["git-core", "gnupg", "flex", "bison", "gperf", "libsdl1.2-dev", "libesd0-dev", "squashfs-tools", "build-essential", "zip", "curl", "libncurses5-dev", "zlib1g-dev", "openjdk-6-jdk", "pngcrush", "schedtool"]
            if plat_v == "12.10" or plat_v == "14":
                P.extend(["libwxgtk2.8-dev"])
            else:
                P.extend(["libwxgtk2.6-dev"])
            for x in P:
                i = chkInstalled(x)
                if i == False:
                    L.extend([x])
        else:
            print "Couldn't detect your os version. Please report this. Found: ( %s | %s | %s )" % (plat_d, plat_v, plat_n)
            del L[:]
            
    
        # Checks for x86_64
        check = (sys.maxsize > 2**32)
        if check is True and pcount == 1:
            if plat_d == "Ubuntu" or plat_d == "LinuxMint":
                if plat_v == "10.04" or plat_v == "9":
                    P = ["g++-multilib" "lib32z1-dev", "lib32ncurses5-dev", "lib32readline5-dev", "gcc-4.3-multilib", "g++-4.3-multilib"]
                    for x in P:
                        i = chkInstalled(x)
                        if i == False:
                            L.extend([x])
                elif plat_v == "11.04" or plat_v == "11":
                    P = ["g++-multilib" "lib32z1-dev", "lib32ncurses5-dev", "lib32readline-gplv2-dev", "gcc-4.3-multilib", "g++-4.3-multilib"]
                    for x in P:
                        i = chkInstalled(x)
                        if i == False:
                            L.extend([x])
                elif plat_v == "12.10" or plat_v == "12.04" or plat_v == "11.10" or plat_v == "14" or plat_v == "13" or plat_v == "12":
                    P = ["g++-multilib", "lib32z1-dev", "lib32ncurses5-dev", "lib32readline-gplv2-dev"]
                    for x in P:
                        i = chkInstalled(x)
                        if i == False:
                            L.extend([x])
                else:
                    print "Nothing to extend, version not matched"
    
        # If package pcount and L are zero, then there was an issue, this shouldn't happen. Either get "True" or a package list.
        if not L and pcount == 0:
            print "Empty package list", "After looking at your packages the list is empty, maybe an unsupported distro or filesystem error. Either way I am not able to help without some information. You will not be able to use most features until you install the needed packages, be warned.\n\n Thanks."
            #exit(1)
        elif not L and pcount == 1:
            pass
            return True
        else:
            return L
            

def install_packages(instance):
    root = BoxLayout(orientation='vertical', spacing=25)
    btn_layout = GridLayout(cols=3, row_force_default=True, row_default_height=50, spacing=25)
    install = Button(text='Install', size_hint_x=None, width=90)
    view = Button(text='View', size_hint_x=None, width=90)
    cancel = Button(text='Cancel', size_hint_x=None, width=90)
    root.add_widget(Label(text='Are You Sure You Want To\nInstall needed packages?'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(install)
    btn_layout.add_widget(view)
    btn_layout.add_widget(cancel)
    popup = Popup(background='atlas://images/eds/pop', title='Install packages',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    cancel.bind(on_release=popup.dismiss)
    popup.open()
    
    def install_now(self):
        import subprocess as sp
        p = getPackages()
        packages = ",".join(p).replace(",", " ")
        print packages
        cmd = "gnome-terminal -e \"sudo apt-get install -y %s\"" % (packages)
        sp.Popen(cmd, shell=True)
        
    def view_packages(instance):
        p = getPackages()
        Box = BoxLayout(orientation="vertical", spacing=10)
        msg = GridLayout(cols=1, spacing=0, size_hint_y=None)
        btn_layout = GridLayout(cols=1)
        btn = Button(text="Done")
        btn_layout.add_widget(btn)
        msg.bind(minimum_height=msg.setter('height'))
        for x in p:
            lbl = (Label(text='%s' % x, font_size=10, size_hint_y=None, height=40))
            msg.add_widget(lbl)
        root = ScrollView(size_hint=(None, None), size=(375, 290), do_scroll_x=False)
        root.add_widget(msg)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
        

        popup = Popup(background='atlas://images/eds/pop', title='Needed packages',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(400, 400))
        btn.bind(on_release=popup.dismiss)
        popup.open()
            
    install.bind(on_press=install_now)
    view.bind(on_press=view_packages)
    install.bind(on_release=popup.dismiss)
       

def source_menu(self):
    try:  
        self.panel_layout.clear_widgets()
        title = Label(text='[b][color=#22A0D6][size=20]Source Rom Building[/size][/color][/b]', markup = True, pos_hint={'x':-.05, 'y':.20})
        p = getPackages()
        package_count = 0
        if p == True:
            package_count = 0
        else:
            for x in p:
                package_count += 1
    except:
        no_os(self)
            
    branch = CustomButton(text='Select Branch', pos_hint={'x':.5, 'y':.375}, size_hint=(.40, .06))
    device = CustomButton(text='Select Device', pos_hint={'x':.0, 'y':.375}, size_hint=(.40, .06))
    jobs = GridLayout(cols=2, spacing=10, size_hint=(0.9, .20), pos_hint={'x':-.05, 'y':.05})
    
    stitle = Label(text='How Many [b]Sync[/b] Jobs, Default = %s' % sync_jobs, markup=True)
    f = float(sync_jobs)
    p = ('1.0','2.0','3.0','4.0','5.0','6.0','7.0','8.0','9.0','10.0','11.0','12.0','13.0','14.0','15.0','16.0')
    sslide = Spinner(text='%s' % f, values=(p),size_hint=(None, None),size=(100, 44),pos_hint={'center_x': .5, 'center_y': .5})
    
    mtitle = Label(text='How Many [b]Make[/b] Jobs, Default = %s' % make_jobs, markup=True)
    m = float(make_jobs)
    j = ('1.0','2.0','3.0','4.0')
    k = ('1.0','2.0','3.0','4.0','5.0','6.0','7.0','8.0')
    mslide = Spinner(text='%s' % m,values=k,size_hint=(None, None),size=(100, 44),pos_hint={'center_x': .5, 'center_y': .5})

    dev = Label(markup=True, text="[b][color=#adadad]Current Device =[/color][/b] %s" % get_device, pos_hint={'x':-.300, 'y':-.15})
    bra = Label(markup=True, text="[b][color=#adadad]Current Branch =[/color][/b] %s" % get_branch, pos_hint={'x':.20, 'y':-.15})
    repo = Label(markup=True, text="[b][color=#adadad]Repo Path =[/color][/b] %s" % repo_path, pos_hint={'x':-.05, 'y':-.0})

    jobs.add_widget(stitle)
    jobs.add_widget(sslide)
    jobs.add_widget(mtitle)
    jobs.add_widget(mslide)
    sync = CustomButton(text='Sync', pos_hint={'x':.0, 'y':-.05}, size_hint=(.40, .06))
    make = CustomButton(text='Make', pos_hint={'x':.5, 'y':-.05}, size_hint=(.40, .06))

    if package_count == 0:
        pass
    else:
        i_packages = Button(text='Install needed packages: %s' % package_count, pos_hint={'x':.0, 'y':.550}, size_hint=(.90, .06), background_color=(1.4, 0, 0, 0.6))
    self.panel_layout.add_widget(title)
    if package_count == 0:
        pass
    else:
        self.panel_layout.add_widget(i_packages)
    self.panel_layout.add_widget(branch)
    self.panel_layout.add_widget(device)
    self.panel_layout.add_widget(jobs)
    self.panel_layout.add_widget(sync)
    self.panel_layout.add_widget(make)
    self.panel_layout.add_widget(bra)
    self.panel_layout.add_widget(dev)
    self.panel_layout.add_widget(repo)

    def branch_select(self):
        Box = BoxLayout(orientation="vertical", spacing=10)
        base = BoxLayout(orientation="vertical", spacing=15, padding=15)
        btn_layout = GridLayout(cols=2, spacing=10)
        cancel = Button(text='Cancel')
        btn_layout.add_widget(cancel)
        
        aosp = CustomButton(text='AOSP')
        cm = CustomButton(text='Cyanogenmod')
        base.add_widget(aosp)
        base.add_widget(cm)
        
        # for root widget do_scroll_y=True to enable scrolling 
        root = ScrollView(size_hint=(None, None), size=(525, 150), do_scroll_x=False, do_scroll_y=True)
        root.add_widget(base)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
    
        popup = Popup(background='atlas://images/eds/pop', title='Branch Selection',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(550, 260))
        cancel.bind(on_release=popup.dismiss)
        aosp.bind(on_release=aosp_branch)
        aosp.bind(on_release=popup.dismiss)
        cm.bind(on_release=cm_branch)
        cm.bind(on_release=popup.dismiss)
        popup.open()
    
    def aosp_branch(self):
        config.read('%s/eds.ini' % Usr)
        Box = BoxLayout(orientation="vertical", spacing=10)
        base = SettingsPanel(title="", settings=self)
        btn_layout = GridLayout(cols=2, spacing=10)
        select = Button(text="Select")
        btn_layout.add_widget(select)
        cancel = Button(text='Cancel')
        btn_layout.add_widget(cancel)
        base.bind(minimum_height=base.setter('height'))
    
        
        GB = SettingItem(panel = base, title = "Gingerbread",disabled=False, desc = "Android 2.3,  kernel 2.6.35,  Api 9-10 ")
        GB_radio = CheckBox(group='base',active=False)
        GB.add_widget(GB_radio)
        base.add_widget(GB)
    
        ICS = SettingItem(panel = base, title = "Ice Cream Sandwitch",disabled=False, desc = "Android 4.0,  kernel 3.0.1,  Api 14-15")
        ICS_radio = CheckBox(group='base',active=False)
        ICS.add_widget(ICS_radio)
        base.add_widget(ICS)
    
        JB = SettingItem(panel = base, title = "Jellybean",disabled=False, desc = "Android 4.1,  kernel 3.1.10,  Api 16-?")
        JB_radio = CheckBox(group='base',active=False)
        JB.add_widget(JB_radio)
        base.add_widget(JB)    
        
        # for root widget do_scroll_y=True to enable scrolling 
        root = ScrollView(size_hint=(None, None), size=(525, 240), do_scroll_x=False, do_scroll_y=False)
        root.add_widget(base)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
    
    ########################################
    # This should be working fine 
    # Not sure if there is a better way to do this
    #########################################
    
        def on_checkbox(checkbox, value):
            title = GB.title
            if value:
                bra.text="[b][color=#adadad]Current Branch =[/color][/b] aosp-gb"
                config.set("Source", "branch", "aosp-gb")
            else:
                pass
    
        GB_radio.bind(active=on_checkbox)
        
        def checkbox_active(checkbox, value):
            title = ICS.title
            if value:
                bra.text="[b][color=#adadad]Current Branch =[/color][/b] aosp-ics"
                config.set("Source", "branch", "aosp-ics")
            else:
                pass
        
        ICS_radio.bind(active=checkbox_active)
        
        def on_active(checkbox, value):
            title = JB.title
            if value:
                bra.text="[b][color=#adadad]Current Branch =[/color][/b] aosp-jb"
                config.set("Source", "branch", "aosp-jb")
            else:
                pass
                            
        JB_radio.bind(active=on_active)
        
        def set_branch(self):
            config.write()
        select.bind(on_release=set_branch)
        
        popup = Popup(background='atlas://images/eds/pop', title='Branch Selection',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(550, 350))
        select.bind(on_release=popup.dismiss)
        cancel.bind(on_release=popup.dismiss)
        popup.open()
    
    def cm_branch(self):
        config.read('%s/eds.ini' % Usr)
        Box = BoxLayout(orientation="vertical", spacing=10)
        base = SettingsPanel(title="", settings=self)
        btn_layout = GridLayout(cols=2, spacing=10)
        select = Button(text="Select")
        btn_layout.add_widget(select)
        cancel = Button(text='Cancel')
        btn_layout.add_widget(cancel)
        base.bind(minimum_height=base.setter('height'))
    
    #################################################
    # Removed branch type selection menu because I think it was useless
    # Should be the same for Aosp and CM 
    # If not I can redo it.
    #################################################
        
        Cm7 = SettingItem(panel = base, title = "Cyanogenmod 7",disabled=False, desc = "Android 2.3,  kernel 2.6.35,  Api 9-10 ")
        Cm7_radio = CheckBox(group='base',active=False)
        Cm7.add_widget(Cm7_radio)
        base.add_widget(Cm7)
    
        Cm9 = SettingItem(panel = base, title = "Cyanogenmod 9",disabled=False, desc = "Android 4.0,  kernel 3.0.1,  Api 14-15")
        Cm9_radio = CheckBox(group='base',active=False)
        Cm9.add_widget(Cm9_radio)
        base.add_widget(Cm9)
    
        Cm10 = SettingItem(panel = base, title = "Cyanogenmod 10",disabled=False, desc = "Android 4.1,  kernel 3.1.10,  Api 16-?")
        Cm10_radio = CheckBox(group='base',active=False)
        Cm10.add_widget(Cm10_radio)
        base.add_widget(Cm10)    
        
        # for root widget do_scroll_y=True to enable scrolling 
        root = ScrollView(size_hint=(None, None), size=(525, 240), do_scroll_x=False, do_scroll_y=False)
        root.add_widget(base)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
    
    ########################################
    # This should be working fine 
    # Not sure if there is a better way to do this
    #########################################
    
        def on_checkbox(checkbox, value):
            title = Cm7.title
            if value:
                bra.text="[b][color=#adadad]Current Branch =[/color][/b] cm-gb"
                config.set("Source", "branch", "cm-gb")
            else:
                pass
    
        Cm7_radio.bind(active=on_checkbox)
        
        def checkbox_active(checkbox, value):
            title = Cm9.title
            if value:
                bra.text="[b][color=#adadad]Current Branch =[/color][/b] cm-ics"
                config.set("Source", "branch", "cm-ics")
            else:
                pass
        
        Cm9_radio.bind(active=checkbox_active)
        
        def on_active(checkbox, value):
            title = Cm10.title
            if value:
                bra.text="[b][color=#adadad]Current Branch =[/color][/b] cm-jb"
                config.set("Source", "branch", "cm-jb")
            else:
                pass
                            
        Cm10_radio.bind(active=on_active)
        
        def set_branch(self):
            config.write()
        select.bind(on_release=set_branch)
        
        popup = Popup(background='atlas://images/eds/pop', title='Branch Selection',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(550, 350))
        select.bind(on_release=popup.dismiss)
        cancel.bind(on_release=popup.dismiss)
        popup.open() 
    def show_branch(instance):
        branch_select(self)
    branch.bind(on_release=show_branch) 

    def device_select(self):
        Box = BoxLayout(orientation="vertical", spacing=10)
        msg = GridLayout(cols=2, padding=15, spacing=10, size_hint_y=None)
        btn_layout = GridLayout(cols=1)
        done = Button(text="Cancel")
        btn_layout.add_widget(done)
        msg.bind(minimum_height=msg.setter('height'))
        popup = Popup(background='atlas://images/eds/pop', title='Device Select',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(700, 500))
        try:
            for name in devices:
                if name in devices:
                    btnname = (CustomButton(text='%s' % name, font_size=10, size_hint_y=None, height=40))
                    msg.add_widget(btnname)
                    btnname.bind(on_release=set_device)
                    btnname.bind(on_release=popup.dismiss)
                
            root = ScrollView(size_hint=(None, None), size=(675, 390), do_scroll_x=False)
            root.add_widget(msg)
            Box.add_widget(root)
            Box.add_widget(btn_layout)
            done.bind(on_release=popup.dismiss)
            popup.open()
            
        except:
            EdsNotify().run("'system/app Directory Not Found", 'Cant Find:\n' + SystemApp)
            
    def set_device(self):
        dev.text="[b][color=#adadad]Current Device =[/color][/b] %s" % self.text
        config.set("Source", "device", self.text)
        config.write()
    
    def show_device(instance):
        device_select(self)
    device.bind(on_release=show_device)


    def sync_slider(self, value):
        s = int(float(value))
        config.set("Source", "sync", s)
        #config.write()
    sslide.bind(text=sync_slider)

    
    def make_slider(self, value):
        m = int(float(value))
        config.set("Source", "make", m)
        #config.write()
    mslide.bind(text=make_slider)

########################################
# Sync and Make Functions  
# Not Sure Exactly what needs to be done here
#########################################

    def sync_now(self):
        config.write()
        import subprocess as sp
        cmd = "gnome-terminal -e \"sudo apt-get install -y %s\""
        sp.Popen(cmd, shell=True)
    sync.bind(on_release=sync_now)

    
    def make_now(self):
        import subprocess as sp
        cmd = "gnome-terminal -e \"sudo apt-get install -y %s\""
        sp.Popen(cmd, shell=True)
    make.bind(on_release=make_now)
    
    if package_count == 0:
        pass
    else:
        i_packages.bind(on_release=install_packages)
