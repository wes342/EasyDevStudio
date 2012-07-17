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


def rm_adw(self):
    try:
        if os.path.exists('%s/ADWLauncher.apk' % SystemApp) == True:
            shutil.move('%s/ADWLauncher.apk' % SystemApp, Removed)
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/ADWLauncher.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/ADWLauncher.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"
        
        
def rm_dsp(self):
    try:
        if os.path.exists('%s/DSPManager.apk' % SystemApp) == True:
            shutil.move('%s/DSPManager.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/DSPManager.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/DSPManager.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"



def rm_spareparts(self):
    try:
        if os.path.exists('%s/SpareParts.apk' % SystemApp) == True:
            shutil.move('%s/SpareParts.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/SpareParts.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/SpareParts.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"


def rm_androidian(self):
    try:
        if os.path.exists('%s/Androidian.apk' % SystemApp) == True:
            shutil.move('%s/Androidian.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/Androidian.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/Androidian.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"


def rm_file_manager(self):
    try:
        if os.path.exists('%s/FileManager.apk' % SystemApp) == True:
            shutil.move('%s/FileManager.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/FileManager.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/FileManager.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_theme_chooser(self):
    try:
        if os.path.exists('%s/ThemeChooser.apk' % SystemApp) == True:
            shutil.move('%s/ThemeChooser.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/ThemeChooser.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/ThemeChooser.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_term(self):
    try:
        if os.path.exists('%s/AndroidTerm.apk' % SystemApp) == True:
            shutil.move('%s/AndroidTerm.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/AndroidTerm.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/AndroidTerm.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_live_walls(self):
    try:
        if os.path.exists('%s/LiveWallpapers.apk' % SystemApp) == True:
            shutil.move('%s/LiveWallpapers.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/LiveWallpapers.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/LiveWallpapers.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_theme_manager(self):
    try:
        if os.path.exists('%s/ThemeManager.apk' % SystemApp) == True:
            shutil.move('%s/ThemeManager.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/ThemeManager.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/ThemeManager.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_cm_parts(self):
    try:
        if os.path.exists('%s/CMParts.apk' % SystemApp) == True:
            shutil.move('%s/CMParts.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/CMParts.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/CMParts.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_live_picker(self):
    try:
        if os.path.exists('%s/LiveWallpapersPicker.apk' % SystemApp) == True:
            shutil.move('%s/LiveWallpapersPicker.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/LiveWallpapersPicker.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/LiveWallpapersPicker.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_torch(self):
    try:
        if os.path.exists('%s/Torch.apk' % SystemApp) == True:
            shutil.move('%s/Torch.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/Torch.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/Torch.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_screenshot(self):
    try:
        if os.path.exists('%s/CMScreenshot.apk' % SystemApp) == True:
            shutil.move('%s/CMScreenshot.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/CMScreenshot.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/CMScreenshot.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_smoke_walls(self):
    try:
        if os.path.exists('%s/MagicSmokeWallpapers.apk' % SystemApp) == True:
            shutil.move('%s/MagicSmokeWallpapers.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/MagicSmokeWallpapers.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/MagicSmokeWallpapers.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_vis_walls(self):
    try:
        if os.path.exists('%s/VisualizationWallpapers.apk' % SystemApp) == True:
            shutil.move('%s/VisualizationWallpapers.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/VisualizationWallpapers.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/VisualizationWallpapers.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_cm_stats(self):
    try:
        if os.path.exists('%s/CMStats.apk' % SystemApp) == True:
            shutil.move('%s/CMStats.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/CMStats.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/CMStats.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_protips(self):
    try:
        if os.path.exists('%s/Protips.apk' % SystemApp) == True:
            shutil.move('%s/Protips.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/Protips.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/Protips.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_cm_update(self):
    try:
        if os.path.exists('%s/CMUpdateNotify.apk' % SystemApp) == True:
            shutil.move('%s/CMUpdateNotify.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/CMUpdateNotify.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/CMUpdateNotify.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_search_box(self):
    try:
        if os.path.exists('%s/QuickSearchBox.apk' % SystemApp) == True:
            shutil.move('%s/QuickSearchBox.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/QuickSearchBox.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/QuickSearchBox.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_cm_walls(self):
    try:
        if os.path.exists('%s/CMWallpapers.apk' % SystemApp) == True:
            shutil.move('%s/CMWallpapers.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/CMWallpapers.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/CMWallpapers.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_rom_manager(self):
    try:
        if os.path.exists('%s/RomManager.apk' % SystemApp) == True:
            shutil.move('%s/RomManager.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/RomManager.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/RomManager.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_cyanobread(self):
    try:
        if os.path.exists('%s/Cyanobread.apk' % SystemApp) == True:
            shutil.move('%s/Cyanobread.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/Cyanobread.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/Cyanobread.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def rm_sound_rec(self):
    try:
        if os.path.exists('%s/SoundRecorder.apk' % SystemApp) == True:
            shutil.move('%s/SoundRecorder.apk' % SystemApp, Removed)
            print 'File has been moved to Removed_Apps if needed later'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move successful", "File is now in 'Removed_Apps' so you can restore if needed")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
                
        elif os.path.exists('%s/SoundRecorder.apk' % Removed) == True:
                print 'Already Removed'
                try:
                    import pynotify
                    if pynotify.init(NAME):
                        n = pynotify.Notification("File Was already removed", "File is in 'Removed_Apps' so you can restore if needed")
                        n.set_urgency(pynotify.URGENCY_NORMAL)
                        n.show()
                    else:
                        print "there was a problem initializing the 'pynotify' module"
                except:
                    print "you don't seem to have 'pynotify' installed"
        else: 
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification("Move Unsuccessfull", "File Could Not Be Found: 'Guess I can't move something thats not found'")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
    except:
        print 'bad stuff happened... Trying to fix the problem'
        os.remove('%s/SoundRecorder.apk' % Removed)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Failed Please Try Again", "Second Try Should have fixed the issue.\nIf Not There is a Issue please submit Bug")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"


def clean_removed(self):
    try:
        if os.listdir(Removed):
            from glob import glob
            for f in glob ('%s/*.apk' % Removed):
                os.unlink (f)
            print 'Removed Files Cleaned'
            try:
                import pynotify
                if pynotify.init(NAME):
                    n = pynotify.Notification('Clean Complete', "'Removed_Apps' Has Been Cleaned")
                    n.set_urgency(pynotify.URGENCY_NORMAL)
                    n.show()
                else:
                    print "there was a problem initializing the 'pynotify' module"
            except:
                print "you don't seem to have 'pynotify' installed"
        else:
            print 'Already Clean: Ill do something else i guess'
    except:
        print "What did you do? no 'Removed_Apps' folder found. Ok Ill Make one for you"
        os.mkdir(Removed)
        
def restore_removed(self):
    for f in os.listdir(Removed):
        print f
        src_file = os.path.join(Removed, f)
        dst_file = os.path.join(SystemApp, f)
        shutil.move(src_file, dst_file)
        try:
            import pynotify
            if pynotify.init(NAME):
                n = pynotify.Notification("Removed Apps Restored", "All of the apps you removed have been restored")
                n.set_urgency(pynotify.URGENCY_NORMAL)
                n.show()
            else:
                print "there was a problem initializing the 'pynotify' module"
        except:
            print "you don't seem to have 'pynotify' installed"

def cm7_bloat_help(self):
    pass
