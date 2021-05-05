import numpy as np
import pandas as pd
import folium
import tkinter as tk
from   tkinter import filedialog #for use in saving file path
#m = folium.Map(location=[45.5236, -122.6750])

def shortpath():
    print("shortpath")




def plotall():
    print('Plotting All')
    print(plotenable.get())

if __name__ == "__main__":
    root = tk.Tk() #creates main canvas
    path = ""
    #sets up canvas size
    canvas = tk.Canvas(root, height = 600, width=600, bg="#5241f0")
    canvas.pack()

    #creates button bar
    frame = tk.Frame(root, bg= "white")
    frame.place(relwidth=0.8,relheight=.8,relx=0.1,rely=0.1)

    #create button for run algorithm
    runalg = tk.Button(root, text = "Find Shortest Flight", padx =10 , pady = 10, fg ="white",bg = "black", command = shortpath)
    runalg.pack()
    #create button to plot all points
    plotenable = tk.IntVar()
    allplot = tk.Checkbutton(root,text = "Plot All Airports", padx = 10, pady = 10,  fg ="black",bg = "white", variable = plotenable , onvalue = 1, offvalue = 0, command = plotall)
    allplot.pack()

    root.mainloop()