import random
import time

while(True):

          #temperature range in dh11 sensor is 0 to 50 Celsius
          temp=round(random.uniform(0,50),2)
          #humidity range in dh11 sensor is 20 to 90%
          humid=round(random.uniform(20,90),2)

          #ideal weather temperature range is 22 C to 30 C
          #ideal weather humidity range is 35% to 60%

          #condition for high temperature
          if(temp>30):
                    print("High Temperature !!!\a\a\a\a\a")
                    print("Temperature : %.2f\tHumidity : %.2f"%(temp,humid))
                    if(humid<35 or humid>60):
                              print("Abnormal Humidity !!!\a\a\a\a\a")
          #condition for low temperature
          if(temp<22):
                    print("Low Temperature !!!\a\a\a\a\a")
                    print("Temperature : %.2f\tHumidity : %.2f"%(temp,humid))
                    if(humid<35 or humid>60):
                              print("Abnormal Humidity !!!\a\a\a\a\a")
          time.sleep(5)
