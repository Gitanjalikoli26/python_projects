from tkinter import *

def calculator(operator):
    try:
        num1 = float(num1_input.get())  # Get value from entry
        num2 = float(num2_input.get())
        
        if operator=='+':
            result=num1+num2
        elif operator=='-':
            result=num1-num2
        elif operator=='*':
            result=num1*num2
        elif operator=='/':
            if num2!=0:
                result=num1/num2
            else:
                result_label.config(text="error : Division by Zero")
                
        result_label.config(text=f'Results:{result}')
            
        
        
    except ValueError:
        result_label.config(text="Please provide the valid numbers!!")
        



root=Tk()

root.title("simple calculator")

root.geometry("400x400")
root.config(background='gray')

num1_label=Label(root,text="Provide the Number 1:",fg='white',background='black')
num1_label.pack(pady=(20,20))
num1_label.config(font=('verdana',15))


num1_input=Entry(root,width=50)
num1_input.pack(ipady=6,pady=(1,15))

num2_label=Label(root,text="Provide the Number 2:",fg='white',background='black')
num2_label.pack(pady=(20,20))
num2_label.config(font=('verdana',15))


num2_input=Entry(root,width=50)
num2_input.pack(ipady=6,pady=(1,15))

result_label=Label(root,text="")
result_label.pack(pady=(10,20))


# buttons:
button_frame=Frame(root,bg="#222")
button_frame.pack()

Button(button_frame,text="+",width=10,bg='skyblue',fg='black',
       command=lambda:calculator("+")).grid(row=0,column=0,padx=10,pady=5)

Button(button_frame,text="-",width=10,bg='skyblue',fg='black',
       command=lambda:calculator("-")).grid(row=0,column=1,padx=10,pady=5)

Button(button_frame,text="*",width=10,bg='skyblue',fg='black',
       command=lambda:calculator("*")).grid(row=1,column=0,padx=10,pady=5)

Button(button_frame,text="/",width=10,bg='skyblue',fg='black',
       command=lambda:calculator("/")).grid(row=1,column=1,padx=10,pady=5)



root.mainloop()


