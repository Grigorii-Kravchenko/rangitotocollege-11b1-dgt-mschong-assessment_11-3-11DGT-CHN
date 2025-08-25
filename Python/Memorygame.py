import tkinter as tk
root = tk.Tk()

grid = [[][][]]



def addToGrid(int position):
    grid.append()






def startGrid():

    c = 0 #variable for column
    r= 0 #veriable for row
    for j in range(9):
        square = tk.Button(root,text="",width=10,height=5,  activebackground="yellow", 
                activeforeground="red").grid(column = c, row = r, padx=5) #displaying in the grid
        c +=1

        if c % 3==0: #if column is divisvle by 3, therefore we need to switch the row
            
            r +=1 
    #square.grid(row=i, column=j)
    #square = tk.Button(root)
startGrid()

root.mainloop()