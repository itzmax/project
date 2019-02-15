import RPI.GPIO as GPIO,time

GPIO.setmode(GPIO.BMC)
GPIO.setwarnings(False)
redled = 23
fountain = 25
GPIO.setup(redled,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(fountain,GPIO.OUT,initial=GPIO.HIGH)
GPIO.output(redled,GPIO.HIGH)
time.sleep(5)
GPIO.output(redled,GPIO.LOW)
GPIO.output(fountain,GPIO.LOW)
time.sleep(10)
GPI.output(fountian,GPIO.HIGH)
