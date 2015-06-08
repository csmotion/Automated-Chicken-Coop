from w1thermsensor import W1ThermSensor

def ReadAllSensors():
	for sensor in W1ThermSensor.get_available_sensors([W1ThermSensor.THERM_SENSOR_DS18B20]):
		print("%s: %.2f" % (sensor.id, sensor.get_temperature()))

def ReadSensor(sn):
	sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, sn)
	return sensor.get_temperature()

if __name__ == "__main__":
	ReadAllSensors()
