from contextlib import nullcontext
from tkinter import Button
import PySimpleGUI as sg
import graphs as g



def start():
    row = 0
    col = 0
    percent = 0
    graph = nullcontext
                

    layout = [  [sg.Text("Cave generator")], 
                [sg.Input(), sg.Input(), sg.Input(), sg.Button('Add')], 
                [sg.Button('Make a random graph')],
                [sg.Button('Modify graph')],
                [sg.Button('Get biggest cave')]]
    

    # Create the window
    window = sg.Window("Demo", layout)
    # Create an event loop
    while True:
        event, values = window.read()
       
        if event == 'Make a random graph':
            print("uuu")
            graph = g.make_graph(row, col, percent)
            g.print_graph(row, col, graph)

           
        if event == 'Add':
            row = int(values[0])
            col = int(values[1])
            percent = int(values[2])

        if event == 'Modify graph':
            print("")
            graph = g.modify_graph(row, col, graph)
            g.print_graph(row, col, graph)

        if event == 'Get biggest cave':
            print("")
            g.search(row, col, graph)
            g.print_graph(row, col, graph)

        if event in (sg.WIN_CLOSED, 'Quit'):
            break
        
    window.close()
    
