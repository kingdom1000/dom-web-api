import urllib2

baseUrl = 'http://dom-home-server.com:12000/servicerequest%20%22Living%20Room%22%20'
baseUrlChannel = 'http://dom-home-server.com:12000/writestate%20userDefined.RequestedChannel%20'

#Off
offURL = '%22%22%20%22%22%20%22%22%20%22%22%20PowerOff'

#Chromecast On
chromecast = 'Chromecast%20%22Video%20Source%22%201%20SVC_AV_HDMI%20PowerOn'

#Kodi On
kodi = '22XBMC%22%20%22Media_server%22%201%20SVC_AV_EXTERNALMEDIASERVER%20PowerOn'

#RetroPie On
retropie = 'RetroPie%20%22Video%20Source%22%201%20SVC_AV_HDMI%20PowerOn'

#Virgin Media
virgin = '%22Virgin%20Media%20TV%22%20%22Cable%20TV%20Tuner%22%201%20SVC_AV_TV%20PowerOn'

def off():
    contents = urllib2.urlopen(baseUrl + offURL).read()

def chromecastOn():
    contents = urllib2.urlopen(baseUrl + chromecast).read()

def kodiOn():
    contents = urllib2.urlopen(baseUrl + kodi).read()

def retropieOn():
    contents = urllib2.urlopen(baseUrl + retropie).read()

def virginOn():
    contents = urllib2.urlopen(baseUrl + virgin).read()

def changeChannel(channel):
    contents = urlicontents = urllib2.urlopen(baseUrlChannel + channel).read()