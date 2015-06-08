import Temp
import time

s1 = '000006c39295'
s2 = '000006c40ed9'

FORMAT = '%Y-%m-%d-%H-%M-%S'

if __name__ == '__main__':
	t1 = Temp.ReadSensor(s1)
	t2 = Temp.ReadSensor(s2)
	dt = time.strftime(FORMAT)

	output = dt + ', ' + str(t1) + ', ' + str(t2) + '\n'
	
	with open("/usr/ChickenCoop/TempLog.txt", "a") as f:
		f.write(output)
		print output
