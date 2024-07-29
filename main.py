import random
import tkinter as tk

class DesktopPet:
    def __init__(self, master):
        self.master = master
        self.x = 1150
        self.y = 910
        self.cycle = 0
        self.check = 1
        self.event_number = random.randrange(1, 3, 1)
        
        self.idle_num = [1, 2, 3, 4]
        self.sleep_num = [10, 11, 12, 13, 15]
        self.walk_left = [6, 7]
        self.walk_right = [8, 9]
        
        self.asset_path = "assets"
        self.load_animations()
        
        self.setup_window()
        self.start_animation()

    def load_animations(self):
        self.animations = {
            'idle': self.load_gif('idle.gif', 5),
            'idle_to_sleep': self.load_gif('idle_to_sleep.gif', 8),
            'sleep': self.load_gif('sleep.gif', 3),
            'sleep_to_idle': self.load_gif('sleep_to_idle.gif', 8),
            'walk_negative': self.load_gif('walking_positive.gif', 8),
            'walk_positive': self.load_gif('walking_negative.gif', 8)
        }

    def load_gif(self, filename, frames):
        return [tk.PhotoImage(file=f'{self.asset_path}/{filename}', format=f'gif -index {i}') for i in range(frames)]

    def setup_window(self):
        self.master.config(highlightbackground='black')
        self.label = tk.Label(self.master, bd=0, bg='black')
        self.master.overrideredirect(True)
        self.master.wm_attributes('-transparentcolor', 'black')
        self.master.attributes('-topmost', True)
        self.label.pack()

        self.label.bind("<Button-1>", self.on_drag_start)
        self.label.bind("<B1-Motion>", self.on_drag_motion)

    def start_animation(self):
        self.master.after(1, self.update)

    def event(self):
        if self.event_number in self.idle_num:
            self.check = 0
            self.master.after(400, self.update)
        elif self.event_number == 5:
            self.check = 1
            self.master.after(100, self.update)
        elif self.event_number in self.walk_left:
            self.check = 4
            self.master.after(100, self.update)
        elif self.event_number in self.walk_right:
            self.check = 5
            self.master.after(100, self.update)
        elif self.event_number in self.sleep_num:
            self.check = 2
            self.master.after(1000, self.update)
        elif self.event_number == 14:
            self.check = 3
            self.master.after(100, self.update)

    def gif_work(self, frames, first_num, last_num):
        if self.cycle < len(frames) - 1:
            self.cycle += 1
        else:
            self.cycle = 0
            self.event_number = random.randrange(first_num, last_num + 1, 1)

    def update(self):
        if self.check == 0:  # idle
            frame = self.animations['idle'][self.cycle]
            self.gif_work(self.animations['idle'], 1, 9)
        elif self.check == 1:  # idle to sleep
            frame = self.animations['idle_to_sleep'][self.cycle]
            self.gif_work(self.animations['idle_to_sleep'], 10, 10)
        elif self.check == 2:  # sleep
            frame = self.animations['sleep'][self.cycle]
            self.gif_work(self.animations['sleep'], 10, 15)
        elif self.check == 3:  # sleep to idle
            frame = self.animations['sleep_to_idle'][self.cycle]
            self.gif_work(self.animations['sleep_to_idle'], 1, 1)
        elif self.check == 4:  # walk toward left
            frame = self.animations['walk_positive'][self.cycle]
            self.gif_work(self.animations['walk_positive'], 1, 9)
            self.x -= 3
        elif self.check == 5:  # walk towards right
            frame = self.animations['walk_negative'][self.cycle]
            self.gif_work(self.animations['walk_negative'], 1, 9)
            self.x += 3

        self.master.geometry(f'100x100+{self.x}+{self.y}')
        self.label.configure(image=frame)
        self.master.after(1, self.event)

    def on_drag_start(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y
        self.window_start_x = self.master.winfo_x()
        self.window_start_y = self.master.winfo_y()

    def on_drag_motion(self, event):
        # Calculate the new position
        new_x = self.window_start_x + event.x - self.drag_start_x
        new_y = self.window_start_y + event.y - self.drag_start_y
        
        # Update position incrementally
        self.master.geometry(f'+{new_x}+{new_y}')
        
        # Update internal position tracking
        self.x = new_x
        self.y = new_y

        # Redraw the window to ensure smooth dragging
        self.master.update_idletasks()
if __name__ == "__main__":
    root = tk.Tk()
    pet = DesktopPet(root)
    root.mainloop()