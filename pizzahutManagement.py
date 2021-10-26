from datetime import datetime
import csv
import os.path            
userhome = os.path.expanduser('~')
filepath= os.path.join(userhome, 'Desktop', 'RAMYA/pizzahutprices.csv')
fileprices = open(filepath,'r')   
fileprices.readline()

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y")
time_string = now.strftime("%H:%M:%S")

import tkinter as tk   
menu = tk.Tk()
bgcolour=("ivory2")
bgcolour2 = ("snow2")
menu.configure(background=bgcolour)
menu.geometry("1500x900+10+10") 
menu.title("MENU")
tk.Label(menu, text="WELCOME TO PIZZA HUT!",fg = "tomato",bg=bgcolour,font = "Verdana 32 bold").pack()   
tk.Label(menu,text=dt_string+"\t\t\t"+time_string+"\n",fg= "black",bg=bgcolour,font="Verdana 16").pack()
tk.Label(menu, text= "Want mouth watering pizzas at your door step?\n",fg = "magenta",bg=bgcolour,font = "Verdana 20").pack()
tk.Label(menu, text="MENU",fg = "blue",bg='yellow',font = "Verdana 26 bold").pack()

var1=tk.IntVar()   
var2=tk.IntVar()
var3=tk.IntVar()
var4=tk.IntVar()
var5=tk.IntVar()
var6=tk.IntVar()
        
var1.set(0) 
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)

topp=0

def topping1price():
    topping.destroy()
    global topp
    topp = 99
    
def topping2price():
    topping.destroy()
    global topp
    topp = 119

def topping3price():
    topping.destroy()
    global topp
    topp = 109

def notoppings():
    topping.destroy()    
    
def toppings():
    global topping
    topping=tk.Tk()
    topping.configure(background=bgcolour)
    topping.geometry("370x290+930+450")
    topping.title("Toppings")
    tk.Label(topping,text="\nClick on the topping you want",fg = "indianred",bg=bgcolour2,font = "Verdana 20").pack()
    tk.Label(topping,text="\n",fg = "indianred",bg=bgcolour2,font = "Verdana 5").pack()
    toppingbtn1=tk.Radiobutton(topping,text="Pepperoni     Rs.   99.00",fg = "indianred",bg="DarkSeaGreen1",font = "Verdana 17 bold",indicatoron = False, command=topping1price).pack()
    tk.Label(topping,text="\n",fg = "indianred",bg=bgcolour2,font = "Verdana 5").pack()
    toppingbtn2=tk.Radiobutton(topping,text="Black olives  Rs. 119.00",fg = "indianred",bg="DarkSeaGreen1",font = "Verdana 17 bold",indicatoron = False,command=topping2price).pack()
    tk.Label(topping,text="\n",fg = "indianred",bg=bgcolour2,font = "Verdana 5").pack()
    toppingbtn2=tk.Radiobutton(topping,text="Mushrooms   Rs. 109.00",fg = "indianred",bg="DarkSeaGreen1",font = "Verdana 17 bold",indicatoron = False,command=topping3price).pack()
    tk.Label(topping,text="\n",fg = "indianred",bg=bgcolour2,font = "Verdana 12").pack()
    tk.Button(topping,text="I don't want toppings",fg="black",bg=bgcolour2,font="cambria 15",width=16,command = notoppings).pack()

c=0
price=[]
fp = csv.reader(fileprices) 

for n in fp:
    ele=[k for k in fp]
    
for r in range(1,7):  
    cd=(ele[r][c])       
    it=(ele[r][c+1])    
    pr=(ele[r][c+2])  
    tk.Label(menu,text= "    "+cd+"\t"+it+"\tRs. "+pr+"   ",fg = "blue",bg=bgcolour2,font = "Verdana 20 ").pack()
    price.append(float(pr))
        
tk.Label(menu, text="\nEnter quantities of items 1 to 6 and click PLACE ORDER.",fg = "black",bg=bgcolour,font = "Verdana 14 bold").pack()
sb1=tk.Spinbox(menu,from_=0, to=20,fg = "black",bg=bgcolour2,font = "Verdana 16 bold",width=3,wrap=True,textvariable=var1,command=toppings).pack() 
sb2=tk.Spinbox(menu,from_=0, to=20,fg = "black",bg=bgcolour2,font = "Verdana 16 bold",width=3,wrap=True,textvariable=var2,command=toppings).pack()
sb3=tk.Spinbox(menu,from_=0, to=20,fg = "black",bg=bgcolour2,font = "Verdana 16 bold",width=3,wrap=True,textvariable=var3,command=toppings).pack()
sb4=tk.Spinbox(menu,from_=0, to=20,fg = "black",bg=bgcolour2,font = "Verdana 16 bold",width=3,wrap=True,textvariable=var4,command=toppings).pack()
sb5=tk.Spinbox(menu,from_=0, to=20,fg = "black",bg=bgcolour2,font = "Verdana 16 bold",width=3,wrap=True,textvariable=var5,command=toppings).pack()
sb6=tk.Spinbox(menu,from_=0, to=20,fg = "black",bg=bgcolour2,font = "Verdana 16 bold",width=3,wrap=True,textvariable=var6,command=toppings).pack()
tk.Label(menu, text= "\n10% discount on orders worth Rs. 850 or more   \nif ordered in next 180 seconds *",fg = "magenta",bg=bgcolour,font = "Verdana 15").pack()
tk.Label(menu, text= "(* Discount is applicable on your next order after today)\n",fg = "black",bg=bgcolour,font = "Verdana 12 italic").pack()
fileprices.close()

def writetofile():
    data = [], [dt_string, time_string,totalval]
    fileorders = open("pizzahutorders.csv", 'a') 
    fo = csv.writer(fileorders)
    fo.writerows(data)
    fileorders.close()
    print("Order value stored in file pizzahutorders.")
    
    data1 = [], [dt_string, time_string,qty1,qty2,qty3,qty4,qty5,qty6] 
    fileorderdetails = open("pizzahutorderdetails.csv", 'a') 
    fod = csv.writer(fileorderdetails)
    fod.writerows(data1)
    fileorderdetails.close()
    print("Order details of items stored in file pizzahutorderdetails.")

    
def workcompleted():
    orderplacedsuccessfully.destroy()
    menu.destroy()
    
def orderplaced():
    addressdetails.destroy()
    global orderplacedsuccessfully
    orderplacedsuccessfully = tk.Tk() 
    orderplacedsuccessfully.configure(background=bgcolour)
    orderplacedsuccessfully.geometry("370x350+970+350")
    orderplacedsuccessfully.title("Order Placed Successfully")
    tk.Label(orderplacedsuccessfully,text="\nYour order placed successfully!\nYou will receive the same\nwithin 30 minutes.\n\nPizza Hut hopes to receive\nmore orders in future.\n\nThank you!\n",fg = "indianred",bg=bgcolour,font = "Verdana 20").pack()
    tk.Button(orderplacedsuccessfully,text="Send my orders fast!\nI am hungry!",fg="black",bg=bgcolour2,font="cambria 20",width=17,command = workcompleted).pack()
    tk.Button(menu,text="CLOSE",fg="black",font="cambria 20",width=11,command = menu.destroy).pack()
    
def ordernotplaced():
    ordernotplacedsuccessfully = tk.Tk() 
    ordernotplacedsuccessfully.geometry("400x160+850+482") 
    ordernotplacedsuccessfully.configure(background=bgcolour)
    ordernotplacedsuccessfully.title("Pizza hut looks forward to serve you in future")
    tk.Label(ordernotplacedsuccessfully,text="\n",fg = "indianred",bg=bgcolour,font = "Verdana 1 ").pack() 
    tk.Label(ordernotplacedsuccessfully,text="Pizza Hut hopes to receive orders\nin future, when you're hungry.",fg = "indianred",bg=bgcolour,font = "Verdana 20 ").pack()
    tk.Label(ordernotplacedsuccessfully,text="Thank you!",fg = "indianred",bg=bgcolour,font = "Verdana 20 ").pack()
    tk.Label(ordernotplacedsuccessfully,text="\n",fg = "indianred",bg=bgcolour,font = "Verdana 1 ").pack() 
    tk.Button(ordernotplacedsuccessfully,text="Ok",fg="black",font="cambria 16",width=5,command = ordernotplacedsuccessfully.destroy).pack()
    tk.Button(menu,text="CLOSE",fg="black",font="cambria 20",width=11,command = menu.destroy).pack()
    
    
def displaydetails():
    carddetails.destroy()
    writetofile()       
    global addressdetails 
    addressdetails = tk.Tk() 
    addressdetails.configure(background=bgcolour)
    addressdetails.geometry("350x280+970+420")
    addressdetails.title("Details")
    tk.Label(addressdetails,text="Your phone number",fg = "indianred",bg=bgcolour,font = "Verdana 20").pack()
    tk.Entry(addressdetails,fg = "indianred",bg=bgcolour,font = "Verdana 15",width=15).pack()
    tk.Label(addressdetails,text="Your address and Landmark",fg = "indianred",bg=bgcolour,font = "Verdana 20").pack()
    tk.Entry(addressdetails,fg = "indianred",bg=bgcolour,font = "Verdana 15",width=30).pack()
    tk.Entry(addressdetails,fg = "indianred",bg=bgcolour,font = "Verdana 15",width=30).pack()
    tk.Entry(addressdetails,fg = "indianred",bg=bgcolour,font = "Verdana 15",width=30).pack()
    tk.Label(addressdetails,text="",fg = "indianred",bg=bgcolour,font = "Verdana 20 bold").pack()
    tk.Button(addressdetails,text="Finish",fg="black",bg=bgcolour2,font="cambria 20",width=12,command =  orderplaced).pack()
    
def cashbuttonclick():
        orders.destroy()
        global carddetails 
        carddetails = tk.Tk()
        carddetails.configure(background=bgcolour)
        carddetails.geometry("1x1+1+1")
        displaydetails()
        
def cardbuttonclick():
    orders.destroy()
    global carddetails 
    carddetails = tk.Tk()
    carddetails.configure(background=bgcolour)
    carddetails.geometry("330x350+970+300")  
    carddetails.title("Payment through credit/debit card")
    tk.Label(carddetails,text="\nYour card details are safe with Pizza hut!\n",fg = "gray30",bg="wheat1",font = "Verdana 14 italic").pack() 
    tk.Label(carddetails,text="Card Number",fg = "indianred",bg=bgcolour,font = "Verdana 20").pack()
    tk.Entry(carddetails,fg = "indianred",bg=bgcolour,font = "Verdana 15",width=20).pack()
    tk.Label(carddetails,text="Expiry MM/YY",fg = "indianred",bg=bgcolour,font = "Verdana 20").pack()
    tk.Entry(carddetails,fg = "indianred",bg=bgcolour,font = "Verdana 15",width=7).pack()
    tk.Label(carddetails,text="cvv",fg = "indianred",bg=bgcolour,font = "Verdana 20").pack()
    tk.Label(carddetails,text="(A 3-digit number on the back side of your card)",fg = "indianred",bg=bgcolour,font = "Verdana 12").pack() 
    tk.Entry(carddetails,bg=bgcolour,font = "Verdana 15",width=3).pack()
    tk.Label(carddetails,text="",fg = "indianred",bg=bgcolour,font = "Verdana 20").pack()  
    cardnext = tk.Button(carddetails,text="Next >",fg="black",bg=bgcolour2,font="cambria 17",width=7,command =  displaydetails)  
    cardnext.pack()
    
def placeorderbuttonclick(): 
    global totalval 
    global qty1
    global qty2
    global qty3
    global qty4
    global qty5
    global qty6
    qty1=var1.get()
    qty2=var2.get()
    qty3=var3.get()
    qty4=var4.get()
    qty5=var5.get()
    qty6=var6.get()
    val1=qty1*price[0]
    val2=qty2*price[1]
    val3=qty3*price[2]
    val4=qty4*price[3]
    val5=qty5*price[4]
    val6=qty6*price[5]
    totalval=val1+val2+val3+val4+val5+val6+topp
    
    if(totalval>0):
        global orders  
        orders=tk.Tk()  
        orders.geometry("320x220+950+435")
        orders.configure(background=bgcolour)
        orders.title("ORDER SUMMARY")
        tk.Label(orders, text="\n",fg = "indianred",bg=bgcolour,font = "Verdana 2").pack()
        tk.Label(orders, text="Please pay Rs.  "+str(totalval)+"0",fg = "indianred",bg=bgcolour,font = "Verdana 20").pack()
        tk.Label(orders, text="\nClick on any payment option",fg = "indianred",bg=bgcolour,font = "Verdana 20 ").pack()
        tk.Label(orders, text="\n",fg = "indianred",bg=bgcolour,font = "Verdana 4").pack()
        cardbutton=tk.Radiobutton(orders,text="Card",fg = "black",bg="ivory3",font = "Verdana 20 bold",indicatoron= False,command=cardbuttonclick).pack()
        tk.Label(orders, text="\n",fg = "indianred",bg=bgcolour,font = "Verdana 2").pack()
        cashbutton=tk.Radiobutton(orders,text="Cash",fg = "black",bg="ivory3",font = "Verdana 20 bold",indicatoron= False,command=cashbuttonclick).pack()
        print("total value of order = ",totalval,"0")
    else:
        noorders=tk.Tk()   
        noorders.configure(background=bgcolour)
        noorders.title("No Quantity Entered")
        noorders.geometry("550x150+850+485")  
        tk.Label(noorders, text="\nYou forgot to enter quantities of items !!\n",fg = "tomato",bg=bgcolour,font = "Verdana 24").pack()
        tk.Button(noorders,text="Let me enter quantities!",fg="black",bg=bgcolour,font="cambria 16",width=20,command = noorders.destroy).pack()

tk.Button(menu,text="Place Order",fg="forest green",bg='yellow2',font="cambria 27 bold",width=11, command=placeorderbuttonclick).pack()
tk.Label(menu, text= "\n",fg = "blue",font = "Verdana 1").pack() 
tk.Button(menu,text="No!  I am not hungry.",fg="black",font="cambria 16",width=15,command = ordernotplaced).pack() 
tk.Label(menu, text= "\n",fg = "blue",font = "Verdana 1").pack()



   

    
        
   























          

                
            
    
        
        
