import tkinter as tk
root = tk.Tk()



def startGrid():
    coordx = 0
    
    coordy = 0
    for j in range(3):
        square = tk.Button(root,text="",width=10,height=5,  activebackground="yellow", 
                activeforeground="red")
        square.pack(padx=200, pady=20)
        
    coordx = 200
    for j in range(3):
        square = tk.Button(root,text="",width=10,height=5,  activebackground="blue", 
                activeforeground="red")
        square.pack(padx=200, pady=20)
        square.place(x=coordx, y = coordy)
    #square.grid(row=i, column=j)
    #square = tk.Button(root)
startGrid()

root.mainloop()