from setuptools import setup

setup(
    name='usbcam-streamer',
    version='0.0.3',
    packages=['usbcam-streamer'],
    scripts=['bin/usbcam-streamer'],
    description='simple mpg streamer for usbcameras',
    long_description=open('README.md').read(),
    install_requires=["opencv-python", "simplejpeg", 'numpy'],
    package_dir={'usbcam-streamer': 'bin'},

)
