

![alt text](lib/html/imgs/cam.jpg "Camera")


# hc-x1000
Control Panasonic's 4k Camera via web.

## Description

An all in one api controller for Panasonic's 4K HC-X1000 camcorder. The api creates a streaming server that connects directly with the camera api and allows for a proxy stream to be created and served to multiple clients. The api gives full control of the camera via the web. As of the moment the Api still doesn't support audio input.

## Install

...

## Usage

...

### Notes

According to ffplay the size that the stream throws is "640x360, 25 tbr, 1200k". The stream is a mjpeg stream being cast via udp port. The node 'keep-image-fresh' script runs so keep the connection alive.



### Self-Reminders

- finish porting over all api commands
- make a better looking controller.. put some imagination behind it.
- npm/ffmpeg/python libs/and other friends are needed. ? Maybe create a docker container? >_<
- make instructions on how to get working
- give a live demo example online.
- k_i_f needs a catch if parameters aren't sent from the get


## Donate

![btc](https://github.com/kod3000/EventsManager/blob/d54efb0e1301a6cc1d508b8a9c571f3bb8da04b8/public/img/bitcoin.png) Bitcoin: `34zin8qyLHUcaN1E9veNoorPujaRVnr6ZZ`
