import pandas as pd
import folium
import tkinter as tk
from   tkinter import filedialog #for use in saving file path
from tkinter import *
#m = folium.Map(location=[45.5236, -122.6750])





class Interface(tk.Tk):

    def __init__(self, *args, **kwargs):
        #creates initial window
        tk.Tk.__init__(self, *args, **kwargs)
        #creates container for frames
        container = tk.Frame(self, background="#5241f0")
        container.pack(fill="both", expand=True)
        #creates objects forr button and main screen
        bman = ButtonManager(container, controller=self)
        main = Main(container, controller=self)
        #sets boundaries for each frame
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=4)
        container.grid_rowconfigure(0, weight=1)
        #sets grid for each frame
        bman.grid(row=0, column=0, sticky="nsew")
        main.grid(row=0, column=1, sticky="nsew")


class ButtonManager(tk.Frame):
    def __init__(self, parent, controller):
        #create button frame
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(background = 'green')
        #creates two sub frames for labels and buttons
        lblFrame = LabelFrame(self, controller)
        btnFrame = ButtonFrame(self, controller)
        #orders the frames
        lblFrame.pack(side="top", fill="x", expand=False)
        btnFrame.pack(side="top", fill="both", expand=True)

class Main(tk.Frame):
    #main screen's code
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#5241f0")
    #main code for graphing data
    def graph(checkbox):
        print("shortpath")
        print("Boxval: %d" % (checkbox.get()))




class LabelFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="blue")

        lblTitleBar = tk.Label(self, text = 'Shortest Path Optimization', background = 'grey', font = ("Arial", 14, ))
        lblTextBar = tk.Label(self, text = 'Enter Airport Codes Below', background = 'grey', font = ("Arial", 10, ))

        lblTitleBar.pack(side="top", fill="x")
        lblTextBar.pack(side="top", fill="x")



class ButtonFrame(tk.Frame):
    #creates and manages buttons
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="white")

        for row in range(7):
            self.grid_rowconfigure(row, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)

        #create input text boxes
        strlbl = tk.Label(self, text = "Starting Airport Code", bg = "white")
        strlbl.pack()
        strtloc = tk.StringVar()
        startprt = tk.Entry(self, bd = 5, textvariable = strtloc)
        startprt.pack()
        endlbl = tk.Label(self, text = "Ending Airport Code", bg = "white")
        endlbl.pack()
        endloc = tk.StringVar()
        endprt = tk.Entry(self, bd = 5 , textvariable = endloc)
        endprt.pack()

        #create  to plot all points
        plotenable = tk.IntVar()
        allplot = tk.Checkbutton(self,text = "Plot All Airports", padx = 10, pady = 10,  fg ="black",bg = "white", command = lambda: plotenable.set(1) if plotenable.get() == 0 else plotenable.set(0))
        allplot.pack()
        #create button for run algorithm, when pressed main's graph function is called
        runalg = tk.Button(self, text = "Find Shortest Flight", padx = 10 , pady = 10, fg ="black",bg = "white",bd=5, command = lambda:Main.graph(plotenable))
        runalg.pack(pady = 8)

       


interface = Interface()
interface.title("Flight Planner")
interface.minsize(800, 480)
interface.mainloop()