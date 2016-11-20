from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from twilio.rest import TwilioRestClient
import time
import os

config = {
	    "database": {
        "host": "127.0.0.1",
        "user": "root",
        "passwd": "password123", 
        "db": "dejavu",
    }
}

djv = Dejavu(config)

account_sid = "AC51365a670d38f32fb1bc163bf0f300fc"
auth_token  = "8cf63b9fd2d05385cabfb175b94dab1b"

client = TwilioRestClient(account_sid, auth_token)

def sendsms (msg, phonenum): 
	message = client.messages.create(body=msg, to="+1"+phonenum,from_="+13472189059")
	print(message.sid)

while True:
	djv.fingerprint_directory("../files", [".wav"], 3)
	# print djv.db.get_num_fingerprints()

	# try:
	# 	song = djv.recognize(FileRecognizer, "../test/file.3gp")
	# 	print song
	# 	# print song
	# 	if song != None:
	# 		print "found"
	# 		sendsms('someone is at the door', '3474595013')
	# 		# os.remove("../test/file.3gp")
	# except:
	# 	pass

	try:
		song = djv.recognize(FileRecognizer, "../test/file.3gp")
		print song
		# print song
		if song != None:
			time.sleep(5)
			print "found"
			sendsms('someone is at the door', '3474595013')
			os.remove("../test/file.3gp")
			break
	except:
		pass

	time.sleep(5)
