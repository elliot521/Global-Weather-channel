# basic tkinter to form interface
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
# clock widgets library
from time import strftime
import time
# weather widgets library
import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
# converter
import tkinter.font as font


# GUI
window = Tk()
window.title("Golbal Weather channel")
window.geometry("630x480")
window.configure(background="white")

# Menu
main_menu = Menu(window)
window.config(menu=main_menu)


def instruction():
    messagebox.showinfo("Instruction",
                        "Main Tool: tkinter. \n This interface"
                        " has the converter function plus "
                        "weather and clock widgets. :)")


def about_us():
    messagebox.showinfo("About Me", "Creator: Elliot Bu")


def FAQ():
    messagebox.showinfo("FAQ",
                        "Q: What features are present? \n A: "
                        "Time, Weather, Converer and Customisation "
                        "functionality. \n Q: Why do users have to connect "
                        "to the internet? \n A:The program relies on an "
                        "internet connection to fetch data from "
                        "Openweather")


reference_menu = Menu(main_menu)
main_menu.add_cascade(label="Reference", menu=reference_menu)
reference_menu.add_command(label="Exit", command=window.quit)
reference_menu.add_command(label="Instruction", command=instruction)

help_menu = Menu(main_menu)
main_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About Me", command=about_us)
help_menu.add_command(label="FAQ", command=FAQ)


# weather part
def getweather(window):
    city = textfield.get()
    # api
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city \
          + "&appid=eebf3a58610ac046f08a74c69178e253"
    # requests function to get data
    json_data = requests.get(api).json()
    # Currently status
    condition = json_data['weather'][0]['main']
    # Currently temp
    temp = int(json_data['main']['temp'] - 273.15)
    # Minimum Temperature
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    # Maximum temperature
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    # pressure
    pressure = json_data['main']['pressure']
    # speed of wind
    wind = json_data['wind']['speed']

    # Display and the consequence
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max temp: " + str(max_temp) + "°C" +\
                 "\n" + "Min temp: " + str(min_temp) + "°C" + "\n" + \
                 "preesure: " + str(pressure) + "mb" + "\n" + "wind: " \
                 + str(wind) + "m/s"
    label1.config(text=final_info)
    label2.config(text=final_data)


# define the size of label1 and label 2
f = ("poppins", 15, 'bold')
t = ("poppins", 25, "bold")
# Entry
textfield = Entry(window, text="", font=1)
textfield.pack(pady=20)
textfield.place(x=377, y=100)
textfield.focus()
textfield.bind("<Return>", getweather)

# Display and position it should be
label1 = Label(window, font=t)
label1.pack()
label1.place(x=377, y=120)
label2 = Label(window, font=f)
label2.pack()
label2.place(x=377, y=200)


# converter
# define convert function(logic)
def convert():
    temp_celsius = celsius_value.get()
    if (temp_celsius.replace('.', '', 1).isdigit()):
        error_msg.grid_forget()
        # logic
        temp_fahrenheit = (float(temp_celsius) * 9 / 5) + 32
        # display
        output_fahrenheit.config(text='Temperature in Fahrenheit : ' +
                                      str(temp_fahrenheit) + "°F")
    else:
        error_msg.grid(row=1, column=1)


# Displaying heading inside window
description = Label(text='Celsius -> Fahrenheit',
                    font=font.Font(size=20), fg="grey")
description.place(x=0, y=0)
# for another part include entry,text, button
frame = Frame(window)
frame.pack(pady=20)
frame.place(x=0, y=50)
# Text
message_one = Label(frame, text='Enter Temperature in Celsius : ',
                    font=font.Font(size=10))
message_one.grid(row=0, column=0)
# Entry
celsius_value = Entry(frame)
celsius_value.grid(row=0, column=1)

# To Display Error Message
error_msg = Label(frame, text='Please enter valid input...',
                  font=font.Font(size=8), fg='red')
# To Display the Output
output_fahrenheit = Label(frame, font=font.Font(size=12))
output_fahrenheit.grid(row=2, column=0, columnspan=2, pady=10)
# Submit Button(convert)
submit_btn = Button(frame, text='Convert', width=30, fg="black",
                    bg="light green", bd=0, padx=20, pady=10,
                    command=convert)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)


# Clock Widget
def time():
    string = strftime("%H: %M :%S %p")
    label.config(text=string)
    label.after(1000, time)


# the colour and text size
label = Label(window, font=("clock", 30), background="black",
              foreground="grey")
time()
label.place(x=377, y=0)  # Position

tip = Label(window, text="City name: ", font=("bold", 20), fg="black")
tip.place(x=377, y=55)


# Display
window.mainloop()
