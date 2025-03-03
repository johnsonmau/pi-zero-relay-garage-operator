# Load libraries
import RPi.GPIO as GPIO
import time
from bottle import route, run, post, request, response
from json import dumps

# Set up the GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.output(7, True)
GPIO.output(11, True)

#define variables
pswd = 'xxxx' # set custom password to operate garage (refactoring to use basic auth at some point)

#Define check_login (function that checks if password is correct by comparing it to the correct one)
def check_login(password):
    if password == pswd:
        return True
    else:
        return False

#Receive and check login info
@route('/garage', method='POST')
def do_login():
    reqData = request.json
    password = reqData.get('operate')

    if check_login(password): #cycle the gpio to open garage if passwords match
        GPIO.output(7, False)
        time.sleep(.8)
        GPIO.output(7, True)
        res = {
            "res": "success"
        }
        response.content_type = 'application/json'
        response.status = 200
        return dumps(res)
    else:
        res = {
            "res": "incorrect password"
        }
        response.content_type = 'application/json'
        response.status = 401
        return dumps(res)

@route('/status', method='GET')
def do_status():

    res = {
        "res": "garage service is running on garage pi"
    }

    response.content_type = 'application/json'
    response.status = 200
    return dumps(res)

#Run the bottle.py server
run(host='0.0.0.0', port=8080)

