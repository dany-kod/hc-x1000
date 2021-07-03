
# hc-x1000
Control Panasonic's 4k Camera via web.

![alt text](imgs/cam.jpg "Camera")


## Description

An all in one api controller for Panasonic's 4K HC-X1000 camcorder. The api creates a streaming server that connects directly with the camera api and allows for a proxy stream to be created and served to multiple clients. The api gives full control of the camera via the web. As of the moment the Api still doesn't support audio input.

## Install

...

## Usage

...

### Notes

According to ffplay the size that the stream throws is "640x360, 25 tbr, 1200k". The stream is a mjpeg stream being cast via udp port. The node 'keep-image-fresh' script runs so keep the connection alive.



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


### Reminders

- finish porting over all api commands
- make a better looking controller.. put some imagination behind it.
- npm/ffmpeg/python libs/and other friends are needed. ? Maybe create a docker container? >_<
- make instructions on how to get working
- give a live demo example online.
- k_i_f needs a catch if parameters aren't sent from the get