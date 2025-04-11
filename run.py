import eel
import os
import sys
import time
import datetime
import subprocess

@eel.expose  # Eel function
def qrBase64Decoder(param):
	jsonObj = {'code':'00'}
	if param['base64Str'] != '':
		filename = '%d.tmp' %int(time.time() * 1000)
		f = open(filename, 'w')
		f.write(param['base64Str'])
		f.close()
		try:
			jsonObj['rlt'] = subprocess.check_output("img2Str %s" %(filename), shell=True).decode('utf-8')
		except:
			jsonObj['rlt'] = subprocess.check_output("img2Str %s" %(filename), shell=True)
			pass
		if os.path.exists(filename):
			os.remove(filename)
	else:
		jsonObj['code'] = '01'

	return jsonObj

if __name__ == '__main__':
	eel.init('web')
	my_options = {
		'mode': "chrome-app", #or "chrome",
		'host': 'localhost',
		'port': 8291,
	}

	try:
		eel.start('index.html', mode='chrome-app', port=8291)
	except (SystemExit, MemoryError, KeyboardInterrupt):
		pass 
	



