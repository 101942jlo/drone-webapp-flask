
# Drone Mission Control in Flask

A webapplication made in Python using the Flask framework to control a DJI Tello drone.

The python file "drone.py" solves all the communication with the drone. The communication goes via UDP using Sockets. Every socket needs to be run in a separate thread to avoid blocking main thread.

The drone receive command through the port 8889 and receive telemtry through the port 8890. It is possible to receive live video from the drone camara. This happens listening on UDP port 11111 and host(0.0.0.0). This function hasn't been implemented yet, but you can find an example of how you can get a video in a webapplication using Flask if you have a look a the python file name: "test_cv2_face_recognition.py".
Using the OpenCV library it makes possible getting video from a webcam and detect faces.



## Screenshots

![App Screenshot](https://i.ibb.co/pnT8T1H/Capture.jpg)


## Installation

Clone the repository

```bash
  git clone https://github.com/101942jlo/drone-webapp-flask.git
  cd drone-webapp-flask
```
And run the main.py python file.

```bash
  python main.py
```
Do not forget to install the requirements.
## Authors

- [@101942jlo](https://www.github.com/101942jlo)


## 🚀 About Me
I'm a student from CVO Groeipunt. Currently following Python level 3 and this is my final project.

