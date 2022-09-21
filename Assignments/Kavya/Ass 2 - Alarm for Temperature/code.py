#Assignment 2
'''
Build a python code, Assume u get temperature and humidity values
(generated with random function to a variable) and
write a condition to continuously detect alarm in case of high temperature.
'''

'''
In python, we are using random module for generating random value.  randint(start,end) func generates random vals from start to end.
The sleep(sec) func is used to delay the output in the run time. This func is inside time module
'''

import random
import time

while(True):

          #temperature range in dh11 sensor is 0 to 50 Celsius
          temp=random.randint(0,50)
          #humidity range in dh11 sensor is 20 to 90%
          humid=random.randint(20,90)

          #ideal weather temperature range is 22 C to 30 C
          #ideal weather humidity range is 35% to 60%

          #condition for high temperature
          if(temp>30):
                    print("High Temperature !!!")
                    print("Temperature : %d\tHumidity : %d"%(temp,humid))

          #condition for low temperature
          if(temp<22):
                    print("Low Temperature !!!")
                    print("Temperature : %d\tHumidity : %d"%(temp,humid))

          #condition for abnormal humidity(using logical OR operator)
          if(humid<35 or humid>60):
                    print("Abnormal Humidity !!!")
                    print("Temperature : %d\tHumidity : %d"%(temp,humid))

          time.sleep(5)
