from oscpy.server import OSCThreadServer
from time import sleep

#initalizing varable osc to OSCThreaded Server class
osc = OSCThreadServer()

#Initializing the object with local pc address and port. 
sock = osc.listen(address='127.0.0.1', port=9002, default=True)

print("running...")

#any OSC message with the address /data will be routed to the address function to be handled.
@osc.address(b'/data') 

#the function is triggered when a OSC signal is received
def callback(left,right):   
  print("Left prediction : ",round(left,2),"Right prediction : ",round(right,2))
  
  #  if(round(left,2) < 0.7 and round(left,2) > 0.6):
  #    print("LEFT...")

    # if(round(right,2) > 0.3):
    #   print("RIGHT...")
    # else:
    #    print(".")

  #print("got values: {}".format(values))
  #sleep(0.5)
sleep(1000)

