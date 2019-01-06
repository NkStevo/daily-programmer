from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import re
import time

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = StopWatchWindow(self)
        self._frame.grid(row=0, column=0, sticky="nsew")

class StopWatchWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.is_first_start = True

        self.stop = "STOP"
        self.start = "START"
        self.lap = "LAP"
        self.state = self.stop

        self.lap_list = list()
        self.display_lap_list = list()
        self.master.protocol("WM_DELETE_WINDOW", self._delete_window)

        self.create_widgets()
        self.stopwatch_update()

    def create_widgets(self):
        self.time_label = Label(self, text=str(0.0))
        self.time_label.grid(row=0, column=1, padx=5, pady=10)

        self.lap_label = Label(self, text="")
        self.lap_label.grid(row=1, column=1, padx=5, pady=10)

        self.start_button = Button(self, text='Start', command=self.start_watch)
        self.start_button.grid(row=2, column=0, padx=5, pady=5)

        self.stop_button = Button(self, text='Stop', command=self.stop_watch)
        self.stop_button.grid(row=2, column=1, padx=5)

        self.lap_reset_button = Button(self, text='Reset', command=self.reset_watch)
        self.lap_reset_button.grid(row=2, column=2, padx=5)

    def start_watch(self):
        self.state = self.start

        if self.is_first_start:
            self.start_time = time.time()
            self.pause_time = -1
            self.lap_list.append(self.start_time)
            self.is_first_start = False

        if self.pause_time != -1:
            self.start_time += time.time() - self.pause_time
            self.lap_list[-1] += time.time() - self.pause_time

        self.lap_reset_button['text'] = 'Lap'
        self.lap_reset_button['command'] = self.lap_watch

    def stop_watch(self):
        if self.state == self.start:
            self.pause_time = time.time()

        self.state = self.stop

        self.lap_reset_button['text'] = 'Reset'
        self.lap_reset_button['command'] = self.reset_watch

    def lap_watch(self):
        self.state = self.lap

    def reset_watch(self):
        self.is_first_start = True
        self.lap_list.clear()

        self.time_label['text'] = str(0.0)
        self.lap_label['text'] = ""

    def stopwatch_update(self):
        if self.state == self.start:
            self.time_label['text'] = str(round(time.time() - self.start_time, 2))
        elif self.state == self.lap:
            self.lap_label['text'] = "Lap " + str(len(self.lap_list)) + ": " + str(round(time.time() - self.lap_list[-1], 2))
            self.time_label['text'] = str(round(time.time() - self.start_time, 2))

            self.display_lap_list.append(str(round(time.time() - self.lap_list[-1], 2)))
            self.lap_list.append(time.time())

            self.state = self.start

        self.after(100, self.stopwatch_update)

    def _delete_window(self):
        with open('data.txt', 'w') as outfile:
            outfile.write(str(round(time.time() - self.start_time, 2)) + "\n")
            outfile.write("\n".join(self.display_lap_list))


        self.master.destroy()


def main():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()
