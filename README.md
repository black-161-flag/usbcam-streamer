# libcamera-streamer
simple streaming server using usb cameras

## usage
python3 usbcam-streamer.py

```
optional arguments:
  -h, --help         show this help message and exit
  --device DEVICE    video device (default: /dev/video0)
  --hflip HFLIP      rotate hflip (default: 0)
  --vflip VFLIP      rotate vflip (default: 0)
  --width WIDTH      width of the video (default: 1280)
  --height HEIGHT    height of the video (default: 720)
  --address ADDRESS  bind address (default: localhost)
  --port PORT        bind port (default: 8000)
```
