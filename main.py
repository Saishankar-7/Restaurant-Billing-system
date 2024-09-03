from tkinter import *
from tkinter import filedialog,messagebox
import random
import time

#functions
def reset():
    textReceipt.delete(1.0,END)
    e_roti.set('0')
    e_daal.set('0')
    e_fish.set('0')
    e_sabji.set('0')
    e_chawal.set('0')
    e_fish.set('0')
    e_mutton.set('0')
    e_kabab.set('0')
    e_chicken.set('0')
    e_paneer.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_shikanji.set('0')
    e_roohafza.set('0')
    e_jaljeera.set('0')
    e_masalatea.set('0')
    e_badammilk.set('0')
    e_cooldrink.set('0')

    e_oreo.set('0')
    e_apple.set('0')
    e_kitkat.set('0')
    e_vanilla.set('0')
    e_blackforest.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')
    
    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textkabab.config(state=DISABLED)
    textchawal.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    
    textlassi.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textshikanji.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    textroohafza.config(state=DISABLED)
    textmasalatea.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textcooldrink.config(state=DISABLED)
    
    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textblackforest.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
         
    Foodvar.set('')
    Drinksvar.set('')
    Cakesvar.set('')
    SubTotalvar.set('')
    ServiceTaxvar.set('')
    TotalCostvar.set('')    
    
    
    
    
    
    
    
def send():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        def send_msg():
            message=textarea.get(1.0,END)
            number=numberfield.get()
            auth='sBRw4GJfWrzOZ5IcSQmvdyLPTagKtjo1kiA8XUV07lqnuxeMDpebLT5mcA6EB2JUfWtMH9XaDIuqxk8C'
            url='https://www.fast2sms.com/dev/bulkV2'
            
            params={
                'authorization':auth,
                'message':message,
                'numbers':number,
                'sender-id':'FSTSMS',
                'route':'p',
                'language':'english'
            }
            response=requests.get(url,params=params)
            dict=response.json()
            result=dict.get('return')
            if result==True:
                messagebox.showinfo('Send Successfully','Message sent successfully')
                
            else:
                messagebox.showerror('Error','Something went wrong')
            
            
            
            
            
        root2=Toplevel()
        
        root2.title("Send Bill")
        root2.config(bg='#5676a9')
        root2.geometry('485x620+50+50')
        
        numberLabel=Label(root2,text='Mobile Number',font=('arial',18,' bold underline'),bg='#5676a9',fg='yellow')
        numberLabel.pack(pady=5)
        
        numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
        numberfield.pack(pady=5)
        
        billLabel=Label(root2,text='Bill Details',font=('arial',18,' bold underline'),bg='#5676a9',fg='yellow')
        billLabel.pack(pady=5)
        
        textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
        textarea.pack(pady=5)
        textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n\n')
        
        if Foodvar.get()!='0 Rs':
            textarea.insert(END,f'cost of Food \t\t\t{priceoffood}Rs\n\n')
        if  Drinksvar.get()!='0 Rs':
            textarea.insert(END,f'cost of Drinks\t\t\t{priceofdrinks}Rs\n\n')
        if Cakesvar.get()!='0 Rs':
            textarea.insert(END,f'cost of Cakes\t\t\t{priceofcake}Rs\n\n')
        
        textarea.insert(END,f'Subtotal\t\t\t{subtotalofitems}Rs\n\n')
        textarea.insert(END,f'Service Tax\t\t\t{50}Rs\n\n')
        textarea.insert(END,f'Total cost\t\t\t{subtotalofitems+50}Rs\n\n')
        
        sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='#5676a9',fg='yellow',bd=5,relief=GROOVE,command=send_msg)
        sendButton.pack(pady=5)
        
        root2.mainloop()





def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:

            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is  Successfully Saved')

def receipt():
    global billnumber,date
    if Foodvar.get()!='' or Drinksvar.get()!='' or Cakesvar.get()!='':
         textReceipt.delete(1.0,END)
         x=random.randint(100,10000)
         billnumber='BILL'+str(x)
         date=time.strftime('%d/%m/%Y')
         textReceipt.insert(END,'RECEIPT Ref:\t\t'+billnumber+'\t\t'+date+'\n')
         textReceipt.insert(END,'*********************************************\n')
         textReceipt.insert(END,'Items:\t\tcost of items(Rs)\n')
         textReceipt.insert(END,'*********************************************\n')
         #food
         if e_roti.get()!='0':
             textReceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*30}\n\n')
         if e_daal.get()!='0':
             textReceipt.insert(END,f'Daal\t\t\t{int(e_daal.get())*60}\n\n')
         if e_fish.get()!='0':
             textReceipt.insert(END,f'Fish\t\t\t{int(e_fish.get())*100}\n\n')
         if e_sabji.get()!='0':
             textReceipt.insert(END,f'Sabji\t\t\t{int(e_sabji.get())*50}\n\n')
         if e_kabab.get()!='0':
             textReceipt.insert(END,f'Kabab\t\t\t{int(e_kabab.get())*60}\n\n')
         if e_chawal.get()!='0':
             textReceipt.insert(END,f'Chawal\t\t\t{int(e_chawal.get())*40}\n\n')
         if e_mutton.get()!='0':
             textReceipt.insert(END,f'Mutton\t\t\t{int(e_mutton.get())*150}\n\n')
         if e_paneer.get()!='0':
             textReceipt.insert(END,f'Paneer\t\t\t{int(e_paneer.get())*100}\n\n')  
         if e_chicken.get()!='0':
             textReceipt.insert(END,f'Chicken\t\t\t{int(e_chicken.get())*120}\n\n')
    
         #drinks
         if e_lassi.get()!='0':
             textReceipt.insert(END,f'Lassi\t\t\t{int(e_lassi.get())*50}\n\n')
         if e_coffee.get()!='0':
             textReceipt.insert(END,f'Coffee\t\t\t{int(e_coffee.get())*30}\n\n')
         if e_faluda.get()!='0':
             textReceipt.insert(END,f'Faluda\t\t\t{int(e_faluda.get())*30}\n\n')
         if e_shikanji.get()!='0':
             textReceipt.insert(END,f'Shikanji\t\t\t{int(e_shikanji.get())*30}\n\n')
         if e_jaljeera.get()!='0':
             textReceipt.insert(END,f'Jaljeera\t\t\t{int(e_jaljeera.get())*30}\n\n')
         if e_roohafza.get()!='0':
             textReceipt.insert(END,f'Roohafza\t\t\t{int(e_roohafza.get())*50}\n\n')
         if e_masalatea .get()!='0':
             textReceipt.insert(END,f'Masala Tea\t\t\t{int(e_masalatea.get())*60}\n\n')
         if e_badammilk.get()!='0':
             textReceipt.insert(END,f'Badam milk\t\t\t{int(e_badammilk.get())*70}\n\n')  
         if e_cooldrink.get()!='0':
             textReceipt.insert(END,f'Cool drink\t\t\t{int(e_cooldrink.get())*100}\n\n')
    
         #cakes
         if e_oreo.get()!='0':
             textReceipt.insert(END,f'Oreo\t\t\t{int(e_oreo.get())*100}\n\n')
         if e_apple.get()!='0':
             textReceipt.insert(END,f'Coffee\t\t\t{int(e_apple.get())*150}\n\n')
         if e_kitkat.get()!='0':
             textReceipt.insert(END,f'Kitkat\t\t\t{int(e_kitkat.get())*100}\n\n')
         if e_vanilla.get()!='0':
             textReceipt.insert(END,f'Vanilla\t\t\t{int(e_vanilla.get())*50}\n\n')
         if e_banana.get()!='0':
             textReceipt.insert(END,f'Banana\t\t\t{int(e_banana.get())*100}\n\n')
         if e_brownie.get()!='0':
             textReceipt.insert(END,f'brownie\t\t\t{int(e_brownie.get())*200}\n\n')
         if e_pineapple .get()!='0':
             textReceipt.insert(END,f'pineapple\t\t\t{int(e_pineapple.get())*150}\n\n')
         if e_chocolate.get()!='0':
            textReceipt.insert(END,f'Chocolate\t\t\t{int(e_chocolate.get())*90}\n\n')  
         if e_blackforest.get()!='0':
             textReceipt.insert(END,f'Black forest\t\t\t{int(e_blackforest.get())*250}\n\n')
        
         textReceipt.insert(END,'*********************************************\n')
         if Foodvar.get()!='0 Rs':
             textReceipt.insert(END,f'cost of Food \t\t\t{priceoffood}Rs\n\n')
         if  Drinksvar.get()!='0 Rs':
             textReceipt.insert(END,f'cost of Drinks\t\t\t{priceofdrinks}Rs\n\n')
         if Cakesvar.get()!='0 Rs':
             textReceipt.insert(END,f'cost of Cakes\t\t\t{priceofcake}Rs\n\n')
    
         textReceipt.insert(END,f'Subtotal\t\t\t{subtotalofitems}Rs\n\n')
         textReceipt.insert(END,f'Service Tax\t\t\t{50}Rs\n\n')
         textReceipt.insert(END,f'Total cost\t\t\t{subtotalofitems+50}Rs\n\n')
         textReceipt.insert(END,'*********************************************\n')
    else:
        messagebox.showerror('Error','No item Is selected')
    
def totalcost():
    global priceoffood,priceofdrinks,priceofcake,subtotalofitems
    if var1.get()!=0 or var2.get()!=0 or var3.get()!=0 or var4.get()!=0 or var5.get()!=0 or var6.get()!=0 or \
       var7.get()!=0 or var8.get()!=0 or var9.get()!=0 or var10.get()!=0 or var11.get()!=0 or var12.get()!=0 or \
       var13.get()!=0 or var14.get()!=0 or var15.get()!=0 or var16.get()!=0 or var17.get()!=0 or var18.get()!=0 or \
       var19.get()!=0 or var20.get()!=0 or var21.get()!=0 or var22.get()!=0 or var23.get()!=0 or var24.get()!=0 or \
       var25.get()!=0 or var26.get()!=0 or var27.get()!=0: 
            item1=int(e_roti.get())
            item2=int(e_daal.get())
            item3=int(e_fish.get())
            item4=int(e_sabji.get())
            item5=int(e_kabab.get())
            item6=int(e_chawal.get())
            item7=int(e_mutton.get())
            item8=int(e_paneer.get())
            item9=int(e_chicken.get())

            item10=int(e_lassi.get())
            item11=int(e_coffee.get())
            item12=int(e_faluda.get())
            item13=int(e_shikanji.get())
            item14=int(e_jaljeera.get())
            item15=int(e_roohafza.get())
            item16=int(e_masalatea.get())
            item17=int(e_badammilk.get())
            item18=int(e_cooldrink.get())

            item19=int(e_oreo.get())
            item20=int(e_apple.get())
            item21=int(e_kitkat.get())
            item22=int(e_vanilla.get())
            item23=int(e_banana.get())
            item24=int(e_brownie.get())
            item25=int(e_pineapple.get())
            item26=int(e_chocolate.get())
            item27=int(e_blackforest.get())

            priceoffood=(item1 * 30) + (item2 * 60) + (item3 * 100) + (item4 * 50) + (item5 * 60)+(item6 *40)+(item7*150)+(item8*100)+(item9*120)
            priceofdrinks=(item10*50)+(item11*30)+(item12*30)+(item13*30)+(item14*30)+(item15*50)+(item16*60)+(item17*70)+(item18*100)
            priceofcake=(item19*100)+(item20*150)+(item21*100)+(item22*50)+(item23*100)+(item24*200)+(item25*150)+(item26*90)+(item27*250)

 
            Foodvar.set(str(priceoffood)+ ' Rs')
            Drinksvar.set(str(priceofdrinks)+ ' Rs')
            Cakesvar.set(str(priceofcake)+' Rs')

            subtotalofitems=priceoffood+priceofdrinks+priceofcake
            SubTotalvar.set(str(subtotalofitems)+ ' Rs')

            ServiceTaxvar.set('50 Rs')

            totalcost=subtotalofitems+50
            TotalCostvar.set(str(totalcost)+' Rs')
    else:
           messagebox.showerror('Error','No Item Is selected')






def rotii():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def daal():
    if var2.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0,END)
        textdaal.focus()
    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')

def fish():
    if var3.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')
def sabji():
    if var4.get()==1:
        textsabji.config(state=NORMAL)
        textsabji.delete(0,END)
        textsabji.focus()
    else:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')
def kabab():
    if var5.get()==1:
        textkabab.config(state=NORMAL)
        textkabab.delete(0,END)
        textkabab.focus()
    else:
        textkabab.config(state=DISABLED)
        e_kabab.set('0')

def chawal():
    if var6.get()==1:
        textchawal.config(state=NORMAL)
        textchawal.delete(0,END)
        textchawal.focus()
    else:
        textchawal.config(state=DISABLED)
        e_chawal.set('0')

def mutton():
    if var7.get()==1:
        textmutton.config(state=NORMAL)
        textmutton.delete(0,END)
        textmutton.focus()
    else:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')

def paneer():
    if var8.get()==1:
        textpaneer.config(state=NORMAL)
        textpaneer.delete(0,END)
        textpaneer.focus()
    else:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')
def chicken():
    if var9.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')
def lassi():
    if var10.get()==1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')
def coffee():
    if var11.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')
def faluda():
    if var12.get()==1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')
def shikanji():
    if var13.get()==1:
        textshikanji.config(state=NORMAL)
        textshikanji.delete(0,END)
        textshikanji.focus()
    else:
        textshikanji.config(state=DISABLED)
        e_shikanji.set('0')
def jaljeera():
    if var14.get()==1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.delete(0,END)
        textjaljeera.focus()
    else:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')
def roohafza():
    if var15.get()==1:
        textroohafza.config(state=NORMAL)
        textroohafza.delete(0,END)
        textroohafza.focus()
    else:
        textroohafza.config(state=DISABLED)
        e_roohafza.set('0')
def masalatea():
    if var16.get()==1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.delete(0,END)
        textmasalatea.focus()
    else:
        textmasalatea.config(state=DISABLED)
        e_masalatea.set('0')
def badammilk():
    if var17.get()==1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.delete(0,END)
        textbadammilk.focus()
    else:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')
def cooldrink():
    if var18.get()==1:
        textcooldrink.config(state=NORMAL)
        textcooldrink.delete(0,END)
        textcooldrink.focus()
    else:
        textcooldrink.config(state=DISABLED)
        e_cooldrink.set('0')
def oreo():
    if var19.get()==1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')
def apple():
    if var20.get()==1:
        textapple.config(state=NORMAL)
        textapple.delete(0,END)
        textapple.focus()
    else:
        textapple.config(state=DISABLED)
        e_apple.set('0')
def kitkat():
    if var21.get()==1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0,END)
        textkitkat.focus()
    else:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')
def vanilla():
    if var22.get()==1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0,END)
        textvanilla.focus()
    else:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')
def banana():
    if var23.get()==1:
        textbanana.config(state=NORMAL)
        textbanana.delete(0,END)
        textbanana.focus()
    else:
        textbanana.config(state=DISABLED)
        e_banana.set('0')
def browine():
    if var24.get()==1:
        textbrownie.config(state=NORMAL)
        textbrownie.delete(0,END)
        textbrownie.focus()
    else:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')
def pineapple():
    if var25.get()==1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0,END)
        textpineapple.focus()
    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')
def chocolate():
    if var26.get()==1:
        textchocolate.config(state=NORMAL)
        textchocolate.delete(0,END)
        textchocolate.focus()
    else:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')   

def blackforest():
    if var27.get()==1:
        textblackforest.config(state=NORMAL)
        textblackforest.delete(0,END)
        textblackforest.focus()
    else:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')
t=Tk()
t.geometry('1270x690+0+0')
t.resizable(0,0)
t.title('RESTAURANT MANAGEMENT')
t.config(bg='#5676a9')
topframe=Frame(t,bd=10,relief=RIDGE,bg='#5676a9')
topframe.pack(side=TOP)
titlelabel=Label(topframe,text="RESTAURANT MANAGEMENT",font=('Times New Roman',30,'bold'),fg='Yellow',bg='#5676a9',bd=9,width=51)
titlelabel.grid(row=0,column=0)
#menuframe
menuframe=Frame(t,bd=10,relief=RIDGE,bg='#5676a9')
menuframe.pack(side=LEFT)

costframe=Frame(menuframe,bd=4,relief=RIDGE,bg='#5676a9',pady=10)
costframe.pack(side=BOTTOM)

foodframe=LabelFrame(menuframe,text='Food',font=('Times New Roman',19,'bold'),bd=10,relief=RIDGE,fg='black')
foodframe.pack(side=LEFT)

drinksframe=LabelFrame(menuframe,text='Drinks',font=('Times New Roman',19,'bold'),bd=10,relief=RIDGE,fg='black')
drinksframe.pack(side=LEFT)

cakesframe=LabelFrame(menuframe,text='cakes',font=('Times New Roman',19,'bold'),bd=10,relief=RIDGE,fg='black')
cakesframe.pack(side=LEFT)

rightframe=Frame(t,bd=15,relief=RIDGE,bg='#5676a9')
rightframe.pack(side=RIGHT)

calframe=Frame(rightframe,bd=1,relief=RIDGE,bg='#5676a9')
calframe.pack()

recieptframe=Frame(rightframe,bd=4,relief=RIDGE,bg='#5676a9')
recieptframe.pack()

btnframe=Frame(rightframe,bd=3,relief=RIDGE,bg='black')
btnframe.pack()
#varibles

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e_roti=StringVar()
e_daal=StringVar()
e_fish=StringVar()
e_sabji=StringVar()
e_chawal=StringVar()
e_fish=StringVar()
e_mutton=StringVar()
e_kabab=StringVar()
e_chicken=StringVar()
e_paneer=StringVar()

e_lassi=StringVar()
e_coffee=StringVar()
e_faluda=StringVar()
e_shikanji=StringVar()
e_roohafza=StringVar()
e_jaljeera=StringVar()
e_masalatea=StringVar()
e_badammilk=StringVar()
e_cooldrink=StringVar()

e_oreo=StringVar()
e_apple=StringVar()
e_kitkat=StringVar()
e_vanilla=StringVar()
e_blackforest=StringVar()
e_banana=StringVar()
e_brownie=StringVar()
e_pineapple=StringVar()
e_chocolate=StringVar()

e_roti.set('0')
e_daal.set('0')
e_fish.set('0')
e_sabji.set('0')
e_chawal.set('0')
e_fish.set('0')
e_mutton.set('0')
e_kabab.set('0')
e_chicken.set('0')
e_paneer.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_shikanji.set('0')
e_roohafza.set('0')
e_jaljeera.set('0')
e_masalatea.set('0')
e_badammilk.set('0')
e_cooldrink.set('0')

e_oreo.set('0')
e_apple.set('0')
e_kitkat.set('0')
e_vanilla.set('0')
e_blackforest.set('0')
e_banana.set('0')
e_brownie.set('0')
e_pineapple.set('0')
e_chocolate.set('0')

Foodvar=StringVar()
Drinksvar=StringVar()
Cakesvar=StringVar()
SubTotalvar=StringVar()
ServiceTaxvar=StringVar()
TotalCostvar=StringVar()



#food

roti=Checkbutton(foodframe,text='Roti',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=rotii)
roti.grid(row=0,column=0,sticky=W)

dal=Checkbutton(foodframe,text='Dal',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=daal)
dal.grid(row=1,column=0,sticky=W)

fish=Checkbutton(foodframe,text='Fish',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=fish)
fish.grid(row=2,column=0,sticky=W)

sabji=Checkbutton(foodframe,text='Sabji',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=sabji)
sabji.grid(row=3,column=0,sticky=W)

kabab=Checkbutton(foodframe,text='kabab',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=kabab)
kabab.grid(row=4,column=0,sticky=W)

chawal=Checkbutton(foodframe,text='Chawal',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=chawal)
chawal.grid(row=5,column=0,sticky=W)

mutton=Checkbutton(foodframe,text='mutton',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=mutton)
mutton.grid(row=6,column=0,sticky=W)

paneer=Checkbutton(foodframe,text='paneer',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=paneer)
paneer.grid(row=7,column=0,sticky=W)

chicken=Checkbutton(foodframe,text='chicken',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=chicken)
chicken.grid(row=8,column=0,sticky=W)

#Entry fields for food items

textroti=Entry(foodframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(foodframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textfish=Entry(foodframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)

textsabji=Entry(foodframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sabji)
textsabji.grid(row=3,column=1)

textkabab=Entry(foodframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kabab)
textkabab.grid(row=4,column=1)

textchawal=Entry(foodframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chawal)
textchawal.grid(row=5,column=1)

textmutton=Entry(foodframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mutton)
textmutton.grid(row=6,column=1)

textpaneer=Entry(foodframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=7,column=1)

textchicken=Entry(foodframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=8,column=1)

#drinks

lassi=Checkbutton(drinksframe,text='lassi',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=lassi)
lassi.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksframe,text='coffee',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

faluda=Checkbutton(drinksframe,text='faluda',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=faluda)
faluda.grid(row=2,column=0,sticky=W)

shikanji=Checkbutton(drinksframe,text='shikanji',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=shikanji)
shikanji.grid(row=3,column=0,sticky=W)

jaljeera=Checkbutton(drinksframe,text='jaljeera',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=jaljeera)
jaljeera.grid(row=4,column=0,sticky=W)

roohafza=Checkbutton(drinksframe,text='roohafz',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=roohafza)
roohafza.grid(row=5,column=0,sticky=W)

masalatea=Checkbutton(drinksframe,text='masalatea',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=masalatea)
masalatea.grid(row=6,column=0,sticky=W)

badammilk=Checkbutton(drinksframe,text='badammilk',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=badammilk)
badammilk.grid(row=7,column=0,sticky=W)

cooldrink=Checkbutton(drinksframe,text='cooldrink',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=cooldrink)
cooldrink.grid(row=8,column=0,sticky=W)

#entry fields for drinks

textlassi=Entry(drinksframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=0,column=1)

textcoffee=Entry(drinksframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1,column=1)

textfaluda=Entry(drinksframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=2,column=1)

textshikanji=Entry(drinksframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_shikanji)
textshikanji.grid(row=3,column=1)

textjaljeera=Entry(drinksframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_jaljeera)
textjaljeera.grid(row=4,column=1)

textroohafza=Entry(drinksframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roohafza)
textroohafza.grid(row=5,column=1)

textmasalatea=Entry(drinksframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_masalatea)
textmasalatea.grid(row=6,column=1)

textbadammilk=Entry(drinksframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_badammilk)
textbadammilk.grid(row=7,column=1)

textcooldrink=Entry(drinksframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cooldrink)
textcooldrink.grid(row=8,column=1)

#cakes

oreocake=Checkbutton(cakesframe,text='oreo',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=oreo)
oreocake.grid(row=0,column=0,sticky=W)

applecake=Checkbutton(cakesframe,text='apple',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=apple)
applecake.grid(row=1,column=0,sticky=W)

kitkatcake=Checkbutton(cakesframe,text='kitkat',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=kitkat)
kitkatcake.grid(row=2,column=0,sticky=W)

vanillacake=Checkbutton(cakesframe,text='vanilla',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=vanilla)
vanillacake.grid(row=3,column=0,sticky=W)

bananacake=Checkbutton(cakesframe,text='Banana',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=banana)
bananacake.grid(row=4,column=0,sticky=W)

browniecake=Checkbutton(cakesframe,text='Brownie',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=browine)
browniecake.grid(row=5,column=0,sticky=W)

pineapplecake=Checkbutton(cakesframe,text='pineapple',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=pineapple)
pineapplecake.grid(row=6,column=0,sticky=W)

chocolatecake=Checkbutton(cakesframe,text='chocolate',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=chocolate)
chocolatecake.grid(row=7,column=0,sticky=W)

blackforestcake=Checkbutton(cakesframe,text='Blackforest',font=('Times New Roman',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=blackforest)
blackforestcake.grid(row=8,column=0,sticky=W)

#entry fields for cakes

textoreo=Entry(cakesframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=0,column=1)

textapple=Entry(cakesframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_apple)
textapple.grid(row=1,column=1)

textkitkat=Entry(cakesframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=2,column=1)

textvanilla=Entry(cakesframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=3,column=1)

textbanana=Entry(cakesframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_banana)
textbanana.grid(row=4,column=1)

textbrownie=Entry(cakesframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_brownie)
textbrownie.grid(row=5,column=1)

textpineapple=Entry(cakesframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=6,column=1)

textchocolate=Entry(cakesframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chocolate)
textchocolate.grid(row=7,column=1)

textblackforest=Entry(cakesframe,font=('Times New Roman',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8,column=1)



#costlabels and entry fields

labelcostofFood=Label(costframe,text="Cost of Food",font=('Times New Roman',16,'bold'),bg="#5676a9",fg='black')
labelcostofFood.grid(row=0,column=0)

textcostofFood=Entry(costframe,font=('Times New Roman',16,'bold'),bd=6,width=14,state='readonly',textvariable=Foodvar)
textcostofFood.grid(row=0,column=1,padx=35)

labelcostofDrinks=Label(costframe,text="Cost of Drinks",font=('Times New Roman',16,'bold'),bg="#5676a9",fg='black')
labelcostofDrinks.grid(row=1,column=0)

textcostofDrinks=Entry(costframe,font=('Times New Roman',16,'bold'),bd=6,width=14,state='readonly',textvariable=Drinksvar)
textcostofDrinks.grid(row=1,column=1,padx=35)

labelcostofCakes=Label(costframe,text="Cost of Cakes",font=('Times New Roman',16,'bold'),bg="#5676a9",fg='black')
labelcostofCakes.grid(row=2,column=0)

textcostofCakes=Entry(costframe,font=('Times New Roman',16,'bold'),bd=6,width=14,state='readonly',textvariable=Cakesvar)
textcostofCakes.grid(row=2,column=1,padx=35)


labelSubtotal=Label(costframe,text="Subtotal",font=('Times New Roman',16,'bold'),bg="#5676a9",fg='black')
labelSubtotal.grid(row=0,column=2)

textSubtotal=Entry(costframe,font=('Times New Roman',16,'bold'),bd=6,width=14,state='readonly',textvariable=SubTotalvar)
textSubtotal.grid(row=0,column=3,padx=35)

labelServiceTax=Label(costframe,text="Service TAX",font=('Times New Roman',16,'bold'),bg="#5676a9",fg='black')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costframe,font=('Times New Roman',16,'bold'),bd=6,width=14,state='readonly',textvariable=ServiceTaxvar)
textServiceTax.grid(row=1,column=3,padx=35)

labelTotalcost=Label(costframe,text="Total cost",font=('Times New Roman',16,'bold'),bg="#5676a9",fg='black')
labelTotalcost.grid(row=2,column=2)

textTotalCost=Entry(costframe,font=('Times New Roman',16,'bold'),bd=6,width=14,state='readonly',textvariable=TotalCostvar)
textTotalCost.grid(row=2,column=3,padx=35)

#buttons

buttonTotal=Button(btnframe,text='Total',font=('Times New Roman',14,'bold'),fg='black',bg='#5676a9',bd=3,padx=16,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReciept=Button(btnframe,text='Receipt',font=('Times New Roman',14,'bold'),fg='black',bg='#5676a9',bd=3,padx=16,command=receipt)
buttonReciept.grid(row=0,column=1)

buttonSave=Button(btnframe,text='Save',font=('Times New Roman',14,'bold'),fg='black',bg='#5676a9',bd=3,padx=16,command=save)
buttonSave.grid(row=0,column=2)

buttonsend=Button(btnframe,text='Send',font=('Times New Roman',14,'bold'),fg='black',bg='#5676a9',bd=3,padx=16,command=send)
buttonsend.grid(row=0,column=3)

buttonReset=Button(btnframe,text='Reset',font=('Times New Roman',14,'bold'),fg='black',bg='#5676a9',bd=3,padx=16,command=reset)
buttonReset.grid(row=0,column=4)

#text area for receipt
textReceipt=Text(recieptframe,font=('Times New Roman',14,'bold'),bd='3',width=50,height=12)
textReceipt.grid(row=0,column=0)

#calculator
operator=''  #7+9
def buttonclick(numbers):
    global operator
    operator=operator+numbers
    calfield.delete(0,END)
    calfield.insert(END,operator)

def Clear():
    global operator
    operator=''
    calfield.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calfield.delete(0,END)
    calfield.insert(0,result)
    operator=''


calfield=Entry(calframe,font=('Times New Roman',16,'bold'),bd=4,width=45)
calfield.grid(row=0,column=0,columnspan=4)

button7=Button(calframe,text='7',font=('Times New Roman',16,'bold'),fg='yellow',bg='#5676a9',bd=6,width=9,command=lambda:buttonclick('7'))
button7.grid(row=1,column=0)

button8=Button(calframe,text='8',font=('Times New Roman',16,'bold'),fg='yellow',bg='#5676a9',bd=6,width=9,command=lambda:buttonclick('8'))
button8.grid(row=1,column=1)

button9=Button(calframe,text='9',font=('Times New Roman',16,'bold'),fg='yellow',bg='#5676a9',bd=6,width=9,command=lambda:buttonclick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calframe,text='+',font=('Times New Roman',16,'bold'),fg='yellow',bg='#5676a9',bd=6,width=9,command=lambda:buttonclick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calframe,text='4',font=('Times New Roman',16,'bold'),fg='yellow',bg='#5676a9',bd=6,width=9,command=lambda:buttonclick('4'))
button4.grid(row=2,column=0)

button5=Button(calframe,text='5',font=('Times New Roman',16,'bold'),fg='#5676a9',bg='white',bd=6,width=9,command=lambda:buttonclick('5'))
button5.grid(row=2,column=1)

button6=Button(calframe,text='6',font=('Times New Roman',16,'bold'),fg='#5676a9',bg='white',bd=6,width=9,command=lambda:buttonclick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calframe,text='-',font=('Times New Roman',16,'bold'),fg='yellow',bg='#5676a9',bd=6,width=9,command=lambda:buttonclick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calframe,text='1',font=('Times New Roman',16,'bold'),fg='yellow',bg='#5676a9',bd=6,width=9,command=lambda:buttonclick('1'))
button1.grid(row=3,column=0)

button2=Button(calframe,text='2',font=('Times New Roman',16,'bold'),fg='#5676a9',bg='white',bd=6,width=9,command=lambda:buttonclick('2'))
button2.grid(row=3,column=1)

button3=Button(calframe,text='3',font=('Times New Roman',16,'bold'),fg='#5676a9',bg='white',bd=6,width=9,command=lambda:buttonclick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calframe,text='*',font=('Times New Roman',16,'bold'),fg='yellow',bg='#5676a9',bd=6,width=9,command=lambda:buttonclick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calframe,text='Ans',font=('Times New Roman',16,'bold'),fg='yellow',bg='#5676a9',bd=6,width=9,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calframe,text='Clear',font=('Times New Roman',16,'bold'),fg='Yellow',bg='#5676a9',bd=6,width=9,command=Clear)
buttonClear.grid(row=4,column=1)

button0=Button(calframe,text='0',font=('Times New Roman',16,'bold'),fg='Yellow',bg='#5676a9',bd=6,width=9,command=lambda:buttonclick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calframe,text='/',font=('Times New Roman',16,'bold'),fg='yellow',bg='#5676a9',bd=6,width=9,command=lambda:buttonclick('/'))
buttonDiv.grid(row=4,column=3)








mainloop()
