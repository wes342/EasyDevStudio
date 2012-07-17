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
from scripts.setting import *

def name(self, value):
    try:
        processing_change = False
        for line in fileinput.input(Reg, inplace=1):
            if line.startswith('Name:'):
                processing_change = True
            else:
                if processing_change:
                    print r'Name:' + value + ''
                    processing_change = False
                print line,
    except:
        print 'cant write'

def reg(self, value):
    reg2(self, value)
 
def list_view(self):
    for line in fileinput.input(ukv, inplace = 1): 
        print line.replace(r"        FileChooserIconView:", r"        FileChooserListView:"),   

def icon_view(self):
    for line in fileinput.input(ukv, inplace = 1): 
        print line.replace(r"        FileChooserListView:", r"        FileChooserIconView:"),
        
# Build In Themes
def ins_stock_theme(self):
    pathtofile = '%s/Eds_stock_theme.zip' % (Themes)
    destpath = '%s' % (Usr)
    z = zipfile.ZipFile(pathtofile)
    z.extractall(destpath)
    restart(self)

    
def ins_red_theme(self):
    pathtofile = '%s/Eds_red_theme.zip' % (Themes)
    destpath = '%s' % (Usr)
    z = zipfile.ZipFile(pathtofile)
    z.extractall(destpath)
    restart(self)
    
def ins_blue_theme(self):
    pathtofile = '%s/Eds_blue_theme.zip' % (Themes)
    destpath = '%s' % (Usr)
    z = zipfile.ZipFile(pathtofile)
    z.extractall(destpath)
    restart(self)   
# Featured User Themes 

def ins_joes_theme(self):
    pass
    
def ins_toms_theme(self):
    pass
