import uuid
import time
import matplotlib
import matplotlib.pyplot as plt
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


#customizes matplotlib default values 
matplotlib.rcParams.update({'font.size': fontsize})

# The StreamInfo object stores the declaration of a data stream.
info = StreamInfo(name='MotorImag-Markers', type='Markers', channel_count=1, nominal_srate=0, channel_format='string',source_id='t8u43t98u')

#used to make streaming data available on networks.
outlet = StreamOutlet(info)

#Start statement
print("Press [Enter] to begin.")
x = input()

#hFigure will store plot point
#ax stores the array of values needed to plot
hFigure, ax = plt.subplots()

#Labels the y-axis and x-axis
ax.set_yticklabels([''])
ax.set_xticklabels([''])

#Text Placement of graph
t = plt.text(0.5, 0.5, '', horizontalalignment='center')

#Limit of x and y axes of graph
plt.xlim(xmin=0, xmax=1)
plt.ylim(ymin=0, ymax=1)

#Turns on interactive mode for matplotlib - (graph will update after each statement)
plt.ion()

#update graph
plt.draw()

#display all figures
plt.show()

try:    
    for trial in range(1, 131): # (Warm-up + trials)*classification
        #Check if the graph exixts, if it doesnt, through exception
        if not plt.fignum_exists(hFigure.number):
            break

        #pick randomly a number from 0 - 1 and store in "choice" 
        choice = random.choice(range(len(labels)))

        #sets the label to "Left" or "Right" depeding on the index from "choice"
        t.set_text(labels[choice])

        #Once "trial" = 10, it will send "calib-begin" out.
        if trial == warmup_trials:
            outlet.push_sample(['calib-begin'])

        #Once "trial" > 10, it will send either "left or right, depending on index -> choice"
        if trial > warmup_trials:
            outlet.push_sample([markers[choice]])

        #Re-draw the updates
        hFigure.canvas.draw()
        #Will hold the change GUI so all UI events are proccessed -> Ensures no errors update 
        hFigure.canvas.flush_events()

        #allow time to complete task
        time.sleep(perform_time)
        t.set_text('')

        hFigure.canvas.draw()
        hFigure.canvas.flush_events()

        time.sleep(wait_time)

        #Take a break after 30 trials
        if trial % pause_every == 0:
            t.set_text('Pause')
            hFigure.canvas.draw()
            hFigure.canvas.flush_events()
            time.sleep(pause_duration)
            t.set_text('')

        hFigure.canvas.draw()
        hFigure.canvas.flush_events()

#If exception is thrown
except Exception as e:
    #print error
    print(e)

#Ctrl + C to END
except KeyboardInterrupt:
    print("Program terminated manually!")
    #Output "end" to outlet
    outlet.push_sample(['calib-end'])
    raise SystemExit

#Output "end" to outlet
outlet.push_sample(['calib-end'])

