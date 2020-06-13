from tkinter import *
from tkinter import ttk
import random
from bubble_sort import BSort
from merge_sort import mergeSort
from quick_sort import quickSort

root = Tk()
root.title("Sorting Algoritm Visualizer")
root.maxsize(900, 600)
root.config(bg = 'black')

#variables
selected_alg = StringVar()

# frame / base layout
UI_Frame = Frame(root, width=600, height=200, bg = 'grey')
UI_Frame.grid(row=0, column=0, padx=10,pady=5)

canvas= Canvas(root, width=600, height = 380, bg='black')
canvas.grid(row=1,column=0,padx=10,pady=5)

#User interface area
#Row[0]
Label(UI_Frame, text="Algoritm: ", bg='grey').grid(row=0,column=0,padx=5, pady=5,sticky = W)
algMenu = ttk.Combobox(UI_Frame, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort', 'Quick Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_Frame, from_=0.0, to = 2.0, length = 200, digits = 2, resolution = 0.2, orient=HORIZONTAL, label="Select speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(UI_Frame, from_= 3, to = 25, resolution = 1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0,padx=5,pady=5)

minEntry = Scale(UI_Frame, from_=0, to = 10, resolution = 1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1,padx=5,pady=5)

maxEntry = Scale(UI_Frame, from_=10, to = 100, resolution = 1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2,padx=5,pady=5)

class App:
    def __init__(self):
        self.data = []

    def drawData(self, colorArray, data = []):
        canvas.delete("all")
        c_height = 380
        c_width = 600
        x_width = c_width/(len(self.data)+1)
        offset = 30
        spacing = 10
        normalizedData = [ i / (max(self.data)) for i in self.data]
        for i, height in enumerate(normalizedData):
            #top left
            x0 = i * x_width + offset + spacing
            y0 = c_height - height *340

            #bottom right
            x1 = (i+1) * x_width + offset
            y1 = c_height

            canvas.create_rectangle(x0,y0,x1,y1, fill=colorArray[i])
            canvas.create_text(x0+2, y0, anchor=SW, text = str(self.data[i]), fill = 'white')
            
        root.update_idletasks()


    def Generate(self):
        minVal = int(minEntry.get())
        maxVal = int(maxEntry.get())
        size = int(sizeEntry.get())

        if minVal > maxVal: minVal, maxVal = maxVal, minVal
        self.data = []
        for _ in range(size):
            self.data.append(random.randrange(minVal, maxVal+1))
        self.drawData(['yellow' for x in range(len(self.data))])

    def StartAlgorithm(self):
        if not self.data: return

        if algMenu.get() == 'Quick Sort':
            quickSort(self.data, 0, len(self.data)-1, self.drawData, speedScale.get())
        
        elif algMenu.get() == 'Bubble Sort':
            BSort.bubbleSort(self.data, self.drawData, speedScale.get())

        elif algMenu.get() == 'Merge Sort':
            mergeSort(self.data, self.drawData, speedScale.get())
        
        drawData(['green' for x in range(len(self.data))])

my_app = App()

start = Button(UI_Frame, text="Start", command=my_app.StartAlgorithm, bg='red').grid(row=0,column=3,padx=5,pady=5)

generate = Button(UI_Frame, text="Generate", command=my_app.Generate, bg='white').grid(row=1,column=3,padx=5,pady=5)

root.mainloop()