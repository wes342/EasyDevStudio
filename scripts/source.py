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
import commands
import platform

def no_os(self):
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=1, row_force_default=True, row_default_height=40, spacing=25)
    cancel = Button(text='Cancel', size_hint_x=None, width=325)
    root.add_widget(Label(halign="center", text='You Must Be Running Linux to Build from source.\nCurrent Supported Distros are:\n"Ubuntu" Or "Linux Mint"'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(cancel)
    popup = Popup(background='atlas://images/eds/pop', title='Add Option',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    cancel.bind(on_release=popup.dismiss)
    popup.open()

def dismiss(self):
    self._popup.dismiss()


def build_kernel(self):
    kernel_menu(self)

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

# Function to return and check installed packages per version. Currently Ubuntu supported.
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
            P = ["git-core", "gnupg", "flex", "bison", "gperf", "libsdl1.2-dev", "libesd0-dev", "libwxgtk2.6-dev","squashfs-tools", "build-essential", "zip", "curl", "libncurses5-dev", "zlib1g-dev", "openjdk-6-jdk", "pngcrush", "schedtool"]
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
                elif plat_v == "12.10" or plat_v == "12.04" or plat_v == "11.10" or plat_v == "13" or plat_v == "12":
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
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=3, row_force_default=True, row_default_height=50, spacing=25)
    install = Button(text='Install', size_hint_x=None, width=85)
    view = Button(text='View', size_hint_x=None, width=85)
    cancel = Button(text='Cancel', size_hint_x=None, width=85)
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
        btn = CustomButton(text="Done")
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
    

def kernel_base(self):
    layout = GridLayout(cols=1, size_hint=(None, 2.5), width=700)
    layout.bind(minimum_height=layout.setter('height'))
    panel = SettingsPanel(title="Camera Mods", settings=self)   
    main = BoxLayout(orientation = 'vertical')
    root = ScrollView(size_hint=(None, None),bar_margin=-11, bar_color=(47 / 255., 167 / 255., 212 / 255., 1.), do_scroll_x=False)
    root.size = (600, 400)
    root.add_widget(layout)
    main.add_widget(root)
    done = Button(text ='Download Kernel Base Now')
    main.add_widget(done)

    aria = SettingItem(panel = panel, title = "HTC Aria",disabled=False, desc = "(HTC) (WWE) (MR) (2.6.32) (v2.2)")
    aria_radio = CheckBox(group='kernel',active=True)
    aria.add_widget(aria_radio)
    layout.add_widget(aria)

    inc = SettingItem(panel = panel, title = "HTC Incredible",disabled=False, desc = "(Verizon) (WWE) (MR) (2.6.35) (v2.3)")
    inc_radio = CheckBox(group='kernel',active=False)
    inc.add_widget(inc_radio)
    layout.add_widget(inc)
    
    inc2 = SettingItem(panel = panel, title = "HTC Incredible 2",disabled=False, desc = "(Verizon) (WWE) (MR) (2.6.35) (v2.3)")
    inc2_radio = CheckBox(group='kernel',active=False)
    inc2.add_widget(inc2_radio)
    layout.add_widget(inc2)
    
    incs = SettingItem(panel = panel, title = "HTC Incredible S",disabled=False, desc = "(Htc) (WWE) (MR) (2.6.35) (v2.3)")
    incs_radio = CheckBox(group='kernel',active=False)
    incs.add_widget(incs_radio)
    layout.add_widget(incs)

    e4g = SettingItem(panel = panel, title = "HTC Evo 4G",disabled=False, desc = "(Sprint) (WWE) (MR) (2.6.35) (v2.3)")
    e4g_radio = CheckBox(group='kernel',active=False)
    e4g.add_widget(e4g_radio)
    layout.add_widget(e4g)
       
    e3d = SettingItem(panel = panel, title = "HTC Evo 3D",disabled=False, desc = "(Sprint) (WWE) (MR) (2.6.35) (v2.3)")
    e3d_radio = CheckBox(group='kernel',active=False)
    e3d.add_widget(e3d_radio)
    layout.add_widget(e3d)
    
    sen = SettingItem(panel = panel, title = "HTC Sensation",disabled=False, desc = "(T-Mobile) (USA) (CRC) (2.6.35) (2.3)")
    sen_radio = CheckBox(group='kernel',active=False)
    sen.add_widget(sen_radio)
    layout.add_widget(sen)
    
    tb = SettingItem(panel = panel, title = "HTC Thunderbolt",disabled=False, desc = "(Verizon) (WWE) (MR) (2.6.35) (v2.3)")
    tb_radio = CheckBox(group='kernel',active=False)
    tb.add_widget(tb_radio)
    layout.add_widget(tb)
    
    ama = SettingItem(panel = panel, title = "HTC Amaze",disabled=False, desc = "(T-Mobile) (USA) (CRC) (2.6.35) (v2.3)")
    ama_radio = CheckBox(group='kernel',active=False)
    ama.add_widget(ama_radio)
    layout.add_widget(ama)
    
    g2 = SettingItem(panel = panel, title = "G2",disabled=False, desc = "(T-Mobile) (USA) (MR) (2.6.35) (v2.3)")
    g2_radio = CheckBox(group='kernel',active=False)
    g2.add_widget(g2_radio)
    layout.add_widget(g2)
    
    i4g = SettingItem(panel = panel, title = "HTC Inspire 4G",disabled=False, desc = "(AT&T) (USA) (MR) (2.6.35) (v2.3)")
    i4g_radio = CheckBox(group='kernel',active=False)
    i4g.add_widget(i4g_radio)
    layout.add_widget(i4g)
    
    popup = Popup(background='atlas://images/eds/pop', title='Kernel Base', content=main, auto_dismiss=True, size_hint=(None, None), size=(630, 500))
    popup.open()

def kernel_mods(self):
    layout = GridLayout(cols=1, size_hint=(None, 2.5), width=700)
    layout.bind(minimum_height=layout.setter('height'))
    panel = SettingsPanel(title="Kernel Mods", settings=self)   
    main = BoxLayout(orientation = 'vertical')
    root = ScrollView(size_hint=(None, None),bar_margin=-11, bar_color=(47 / 255., 167 / 255., 212 / 255., 1.), do_scroll_x=False)
    root.size = (600, 400)
    root.add_widget(layout)
    main.add_widget(root)
    done = Button(text ='Done Selecting Mods')
    main.add_widget(done)

    oc = SettingItem(panel = panel, title = "Add Over Clocking",disabled=False, desc = "Adds Over Clocking Capabilities")
    oc_switch = Switch(active=False)
    oc.add_widget(oc_switch)
    layout.add_widget(oc)
  
    modu = SettingItem(panel = panel, title = "Add Module Support",disabled=False, desc = "Adds Module support to kernel")
    modu_switch = Switch(active=False)
    modu.add_widget(modu_switch)
    layout.add_widget(modu)
 
    wifi = SettingItem(panel = panel, title = "Compile Wifi Module",disabled=False, desc = "The wifi module may be unstable or unusable / The solution is to recompile the module, linking it to the new kernel build")
    wifi_switch = Switch(active=False)
    wifi.add_widget(wifi_switch)
    layout.add_widget(wifi)

    sass = SettingItem(panel = panel, title = "Add Smart Ass Governor",disabled=False, desc = "Adds Smart Ass as Default Governor")
    sass_switch = Switch(active=False)
    sass.add_widget(sass_switch)
    layout.add_widget(sass)

    popup = Popup(background='atlas://images/eds/pop', title='Kernel Mods', content=main, auto_dismiss=True, size_hint=(None, None), size=(630, 500))
    popup.open()

def pull_conf(self):
    print 'Pull Config file from Device'

def kernel_other(self):
    root = BoxLayout(orentation = 'vertical')
    done = CustomButton(text='Test')
    root.add_widget(done)
    scroll = ScrollView(size_hint=(None, 2.5), do_scroll_x=False)
    root.add_widget(scroll)
    btn_layout = GridLayout(cols=1)
    scroll.add_widget(btn_layout)

    layout = GridLayout(cols=1, size_hint=(None, 2.5), width=700)
    layout.bind(minimum_height=layout.setter('height'))
    panel = SettingsPanel(title="Advanced Kernel Options", settings=self)   
    main = BoxLayout(orientation = 'vertical')
    root = ScrollView(size_hint=(None, None),bar_margin=-11, bar_color=(47 / 255., 167 / 255., 212 / 255., 1.), do_scroll_x=False)
    root.size = (600, 400)
    root.add_widget(layout)
    main.add_widget(root)
    layout.add_widget(panel)
    done = Button(text ='Done')
    main.add_widget(done)
 
   
    popup = Popup(background='atlas://images/eds/pop', title='Advanced Kernel Options', content=main, auto_dismiss=True, size_hint=(None, None), size=(630, 500))
    popup.open()
    
def kernel_menu(self):
    try:
        if (os.name == "posix"):
            self.panel_layout.clear_widgets()
            title = Label(text='[b][color=ff2222][size=20]Kernel Building[/size][/color][/b]', markup = True, pos_hint={'x':-.05, 'y':.20})
            p = getPackages()
            package_count = 0
            if p == True:
                package_count = 0
            else:
                for x in p:
                    package_count += 1
            
            grid_layout = GridLayout(cols=1, row_force_default=True, row_default_height=40, spacing=10, pos_hint={'x':-.05, 'y':-.50})
            k_base = CustomButton(text='2. Select Kernel Base', pos_hint={'x':.0, 'y':.550}, size_hint=(.90, .06))
            k_conf = CustomButton(text='3. Pull Config from Device', pos_hint={'x':.0, 'y':.300}, size_hint=(.90, .06))
            k_mods = CustomButton(text='4. Select Kernel Mods', pos_hint={'x':.0, 'y':.550}, size_hint=(.90, .06))
            k_build = CustomButton(text='5. Build Kernel', pos_hint={'x':.0, 'y':.550}, size_hint=(.90, .06))
            k_other = CustomButton(text='Other Kernel Options', pos_hint={'x':.0, 'y':.550}, size_hint=(.90, .06))
            self.panel_layout.add_widget(title)
            if package_count == 0:
                pass
            else:
                i_packages = Button(text='Install needed packages: %s' % package_count, pos_hint={'x':.0, 'y':.550}, size_hint=(.90, .06), background_color=(1.4, 0, 0, 0.6))
            self.panel_layout.add_widget(title)
            if package_count == 0:
                pass
            else:
                self.panel_layout.add_widget(i_packages)
            self.panel_layout.add_widget(grid_layout)
            grid_layout.add_widget(k_base)
            grid_layout.add_widget(k_conf)
            grid_layout.add_widget(k_mods)
            grid_layout.add_widget(k_build)
            grid_layout.add_widget(k_other)
            
            def ker_base(instance):
                kernel_base(self)
            k_base.bind(on_release=ker_base)
    
            def ker_conf(instance):
                pull_conf(self)
            k_conf.bind(on_release=ker_conf)
    
            def ker_mods(instance):
                kernel_mods(self)
            k_mods.bind(on_release=ker_mods)
            
            def ker_build(instance):
                print "build kernel"
            k_build.bind(on_release=ker_build)
    
            def ker_other(instance):
                kernel_other(self)
            k_other.bind(on_release=ker_other)
            
        else:
            self.panel_layout.clear_widgets()
            title = Label(text='[b][color=ff2222][size=20]Kernel Building[/size][/color][/b]', markup = True, pos_hint={'x':-.05, 'y':.20})
            lin = Label(text='[b][color=ffffff][size=15]You Must Be Using Linux to Build Kernels[/size][/color][/b]', markup = True, pos_hint={'x':-.05, 'y':.100})
            self.panel_layout.add_widget(title)
            self.panel_layout.add_widget(lin)
            
        if package_count == 0:
            pass
        else:
            i_packages.bind(on_release=install_packages)
    except:
        no_os(self)
        
def source_menu(self):
    try:  
        self.panel_layout.clear_widgets()
        title = Label(text='[b][color=ff2222][size=20]Source Rom Building[/size][/color][/b]', markup = True, pos_hint={'x':-.05, 'y':.20})
        p = getPackages()
        package_count = 0
        if p == True:
            package_count = 0
        else:
            for x in p:
                package_count += 1
    
        aosp_source = CustomButton(text='Aosp ', pos_hint={'x':.0, 'y':.450}, size_hint=(.90, .06))
        cm_source = CustomButton(text='Cyanogenmod', pos_hint={'x':.0, 'y':.350}, size_hint=(.90, .06))
        miui_source = CustomButton(text='Miui', pos_hint={'x':.0, 'y':.250}, size_hint=(.90, .06))
        clean = Button(text='Clean Out Old Rom Source', pos_hint={'x':.0, 'y':-.05}, size_hint=(.90, .06), background_color=(1.4, 0, 0, 0.6))
    
        if package_count == 0:
            pass
        else:
            i_packages = Button(text='Install needed packages: %s' % package_count, pos_hint={'x':.0, 'y':.550}, size_hint=(.90, .06), background_color=(1.4, 0, 0, 0.6))
        self.panel_layout.add_widget(title)
        if package_count == 0:
            pass
        else:
            self.panel_layout.add_widget(i_packages)
        self.panel_layout.add_widget(aosp_source)
        self.panel_layout.add_widget(cm_source)
        self.panel_layout.add_widget(miui_source)
        self.panel_layout.add_widget(clean)
        
    
        def clean_files(instance):
            root = BoxLayout(orientation='vertical', spacing=20)
            btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
            remove = Button(text='Clean', size_hint_x=None, width=150)
            cancel = Button(text='Cancel', size_hint_x=None, width=150)
            root.add_widget(Label(text='Are You Sure You Want To\nClean Out Current Rom Files?'))
            root.add_widget(btn_layout)
            btn_layout.add_widget(remove)
            btn_layout.add_widget(cancel)
            popup = Popup(background='atlas://images/eds/pop', title='Add Option',content=root, auto_dismiss=False,
            size_hint=(None, None), size=(350, 200))
            cancel.bind(on_release=popup.dismiss)
            popup.open()
            
            def clean_now(self):
                for root, dirs, files in os.walk(Rom):
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        try:
                            import pynotify
                            if pynotify.init(NAME):
                                n = pynotify.Notification("Clean Successful", 'Rom Files Have Been Removed')
                                n.set_urgency(pynotify.URGENCY_NORMAL)
                                n.show()
                            else:
                                print "there was a problem initializing the 'pynotify' module"
                        except:
                            print "you don't seem to have 'pynotify' installed" 
            remove.bind(on_press=clean_now)
            remove.bind(on_release=popup.dismiss)
    
        clean.bind(on_release=clean_files)
        if package_count == 0:
            pass
        else:
            i_packages.bind(on_release=install_packages)
    except: 
        no_os(self)
