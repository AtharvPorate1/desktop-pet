import random
import tkinter as tk

x = 400  # Adjusted initial x coordinate
cycle = 0
check = 1
idle_num = [1, 2, 3, 4]
sleep_num = [10, 11, 12, 13, 15]
walk_left = [6, 7]
walk_right = [8, 9]
event_number = random.randrange(1, 3, 1)

def event(cycle, check, event_number, x):
    print(f"Event called with cycle: {cycle}, check: {check}, event_number: {event_number}, x: {x}")
    if event_number in idle_num:
        check = 0
        print('Idle event')
        window.after(400, update, cycle, check, event_number, x)  # no. 1, 2, 3, 4 = idle
    elif event_number == 5:
        check = 1
        print('Transition from idle to sleep')
        window.after(100, update, cycle, check, event_number, x)  # no. 5 = idle to sleep
    elif event_number in walk_left:
        check = 4
        print('Walking towards left')
        window.after(100, update, cycle, check, event_number, x)  # no. 6, 7 = walk towards left
    elif event_number in walk_right:
        check = 5
        print('Walking towards right')
        window.after(100, update, cycle, check, event_number, x)  # no 8, 9 = walk towards right
    elif event_number in sleep_num:
        check = 2
        print('Sleep event')
        window.after(1000, update, cycle, check, event_number, x)  # no. 10, 11, 12, 13, 15 = sleep
    elif event_number == 14:
        check = 3
        print('Transition from sleep to idle')
        window.after(100, update, cycle, check, event_number, x)  # no. 14 = sleep to idle

def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)
    return cycle, event_number

def update(cycle, check, event_number, x):
    print(f"Update called with cycle: {cycle}, check: {check}, event_number: {event_number}, x: {x}")
    if check == 0:  # idle
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)
    elif check == 1:  # idle to sleep
        frame = idle_to_sleep[cycle]
        cycle, event_number = gif_work(cycle, idle_to_sleep, event_number, 10, 10)
    elif check == 2:  # sleep
        frame = sleep[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 10, 15)
    elif check == 3:  # sleep to idle
        frame = sleep_to_idle[cycle]
        cycle, event_number = gif_work(cycle, sleep_to_idle, event_number, 1, 1)
    elif check == 4:  # walk toward left
        frame = walk_positive[cycle]
        cycle, event_number = gif_work(cycle, walk_positive, event_number, 1, 9)
        x -= 3
    elif check == 5:  # walk towards right
        frame = walk_negative[cycle]
        cycle, event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
        x += 3
    window.geometry(f'100x100+{x}+100')  # Adjusted y coordinate
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x)

window = tk.Tk()

# Load buddy's action gifs
idle = [tk.PhotoImage(file='idle.gif', format='gif -index %i' % i) for i in range(5)]  # idle gif
idle_to_sleep = [tk.PhotoImage(file='idle_to_sleep.gif', format='gif -index %i' % i) for i in range(8)]  # idle to sleep gif
sleep = [tk.PhotoImage(file='sleep.gif', format='gif -index %i' % i) for i in range(3)]  # sleep gif
sleep_to_idle = [tk.PhotoImage(file='sleep_to_idle.gif', format='gif -index %i' % i) for i in range(8)]  # sleep to idle gif
walk_positive = [tk.PhotoImage(file='walking_positive.gif', format='gif -index %i' % i) for i in range(8)]  # walk to left gif
walk_negative = [tk.PhotoImage(file='walking_negative.gif', format='gif -index %i' % i) for i in range(8)]  # walk to right gif

# Window configuration
window.config(highlightbackground='black')
label = tk.Label(window, bd=0, bg='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'black')
label.pack()

# Start the loop
window.after(1, update, cycle, check, event_number, x)
window.mainloop()
