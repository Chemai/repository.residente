import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR gold][B]Star [/COLOR]*[COLOR red]WZRD[/B][/COLOR]'
EXCLUDES       = [ADDON_ID, 'plugin.program.StarWZRD', 'repository.star']
# Text File with build info in it.
BUILDFILE      = 'https://dl.dropbox.com/s/e40pc2ybxu8ntlx/Star-autobuilds.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 3
# Text File with apk info in it.
APKFILE        = 'https://dl.dropbox.com/s/u722le9svpr0qy3/apks.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'VideoTutoriales Star'
YOUTUBEFILE    = 'https://dl.dropbox.com/s/elu8mhz9flkl8l7/youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'https://dl.dropbox.com/s/962hgkht9v5w56z/addons.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'https://dl.dropbox.com/s/rb80c4bkvuysrpb/advanced.txt'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = os.path.join(ART, '0.png')
ICONMAINT      = os.path.join(ART, '1.png')
ICONAPK        = os.path.join(ART, '2.png')
ICONADDONS     = os.path.join(ART, '3.png')
ICONYOUTUBE    = os.path.join(ART, '4.png')
ICONSAVE       = os.path.join(ART, '5.png')
ICONTRAKT      = os.path.join(ART, '6.png')
ICONREAL       = os.path.join(ART, '7.png')
ICONLOGIN      = os.path.join(ART, '8.png')
ICONCONTACT    = os.path.join(ART, '9.png')
ICONSETTINGS   = os.path.join(ART, '10.png')
ICONRETRO      = os.path.join(ART, '13.png')
ICONSPEED      = os.path.join(ART, '14.png')
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '*'

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'gold'
COLOR2         = 'white'
COLOR3         = 'lime'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR3+'][B]([COLOR '+COLOR1+']*[/COLOR])[/COLOR]  [COLOR '+COLOR2+']%s[/COLOR][/B]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR cyan]Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = '[B]Gracias por elegir [COLOR gold]Star [/COLOR]WZRD.\r\nVisitanos en \r\n\r\nTelegram: https://t.me/star\r\n\r\nFacebook: http://facebook.com/star[/B]'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = os.path.join(ART, '9.png')
CONTACTFANART  = os.path.join(ART, 'fondo.jpg')
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'https://dl.dropbox.com/s/e40pc2ybxu8ntlx/Star-autobuilds.txt'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.residente'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://raw.githubusercontent.com/chemai/repository.residente/master/zips/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://raw.githubusercontent.com/chemai/repository.residente/master/zips/'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://dl.dropbox.com/s/monh3pjvlcgtvdd/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = '[COLOR gold][B]Star[/B] [/COLOR]WZRD'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = 'https://i.imgur.com/JUtrWVL.jpg'
#########################################################