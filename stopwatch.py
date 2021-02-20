from datetime import datetime
from tkinter import *  

temp = 0 # seconds quantity after stopwatch's start
after_id = '' # id returned by 'after' method 
    
window = Tk()  
window.title('Stopwatch')
window.iconbitmap('stopwatch-icon.ico')

# it is called recursively every second
def tick():
	global temp, after_id
	after_id = window.after(1000, tick)

	f_temp = datetime.fromtimestamp(temp).strftime("%M:%S") # formatting
	time_label.configure(text = str(f_temp))
	temp += 1

def start_stopwatch():
	btn_start.grid_forget()
	# sticky defines a border for widget
	btn_stop.grid(row = 1, columnspan = 2, sticky = "ew")
	tick()

def stop_stopwatch():
	btn_stop.grid_forget()
	btn_continue.grid(row = 1, column = 0, sticky = "ew")
	btn_reset.grid(row = 1, column = 1, sticky = "ew")

	window.after_cancel(after_id) #stop 'after' cycle


def continue_stopwatch():
	btn_continue.grid_forget()
	btn_reset.grid_forget()
	btn_stop.grid(row = 1, columnspan = 2, sticky = "ew")
	tick()

def reset_stopwatch():
	global temp
	temp = 0
	time_label.configure(text = "00:00")

	btn_continue.grid_forget()
	btn_reset.grid_forget()
	btn_start.grid(row = 1, columnspan = 2, sticky = "ew")


time_label = Label(window, width = 5, font = ("Arial", 100), text = "00:00")

time_label.grid(row = 0, columnspan = 2)

btn_start = Button(window, text = "Start", font = ("Arial", 30), command = start_stopwatch) 
btn_stop = Button(window, text = "Stop", font = ("Arial", 30), command = stop_stopwatch)
btn_continue = Button(window, text = "Continue", font = ("Arial", 30), command = continue_stopwatch)
btn_reset = Button(window, text = "Reset", font = ("Arial", 30), command = reset_stopwatch)

btn_start.grid(row =1, columnspan = 2, sticky = "ew")  

window.mainloop()