# Graphical user interface CALUCLATOR
# Import tkinter which provides GUI
import tkinter as tk


# Main window
window = tk.Tk()
window.title('Calculator')
window.geometry('380x610')
window.resizable(False,False)


#Developer
maintext = tk.Label(window,text='Designed by Hadi Mahar', font=('Arial',20,'bold'), bg='black',fg='white')
maintext.place(x=10, y=7 , width=360 , height=100)

#Clicking function
def click(number):
    start = result.cget('text')
    if start == '0':
        result.config(text=number)
    else:
        result.config(text = start + number)


#Backspace button
def backspace():
    current = result.cget('text')
    result.config(text=current[:-1])
    if current[:-1] == '':
        result.config(text='0')


# Calculation functions
def calculate():
    expression = result.cget('text')
    try:
          expression = expression.replace('x','*')
          expression = expression.replace('÷','/') 

          answer = eval(expression)

          result.config(text=str(answer))   
    except ( ValueError , ZeroDivisionError , SyntaxError):
                result.config(text='Error')


def C():
    result.config(text= '0')

# Buttons
box = tk.Frame(window, bg='white', padx=3,pady=3)

buttonC = tk.Button(box,text = 'C', height=4, width=9,fg='white', bg='green',font =('Arial',11,'bold'), command= C)
buttonC.grid(row = 1 ,column=3 ,padx=3, pady=3,)

buttonplus = tk.Button(box,text = '+', height=4, width=9,fg='white', bg='red',font =('Arial',11,'bold'), command= lambda: click('+'))
buttonplus.grid(row = 0 ,column=0 ,padx=3, pady=4,)

buttonsub = tk.Button(box,text = '-', height=4, width=9,fg='white', bg='red', font =('Arial',11,'bold'), command= lambda: click('-'))
buttonsub.grid(row = 0 ,column=1 ,padx=3, pady=3)

buttonmul = tk.Button(box,text = 'x', height=4, width=9,fg='white', bg='red', font =('Arial',11,'bold'), command= lambda: click('x'))
buttonmul.grid(row = 0 ,column=2 ,padx=3, pady=3)

buttondev = tk.Button(box,text = '÷', height=4, width=9,fg='white', bg='red', font =('Arial',11,'bold'), command= lambda: click('÷'))
buttondev.grid(row = 0 ,column=3 ,padx=3, pady=3)

button1 = tk.Button(box,text = '1', height=4, width=9,fg='white', bg='black', font =('Arial',11,'bold'), command= lambda: click('1'))
button1.grid(row = 1 ,column=0 ,padx=3, pady=3)

button2 = tk.Button(box,text = '2', height=4,width=9,fg='white', bg='black', font =('Arial',11,'bold'), command= lambda: click('2'))
button2.grid(row = 1 ,column=1 ,padx=3, pady=3)

button3 = tk.Button(box,text = '3', height=4,width=9,fg='white', bg='black', font =('Arial',11,'bold') , command= lambda: click('3'))
button3.grid(row = 1 ,column=2 ,padx=3, pady=3)

button4 = tk.Button(box,text = '4', height=3,width=9,fg='white', bg='black' , font =('Arial',11,'bold'), command= lambda: click('4'))
button4.grid(row = 2 ,column=0 ,padx=3, pady=3)

button5 = tk.Button(box,text = '5', height=3,width=9,fg='white', bg='black' , font =('Arial',11,'bold'), command= lambda: click('5'))
button5.grid(row = 2 ,column=1 ,padx=3, pady=3)

button6 = tk.Button(box,text = '6', height=3,width=9,fg='white', bg='black' , font =('Arial',11,'bold'), command= lambda: click('6'))
button6.grid(row = 2 ,column=2 ,padx=3, pady=3)

button7 = tk.Button(box,text = '7', height=3,width=9,fg='white', bg='black' , font =('Arial',11,'bold'), command= lambda: click('7'))
button7.grid(row = 3 ,column=0 ,padx=3, pady=3)

button8 = tk.Button(box,text = '8', height=3,width=9,fg='white', bg='black' , font =('Arial',11,'bold'), command= lambda: click('8'))
button8.grid(row = 3 ,column=1 ,padx=3, pady=3)

button9 = tk.Button(box,text = '9', height=3,width=9,fg='white', bg='black' , font =('Arial',11,'bold'), command= lambda: click('9'))
button9.grid(row = 3 ,column=2 ,padx=3, pady=3)

button0 = tk.Button(box,text = '0', height=3,width=19,fg='white', bg='black' , font =('Arial',11,'bold'), command= lambda: click('0'))
button0.grid(row = 4 ,column=0, columnspan=2  ,padx=3, pady=3)

buttonbackspace = tk.Button(box,text = '⌫', height=3,width=9,fg='white', bg='green' , font =('Arial',11,'bold'), command =backspace)
buttonbackspace.grid(row = 2 ,column=3,padx=3, pady=3)

buttonequal = tk.Button(box,text = '=', height=7,width=9,fg='white', bg='green' , font =('Arial',11,'bold'), command = calculate)
buttonequal.grid(row = 3, rowspan=3   ,column=3 ,padx=3, pady=3)

buttondot = tk.Button(box,text = '.', height=3,width=9,fg='white', bg='black' , font =('Arial',11,'bold'), command= lambda: click('.'))
buttondot.grid(row = 4 ,column=2,padx=3, pady=3)

buttons = [ button1 , button2 , button3 , button4 , 
        button5 , button6 , button7 , button8 , 
        button9 , button0 , buttonequal , 
        buttonbackspace , buttonplus , buttonsub , 
        buttonmul , buttondev, buttonC, buttondot ]

box.pack(side='bottom', fill ='x')

# Result box
result = tk.Label(window,text='0', font=('Arial',30,'bold'), bg='white',fg='grey')
result.place(x=8, y=90 , width=362 , height=100)


for col in range(4):
    box.grid_columnconfigure(col, weight=1, uniform='col')

window.mainloop()
