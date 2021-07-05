import requests
from tkinter import messagebox

url = "http://www.kite.com"

timeout = 5.
try:
    request = requests.get(url, timeout=timeout)  # link to url testing
    exec(open('Content.py').read())  # open the file if network works
except (requests.ConnectionError, requests.Timeout) as exception:
    messagebox.showinfo("Error", "Please check your network connection")
