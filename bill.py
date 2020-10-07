from tkinter import *
import math,random,os
from tkinter import messagebox

class Bill_app:
    def __init__(self, root):
        self.root = root
        # width x height + starting cordinates(x,y)
        self.root.geometry('1380x700+0+0')
        self.root.title('Billing Software')
        bg_color = '#074463'
        title = Label(self.root, text='Billing Software', bd=12, relief=GROOVE, bg=bg_color,
                      fg='White', font=('times new roman', 30, 'bold'), pady=2).pack(fill=X)
        
        # ==========variable======
        # =======cosmatics========

        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.hair_gel = IntVar()
        self.body_loshon = IntVar()

        #========grocery=====
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.suger = IntVar()
        self.tea = IntVar()

        #======cold drink=======

        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        # ==========total price & tax =========

        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        #===========customer ==========
        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        

        # ===========  Customer detail frame
        F1 = LabelFrame(self.root, text='Customer Detail', fg='gold', font=(
            'times new roman', 15, 'bold'), bd=12, relief=GROOVE, bg=bg_color)
        F1.place(x=0, y=78, relwidth=1)

        cname_l = Label(F1, text='Customer Name', font=('times new roman', 15, 'bold'),
                        bg=bg_color, fg='white').grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, font='arial 15',textvariable = self.c_name, bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=5, padx=10)

        cphone_l = Label(F1, text='Phone No.', font=(
            'times new roman', 15, 'bold'), bg=bg_color, fg='white').grid(row=0, column=2, padx=20, pady=5)
        cphone_txt = Entry(F1, width=15, font='arial 15',textvariable = self.c_phone, bd=7, relief=SUNKEN).grid(
            row=0, column=3, pady=5, padx=10)

        cbill_l = Label(F1, text='Bill Number', font=('times new roman', 15, 'bold'),
                        bg=bg_color, fg='white').grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width=15,textvariable = self.search_bill, font='arial 15', bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1,command=self.find_bill, text='Search', width=10, bd=7, font='arial 12 bold').grid(
            row=0, column=6, pady=10, padx=10)




        # =================     cosmatic frame
        F2 = LabelFrame(self.root, text='Cosmetics', fg='gold', font=(
            'times new roman', 15, 'bold'), bd=12, relief=GROOVE, bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        bath_l = Label(F2, text='Bath Soap', font=('times new roman', 16, 'bold'),
                       bg=bg_color, fg='lightgreen').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        bath_txt = Entry(F2, width=10,textvariable = self.soap, font=('times new roman', 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10, sticky='w')

        face_cream_l = Label(F2, text='Face Cream', font=('times new roman', 16, 'bold'),
                             bg=bg_color, fg='lightgreen').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        face_cream_txt = Entry(F2, width=10,textvariable = self.face_cream, font=('times new roman', 16, "bold"), bd=5, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=10, sticky='w')

        face_wash_l = Label(F2, text='Face Wash', font=('times new roman', 16, 'bold'),
                            bg=bg_color, fg='lightgreen').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        face_wash_txt = Entry(F2, width=10,textvariable = self.face_wash, font=('times new roman', 16, "bold"), bd=5, relief=SUNKEN).grid(
            row=2, column=1, padx=10, pady=10, sticky='w')

        hair_spray_l = Label(F2, text='Hair Spray', font=('times new roman', 16, 'bold'),
                             bg=bg_color, fg='lightgreen').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        hair_spray_txt = Entry(F2, width=10,textvariable = self.hair_spray, font=('times new roman', 16, "bold"), bd=5, relief=SUNKEN).grid(
            row=3, column=1, padx=10, pady=10, sticky='w')

        hair_gel_l = Label(F2, text='Hair Gel', font=('times new roman', 16, 'bold'),
                           bg=bg_color, fg='lightgreen').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        hair_gel_txt = Entry(F2, width=10,textvariable = self.hair_gel, font=('times new roman', 16, "bold"),
                             bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10, sticky='w')

        body_loshan_l = Label(F2, text='Body Loshon', font=('times new roman', 16, 'bold'),
                              bg=bg_color, fg='lightgreen').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        body_loshan_txt = Entry(F2, width=10,textvariable = self.body_loshon, font=('times new roman', 16, "bold"), bd=5, relief=SUNKEN).grid(
            row=5, column=1, padx=10, pady=10, sticky='w')




        # =================     grocery frame
        F3 = LabelFrame(self.root, text='Grocery', fg='gold', font=(
            'times new roman', 15, 'bold'), bd=12, relief=GROOVE, bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        rice_l = Label(F3, text='Rice', font=('times new roman', 16, 'bold'), bg=bg_color,
                       fg='lightgreen').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        rice_txt = Entry(F3, width=10,textvariable = self.rice, font=('times new roman', 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10, sticky='w')

        food_oil_l = Label(F3, text='Food Oil', font=('times new roman', 16, 'bold'),
                           bg=bg_color, fg='lightgreen').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        food_oil_txt = Entry(F3, width=10,textvariable = self.food_oil, font=('times new roman', 16, "bold"),
                             bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10, sticky='w')

        daal_l = Label(F3, text='Daal', font=('times new roman', 16, 'bold'), bg=bg_color,
                       fg='lightgreen').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        daal_txt = Entry(F3, width=10,textvariable = self.daal, font=('times new roman', 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10, sticky='w')

        wheat_l = Label(F3, text='Wheat', font=('times new roman', 16, 'bold'), bg=bg_color,
                        fg='lightgreen').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        wheat_txt = Entry(F3, width=10,textvariable = self.wheat, font=('times new roman', 16, "bold"), bd=5, relief=SUNKEN).grid(
            row=3, column=1, padx=10, pady=10, sticky='w')

        suger_l = Label(F3, text='Suger', font=('times new roman', 16, 'bold'), bg=bg_color,
                        fg='lightgreen').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        suger_txt = Entry(F3, width=10,textvariable = self.suger, font=('times new roman', 16, "bold"), bd=5, relief=SUNKEN).grid(
            row=4, column=1, padx=10, pady=10, sticky='w')

        tea_l = Label(F3, text='Tea', font=('times new roman', 16, 'bold'), bg=bg_color,
                      fg='lightgreen').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        tea_txt = Entry(F3, width=10,textvariable = self.tea, font=('times new roman', 16, "bold"), bd=5,
                        relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10, sticky='w')




        # =================     cold drink frame
        F4 = LabelFrame(self.root, text='Cold Drinks', fg='gold', font=(
            'times new roman', 15, 'bold'), bd=12, relief=GROOVE, bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        maza_l = Label(F4, text='Maza', font=('times new roman', 16, 'bold'), bg=bg_color,
                       fg='lightgreen').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        maza_txt = Entry(F4, width=10,textvariable = self.maza, font=('times new roman', 16, "bold"), bd=5,
                         relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10, sticky='w')

        coka_cola_l = Label(F4, text='Coka Cola', font=('times new roman', 16, 'bold'),
                            bg=bg_color, fg='lightgreen').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        coka_cola_txt = Entry(F4, width=10,textvariable = self.coke, font=('times new roman', 16, "bold"), bd=5, relief=SUNKEN).grid(
            row=1, column=1, padx=10, pady=10, sticky='w')

        frooti_l = Label(F4, text='Frooti', font=('times new roman', 16, 'bold'), bg=bg_color,
                         fg='lightgreen').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        frooti_txt = Entry(F4, width=10,textvariable = self.frooti, font=('times new roman', 16, "bold"), bd=5, relief=SUNKEN).grid(
            row=2, column=1, padx=10, pady=10, sticky='w')

        thumbs_up_l = Label(F4, text='Thumbs Up', font=('times new roman', 16, 'bold'),
                            bg=bg_color, fg='lightgreen').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        thumbs_up_txt = Entry(F4, width=10,textvariable = self.thumbsup, font=('times new roman', 16, "bold"), bd=5, relief=SUNKEN).grid(
            row=3, column=1, padx=10, pady=10, sticky='w')

        limca_l = Label(F4, text='Limca', font=('times new roman', 16, 'bold'), bg=bg_color,
                        fg='lightgreen').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        limca_txt = Entry(F4, width=10,textvariable = self.limca, font=('times new roman', 16, "bold"), bd=5, relief=SUNKEN).grid(
            row=4, column=1, padx=10, pady=10, sticky='w')

        sprite_l = Label(F4, text='Sprite', font=('times new roman', 16, 'bold'), bg=bg_color,
                         fg='lightgreen').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        sprite_txt = Entry(F4, width=10,textvariable = self.sprite, font=('times new roman', 16, "bold"), bd=5, relief=SUNKEN).grid(
            row=5, column=1, padx=10, pady=10, sticky='w')

        
        #=============Bill Area========

        F5 = Frame(self.root,bd=10, relief=GROOVE,)
        F5.place(x=1010, y=180, width=370,height = 380)
        bill_title = Label(F5,text = 'Bill Area',font = 'arial 15 bold',bd= 7,relief = GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5,orient = VERTICAL)
        self.textarea = Text(F5,yscrollcommand = scrol_y.set)
        scrol_y.pack(side = RIGHT,fill =Y)
        scrol_y.config(command = self.textarea.yview)
        self.textarea.pack(fill= BOTH)



        #=========button frame=====
        F6 = LabelFrame(self.root, text='Billing Menu', fg='gold', font=(
            'times new roman', 15, 'bold'), bd=12, relief=GROOVE, bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl=Label(F6,text = 'Total Cosmetic Price',bg=bg_color,fg='lightgreen',font=('times new roman', 14, 'bold')).grid(row=0,column=0,padx=20,pady=1,sticky='w')
        m1_txt = Entry(F6,font='arial 10 bold',textvariable = self.cosmetic_price,bd=7,relief=SUNKEN,width=18).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text = 'Total Grocery Price',bg=bg_color,fg='lightgreen',font=('times new roman', 14, 'bold')).grid(row=1,column=0,padx=20,pady=1,sticky='w')
        m2_txt = Entry(F6,font='arial 10 bold',textvariable = self.grocery_price,bd=7,relief=SUNKEN,width=18).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text = 'Total Cold Drinks Price',bg=bg_color,fg='lightgreen',font=('times new roman', 14, 'bold')).grid(row=2,column=0,padx=20,pady=1,sticky='w')
        m3_txt = Entry(F6,font='arial 10 bold',textvariable = self.cold_drink_price,bd=7,relief=SUNKEN,width=18).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text = 'Cosmetic Tax',bg=bg_color,fg='lightgreen',font=('times new roman', 14, 'bold')).grid(row=0,column=2,padx=20,pady=1,sticky='w')
        c1_txt = Entry(F6,font='arial 10 bold',textvariable = self.cosmetic_tax,bd=7,relief=SUNKEN,width=18).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text = 'Grocery Tax',bg=bg_color,fg='lightgreen',font=('times new roman', 14, 'bold')).grid(row=1,column=2,padx=20,pady=1,sticky='w')
        c2_txt = Entry(F6,font='arial 10 bold',bd=7,textvariable = self.grocery_tax,relief=SUNKEN,width=18).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text = 'Cold Drinks Tax',bg=bg_color,fg='lightgreen',font=('times new roman', 14, 'bold')).grid(row=2,column=2,padx=20,pady=1,sticky='w')
        c3_txt = Entry(F6,font='arial 10 bold',bd=7,textvariable = self.cold_drink_tax,relief=SUNKEN,width=18).grid(row=2,column=3,padx=10,pady=1)

        btn_f = Frame(F6,bd = 7, relief=GROOVE)
        btn_f.place(x=750,width=600,height=105)

        total_btn = Button(btn_f,command = self.total,text = 'Total',bg='cadetblue',fg='white',pady=15,bd=5,width=10,font='arial 15 bold').grid(row=0,column=0,padx=5,pady=5)
        generate_bill_btn = Button(btn_f,command = self.bill_ar,text = 'Generate Bill',bg='cadetblue',fg='white',pady=15,bd=5,width=10,font='arial 15 bold').grid(row=0,column=1,padx=5,pady=5)
        clear_btn = Button(btn_f,command = self.clear_data,text = 'Clear',bg='cadetblue',fg='white',pady=15,bd=5,width=10,font='arial 15 bold').grid(row=0,column=2,padx=5,pady=5)
        exit_btn = Button(btn_f,command = self.exit_app,text = 'Exit',bg='cadetblue',fg='white',pady=15,bd=5,width=10,font='arial 15 bold').grid(row=0,column=3,padx=5,pady=5)

        self.welcome_bill()

    def total(self):
        self.c_s = self.soap.get()*40
        self.c_fc = self.face_cream.get()*120
        self.c_fw = self.face_wash.get()*60
        self.c_hs = self.hair_spray.get()*180
        self.c_hg = self.hair_gel.get()*140
        self.c_bl = self.body_loshon.get()*180

        self.total_cosmetic_price = float(
            self.c_s+
            self.c_fc+
            self.c_fw+
            self.c_hs+
            self.c_hg+
            self.c_bl
        )
        self.cosmetic_price.set('Rs. '+str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price*0.18),2)
        self.cosmetic_tax.set('Rs. '+str(self.c_tax))

        self.g_r = self.rice.get()*80
        self.g_f = self.food_oil.get()*180
        self.g_d  = self.daal.get()*60
        self.g_w  = self.wheat.get()*240
        self.g_s  = self.suger.get()*45
        self.g_t  = self.tea.get()*150
        self.total_grocery_price = float(
            self.g_r +
            self.g_f +
            self.g_d +
            self.g_w +
            self.g_s +
            self.g_t 
        )
        self.grocery_price.set('Rs. '+str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.05),2)
        self.grocery_tax.set('Rs. '+str(self.g_tax))


        self.d_m = self.maza.get()*60
        self.d_c = self.coke.get()*60
        self.d_f = self.frooti.get()*50
        self.d_t = self.thumbsup.get()*45
        self.d_l = self.limca.get()*40
        self.d_s = self.sprite.get()*60
        self.total_cold_drink_price = float(
            self.d_m +
            self.d_c +
            self.d_f +
            self.d_t +
            self.d_l +
            self.d_s 
        )
        self.cold_drink_price.set('Rs. '+str(self.total_cold_drink_price))
        self.d_tax = round((self.total_cold_drink_price*0.12),2)
        self.cold_drink_tax.set('Rs. '+str(self.d_tax))
    
        self.total_bill = float(self.total_cosmetic_price + self.c_tax + self.total_grocery_price + self.g_tax + self.total_cold_drink_price + self.d_tax)


    def welcome_bill(self):

        self.textarea.delete('1.0',END)         # for deleting previous data

        self.textarea.insert(END,'\tWelcome Ravinder Shop    \n')
        self.textarea.insert(END,f'\n Bill Number : {self.bill_no.get()}')
        self.textarea.insert(END,f'\n Customer Name : {self.c_name.get()}')
        self.textarea.insert(END,f'\n Phone Number : {self.c_phone.get()}')
        self.textarea.insert(END,f'\n=========================================')
        self.textarea.insert(END,f'\n Products\t\tQty\t\tPrice')
        self.textarea.insert(END,f'\n=========================================')



    def bill_ar(self):
        if self.c_name.get() == '' or self.c_phone.get() == '':
            messagebox.showerror('Error','Customer details are must')
        elif self.cosmetic_price.get()=='Rs. 0.0' and self.grocery_price.get()=='Rs. 0.0' and self.cold_drink_price.get()=='Rs. 0.0':
            messagebox.showerror('Error',"No Product Purchased")

        else:

            self.welcome_bill()

            #========cosmetics=====
            if self.soap.get() != 0:
                self.textarea.insert(END,f'\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s}')
            if self.face_cream.get() != 0:
                self.textarea.insert(END,f'\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc}')
            if self.face_wash.get() != 0:
                self.textarea.insert(END,f'\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw}')
            if self.hair_spray.get() != 0:
                self.textarea.insert(END,f'\n Hair Spray\t\t{self.hair_spray.get()}\t\t{self.c_hs}')
            if self.hair_gel.get() != 0:
                self.textarea.insert(END,f'\n Hair Gel\t\t{self.hair_gel.get()}\t\t{self.c_hg}')
            if self.body_loshon.get() != 0:
                self.textarea.insert(END,f'\n Body Loshon\t\t{self.body_loshon.get()}\t\t{self.c_bl}')
            #========Grocery=====
            if self.rice.get() != 0:
                self.textarea.insert(END,f'\n Rice\t\t{self.rice.get()}\t\t{self.g_r}')
            if self.food_oil.get() != 0:
                self.textarea.insert(END,f'\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f}')
            if self.daal.get() != 0:
                self.textarea.insert(END,f'\n Daal\t\t{self.daal.get()}\t\t{self.g_d}')
            if self.wheat.get() != 0:
                self.textarea.insert(END,f'\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w}')
            if self.suger.get() != 0:
                self.textarea.insert(END,f'\n Suger\t\t{self.suger.get()}\t\t{self.g_s}')
            if self.tea.get() != 0:
                self.textarea.insert(END,f'\n Tea\t\t{self.tea.get()}\t\t{self.g_t}')
            #========cold drink=====
            if self.maza.get() != 0:
                self.textarea.insert(END,f'\n Maza\t\t{self.maza.get()}\t\t{self.d_m}')
            if self.coke.get() != 0:
                self.textarea.insert(END,f'\n Coca Cola\t\t{self.coke.get()}\t\t{self.d_c}')
            if self.frooti.get() != 0:
                self.textarea.insert(END,f'\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f}')
            if self.thumbsup.get() != 0:
                self.textarea.insert(END,f'\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.d_t}')
            if self.limca.get() != 0:
                self.textarea.insert(END,f'\n Limca\t\t{self.limca.get()}\t\t{self.d_l}')
            if self.sprite.get() != 0:
                self.textarea.insert(END,f'\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s}')
            
            self.textarea.insert(END,f'\n-----------------------------------------')
            if self.cosmetic_tax.get() != 'Rs. 0.0':
                self.textarea.insert(END,f'\n Cosmetic Tax : \t\t\t{self.cosmetic_tax.get()}')
            if self.grocery_tax.get() != 'Rs. 0.0':
                self.textarea.insert(END,f'\n Grocery Tax : \t\t\t{self.grocery_tax.get()}')
            if self.cold_drink_tax.get() != 'Rs. 0.0':
                self.textarea.insert(END,f'\n Cold drink Tax : \t\t\t{self.cold_drink_tax.get()}')

            self.textarea.insert(END,f'\n Total Bill: \t\t\tRs. {self.total_bill}')
            self.textarea.insert(END,f'\n-----------------------------------------')
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno('Save Bill','Do you want to save Bill?')
        if op>0:

            self.bill_data = self.textarea.get('1.0',END)
            f1 = open('bills/'+str(self.bill_no.get())+'.txt','w')
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo('Saved',f'Bill no. {self.bill_no.get()} saved successfully!!')
        else:
            return
    
    def find_bill(self):
        present = 'no'
        for i in os.listdir('bills/'):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f'bills/{i}','r')
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                present = 'yes'
        
        if present=='no':
            messagebox.showerror('Error','Invalid Bill No.\t')

    def clear_data(self):
        op = messagebox.askyesno('Clear',"Do you really want to Clear?")
        if op>0:
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_spray.set(0)
            self.hair_gel.set(0)
            self.body_loshon.set(0)

            #========grocery=====
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.suger.set(0)
            self.tea.set(0)

            #======cold drink=======

            self.maza.set(0)
            self.coke.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            # ==========total price & tax =========

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            #===========customer ==========
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno('Exit',"Do you really want to Exit?")
        if op>0:
            self.root.destroy()






root = Tk()
root.maxsize(1380,700)
obj = Bill_app(root)


root.mainloop()
