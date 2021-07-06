# Description

The following api end points have been found by reverse engineering the cgi script. Not all end points are listed but the most important ones are here and should be integrated into the python server.


### Start view of Stream and send it to udp port '9100'

	/cam.cgi?mode=startstream&value=9100
	/cam.cgi?mode=stopstream
 
now view it using ffplay

  ffplay -f mjpeg -i udp://:9100

## HC-X1000 API Detailed

### Menus
	
	/cam.cgi?mode=getinfo&type=allmenu
	/cam.cgi?mode=getinfo&type=curmenu
	/cam.cgi?mode=getinfo&type=lens


### Info

	/cam.cgi?mode=getinfo&type=capability
	/cam.cgi?mode=getinfo&type=curmode
	/cam.cgi?mode=getstate
	/cam.cgi?mode=getstate&type=keep_alive
	/cam.cgi?mode=getinfo&type=initialsetinfo
	/cam.cgi?mode=getinfo&type=ddd
	/cam.cgi?mode=getsetting&type=videoformat


### Settings


	/cam.cgi?mode=getsetting&type=focusmode
	/cam.cgi?mode=getsetting&type=angle
	/cam.cgi?mode=setsetting&type=angle&value=wide/standard
	/cam.cgi?mode=getsetting&type=focusassist

Shutter Speed

	/cam.cgi?mode=setsetting&type=shtrspeed&value=60

White Balance Control

	/cam.cgi?mode=camcmd&value=wbset
	/cam.cgi?mode=setsetting&type=wb_semipro&value=auto
	/cam.cgi?mode=setsetting&type=wb_semipro&value=var&value2=2500

### Actions

	/cam.cgi?mode=camcmd&value=poweroff
	/cam.cgi?mode=camcmd&value=wifioff
	/cam.cgi?mode=camcmd&value=far_max
	/cam.cgi?mode=camcmd&value=pushaf

Zoom-in Automated

	/cam.cgi?mode=camcmd&value=tele-normal
	/cam.cgi?mode=camcmd&value=tele-fast

Zoom-out Automated

	/cam.cgi?mode=camcmd&value=wide-normal
	/cam.cgi?mode=camcmd&value=wide-fast


Record 

	/cam.cgi?cam.cgi?mode=camcmd&value=recstart
	/cam.cgi?cam.cgi?mode=camcmd&value=capture
	/cam.cgi?mode=camcmd&value=recmode

???

	/cam.cgi?mode=pantiltcmd&type=checkstart
	/cam.cgi?mode=pantiltcmd&type=autostart
	/cam.cgi?mode=pantiltcmd&type=autopause
	/cam.cgi?mode=exclusion
  
  
More Examples 

	/cam.cgi?mode=camctrl&type=focus&value=tele-fast
	/cam.cgi?mode=camctrl&type=focus&value=tele-normal
	/cam.cgi?mode=camctrl&type=focus&value=wide-normal
	/cam.cgi?mode=setsetting&type=focal&value=53
	/cam.cgi?mode=setsetting&type=expandzoom&value=x5
	/cam.cgi?mode=setsetting&type=wb_semipro&value=var&value2=2400


## References 

- https://linuxhint.com/send_receive_udp_python/
- https://stackoverflow.com/questions/19210414/byte-array-to-hex-string
- https://stackoverflow.com/questions/37618851/socket-reading-udp-packet
- https://wiki.python.org/moin/UdpCommunication
- https://github.com/yushuhuang/webcam/blob/master/receive.py
- https://github.com/maiermic/panasonic-image-app
- https://github.com/isontheline/panasonic-html-image-app
- https://github.com/auberginehill/panasonic-html-image-app
- http://www.personal-view.com/talks/discussion/6703/control-your-gh3-from-a-web-browser-now-with-video-/p1