from connection import do_connect
#from ufirebase import firebase_real_time_database
from ufirebase import firebase_get_data
#from post_data import init
#from post_to_dynamo import do_post
from temperature import get_temperature
import time
import gc
import machine
from firestorage import bratzinai
import uart
#from firestorage import post_data


gc.collect()
do_connect()

fan = machine.Pin(2,machine.Pin.OUT)
light = machine.Pin(16,machine.Pin.OUT)
while True:
    gc.collect()
    temp = get_temperature()
    data_from_firebase = firebase_get_data('ring/ring')
    data_from_firebase_two = firebase_get_data('ring_time/ring_time')
    print('data from firebase ->', data_from_firebase)
    if data_from_firebase == True:
        print('fan on')
        fan.on()
    else:
        fan.off()
    if data_from_firebase_two == True:
        ligth.on()
        print('light on')
    else :
        light.off()
    print('data from firebase two ->', data_from_firebase_two)
    try:
        print('temperature successs ==>', temp)
        bratzinai('chameleon-test', temp)
    except Exception as e:
        print('Can not post', e)
    time.sleep(1)
    
    gc.collect()
