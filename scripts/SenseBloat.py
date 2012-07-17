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


def rm_adobe(self):
    try:
        if os.path.exists('%s/AdobeReader.apk' % SystemApp) == True:
            shutil.move('%s/AdobeReader.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/AdobeReader.apk' % Removed) == True:
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
        os.remove('%s/AdobeReader.apk' % Removed)
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
    
def rm_amazon(self):
    try:
        if os.path.exists('%s/amazonmp3.apk' % SystemApp) == True:
            shutil.move('%s/amazonmp3.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/amazonmp3.apk' % Removed) == True:
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
        os.remove('%s/amazonmp3.apk' % Removed)
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
    
    
def rm_app_share(self):
    try:
        if os.path.exists('%s/AppSharing.apk' % SystemApp) == True:
            shutil.move('%s/AppSharing.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/AppSharing.apk' % Removed) == True:
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
        os.remove('%s/AppSharing.apk' % Removed)
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
    

def rm_blockbuster(self):
    try:
        if os.path.exists('%s/Blockbuster_Stub_HTC.apk' % SystemApp) == True:
            shutil.move('%s/Blockbuster_Stub_HTC.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/Blockbuster_Stub_HTC.apk' % Removed) == True:
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
        os.remove('%s/Blockbuster_Stub_HTC.apk' % Removed)
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
    

def rm_bluesky(self):
    try:
        if os.path.exists('%s/BlueSky.apk' % SystemApp) == True:
            shutil.move('%s/BlueSky.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/BlueSky.apk' % Removed) == True:
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
        os.remove('%s/BlueSky.apk' % Removed)
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
    

def rm_burgandy(self):
    try:
        if os.path.exists('%s/Burgandy.apk' % SystemApp) == True:
            shutil.move('%s/Burgandy.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/Burgandy.apk' % Removed) == True:
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
        os.remove('%s/Burgandy.apk' % Removed)
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
    

def rm_dcs(self):
    try:
        if os.path.exists('%s/DCSStock.apk' % SystemApp) == True:
            shutil.move('%s/DCSScock.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/DCSStock.apk' % Removed) == True:
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
        os.remove('%s/DCSStock.apk' % Removed)
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
    

def rm_field(self):
    try:
        if os.path.exists('%s/FieldTrial.apk' % SystemApp) == True:
            shutil.move('%s/FieldTrial.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/FieldTrial.apk' % Removed) == True:
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
        os.remove('%s/FieldTrial.apk' % Removed)
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
    

def rm_flickr(self):
    try:
        if os.path.exists('%s/Flickr.apk' % SystemApp) == True:
            shutil.move('%s/Flickr.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/Flickr.apk' % Removed) == True:
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
        os.remove('%s/Flickr.apk' % Removed)
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
    

def rm_hornet(self):
    try:
        if os.path.exists('%s/GreenHornet3D.apk' % SystemApp) == True:
            shutil.move('%s/GreenHornet3D.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/GreenHornet3D.apk' % Removed) == True:
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
        os.remove('%s/GreenHornet3D.apk' % Removed)
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
    

def rm_car_pannel(self):
    try:
        if os.path.exists('%s/HtcCarPanel.apk' % SystemApp) == True:
            shutil.move('%s/HtcCarPanel.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/HtcCarPanel.apk' % Removed) == True:
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
        os.remove('%s/HtcCarPanel.apk' % Removed)
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
    

def rm_direct(self):
    try:
        if os.path.exists('%s/HtcDirect.apk' % SystemApp) == True:
            shutil.move('%s/HtcDirect.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/HtcDirect.apk' % Removed) == True:
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
        os.remove('%s/HtcDirect.apk' % Removed)
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
    

def rm_feedback(self):
    try:
        if os.path.exists('%s/HtcFeedback.apk' % SystemApp) == True:
            shutil.move('%s/HtcFeedback.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/HtcFeedback.apk' % Removed) == True:
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
        os.remove('%s/HtcFeedback.apk' % Removed)
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

def rm_sync_provider(self):
    try:
        if os.path.exists('%s/HtcHubSyncProvider.apk' % SystemApp) == True:
            shutil.move('%s/HtcHubSyncProvider.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/HtcHubSyncProvider.apk' % Removed) == True:
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
        os.remove('%s/HtcHubSyncProvider.apk' % Removed)
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

def rm_streak(self):
    try:
        if os.path.exists('%s/HTCLivewallpaperStreak.apk' % SystemApp) == True:
            shutil.move('%s/HTCLivewallpaperStreak.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/HTCLivewallpaperStreak.apk' % Removed) == True:
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
        os.remove('%s/HTCLivewallpaperStreak.apk' % Removed)
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

def rm_weather_wall(self):
    try:
        if os.path.exists('%s/HtcWeatherWallpaper.apk' % SystemApp) == True:
            shutil.move('%s/HtcWeatherWallpaper.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/HtcWeatherWallpaper.apk' % Removed) == True:
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
        os.remove('%s/HtcWeatherWallpaper.apk' % Removed)
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

def rm_smoke_wall(self):
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

def rm_mode_10(self):
    try:
        if os.path.exists('%s/Mode10Wallpapers.apk' % SystemApp) == True:
            shutil.move('%s/Mode10Wallpapers.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/Mode10Wallpapers.apk' % Removed) == True:
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
        os.remove('%s/Mode10Wallpapers.apk' % Removed)
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

def rm_mspot(self):
    try:
        if os.path.exists('%s/mSpotRadioSprint_VPL.apk' % SystemApp) == True:
            shutil.move('%s/mSpotRadioSprint_VPL.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/mSpotRadioSprint_VPL.apk' % Removed) == True:
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
        os.remove('%s/mSpotRadioSprint_VPL.apk' % Removed)
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

def rm_my_htc(self):
    try:
        if os.path.exists('%s/MyHTC.apk' % SystemApp) == True:
            shutil.move('%s/MyHTC.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/MyHTC.apk' % Removed) == True:
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
        os.remove('%s/MyHTC.apk' % Removed)
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

def rm_my_report(self):
    try:
        if os.path.exists('%s/MyReportAgent.apk' % SystemApp) == True:
            shutil.move('%s/MyReportAgent.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/MyReportAgent.apk' % Removed) == True:
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
        os.remove('%s/MyReportAgent.apk' % Removed)
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

def rm_nscm(self):
    try:
        if os.path.exists('%s/NscmStub.apk' % SystemApp) == True:
            shutil.move('%s/NscmStub.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/NscmStub.apk' % Removed) == True:
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
        os.remove('%s/NscmStub.apk' % Removed)
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

def rm_asset(self):
    try:
        if os.path.exists('%s/OnlineAssetDetail.apk' % SystemApp) == True:
            shutil.move('%s/OnlineAssetDetail.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/OnlineAssetDetail.apk' % Removed) == True:
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
        os.remove('%s/OnlineAssetDetail.apk' % Removed)
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

def rm_picasa(self):
    try:
        if os.path.exists('%s/picasapryramid.apk' % SystemApp) == True:
            shutil.move('%s/picasapryramid.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/picasapryramid.apk' % Removed) == True:
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
        os.remove('%s/picasapryramid.apk' % Removed)
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

def rm_poloris(self):
    try:
        if os.path.exists('%s/PolarisOffice.apk' % SystemApp) == True:
            shutil.move('%s/PolarisOffice.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/PolarisOffice.apk' % Removed) == True:
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
        os.remove('%s/PolarisOffice.apk' % Removed)
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

def rm_qik(self):
    try:
        if os.path.exists('%s/qik.apk' % SystemApp) == True:
            shutil.move('%s/qik.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/qik.apk' % Removed) == True:
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
        os.remove('%s/qik.apk' % Removed)
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

def rm_lookup(self):
    try:
        if os.path.exists('%s/QuickLookup.apk' % SystemApp) == True:
            shutil.move('%s/QuickLookup.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/QuickLookup.apk' % Removed) == True:
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
        os.remove('%s/QuickLookup.apk' % Removed)
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

def rm_qxdm(self):
    try:
        if os.path.exists('%s/QXDM2SD.apk' % SystemApp) == True:
            shutil.move('%s/QXDM2SD.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/QXDM2SD.apk' % Removed) == True:
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
        os.remove('%s/QXDM2SD.apk' % Removed)
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

def rm_guide(self):
    try:
        if os.path.exists('%s/SIE_HTCMobileGuide_Shooter.apk' % SystemApp) == True:
            shutil.move('%s/SIE_HTCMobileGuide_Shooter.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/SIE_HTCMobileGuide_Shooter.apk' % Removed) == True:
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
        os.remove('%s/SIE_HTCMobileGuide_Shooter.apk' % Removed)
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

def rm_smith(self):
    try:
        if os.path.exists('%s/Smith.apk' % SystemApp) == True:
            shutil.move('%s/Smith.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/Smith.apk' % Removed) == True:
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
        os.remove('%s/Smith.apk' % Removed)
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

def rm_spidy(self):
    try:
        if os.path.exists('%s/Spiderman_HTC_EVO2_ML_IGP_3D_Sprint_122.apk' % SystemApp) == True:
            shutil.move('%s/Spiderman_HTC_EVO2_ML_IGP_3D_Sprint_122.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/Spiderman_HTC_EVO2_ML_IGP_3D_Sprint_122.apk' % Removed) == True:
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
        os.remove('%s/Spiderman_HTC_EVO2_ML_IGP_3D_Sprint_122.apk' % Removed)
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

def rm_installer(self):
    try:
        if os.path.exists('%s/Sprint_InstallerNC_v2_1_0.apk' % SystemApp) == True:
            shutil.move('%s/Sprint_InstallerNC_v2_1_0.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/Sprint_InstallerNC_v2_1_0.apk' % Removed) == True:
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
        os.remove('%s/Sprint_InstallerNC_v2_1_0.apk' % Removed)
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

def rm_wallet(self):
    try:
        if os.path.exists('%s/SprintMobileWallet.apk' % SystemApp) == True:
            shutil.move('%s/SprintMobileWallet.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/SprintMobileWallet.apk' % Removed) == True:
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
        os.remove('%s/SprintMobileWallet.apk' % Removed)
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

def rm_nav(self):
    try:
        if os.path.exists('%s/Sprint_Navigator_stub.apk' % SystemApp) == True:
            shutil.move('%s/Sprint_Navigator_stub.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/Sprint_Navigator_stub.apk' % Removed) == True:
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
        os.remove('%s/Sprint_Navigator_stub.apk' % Removed)
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

def rm_tv(self):
    try:
        if os.path.exists('%s/SprintTVStub_Signed.apk' % SystemApp) == True:
            shutil.move('%s/SprintTVStub_Signed.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/SprintTVStub_Signed.apk' % Removed) == True:
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
        os.remove('%s/SprintTVStub_Signed.apk' % Removed)
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

def rm_zone(self):
    try:
        if os.path.exists('%s/SprintZoneNC.apk' % SystemApp) == True:
            shutil.move('%s/SprintZoneNC.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/SprintZoneNC.apk' % Removed) == True:
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
        os.remove('%s/SprintZoneNC.apk' % Removed)
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

def rm_stock(self):
    try:
        if os.path.exists('%s/Stock.apk' % SystemApp) == True:
            shutil.move('%s/Stock.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/Stock.apk' % Removed) == True:
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
        os.remove('%s/Stock.apk' % Removed)
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

def rm_vis_wall(self):
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

def rm_weather_live(self):
    try:
        if os.path.exists('%s/WeatherLiveWallpaper.apk' % SystemApp) == True:
            shutil.move('%s/WeatherLiveWallpaper.apk' % SystemApp, Removed)
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
                
        elif os.path.exists('%s/WeatherLiveWallpaper.apk' % Removed) == True:
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
        os.remove('%s/WeatherLiveWallpaper.apk' % Removed)
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
