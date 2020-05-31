This is the ALPHAbot created for NS-Alpha LG to assist in administration for the entire lifegroup
This is mainly done so by:
    1. Storing upcoming events
    2. Giving timely reminders as these events are approaching
    3. Storing recent sermons that LG members may have missed
    4. Sending broadcasts to all members via pm
    5. Spamming the group when a call (i.e. on Zoom is started)
    6. Staying cool while doing all these

### Running it on docker (cannot be used on the pi):
- Using python:3.7.7-buster image
$ docker build -t <image name> <src_path>
$ docker run <image name>

### Running it on docker on the pi:
- Using arm32v6/python:3.7.7-alpine image
$ docker build -t <image name> <src_path>
$ docker run <image name>

^ This does not work because cryptography cannot be properly installed on alpine (required in emojize)

# Problems installing cryptography build try:
- upgrading pip 
- edit Dockerfile pip install the list of libraries

#### CURRENTLY FOR PI:
run start.sh