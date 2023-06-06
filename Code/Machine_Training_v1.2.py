import time
import random
from pylsl import StreamInfo, StreamOutlet

warmup_trials = 10
trials_per_class = 60
perform_time = 3.5
wait_time = 1
pause_every = 30
pause_duration = 20
fontsize = 30
labels = ['Left', 'Right']
markers = ['left', 'right']

# The StreamInfo object stores the declaration of a data stream.
info = StreamInfo(name='Python-Markers', type='Markers', channel_count=1, nominal_srate=0, channel_format='string',source_id='t8u43t98u')


#used to make streaming data available on networks.
outlet = StreamOutlet(info)

#Start Condition
print("Press [Enter] to begin.")
x = input()
n=0

try:    
    for trial in range(1, 131): # (Warm-up + trials)*classification

        #pick randomly a number from 0 - 1 and store in "choice" 
        choice = random.choice(range(len(labels)))

        #sets the label to "Left" or "Right" depeding on the index from "choice"
        print(labels[choice])

        #Once "trial" = 10, it will send "calib-begin" out.
        if trial == warmup_trials:
            outlet.push_sample(['calib-begin'])
            

        #Every collection made when "trial" > 10, it will send either "left or right, depending on index -> choice with its corressponding data"
        if trial > warmup_trials:
            
            #allow time to complete task
            print("collecting...")
            print(' ')
            time.sleep(perform_time)
            outlet.push_sample([markers[choice]])

        #rest
        time.sleep(wait_time)

        #Take a break after 30 trials
        if trial == 20+n:
            n=n+10
            print('REST')
            time.sleep(pause_duration)

#If exception is thrown
except Exception as e:
    #print error
    print(e)

#Output "end" to outlet
outlet.push_sample(['calib-end'])