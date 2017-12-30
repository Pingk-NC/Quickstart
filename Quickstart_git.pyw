#! Python 3.6

import tkinter as tk
import subprocess
from os import popen
from time import sleep
from re import match

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('Quickstart.py')
        self.pack(fill=tk.BOTH, expand=True)

        quitbutton = tk.Button(self, text='Quit', width=10, command=self.exit_negative)
        quitbutton.grid(row=0, column=1)

        gobutton = tk.Button(self, text='Begin', width=10, command=self.exit_positive)
        gobutton.grid(row=0, column=0)

    def exit_negative(self):
        global result
        result = False
        self.master.quit()

    def exit_positive(self):
        global result
        result = True
        self.master.quit()

def launch_apps():
    # Setting up subprocess.Popen so apps open as minimised
    MINIMISE = 6
    info = subprocess.STARTUPINFO()
    info.dwFlags = subprocess.STARTF_USESHOWWINDOW
    info.wSHOWWINDOW = MINIMISE

    exe_list = []
    raw_list = popen('tasklist').read().strip().split('\n') # Get the list of processes

    # Put all the app.exe in exe_list
    for item in raw_list:
        item = match('(\w+\.\w{3})', item)
        if item:
            exe_list.append(item.group(1))

    if 'Viber.exe' not in exe_list:
        viber = subprocess.Popen('start /min C:\\Users\\XXXXXX\\AppData\\Local\\Viber\\Viber.exe', shell=True, startupinfo=info)
        sleep(5)
    if 'GalaxyClient.exe' not in exe_list:
        galaxy = subprocess.Popen('start /min C:\\\"Program Files (x86)\"\\\"GOG Galaxy\"\\GalaxyClient.exe', shell=True, startupinfo=info)
        sleep(5)
    if 'Discord.exe' not in exe_list:
        discord = subprocess.Popen('start /min C:\\Users\\XXXXXX\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe', shell=True, startupinfo=info)
        sleep(5)
    if 'Steam.exe' not in exe_list:
        steam = subprocess.Popen('start /min C:\\\"Program Files (x86)\"\\Steam\\Steam.exe', shell=True, startupinfo=info)
        sleep(5)
    if 'MusicManager.exe' not in exe_list:
        gmusic = subprocess.Popen('start /min C:\\Users\\XXXXXX\\AppData\\Local\\Programs\\Google\\MusicManager\\MusicManager.exe', shell=True, startupinfo=info)
        sleep(5)
    if 'LCore.exe' not in exe_list:
        logitech = subprocess.Popen('start /min C:\\\"Program Files\"\\\"Logitech Gaming Software\"\\LCore.exe', shell=True, startupinfo=info)

    return True

def main():
    root = tk.Tk()

    window_x = 160
    window_y = 25
    centre_x = (1920-window_x)/2
    centre_y = (1080-window_y)/2

    root.geometry('%dx%d+%d+%d' % (window_x, window_y, centre_x, centre_y))
    root.lift()

    app = Window(root)

    root.mainloop()

    # Can put more code down here and it will be executed
    if result:
        launch_apps()
    else:
        return(None)

main()
