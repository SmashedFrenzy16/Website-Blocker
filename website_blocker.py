from tkinter import *
from tkinter import ttk
import platform
import sv_ttk
import sys
import pywinstyles
import darkdetect

"""
Hosts Paths On Windows, Mac & Linux:

Windows: C:\Windows\System32\drivers\etc\hosts

Mac & Linux: /etc/hosts
"""

h_path = "ENTER HOSTS FILE PATH HERE"

redirect = "127.0.0.1"

website_arr = []

def web_add():

    website_arr.append(website_entry.get())

    print(website_arr)

def block():

    path = open(h_path, "r+")

    path_r = path.read()

    for website in website_arr:

        path.write(f"{redirect} {website}\n")
    
def unblock():
    
    with open(h_path, "r+") as path:

        path_r = path.readlines()

        path.seek(0)

        for line in path_r:
        
            if not any(website in line for website in website_arr):

                path.write(line)
        
        path.truncate()

root = Tk()

root.title("Website Blocker by @SmashedFrenzy16")

title_label = ttk.Label(root, text="Website Blocker", font=("Arial", 48))
title_label.pack()

blank_label = ttk.Label(root, text="").pack()

website_entry = ttk.Entry(root, width=100)
website_entry.insert(0, "Enter website URL here")
website_entry.pack()

add_website = ttk.Button(root, text="Add", command=web_add)
add_website.pack()

blank_label2 = ttk.Label(root, text="").pack()

block_button = ttk.Button(root, text="Block", command=block)
block_button.pack(side=LEFT)

unblock_button = ttk.Button(root, text="Unblock", command=unblock)
unblock_button.pack(side=RIGHT)

sv_ttk.set_theme(darkdetect.theme())

if platform.system() == "Windows":

    if sys.getwindowsversion().major == 10 and sys.getwindowsversion().build >= 22000:

        if sv_ttk.get_theme() == "dark":

            pywinstyles.change_header_color(root, "#000000")

root.mainloop()
