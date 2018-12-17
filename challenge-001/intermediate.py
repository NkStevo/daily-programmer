from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import re

event_dict = {}

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(EventListWindow)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)

        if self._frame is not None:
            self._frame.destroy()

        self._frame = new_frame
        self._frame.grid(row=0, column=0, sticky="nsew")

    def switch_frame_edit(self, current_report):
        new_frame = AddEventWindow(self, current_report=current_report)

        if self._frame is not None:
            self._frame.destroy()

        self._frame = new_frame
        self._frame.grid(row=0, column=0, sticky="nsew")

class EventListWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.init_treeview()

        self.add_report_button = Button(self, text='Add Event', command=self.add_report)
        self.add_report_button.grid(row=1, column=0, padx=5, pady=5)

        self.edit_report_button = Button(self, text='Edit Event', command=self.edit_report)
        self.edit_report_button.grid(row=1, column=1, padx=5)

        self.delete_report_button = Button(self, text='Delete Event', command=self.delete_report)
        self.delete_report_button.grid(row=1, column=2, padx=5)

    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]

        if col == 'starttime' or col == 'endtime':
            l.sort(key=lambda cell: int(cell[0][0:2] + cell[0][3:5]), reverse=reverse)
        else:
            l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))

    def init_treeview(self):
        self.tree = Treeview(self)
        self.tree['columns'] = ('starttime', 'endtime')

        self.tree.heading("#0", text='Event Name', command=lambda: self.treeview_sort_column(self.tree, "#0", False))
        self.tree.column("#0", anchor='center', width=250)

        self.tree.heading('starttime', text='Start Time', command=lambda: self.treeview_sort_column(self.tree, 'starttime', False))
        self.tree.column('starttime', anchor='center', width=100)

        self.tree.heading('endtime', text='End Time', command=lambda: self.treeview_sort_column(self.tree, 'endtime', False))
        self.tree.column('endtime', anchor='center', width=100)

        global event_dict

        if event_dict:
            for name, times in event_dict.items():
                self.tree.insert('', 'end', name, text=name, values=times)

        self.tree.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky = (N,S,W,E))

    def add_report(self):
        self.master.switch_frame(AddEventWindow)

    def edit_report(self):
        if len(self.tree.selection()) > 0:
            self.master.switch_frame_edit(self.tree.item(self.tree.selection()[0]))

    def delete_report(self):
        selected_item = self.tree.selection()[0]
        print(self.tree.item(selected_item))
        print(len(self.tree.selection()))
        self.tree.delete(selected_item)

        global event_dict

        del event_dict[selected_item]

class AddEventWindow(Frame):
    def __init__(self, master=None, event_list_window=None, current_report=None):
        super().__init__(master)
        self.master = master
        self.event_list_window = event_list_window
        self.current_report = current_report

        self.create_widgets()

    def create_widgets(self):
        self.event_name_label = Label(self, text='Event Name:')
        self.event_name_label.grid(row=0, column=0, padx=5, pady=10)

        self.start_time_label = Label(self, text='Start Time (24 HR):')
        self.start_time_label.grid(row=1, column=0, padx=5, pady=10)

        self.end_time_label = Label(self, text='End Time (24 HR):')
        self.end_time_label.grid(row=2, column=0, padx=5, pady=10)

        self.event_name_entry = Entry(self)
        self.event_name_entry.grid(row=0, column=1, padx=5)

        self.start_time_entry = Entry(self)
        self.start_time_entry.grid(row=1, column=1, padx=5)

        self.end_time_entry = Entry(self)
        self.end_time_entry.grid(row=2, column=1, padx=5)

        if self.current_report:
            self.event_name_entry.insert(END, self.current_report['text'])
            self.start_time_entry.insert(END, self.current_report['values'][0])
            self.end_time_entry.insert(END, self.current_report['values'][1])

        self.submit_button = Button(self, text='Submit', command=self.submit)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=5)

    def is_time_invalid(self, start_time, end_time):
        return int(start_time[0:2] + start_time[3:5]) >= int(end_time[0:2] + end_time[3:5])

    def submit(self):
        global event_dict

        if len(self.event_name_entry.get()) == 0 or len(self.start_time_entry.get()) == 0 or len(self.end_time_entry.get()) == 0:
            messagebox.showerror("Entry Error", "Please input values for every entry")
        elif not re.match('^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', self.start_time_entry.get()) or not re.match('^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', self.start_time_entry.get()):
            messagebox.showerror("Entry Error", "Please input time in valid 24 hour HH:MM format")
        elif self.event_name_entry.get() in event_dict and not self.current_report:
            messagebox.showerror("Entry Error", "An event with that name already exists")
        elif self.is_time_invalid(self.start_time_entry.get(), self.end_time_entry.get()):
            messagebox.showerror("Entry Error", "Start time must be less than end time")
        else:
            if self.current_report and self.current_report['text'] != self.event_name_entry.get():
                del event_dict[self.current_report['text']]

            event_dict[self.event_name_entry.get()] = (self.start_time_entry.get(), self.end_time_entry.get())
            self.master.switch_frame(EventListWindow)

def main():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()
