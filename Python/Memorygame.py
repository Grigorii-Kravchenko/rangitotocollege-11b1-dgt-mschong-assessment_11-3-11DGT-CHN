import tkinter as tk
root = tk.Tk()

grid = []

start = True
for i in range(0,9):
    grid.append(0)


sequence = []


def makeOn(position, start,finished):
    print(start)
    print(finished)
    if start == False and finished == True:
        if grid[position] != 1:
            sequence.append(position)
            grid[position] = 1
            print(f"changed {position}")
            print(sequence)
    print(grid)
    print("button was pressed")




def startGrid():
    start = True
    finished = False
    c = 0 #variable for column
    r= 0 #veriable for row
    counter = 0
    for j in range(0,9):
        
        square = tk.Button(root,text="",width=10,height=5,  activebackground="yellow", 
                activeforeground="red",command = makeOn(counter, start, finished)).grid(column = c, row = r, padx=5,) #displaying in the grid
        c +=1
        counter+=1
        start = False
        if c % 3==0: #if column is divisvle by 3, therefore we need to switch the row
            c = 0
            r +=1 
    #square.grid(row=i, column=j)
    #square = tk.Button(root)
    finished = True
startGrid()

root.mainloop()
