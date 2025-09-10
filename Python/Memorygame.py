import tkinter as tk
import random as r
import time
root = tk.Tk()
root.geometry("270x350")

grid = []
buttons = {}
sequence = []
insequence = []
game = True
buttons = []
counter = 3
stop = 0.5

nextbutton = tk.Button(root,text="Next",width=10,height=2,  activebackground="yellow", 
                activeforeground="red",command = lambda: nextlevel()) #displaying in the grid
nextbutton.place(relx=0.5, rely=0.8, anchor='center')
submit = tk.Button(root,text="Submit",width=10,height=2,  activebackground="yellow", 
                activeforeground="red",command = lambda: checkSeq(counter)) #displaying in the grid
submit.place(relx=0.5, rely=0.9, anchor='center')


start = True
for i in range(0,9):
    grid.append(0)





def paintButton(index):
    buttons[index].config(bg = "red")
    root.update()
    time.sleep(stop)
    buttons[index].config(bg = "SystemButtonFace")


def nextlevel():
    root.configure(bg="SystemButtonFace")
    global counter
    sequence.clear()
    insequence.clear()
    for each in buttons:
        each.config(bg = "SystemButtonFace")
    for i in range(counter):
        while True:
            number = r.randint(0,8)
            if number not in sequence:
                sequence.append(number)
                print(sequence)
                break
    for each in sequence:
        paintButton(each)
    counter +=1
    #buttons[0].config(bg = "red")
    #print(sequence)
    return sequence

def checkSeq(count):
    if insequence == sequence:
        root.configure(bg="green")
       
        print("Level complete")
        
    else:
        print("Unforternutly you did mistake")
    print(sequence)  

def makeOn(position, start,finished):
    print(f"Added {position}")
    if start == False and finished == True:
        if grid[position] != 1:
            #sequence.append(position)
            grid[position] = 1
            print(f"changed {position}")
            insequence.append(position)
            #print(sequence)
            #print(grid)
        elif grid[position] == 1:
            insequence.append(position)
            grid[position] = 0
            #print(f"changed {position}")
            #print(sequence)
            #print(grid)
    #print(grid)
    #print(insequence)
    print("button was pressed")



def print1():
    print("123")


def startGrid():
    start = True
    finished = False
    c = 0 #variable for column
    r= 0 #veriable for row
    counter = 0
    '''
    for j in range(0,9):
        print(j)
        square = tk.Button(root,text="",width=10,height=5,  activebackground="yellow", 
                activeforeground="red",command = lambda: makeOn(j, start, finished)).grid(column = c, row = r, padx=5) #displaying in the grid
        c +=1
  
        start = False
        if c % 3==0: #if column is divisvle by 3, therefore we need to switch the row
            c = 0
            r +=1
'''

    square = tk.Button(root,text="",width=10,height=5,  activebackground="yellow", 
                activeforeground="red",command = lambda: makeOn(0, start, finished))
    
    square.grid(column = 0, row = 0, padx=5) #displaying in the grid
    buttons.append(square)

    square = tk.Button(root,text="",width=10,height=5,  activebackground="yellow", 
                activeforeground="red",command = lambda: makeOn(1, start, finished))
    
    square.grid(column = 1, row = 0, padx=5) #displaying in the grid
    buttons.append(square)
 
    square = tk.Button(root,text="",width=10,height=5,  activebackground="yellow", 
                activeforeground="red",command = lambda: makeOn(2, start, finished))
    
    square.grid(column = 2, row = 0, padx=5) #displaying in the grid
    buttons.append(square)

   

    square = tk.Button(root,text="",width=10,height=5,  activebackground="yellow", 
                activeforeground="red",command = lambda: makeOn(3, start, finished))
    

    square.grid(column = 0, row = 1, padx=5) #displaying in the grid
    buttons.append(square)
 
    square = tk.Button(root,text="",width=10,height=5,  activebackground="yellow", 
                activeforeground="red",command = lambda: makeOn(4, start, finished))
    
    square.grid(column = 1, row = 1, padx=5) #displaying in the grid
    buttons.append(square)

    square = tk.Button(root,text="",width=10,height=5,  activebackground="yellow", 
                activeforeground="red",command = lambda: makeOn(5, start, finished))
    
    square.grid(column = 2, row = 1, padx=5) #displaying in the grid
    buttons.append(square)
 


    square = tk.Button(root,text="",width=10,height=5,  activebackground="yellow", 
                activeforeground="red",command = lambda: makeOn(6, start, finished))
    
    square.grid(column = 0, row = 2, padx=5) #displaying in the grid
    buttons.append(square)

    square = tk.Button(root,text="",width=10,height=5,  activebackground="yellow", 
                activeforeground="red",command = lambda: makeOn(7, start, finished))
    
    square.grid(column = 1, row = 2, padx=5) #displaying in the grid
    buttons.append(square)

    square = tk.Button(root,text="",width=10,height=5,  activebackground="yellow", 
                activeforeground="red",command = lambda: makeOn(8, start, finished))
    
    square.grid(column = 2, row = 2, padx=5) #displaying in the grid
    buttons.append(square)











    #square.config(background = "red")
    #buttons.append(square)
    
    start = False
    finished = True
    #print(buttons[0])
    #buttons[0].activebackground = "yellow"

    print(buttons[8])
startGrid()

     



root.mainloop()
