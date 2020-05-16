from tkinter import *
from tkinter import messagebox
from math import *
from random import randint




# To Enter The Data Into Entry Widget
def Entryset(k):
    e.config(fg='blue')
    if(v.get()=='ERROR'):
        e.delete(0,END)
    e.insert(END,k)

# To Evaluate The Result
def Evaluate(k):
    s=v.get()
    try:
        result=eval(s)
        v.set(result)
    except:
        e.config(fg='red')
        v.set("ERROR")


# SIn evaluator
def my_evaluate(s):
    my_list=['sin(','cos(','tan(']
    for i in my_list:
        op=i
        while(op in s):
            t=s.index(op)
            f=t
            t = t + 4
            res = ''
            while (s[t] != ')'):
                res = res + s[t]
                t = t + 1
            if(op=='sin('):
                d = sin(radians(int(res)))
            elif(op=='cos('):
                d = cos(radians(int(res)))
            elif(op=='tan('):
                d = tan(radians(int(res)))
            s=s[0:f]+str(d)+s[f+5+len(res):]
    s = s.replace('sin-1', 'asin')
    s = s.replace('cos-1', 'acos')
    s = s.replace('tan-1', 'atan')
    return s

# Scientific Evaluator
def SEvaluate(k):
    s=v.get()
    try:
        s=my_evaluate(s)
        result=eval(s)
        result=round(result,5)
        v.set(result)
    except:
        e.config(fg='red')
        v.set("ERROR")




# To Clear The Entry Field
def PressAc():
    e.delete(0,END)
# MixButton Function
def Button_Mix():
    s=v.get()
    if(len(s)>0):
        if(s[0]!='-'):
            e.insert(0,'-')
        else:
            e.delete(0)
def fun():
    pass
#craeting fun for Basic window
def Basic_windoow():
    messagebox.showinfo('BASIC WINDOW','The Current Window Is The Basic Window')


########################################## PROGRAMMER CALCULATOR ######################################################
def Programmer():
    w.destroy()
    global e
    global v
    global k

    # FUNCTIONS
    def onesComplement():
        try:
            n=int(v.get())
            number_of_bits = (int)(floor(log(n) / log(2))) + 1;
            ones = ((1 << number_of_bits) - 1) ^ n;
            v.set(str(ones))
        except:
            e.config(fg='red')
            v.set("ERROR")
    def twosComplement():
        pass

    def Binary():
        try:
            n=int(v.get())
            number=bin(n)
            v.set(number[2:])
        except:
            e.config(fg='red')
            v.set("ERROR")
    def clear():
        try:
            s=v.get()
            s=s[0:len(s)-1]
            v.set(s)
        except:
            e.config(fg='red')
            v.set("ERROR")

    w1 = Tk()
    # Creating PRO Calculator
    w1.title("HEY!  ProGrammer")
    w1.geometry("+300+300")
    w1.resizable(width=False, height=False)
    root=Frame(w1)
    v = StringVar()
    e = Entry(root, width=35, textvariable=v, fg='blue')
    e.grid(row=0, column=0, columnspan=7)
    # e.icursor(0)
    w1.propagate(0)



    # Creating Buttons in Row-1
    button1 = Button(root, text="AND", width=5, height=3, fg='blue', command=lambda: Entryset("&")).grid(row=1, column=0)
    button2 = Button(root, text="OR", width=5, height=3, fg='blue', command=lambda: Entryset("|")).grid(row=1, column=1)
    button3 = Button(root, text="7", width=5, height=3, fg='black', command=lambda: Entryset("7")).grid(row=1, column=2)
    button4 = Button(root, text="8", width=5, height=3, fg='black', command=lambda: Entryset("8")).grid(row=1, column=3)
    button5 = Button(root, text="9", width=5, height=3, fg='black', command=lambda: Entryset("9")).grid(row=1, column=4)
    button6 = Button(root, text="AC", width=5, height=3, fg='red', command=PressAc).grid(row=1, column=5)
    button6 = Button(root, text="C", width=5, height=3, fg='red', command=clear).grid(row=1, column=6)

    # Creating Buttons in Row-2
    button1 = Button(root, text="~", width=5, height=3, fg='blue', command=lambda: Entryset("~")).grid(row=2, column=0)
    button2 = Button(root, text="XOR", width=5, height=3, fg='blue', command=lambda: Entryset("^")).grid(row=2, column=1)
    button3 = Button(root, text="4", width=5, height=3, fg='black', command=lambda: Entryset("4")).grid(row=2, column=2)
    button4 = Button(root, text="5", width=5, height=3, fg='black', command=lambda: Entryset("5")).grid(row=2, column=3)
    button5 = Button(root, text="8", width=5, height=3, fg='black', command=lambda: Entryset("8")).grid(row=2, column=4)
    button6 = Button(root, text="2's", width=5, height=3, fg='blue', command=twosComplement).grid(row=2, column=5)
    button6 = Button(root, text="1's", width=5, height=3, fg='blue', command=onesComplement).grid(row=2, column=6)

    # Creating Buttons in Row-3
    button1 = Button(root, text="<<", width=5, height=3, fg='blue', command=lambda: Entryset("<<")).grid(row=3, column=0)
    button2 = Button(root, text=">>", width=5, height=3, fg='blue', command=lambda: Entryset(">>")).grid(row=3, column=1)
    button3 = Button(root, text="1", width=5, height=3, fg='black', command=lambda: Entryset("1")).grid(row=3, column=2)
    button4 = Button(root, text="2", width=5, height=3, fg='black', command=lambda: Entryset("2")).grid(row=3, column=3)
    button5 = Button(root, text="3", width=5, height=3, fg='black', command=lambda: Entryset("3")).grid(row=3, column=4)
    button6 = Button(root, text="/", width=5, height=3, fg='magenta', command=lambda: Entryset("/")).grid(row=3, column=5)
    button6 = Button(root, text="+", width=5, height=3, fg='magenta', command=lambda: Entryset("+")).grid(row=3, column=6)

    # Creating Buttons in Row-4
    #button1 = Button(root, text="X<<Y", width=5, height=3, fg='blue', command=lambda: Entryset("")).grid(row=4, column=0)
    button2 = Button(root, text="B", width=5, height=3, fg='blue', command=Binary).grid(row=4, column=0)
    button3 = Button(root, text="0", width=10, height=3, fg='black', command=lambda: Entryset("0")).grid(row=4, column=1,columnspan=2)
    button4 = Button(root, text="=", width=10, height=3, fg='magenta',command=lambda :Evaluate(k)).grid(row=4, column=3,columnspan=2)

    button6 = Button(root, text="*", width=5, height=3, fg='magenta', command=lambda: Entryset("*")).grid(row=4, column=5)
    button6 = Button(root, text="-", width=5, height=3, fg='magenta', command=lambda: Entryset("-")).grid(row=4, column=6)

    root.grid(row=0,column=0)
    w1.bind("<Return>", Evaluate)
    w1.mainloop()



########################################## Scientific Calculator ######################################################
def Scientific():


    # functions
    def square(p):
        try:
            s = float(v.get())
            result = round(pow(s,p),5)
            v.set(result)
        except:
            e.config(fg='red')
            v.set("ERROR")

    def epowerx(pie):
        try:
            s = float(v.get())
            result = round(pow(pie,s),5)
            v.set(result)
        except:
            e.config(fg='red')
            v.set("ERROR")


    def spower(k):
        try:
            s = float(v.get())
            result = round(pow(s,k),5)
            v.set(result)
        except:
            e.config(fg='red')
            v.set("ERROR")

    def onebyx():
        try:
            s = float(v.get())
            result = round(1/s,5)
            v.set(result)
        except:
            e.config(fg='red')
            v.set("ERROR")

    def my_factorial():
        try:
            s = float(v.get())
            result = factorial(s)
            v.set(result)
        except:
            e.config(fg='red')
            v.set("ERROR")

    def Rand():
        e.delete(0, END)
        v.set(str(randint(1,10000000000)))


    w.destroy()
    global e
    global v
    w1=Tk()

    # Creating Scientific Calculator
    w1.title("Scientific Calculator")
    w1.geometry("+300+300")
    w1.resizable(width=False, height=False)
    root = Frame(w1)
    v = StringVar()
    e = Entry(root, width=45, textvariable=v, fg='blue')
    e.grid(row=0, column=0, columnspan=9)
    # e.icursor(0)
    w1.propagate(0)


    # Creating buttons in Row-1
    buttonac = Button(root, text="(", width=5, height=3, fg='blue', command=lambda: Entryset("(")).grid(row=1, column=0)
    button1_mix = Button(root, text=")", width=5, height=3, fg='blue', command=lambda: Entryset(")")).grid(row=1, column=1)
    button_modulo = Button(root, text="2√x", width=5, height=3, fg='blue', command=lambda:spower(1/2)).grid(row=1,column=2)
    button_division = Button(root, text="3√x", width=5, height=3, fg='blue', command=lambda:spower(1/3)).grid(row=1,column=3)
    buttoncosi=Button(root, text="log10", width=5, height=3, fg='blue', command=lambda: Entryset("log10(")).grid(row=1,column=4)
    buttonac = Button(root, text="AC", width=5, height=3, fg='red', command=PressAc).grid(row=1, column=5)
    button1_mix = Button(root, text="+/-", width=5, height=3, fg='magenta', command=Button_Mix).grid(row=1, column=6)
    button_modulo = Button(root, text="%", width=5, height=3, fg='magenta', command=lambda: Entryset("%")).grid(row=1,
                                                                                                             column=7)
    button_division = Button(root, text="/", width=5, height=3, fg='magenta', command=lambda: Entryset("/")).grid(row=1,
                                                                                                               column=8)

    # Creating buttons in Row-2
    button1 = Button(root, text="x^2", width=5,fg='blue', height=3, command=lambda :square(2)).grid(row=2, column=0)
    button2 = Button(root, text="x^3", width=5,fg='blue', height=3, command=lambda :square(3)).grid(row=2, column=1)
    button3 = Button(root, text="e^x", width=5,fg='blue', height=3, command=lambda :epowerx(2.718281828459045)).grid(row=2, column=2)
    button_plus = Button(root, text="10^x", width=5, height=3, fg='blue', command=lambda :epowerx(10)).grid(row=2,column=3)
    button_plus = Button(root, text="2^x", width=5, height=3, fg='blue', command=lambda :epowerx(2)).grid(row=2,column=4)
    button1 = Button(root, text="1", width=5, height=3, command=lambda: Entryset("1")).grid(row=2, column=5)
    button2 = Button(root, text="2", width=5, height=3, command=lambda: Entryset("2")).grid(row=2, column=6)
    button3 = Button(root, text="3", width=5, height=3, command=lambda: Entryset("3")).grid(row=2, column=7)
    button_plus = Button(root, text="+", width=5, height=3, fg='magenta', command=lambda: Entryset("+")).grid(row=2,
                                                                                                           column=8)
    # Creating buttons in Row-3
    button4 = Button(root, text="1/x", width=5, height=3,fg='blue', command=onebyx).grid(row=3, column=0)
    button5 = Button(root, text="sin-1", width=5, height=3,fg='blue', command=lambda: Entryset("sin-1(")).grid(row=3, column=1)
    button6 = Button(root, text="cos-1", width=5, height=3,fg='blue', command=lambda: Entryset("cos-1(")).grid(row=3, column=2)
    button_minus = Button(root, text="tan-1", width=5, height=3, fg='blue', command=lambda: Entryset("tan-1(")).grid(row=3,column=3)
    button_minus = Button(root, text="log", width=5, height=3, fg='blue', command=lambda: Entryset("log(")).grid(row=3, column=4)
    button4 = Button(root, text="4", width=5, height=3, command=lambda: Entryset("4")).grid(row=3, column=5)
    button5 = Button(root, text="5", width=5, height=3, command=lambda: Entryset("5")).grid(row=3, column=6)
    button6 = Button(root, text="6", width=5, height=3, command=lambda: Entryset("6")).grid(row=3, column=7)
    button_minus = Button(root, text="-", width=5, height=3, fg='magenta', command=lambda: Entryset("-")).grid(row=3,
                                                                                                            column=8)
    # Creating buttons in Row-4
    button7 = Button(root, text="x!", width=5, height=3,fg='blue', command=my_factorial).grid(row=4, column=0)
    button8 = Button(root, text="sin", width=5, height=3,fg='blue', command=lambda: Entryset("sin(")).grid(row=4, column=1)
    button9 = Button(root, text="cos", width=5, height=3,fg='blue', command=lambda: Entryset("cos(")).grid(row=4, column=2)
    button_multiply = Button(root, text="tan", width=5, height=3, fg='blue', command=lambda: Entryset("tan(")).grid(row=4,
                                                                                                               column=3)
    button_multiply = Button(root, text="e", width=5, height=3, fg='blue', command=lambda: Entryset("2.71828182")).grid(row=4,
                                                                                                                 column=4)
    button7 = Button(root, text="7", width=5, height=3, command=lambda: Entryset("7")).grid(row=4, column=5)
    button8 = Button(root, text="8", width=5, height=3, command=lambda: Entryset("8")).grid(row=4, column=6)
    button9 = Button(root, text="9", width=5, height=3, command=lambda: Entryset("9")).grid(row=4, column=7)
    button_multiply = Button(root, text="*", width=5, height=3, fg='magenta', command=lambda: Entryset("*")).grid(row=4,
                                                                                                               column=8)
    # Creating buttons in Row-5
    button7 = Button(root, text="Rand", width=5, height=3,fg='blue', command=Rand).grid(row=5, column=0)
    button8 = Button(root, text="sinh", width=5, height=3,fg='blue', command=lambda: Entryset("sinh(")).grid(row=5, column=1)
    button9 = Button(root, text="cosh", width=5, height=3,fg='blue', command=lambda: Entryset("cosh")).grid(row=5, column=2)
    button_multiply = Button(root, text="tanh", width=5, height=3, fg='blue', command=lambda: Entryset("tanh")).grid(row=5,
                                                                                                                 column=3)
    button_multiply = Button(root, text="π", width=5, height=3, fg='blue',command=lambda: Entryset("3.1415926")).grid(row=5,
                                                                                                               column=4)
    button0 = Button(root, text="0", width=10, height=3, command=lambda: Entryset("0")).grid(row=5, column=5,
                                                                                             columnspan=2)
    button_dot = Button(root, text=".", width=5, height=3, fg='magenta', command=lambda: Entryset(".")).grid(row=5,
                                                                                                          column=7)
    k = None
    button_equal = Button(root, text="=", width=5, height=3, fg='green', command=lambda: SEvaluate(k)).grid(row=5,
                                                                                                           column=8)

    # Binding Enter Button
    w1.bind("<Return>", SEvaluate)
    root.grid(row=0, column=0)
    w1.mainloop()




######################################### MAIN CALCULATOR #############################################################
#creating a Main Window
w=Tk()


# Creating a menu

main_menu=Menu(w)
w.config(menu=main_menu)
submenu1=Menu(main_menu)
submenu2=Menu(main_menu)
main_menu.add_cascade(label='View',menu=submenu1)
submenu1.add_command(label='Basic',command=Basic_windoow)
submenu1.add_command(label='Scientific',command=Scientific)
submenu1.add_command(label='Programmar',command=Programmer)
main_menu.add_cascade(label='Options',menu=submenu2)
submenu2.add_command(label='Help',command=None)
submenu2.add_command(label='Exit',command=quit)


#Creating Normal Calculator
w.title("Calculator")
w.geometry("+300+300")
w.resizable(width=False,height=False)
root=Frame(w)
v=StringVar()
e=Entry(root,width=20,textvariable=v,fg='blue')
e.grid(row=0,column=0,columnspan=4)
#e.icursor(0)
w.propagate(0)

# Creating buttons in Row-1
buttonac=Button(root,text="AC",width=5,height=3,fg='red',command=PressAc).grid(row=1,column=0)
button1_mix=Button(root,text="+/-",width=5,height=3,fg='blue',command=Button_Mix).grid(row=1,column=1)
button_modulo=Button(root,text="%",width=5,height=3,fg='blue',command=lambda :Entryset("%")).grid(row=1,column=2)
button_division=Button(root,text="/",width=5,height=3,fg='blue',command=lambda :Entryset("/")).grid(row=1,column=3)

# Creating buttons in Row-2
button1=Button(root,text="1",width=5,height=3,command=lambda :Entryset("1")).grid(row=2,column=0)
button2=Button(root,text="2",width=5,height=3,command=lambda :Entryset("2")).grid(row=2,column=1)
button3=Button(root,text="3",width=5,height=3,command=lambda :Entryset("3")).grid(row=2,column=2)
button_plus=Button(root,text="+",width=5,height=3,fg='blue',command=lambda :Entryset("+")).grid(row=2,column=3)

# Creating buttons in Row-3
button4=Button(root,text="4",width=5,height=3,command=lambda :Entryset("4")).grid(row=3,column=0)
button5=Button(root,text="5",width=5,height=3,command=lambda :Entryset("5")).grid(row=3,column=1)
button6=Button(root,text="6",width=5,height=3,command=lambda :Entryset("6")).grid(row=3,column=2)
button_minus=Button(root,text="-",width=5,height=3,fg='blue',command=lambda :Entryset("-")).grid(row=3,column=3)

# Creating buttons in Row-4
button7=Button(root,text="7",width=5,height=3,command=lambda :Entryset("7")).grid(row=4,column=0)
button8=Button(root,text="8",width=5,height=3,command=lambda :Entryset("8")).grid(row=4,column=1)
button9=Button(root,text="9",width=5,height=3,command=lambda :Entryset("9")).grid(row=4,column=2)
button_multiply=Button(root,text="*",width=5,height=3,fg='blue',command=lambda :Entryset("*")).grid(row=4,column=3)

# Creating buttons in Row-5
button0=Button(root,text="0",width=10,height=3,command=lambda :Entryset("0")).grid(row=5,column=0,columnspan=2)
button_dot=Button(root,text=".",width=5,height=3,fg='blue',command=lambda :Entryset(".")).grid(row=5,column=2)
k=None
button_equal=Button(root,text="=",width=5,height=3,fg='green',command=lambda :Evaluate(k)).grid(row=5,column=3)

# Binding Enter Button
w.bind("<Return>",Evaluate)
root.grid(row=0,column=0)
w.mainloop()
