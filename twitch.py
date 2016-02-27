#!/usr/bin/env python3

# Zoey Twitch script
# v0.1.0 (27 Feb 2016)
# To-Do:
#  + add command line args
#  + add command line arg for making xspf
#  + add command line for making m3u8 file (2easy)

import urllib.request
import urllib.parse
import json
import random
from xml.etree import ElementTree as xmlEt
from xml.dom import minidom

TWITCH_API = 'http://api.twitch.tv/api/{0}'
TWITCH_USHER = 'http://usher.twitch.tv/api/{0}'
# TWITCH_KRAKEN = 'https://api.twitch.tv/kraken/{0}'
RAN = random.randint(0,1E7)
# testChannel = 'pamcakes'
testChannel = 'luxxbunny'

# m3u8 protocol bla
#

def api_call(url):
	req = urllib.request.Request(url)
	r = urllib.request.urlopen(req)
	with r as f:
		return f.read().decode('utf-8')

#def kraken_call(url):
#	req = urllib.request.Request(url)
#	req.add_header('Accept', 'application/vnd.twitchtv.v3+json')
#	r = urllib.request.urlopen(req)
#	with r as f:
#		print(f.read().decode('utf-8'))

def get_access_token():
	tokenCall = 'channels/{0}/access_token'.format(testChannel)
	apiCall = api_call(TWITCH_API.format(tokenCall))
	data = json.loads(apiCall)
	token = urllib.parse.quote(data['token'])
	sig = data['sig']
	return token, sig

def get_m3u8_data():
	token, sig = get_access_token()
	urlsCall = 'channel/hls/{channel}.m3u8?p={random}&token={token}&allow_source=true&allow_audio_only=true&player=twitchweb&allow_spectre=true&sig={sig}'.format(channel=testChannel, token=token, sig=sig, random=RAN)
	# extra params:
	#   &allow_audio_only=true (in use)
	#   &type=any

	# print('[DEBUG] Making API call: {0}'.format(TWITCH_USHER.format(urlsCall)))
	# print('\n\n\n')
	return api_call(TWITCH_USHER.format(urlsCall))

def print_urls():
	rawData = get_m3u8_data().split('\n')
	m3u8Protocols = '#EXT'
	#print(rawData)
	for ln in rawData:
		if not ln.startswith(m3u8Protocols):
			print(ln)
	#print(data)

def make_xspf():
	rawData = get_m3u8_data().split('\n')
	m3u8Protocols = '#EXT'
	links = []
	for ln in rawData:
		if not ln.startswith(m3u8Protocols):
			links.append(ln)
			# print(ln)
	
	root = xmlEt.Element('playlist')     # create an element in the element tree
	root.attrib = {"xmlns": "http://xspf.org/ns/0/", "xmlns:vlc": "http://www.videolan.org/vlc/playlist/ns/0/", "version": "1"}
	title = xmlEt.SubElement(root, 'title')
	title.text = 'Playlist'
	trackList = xmlEt.SubElement(root, 'trackList')

	vlcId = 0
	for link in links:
		track = xmlEt.SubElement(trackList, 'track')
		location = xmlEt.SubElement(track, 'location')
		location.text = link
		title = xmlEt.SubElement(track, 'title')
		title.text = testChannel + " ♥"
		album = xmlEt.SubElement(track, 'album')
		album.text = "fmt{0}".format(str(vlcId))
		extension = xmlEt.SubElement(track, 'extension')
		extension.attrib = {"application": "http://www.videolan.org/vlc/playlist/0"}
		vlcid = xmlEt.SubElement(extension, 'vlc:id')
		vlcid.text = str(vlcId)
		vlcId+=1

	extension = xmlEt.SubElement(root, 'extension')
	extension.attrib = {"application": "http://www.videolan.org/vlc/playlist/0"}
	
	i = 0
	while i < vlcId:
		vlcitem = xmlEt.SubElement(extension, 'vlc:item')
		vlcitem.attrib = {"tid": str(i)}
		i += 1
	
	reparsed = minidom.parseString(xmlEt.tostring(root))
	return reparsed.toprettyxml()

print(make_xspf())
# print_urls()
