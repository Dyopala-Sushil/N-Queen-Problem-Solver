#N-Queen Problem Solver
from tkinter import *
import numpy as np
import random

root = Tk()
root.geometry("500x500")
root.title("N-Queen Problem Solver")
sol =[]
sol_num = 0


def get_dimension():
    try:
        global N, count, m
        count=0

        dimension_btn['state']=NORMAL

        N=int(entry.get())

        m = np.zeros((N,N))
        solution(N,m)


        solution_count='Possible Solution = '+str(count)
        count_label=Label(top_frame,text=solution_count)
        count_label.grid(row=0,column=3,padx=30)


        generate_board(N)   


        # entry.delete(0,END)
        dimension_btn['state']=DISABLED
        
    except:
        print('Something Went Wrong!')


def generate_board(N):
    next_solution['state']=NORMAL
    global sol_num
    if N<4:
        next_solution['state']=DISABLED
        label=Label(bottom_frame,text="Oops! Dimension must be greater than 3",bg='black',fg='white')
        label.grid()

    else:
        if sol_num==(count-1):
            next_solution['state']=DISABLED

        for i in range(N):
            for j in range(N):
                if sol[sol_num][i][j]==1:
                    val='Q'
                else:
                    val= ' '
               
                label=Label(bottom_frame,text=val,bg=col(i,j),fg='red',width=4,height=2)
                label.grid(row=i,column=j)
        sol_num_label=Label(last_frame,text="Solution Number : "+str(sol_num+1))    
        sol_num_label.grid(row=0,column=1,padx=30)   
        sol_num+=1

def col(i,j):
    if (i+j)%2==0:
        return 'white'
    return 'black'

def store_result(mat):
        global sol
        sol.append(mat)
        # print(sol)


def solution(N,m,col=0):   
    if col>=N:
        global count
        count+=1
        mat=m.copy()
        store_result(mat)
        return False

    for i in range(N):
        if isSafe(m,i,col):
            m[i][col] = 1
            solution(N,m,col+1)
        m[i][col]=0
    return False

def isSafe(m,row,col): 
  
    # Check this row on left side 
    for i in range(col): 
        if m[row][i] == 1: 
            return False
  
    # Check upper diagonal on left side 
    for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
        if m[i][j] == 1: 
            return False
  
    # Check lower diagonal on left side 
    for i, j in zip(range(row, N, 1),  
                    range(col, -1, -1)): 
        if m[i][j] == 1: 
            return False
  
    return True
#------------------------------------------------GUI FRAMES-----------------------------------------------------------------------------

top_frame = Frame(root)
top_frame.grid(padx=30,pady=10)

global bottom_frame
bottom_frame= Frame(root,height=350,width=350)
bottom_frame.grid()

last_frame = Frame(root)
last_frame.grid(pady=20)

#------------------------WIDGETS-----------------------------------

entry=Entry(top_frame,width=10,borderwidth=3)
entry.grid(row=0,column=1)
entry.insert(0,4)

dimension_btn=Button(top_frame,text='Set Dimension',command=get_dimension)
dimension_btn.grid(row=0,column=0,padx=5)

next_solution= Button(last_frame,text="Next Solution",command=lambda:generate_board(N))
next_solution.grid(row=0,column=0,padx=20)
next_solution['state']=DISABLED


exit_btn= Button(last_frame,text = "Exit",command = root.quit)
exit_btn.grid(row=0,column=2,padx=50)


root.mainloop()
