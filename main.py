from connection import do_connect
#from ufirebase import firebase_real_time_database
#from ufirebase import firebase_get_data
#from post_data import init
#from post_to_dynamo import do_post
from temperature import get_temperature
import time
import gc
import machine
from firestorage import bratzinai
#from firestorage import post_data


gc.collect()
do_connect()

fan = machine.Pin(2,machine.Pin.OUT)
light = machine.Pin(16,machine.Pin.OUT)
while True:
    gc.collect()
    temp = get_temperature()
    try:
        print('temperature successs ==>', temp)
        bratzinai('chameleon-test', temp)
    except Exception as e:
        print('Can not post', e)
    time.sleep(5)
    
    gc.collect()
    #get_humidity()
    #dic_temp = firebase_get_data("Estado/test")
    #temp_setup = dic_temp["temperature"] 
    #do_post()
    #print("The temperature configured is: " + str(temp_setup))

#    if temp > temp_setup:
#        fan.off()
#        light.on()
#    else:
#        fan.on()
#        light.off()
#    time.sleep(2)
#    gc.collect()
