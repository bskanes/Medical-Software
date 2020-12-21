import tkinter as tk
import datetime
import pathlib
from tkinter import simpledialog
import matplotlib.pyplot as plt
import numpy

window = tk.Tk()
window.title('Medical Bacteria Recorder')

# Stringvar
culture_id_input_var = tk.StringVar()
bacteria_option_menu_var = tk.StringVar()
medicine_option_menu_var = tk.StringVar()
morning_count_var = tk.StringVar()
evening_count_var = tk.StringVar()


# GUI FUNCTIONS
def confirm_function():
    culture = int(culture_id_input_var.get())
    bacteria = bacteria_option_menu_var.get()
    medicine = medicine_option_menu_var.get()
    morning = float(morning_count_var.get())
    evening = float(evening_count_var.get())
    time = datetime.datetime.now()
    count_change = ((evening/morning)-1)
    output = ('Culture ID({}) – Bacteria Type({}) – Medicine Type({}) – Morning Population Reading({}) – Evening Population\
 Reading({}) – Calculated Rate Of Change({}) - Time({})'.format(culture, bacteria, medicine, morning, evening,
                                                                    count_change, time))
    lb.insert(tk.END, output)


def save_function():
    save_file_location = tk.simpledialog.askstring("Save Data", "Please enter a file name: ")
    if save_file_location is None:
        return
    pathlib.Path(save_file_location).touch()
    with open(save_file_location, "a") as f:
        for entry in lb.get(0, tk.END):
            f.write(entry + "\n")


def plot_values(xs, ys):
    plt.plot(xs, ys)
    plt.show()


def plot_function():
    morning = float(morning_count_var.get())
    evening = float(evening_count_var.get())
    a = float((evening-morning)/12)
    b = float(morning)
    range_start = tk.simpledialog.askstring('Range Start', "Please input the initial x value for the range:")
    range_end = tk.simpledialog.askstring('Range End', "Please input the final x value for the range:")
    range_int = tk.simpledialog.askstring('Range Int', "Please input the plotting resolution in terms of steps between x values:")
    range_startone = float(range_start)
    range_endone = float(range_end)
    range_intone = float(range_int)
    xs = list(numpy.arange(range_startone, range_endone + range_intone, range_intone))
    ys = []
    for x in xs:
        y = a * x + b
        ys.append(y)
    plot_values(xs, ys)


def exit_function():
    exit(0)


culture_id_label = tk.Label(window, text="Culture ID:")
culture_id_label.grid(row=0, column=0)
culture_id_input = tk.Entry(window, textvariable=culture_id_input_var)
culture_id_input.grid(row=0, column=1)

bacteria_label = tk.Label(window, text='Bacteria:')
bacteria_label.grid(row=1, column=0)


def delete_function():
    lb.delete(tk.ANCHOR)


f = open('bacteria.dat', 'r')
lines = f.readlines()


bacteria_options = ["NONE"]


linenumber = 0
linecount = len(lines)

while True:
    if linenumber >= linecount:
        break
    else:
        something = lines[linenumber].strip('\n').split(' : ')
        linenumber += 1
        bacteria_options.extend(something)
        continue
# FILE LABELS/OPTION MENU
bacteria_option_menu_var.set(bacteria_options[0])
bacteria_option_menu = tk.OptionMenu(window, bacteria_option_menu_var, *bacteria_options)
bacteria_option_menu.grid(row=1, column=1)
f.close()

medicine_label = tk.Label(window, text='Medicine:')
medicine_label.grid(row=2, column=0)

f = open('medicine.dat', 'r')
lines = f.readlines()


medicine_options = ["NONE"]

linenumber2 = 0
linecount2 = len(lines)

while True:
    if linenumber2 >= linecount2:
        break
    else:
        something2 = lines[linenumber2].strip('\n').split(' : ')
        linenumber2 += 1
        medicine_options.extend(something2)
        continue

medicine_option_menu_var.set(medicine_options[0])
medicine_option_menu = tk.OptionMenu(window, medicine_option_menu_var, *medicine_options)
medicine_option_menu.grid(row=2, column=1)
f.close()

# LABELS/ENTRY/LISTBOX
morning_count_label = tk.Label(window, text='Morning Bacteria Count:')
morning_count_label.grid(row=3, column=0)

morning_count = tk.Entry(window, textvariable=morning_count_var)
morning_count.grid(row=3, column=1)

evening_count_label = tk.Label(window, text='Evening Bacteria Count:')
evening_count_label.grid(row=4, column=0)

evening_count = tk.Entry(window, textvariable=evening_count_var)
evening_count.grid(row=4, column=1)

data_label = tk.Label(window, text='-DATA OUTPUT-')
data_label.grid(row=0, column=2)

lb = tk.Listbox(window)
lb.grid(row=1, column=2, rowspan=4, sticky='WE')
lb.config(width=40, height=8)

# BUTTONS
confirm_button = tk.Button(window, text='Confirm', command=confirm_function)
confirm_button.grid(row=5, column=1)

save_button = tk.Button(window, text='Save', command=save_function)
save_button.grid(row=1, column=3)

linear_projection_button = tk.Button(window, text='Linear Projection', command=plot_function)
linear_projection_button.grid(row=3, column=3)

exit_button = tk.Button(window, text="Exit Program", command=exit_function)
exit_button.grid(row=5, column=2)

delete_button = tk.Button(window, text='Delete Selection', command=delete_function)
delete_button.grid(row=2, column=3)

window.mainloop()
