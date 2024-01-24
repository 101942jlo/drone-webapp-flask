from flask import Flask, render_template, redirect, url_for
import threading
from drone import Tello
# import cv2

app = Flask(__name__)

drone = Tello()

# STATUS
is_connected = drone.connected
webcam_on = False
is_flying = False

# webcam = cv2.VideoCapture(0) # to test the camera.


@app.route('/')
def index():
    global is_connected
    return render_template('dashboard.html', is_connected=is_connected)


@app.route('/connect', methods=['POST'])
def connect():
    drone.connect()
    global is_connected
    is_connected = True
    return redirect(url_for('index'))


@app.route('/disconnect', methods=['POST'])
def disconnect():
    global is_connected
    is_connected = False
    return redirect(url_for('index'))


# Here all the route to control the drone
@app.route('/left', methods=['POST'])
def move_left():
    drone.move_left(70)
    return redirect(url_for('index'))


@app.route('/right', methods=['POST'])
def move_right():
    drone.move_right(70)
    return redirect(url_for('index'))


@app.route('/up', methods=['POST'])
def move_up():
    drone.move_up(40)
    return redirect(url_for('index'))


@app.route('/down', methods=['POST'])
def move_down():
    drone.move_down(40)
    return redirect(url_for('index'))


@app.route('/forward', methods=['POST'])
def move_forward():
    drone.move_forward(80)
    return redirect(url_for('index'))


@app.route('/back', methods=['POST'])
def move_back():
    drone.move_back(80)
    return redirect(url_for('index'))


@app.route('/turn_left', methods=['POST'])
def turn_left():
    drone.turn_left(30)
    return redirect(url_for('index'))


@app.route('/turn_right', methods=['POST'])
def turn_right():
    drone.turn_right(30)
    return redirect(url_for('index'))


@app.route('/flip', methods=['POST'])
def flip():
    drone.flip("f")
    return redirect(url_for('index'))


@app.route('/takeoff', methods=['POST'])
def takeoff():
    drone.takeoff()
    return redirect((url_for('index')))


@app.route('/land', methods=['POST'])
def land():
    drone.land()
    return redirect((url_for('index')))


if __name__ == '__main__':
    """I made a separated thread for the app to avoid problem with the UDP socket"""
    webapp = threading.Thread(target=app.run())
    webapp.daemon = True
    webapp.start()

    # app.run(debug=True)
