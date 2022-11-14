from gpiozero import TrafficLights
from time import sleep    

lights = TrafficLights(25, 8, 7)    
    
while True:
           light.green.on()
           sleep(5)
           lights.amber.on()
           sleep(5)
           lights.red.on()
           sleep(5)
           lights.off()
