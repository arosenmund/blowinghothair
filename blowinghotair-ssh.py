import binascii
import time
import os

message = "Mark1"

n = bin(int.from_bytes(message.encode(), 'big'))
print(n)
n = "0"+n[2:]
n_array = list(n)

#setup for each loop

t = len(n)
print(t)
while i < t:
    print(n_array[i])
    f = n_array[i]
    if f == '1':
    	m = '90'
    else:
        m = '40'
    fancontrol = "DISPLAY=:0 nvidia-settings -a '[gpu:0]/GPUFanControlState=1' -a '[fan:0]/GPUTargetFanSpeed="+m+"'"
    os.system(fancontrol)
    i += 1
    #run command (x)

    time.sleep(2)
#retun to normal fan speed
f = 40
fancontrol = "DISPLAY=:0 nvidia-settings -a '[gpu:0]/GPUFanControlState=1' -a '[fan:0]/GPUTargetFanSpeed="+f+"'"
print('Message transmission completed')

#
#def bits2a(b):
#     return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))
