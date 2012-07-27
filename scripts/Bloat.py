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
 
check = ["AccountSyncManager.apk","ApplicationsProvider.apk","AudioEffectService.apk","Bluetooth.apk","BrcmBluetoothServices.apk",
         "CertInstaller.apk","CheckinProvider.apk","com.coremobility.app.vnotes.apk","com.htc.idlescreen_SN.apk","com.noshufou.android.su.apk",
         "ContactsProvider.apk","CSPeopleSyncService.apk","CustomizationSettingsProvider.apk","CustomizationSetup.apk","DefaultContainerService.apk",
         "DFPI.apk","DMClient.apk","DMPortRead.apk","dms.apk","DockMode.apk","DownloadProvider.apk","DownloadProviderUi.apk","DrmProvider.apk",
         "EPST.apk","fusion.apk","GoogleBackupTransport.apk","GoogleCalendarSyncAdapter.apk","GoogleContactsSyncAdapter.apk","GoogleFeedback.apk",
         "GooglePartnerSetup.apk","GoogleServicesFramework.apk","GSD.apk","HomePersonalize.apk","HtcBeatsNotify.apk","HtcCdmaMccProvider.apk",
         "HtcCompressViewer.apk","HtcDialer.apk","HtcDm.apk","HtcDMC.apk","HTC_IME.apk","HtcLocationPicker.apk","HtcLocationService.apk",
         "HtcLockScreen.apk","HTCMediaAutoUploadSetting.apk","HtcMediaCacheService.apk","HtcMessageCS.apk","HtcMessageProvider.apk",
         "HtcMessageUploader.apk","HtcMusicEnhancer.apk","HtcPainterView.apk","HtcResetNotify.apk","HtcSettingsProvider.apk","HTCSetupWizard.apk",
         "HtcSoundRecorder.apk","HtcSoundSetDownloadManager.apk","HtcSprintService.apk","HtcStreamPlayer.apk","HTMLViewer.apk","Idlescreen_Base.apk",
         "idlescreen_photo.apk","idlescreen_shortcut.apk","IdleScreen_Weather.apk","LMW.apk","MarketUpdater.apk","MediaProvider.apk","MediaUploader.apk",
         "MessageTabPlugin.apk","Mms.apk","MySketcher.apk","NetworkLocation.apk","OnlineAssetDetails.apk","PackageInstaller.apk","PCSCII.apk","Phone.apk",
         "PicoTts.apk","PluginManager.apk","restartapp.apk","Rosie.apk","Settings.apk","SettingsProvider.apk","SetupWizard.apk","SPCSCorp4G.apk","SystemUI.apk",
         "TaskManager.apk","TelephonyProvider.apk","TtsService.apk","TVOUT.apk","Tweaks.apk","Updater.apk","UpgradeSetup.apk","UploadProvider.apk",
         "UserDictionaryProvider.apk","VoiceDiler.apk","VpnServices.apk","Weather.apk","WeatherAgentService.apk","WeatherProvider.apk","WeatherSyncProvider.apk",
         "WifiRouter.apk","WorldClock.apk","HtcDLNAMiddleLayer.apk","CalendarProvider.apk","CalendarProvider.apk","HtcVideoPlayer.apk","HtcContacts.apk",
         "HtcConnectedMedia.apk","HtcDirectDownloadsProvider.apk","HtcListen.apk","FlashLitePlugin.apk","Gallery2.apk","NovaLauncher.apk","Provision.apk",
         "Gallery2.apk","Gallery.apk","Camera.apk","VpnDialogs.apk","Superuser.apk","Exchange.apk","Launcher2.apk","LatinIME.apk","WAPPushManager.apk","KeyChain.apk",
         "CMWimaxSettings.apk","Email.apk","BackupRestoreConfirmation.apk","SharedStorageBackup.apk","GoogleLoginService.apk","OneTimeInitializer.apk","Vending.apk",
         "Market.apk", "GooglePackageVerifierUpdater.apk","GooglePackageVerifier.apk","NetworkAssistant.apk","MiuiSystemUi.apk","MiuiHome.apk","GuardProvider.apk",
         "LBESEC_MIUI.apk","MIUIStats.apk","TelocationProvider.apk","WiMAXSettings.apk","WiMAXHiddenMenu.apk","XiaomiServiceFramework.apk","HtcEmailPolicy.apk",
         "SearchAnywhere.apk","HtcSettings.apk","HtcMusicMarkedItems.apk","DCSUtility.apk","Qxdmlog.apk","HtcCopright.apk","FieldTest.apk","HtcPushMedia.apk","Clicker.apk",
         "DCSImpl.apk"]

def show_disclaimer(self):
    root = BoxLayout(orientation='vertical',padding=25, spacing=60)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=40, spacing=10)
    agree = Button(text='Agree', width=150)
    decline = Button(text='Decline', width=150)
    root.add_widget(Label(markup=True, halign="center", text="""Removing apks from a rom can make rom unbootable.\nBe sure to take your time, don't remove\n
    an apk unless you know what you are removing.\n[/color][/b]\n[color=#18B3D6][b]Easy Mode :[/b] Hints to what apps [b]MAY[/b] be safe to remove.[/color]\n
    [b][color=#D61818]Remember :[/b] You are doing this at your own risk."""))
    root.add_widget(btn_layout)
    btn_layout.add_widget(agree)
    btn_layout.add_widget(decline)
    popup = Popup(background='atlas://images/eds/pop', title='Disclaimer',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(425, 250))
    decline.bind(on_release=popup.dismiss)
    agree.bind(on_release=load_apps)
    agree.bind(on_release=popup.dismiss)
    popup.open()
                   
def load_apps(self):
    Box = BoxLayout(orientation="vertical", spacing=10)
    msg = GridLayout(cols=2, padding=15, spacing=10, size_hint_y=None)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    adv = Button(text='Show Advanced Mode',size_hint_y=(None), height=25)
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    try:
        for name in os.listdir(SystemApp):
            if not name in check:
                btnname = (CustomButton(text='%s' % name, font_size=10, size_hint_y=None, height=40))
                msg.add_widget(btnname)
                btnname.bind(on_release=do_button)
            
        root = ScrollView(size_hint=(None, None), size=(675, 350), do_scroll_x=False)
        root.add_widget(msg)
        Box.add_widget(adv)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
        adv.bind(on_release=load_adv_apps)
        
        popup = Popup(background='atlas://images/eds/pop', title='Easy Mode',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(700, 500))
        done.bind(on_release=popup.dismiss)
        adv.bind(on_release=popup.dismiss)
        popup.open()
        
    except:
        EdsNotify().run("'system/app Directory Not Found", 'Cant Find:\n' + SystemApp)

def load_adv_apps(self):
    Box = BoxLayout(orientation="vertical", spacing=10)
    msg = GridLayout(cols=2, padding=15, spacing=10, size_hint_y=None)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    ez = Button(text='Show Easy Mode',size_hint_y=(None), height=25)
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    try:
        for name in os.listdir(SystemApp):
            btnname = (Button(text='%s' % name, font_size=10, size_hint_y=None, height=40, background_color=(1.4,0,0,0.6)))
            msg.add_widget(btnname)
            btnname.bind(on_release=do_adv_button)
            
        root = ScrollView(size_hint=(None, None), size=(675, 350), do_scroll_x=False)
        root.add_widget(msg)
        Box.add_widget(ez)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
        ez.bind(on_release=load_apps)
        
        popup = Popup(background='atlas://images/eds/pop', title='Advanced Mode',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(700, 500))
        done.bind(on_release=popup.dismiss)
        ez.bind(on_release=popup.dismiss)
        popup.open()
        
    except:
        EdsNotify().run("'system/app Directory Not Found", 'Cant Find:\n' + SystemApp) 
        
              
def do_button(self):
    filepath = "%s/%s" % (SystemApp, self.text)        
    shutil.move(filepath, Removed)


def do_adv_button(self):
    filepath = "%s/%s" % (SystemApp, self.text)        
    root = BoxLayout(orientation='vertical', spacing=20)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=25)
    remove = Button(text='Remove', size_hint_x=None, width=150)
    cancel = Button(text='Cancel', size_hint_x=None, width=150)
    root.add_widget(Label(text='Are You Sure You Want To Remove This\nApp This could Cause Issues with your rom.'))
    root.add_widget(btn_layout)
    btn_layout.add_widget(remove)
    btn_layout.add_widget(cancel)
    popup = Popup(background='atlas://images/eds/pop', title='NOTICE',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    cancel.bind(on_release=popup.dismiss)
    popup.open()
    
    def remove_now(self):
        shutil.move(filepath, Removed)
    remove.bind(on_release=remove_now)
    remove.bind(on_release=popup.dismiss)

def load_usr_apps(self):
    Box = BoxLayout(orientation="vertical", spacing=10)
    msg = GridLayout(cols=2, padding=15, spacing=10, size_hint_y=None)
    btn_layout = GridLayout(cols=1)
    done = Button(text="Done")
    btn_layout.add_widget(done)
    msg.bind(minimum_height=msg.setter('height'))
    try:
        for name in os.listdir(DataApp):
            btnname = (Button(text='%s' % name, font_size=10, size_hint_y=None, height=40))
            msg.add_widget(btnname)
            btnname.bind(on_release=do_adv_button)
            
        root = ScrollView(size_hint=(None, None), size=(675, 390), do_scroll_x=False)
        root.add_widget(msg)
        Box.add_widget(root)
        Box.add_widget(btn_layout)
        
        popup = Popup(background='atlas://images/eds/pop', title='User Apps',content=Box, auto_dismiss=True,
        size_hint=(None, None), size=(700, 500))
        done.bind(on_release=popup.dismiss)
        popup.open()
        
    except:
        EdsNotify().run("'data/app Directory Not Found", 'Cant Find:\n' + DataApp)

def ask_remove_user(self):
    root = BoxLayout(orientation='vertical',padding=25, spacing=60)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=40, spacing=10)
    agree = Button(text='I am sure', width=150)
    decline = Button(text='Cancel', width=150)
    root.add_widget(Label(markup=True,halign="center", text="Are You Sure You Want To\nremove apks from data/app?"))
    root.add_widget(btn_layout)
    btn_layout.add_widget(agree)
    btn_layout.add_widget(decline)
    popup = Popup(background='atlas://images/eds/pop', title='Remove User Apks',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    decline.bind(on_release=popup.dismiss)
    agree.bind(on_release=load_usr_apps)
    agree.bind(on_release=popup.dismiss)
    popup.open()

def ask_restore_removed(self):
    root = BoxLayout(orientation='vertical',padding=25, spacing=60)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=40, spacing=10)
    agree = Button(text='Restore', width=150)
    decline = Button(text='Cancel', width=150)
    root.add_widget(Label(markup=True,halign="center", text="Are You Sure You Want To\nRestore all removed apps?"))
    root.add_widget(btn_layout)
    btn_layout.add_widget(agree)
    btn_layout.add_widget(decline)
    popup = Popup(background='atlas://images/eds/pop', title='Restore',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    decline.bind(on_release=popup.dismiss)
    agree.bind(on_release=restore_removed)
    agree.bind(on_release=popup.dismiss)
    popup.open()
    
def restore_removed(self):
    for name in os.listdir(Removed):
        shutil.move(Removed + "/" + name, SystemApp)

def ask_clean_removed(self):
    root = BoxLayout(orientation='vertical',padding=25, spacing=60)
    btn_layout = GridLayout(cols=2, row_force_default=True, row_default_height=40, spacing=10)
    agree = Button(text='DANGER', width=150, background_color=(2,0,0,1.0))
    decline = Button(text='Cancel', width=150)
    root.add_widget(Label(markup=True,halign="center", text="Are You Sure You Want to Permanently\nDelete All Removed Apps?\n[b][color=#D61818]DANGER: THIS IS IRREVERSIBLE.[/color][/b]"))
    root.add_widget(btn_layout)
    btn_layout.add_widget(agree)
    btn_layout.add_widget(decline)
    popup = Popup(background='atlas://images/eds/pop', title='Danger',content=root, auto_dismiss=False,
    size_hint=(None, None), size=(350, 200))
    decline.bind(on_release=popup.dismiss)
    agree.bind(on_release=restore_removed)
    agree.bind(on_release=popup.dismiss)
    popup.open()
    
def clean_removed(self):
    for name in os.listdir(Removed):
        os.remove(Removed + "/" + name)
        
        
