from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from twilio.rest import TwilioRestClient
import json
import random
import string
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'boing'
socketio = SocketIO(app)

@app.route('/')
def index():
	return "Hello"


@socketio.on('audio')
def getAudio(audio):
	# name = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(0, 6))
	name = 'file'
	print audio
	fileName = 'test/'+name+'.3gp'
	f = open(fileName, 'wb')
	f.write(audio)
	f.close()



	# sendsms('there was a knock on the door', '3474595013')


@socketio.on('sample')
def getSample(sample):
	print sample




# @socketio.on('action')
# def getAction(action):
# 	j = json.loads(action)
# 	name = j["name"]



# 	print action



# def save_config(json):
# 	outFile = open(, 'w')
# 	outFile.write(lang)
# 	outFile.close()


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')