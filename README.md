# Image Processing Homeworks & Exams

## Installation
```
$ virtualenv -p python3 .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
```

## Test
```
$ python3 test_installation.py
```

## Realtime Object Detection
```
$ python3 real_time_object_detection.py --prototxt model/MobileNetSSD_deploy.prototxt.txt --model model/MobileNetSSD_deploy.caffemodel
```