# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 23:44:05 2017

@author: Aaron(Linghou) Kong, Qiu Jin, Yuexi Jiang
"""


import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import *
import re
from datetime import datetime
import random
import sys
import os

LARGE_FONT = ("Veranda", 18)


trackingNoList = []
class DataBaseapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        
        self.title("DataBase app")
        container = tk.Frame(self)
        
        container.pack(side="top",fill="both",expand = True)
        
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames = {}
        for F in (StartPage,PageOne,PageTwo,cRegister,AgentPage,CustomerUI):
            frame = F(container,self)
            
            self.frames[F] = frame
            
            frame.grid(row = 0, column = 0, sticky="nsew")
        
        self.show_frame(StartPage)
    
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
    def get_page(self, page_class):
        return self.frames[page_class]
    
        

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        
        label = tk.Label(self, text="You are logging in as:")
        label.pack(pady=20,padx=20)
        
        button1 = tk.Button(self, text="Agent", 
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()
        
        button2 = tk.Button(self, text="Customer",
                            command = lambda: controller.show_frame(PageTwo))
        button2.pack()
        
        
        

class PageOne(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        
        label = tk.Label(self, text="Agent Login")
        
        label.grid(sticky="E")
        
        
        nameL = tk.Label(self, text='UserID: ') 
        pwordL = tk.Label(self, text='Password: ')
        nameL.grid(row=1, sticky="W")
        pwordL.grid(row=2, sticky="W")
        
        self.idaEntry = ttk.Entry(self) 
        self.paEntry = ttk.Entry(self, show='*')
        
        self.idaEntry.grid(row=1, column=1)
        self.paEntry.grid(row=2, column=1)
     
        loginB = tk.Button(self, text='Login', command = lambda: self.agentCheckLogin(self.idaEntry,self.paEntry)) 
        loginB.grid(columnspan=2, sticky="W")
        ReturnButton = tk.Button(self, text="Close", 
                            command=lambda: controller.show_frame(StartPage))
        
        ReturnButton.grid(row=6, sticky="W")
     def agentCheckLogin(self,IDAgent,pwordAgent):
        
        agent_id = IDAgent.get()
        agent_pwd = pwordAgent.get()
        #conn = sqlite3.connect('./pronew.db')
        conn = sqlite3.connect(Database_name)
        login_checker_curser1 = conn.cursor()
        if ((re.match("^[A-Za-z0-9_]*$",agent_id)) and (re.match("^[A-Za-z0-9_]*$",agent_pwd))):
            login_checker_curser1.execute("SELECT*FROM agents WHERE aid=? and pwd=?;", (agent_id,agent_pwd))
            rows_checker1 = login_checker_curser1.fetchall()
        #####################################################################
        ####################################################################
            if (len(rows_checker1) == 1):
                self.controller.show_frame(AgentPage)
        ####################################################################
        ######################################################################
            else:
                r = Tk()
                r.title('D:')
                r.geometry('200x100')
                rlbl = Label(r, text='\n[!] Invalid Login')
                rlbl.pack()
                r.mainloop()
            
        else:
            r = Tk()
            r.geometry('200x200')
            rlbl = Label(r, text='\n[!] Invalid Login\nNo special character such as space')
            rlbl.pack()
            r.mainloop()
            
        

class PageTwo(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        
        label = tk.Label(self, text="Customer Login")
       
        label.grid(sticky="E")
        
        
        
        nameL = tk.Label(self, text='UserID: ') 
        pwordL = tk.Label(self, text='Password: ')
        nameL.grid(row=1, sticky="W")
        pwordL.grid(row=2, sticky="W")
        
        self.idEntry = ttk.Entry(self) 
        self.pEntry = ttk.Entry(self, show='*')
        
        self.idEntry.grid(row=1, column=1)
        self.pEntry.grid(row=2, column=1)
     
        loginB = tk.Button(self, text='Login', command = lambda: self.customerCheckLogin(self.idEntry,self.pEntry)) 
        loginB.grid(columnspan=2, sticky="W")
        
        loginC = tk.Button(self, text="Register", 
                           command = lambda: controller.show_frame(cRegister))
        loginC.grid(columnspan=2,sticky="W")
        ReturnButton = tk.Button(self, text="Close", 
                            command=lambda: controller.show_frame(StartPage))
        
        ReturnButton.grid(row=6, sticky="W")
        
        
        
        


     def customerCheckLogin(self,IDCustomer,pwordCustomer):
        
        customer_id = IDCustomer.get()
        customer_pwd = pwordCustomer.get()
        
        
        
        #conn1 = sqlite3.connect('./pronew.db')
        conn1 = sqlite3.connect(Database_name)
        login_checker_curser2 = conn1.cursor()
        if ((re.match("^[A-Za-z0-9_]*$",customer_id)) and (re.match("^[A-Za-z0-9_]*$",customer_pwd))):
            login_checker_curser2.execute("SELECT*FROM customers WHERE cid=? and pwd=?;", (customer_id,customer_pwd))
            rows_checker2 = login_checker_curser2.fetchall()
        ##########################################################################################
        #####################################################################################
            if (len(rows_checker2) == 1):
                
               self.controller.show_frame(CustomerUI)
               
        ##################################################################################
        #################################################################################
            elif(len(rows_checker2) != 1):
                r = Tk()
                r.geometry('200x100')
                rlbl = Label(r, text='\n[!] Invalid Login')
                rlbl.pack()
                r.mainloop()
            
        else:
            r = Tk()
            r.geometry('300x300')
            rlbl = Label(r, text='\n[!] Invalid Login\n No special character such as space')
            rlbl.pack()
            r.mainloop()

   
    

class cRegister(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Please fill the following information")
        #label.pack(pady=10,padx=10)
        label.grid(sticky="E")
        global idCustomer
        global nameCustomer
        global addressCustomer
        global npwordCustomer
        
        idL = tk.Label(self, text="UserID: ")
        nameL = tk.Label(self,text="UserName")
        addressL = tk.Label(self,text="Addresss")
        pwordL = tk.Label(self, text="Password: ")
        
        idL.grid(row=1,sticky="W")
        nameL.grid(row=2, sticky="W")
        addressL.grid(row=3,sticky="W")
        pwordL.grid(row=4, sticky="W")
        
        idCustomer = tk.Entry(self)
        nameCustomer = tk.Entry(self)
        addressCustomer = tk.Entry(self)
        npwordCustomer = tk.Entry(self)
        
        idCustomer.grid(row=1, column=1)
        nameCustomer.grid(row=2, column=1)
        addressCustomer.grid(row=3, column=1)
        npwordCustomer.grid(row=4, column=1)
        rgA = tk.Button(self, text='Go Login', command=lambda: controller.show_frame(PageTwo))
        rgA.grid(row=5,sticky="W")
        rgB = tk.Button(self, text='Register', command=self.customerRegisterLogin) 
        rgB.grid(row=6, sticky="W")
        


    def customerRegisterLogin(self):
        customer_newid = idCustomer.get()
        customer_newname = nameCustomer.get()
        customer_newaddrs = addressCustomer.get()
        customer_newpwd = npwordCustomer.get()
        #conn = sqlite3.connect('./pronew.db')
        conn = sqlite3.connect(Database_name)
        rg_checker_curser = conn.cursor()
        if ((customer_newid != '') and (customer_newname != '') and (customer_newaddrs != '') and (customer_newpwd != '')):
            if ((re.match("^[A-Za-z0-9_]*$",customer_newid)) and (re.match("^[A-Za-z0-9_]*$",customer_newpwd))):
                rg_checker_curser.execute("SELECT*FROM customers WHERE cid='%s';" % (customer_newid))
                rows_rg = rg_checker_curser.fetchall()
                if (len(rows_rg) == 0):
                    rg_checker_curser.execute("INSERT INTO customers VALUES('%s','%s','%s','%s');" %(customer_newid,customer_newname,customer_newaddrs,customer_newpwd))
                    conn.commit()
                    conn.close()
                    r = Tk()
                    r.geometry('200x200')
                    rlbl = Label(r, text='\n:D Successfully registered\n Please go back to login page')
                    rlbl.pack()
                    r.mainloop()
                else:
                    r = Tk()
                    r.geometry('300x300')
                    rlbl = Label(r, text='\n[!] User ID already exist')
                    rlbl.pack()
                    r.mainloop()
            else:
                r = Tk()
                r.geometry('300x300')
                rlbl = Label(r, text='\n[!] Invalid Register\n No special character such as space in ID and Password')
                rlbl.pack()
                r.mainloop()
        else:
            r = Tk()
            rlbl = Label(r, text='\n[!] Invalid Register\nPlease fill all fields')
            rlbl.pack()
            r.mainloop()

        
        
        
        
           
        
    
####above comment want to use this instead
#################################################################################################

class AgentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        

        label1 = tk.Label(self, text="Agent User Interface")
        label1.grid(sticky="W")
        
        btnA = tk.Button(self, text='Set up a delivery',
        	command = self.DeliverySetUp)
        btnA.grid(columnspan=2, sticky="W")

        btnB = tk.Button(self, text='Update a delivery',
        	command = self.DeliveryUpdate)
        btnB.grid(columnspan=2, sticky="W")
        
        btnC = tk.Button(self,text='Edit Stocks',
                         command = self.StockUpdate)
        btnC.grid(columnspan=2, sticky='W')
        
        button1 = tk.Button(self, text="Log Out", 
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(sticky="W")

		# btnC = tk.Button(self, text='Add to stock')
		# btnC.grid(columnspan=2, sticky="W")
	
    # set up delivery child window
    # define tracing number which is the largest index of delivery plus 1 
    def DeliverySetUp(self):
        # Delivery set up window is the child window of agent page
        self.DeliverySetUpWindow = tk.Toplevel(master = self, width = 1000, height = 1000)
        
        global trackingNo
        # conn_delivery = sqlite3.connect('./pronew.db')
        # delivery_cursor = conn_delivery.cursor()
        # delivery_cursor.execute("SELECT * FROM deliveries ORDER BY trackingNo DESC LIMIT 1")
        # result = delivery_cursor.fetchone()
        # trackingNo = result[0] + 1
        # conn_delivery.close()
        #trackingNo = random.randint(1, 100)
        tmpNo = random.randint(1, 1000)
        while 1:
            if tmpNo not in trackingNoList:
                trackingNo = tmpNo
                trackingNoList.append(trackingNo)
                break
            else:
                tmpNo = random.randint(1, 100)
        
    
        
        self.rlbl= tk.Label(self.DeliverySetUpWindow,text='\nThe generated trackingNo is '+str(trackingNo))
        self.rlbl.grid(columnspan=2, sticky="W")

        # define a button to go to add order page
        self.SetUpBtnA = tk.Button(self.DeliverySetUpWindow, text='Search Order', 
            command = self.AddOrder)
        self.SetUpBtnA.grid(columnspan=2, sticky="W")

    # Let user enter an order id to insert it into delivery
    def AddOrder(self):
        self.AddOrderWindow = tk.Toplevel(master = self.DeliverySetUpWindow)


        self.orderLabel = tk.Label(self.AddOrderWindow, text='Orders are shown below:')
        self.orderLabel.grid(sticky="W")

        #conn_delivery = sqlite3.connect('./pronew.db')
        conn_delivery = sqlite3.connect(Database_name)
        delivery_cursor = conn_delivery.cursor()
        # query all the data achieved by tracking number
        delivery_cursor.execute('SELECT*FROM orders;')
        order_result = delivery_cursor.fetchall()
        conn_delivery.commit()
        conn_delivery.close()


        l = Listbox(self.AddOrderWindow, height=5, width=20)
        l.grid(column=0, row=0, sticky=(N,W,E,S))
        # s = tk.Scrollbar(self.l, orient=VERTICAL, command=l.yview)
        # s.grid(column=1, row=0, sticky=(N,S))
        # l['yscrollcommand'] = s.set
        # ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        for each in order_result:
            l.insert('end', each)

        # get order_id from user input 
        global IdOrder
        self.label = tk.Label(self.AddOrderWindow, text='Enter Order ID:')
        self.label.grid(sticky="W")
        IdOrder = tk.Entry(self.AddOrderWindow)
        IdOrder.grid(sticky="E")

        # Click on edit delivery to set pickup time
        self.editDelivery = tk.Button(self.AddOrderWindow, text='Edit Delivery', command = self.EditDelivery)
        self.editDelivery.grid(columnspan=2, sticky="W")

    # Choose pickup time 
    def EditDelivery(self):
        self.EditDeliveryWindow = tk.Toplevel(master = self.AddOrderWindow,width = 100, height = 100)
        global order_id
        global pickUpTimeEnter
        order_id = IdOrder.get()
        order_id = int(order_id)
        
        # Enter pick up time and record
        self.pickUpLabel = tk.Label(self.EditDeliveryWindow, text='Enter Pickup Time:\n Use %Y-%m-%d %H:%M:%S format')
        self.pickUpLabel.pack()
        pickUpTimeEnter = tk.Entry(self.EditDeliveryWindow)
        pickUpTimeEnter.pack()

        # Once confirm, user cannot click on it again.
        self.confirmBtn = tk.Button(self.EditDeliveryWindow, text='Confirm', command = self.ConfirmDelivery)
        self.confirmBtn.pack()

    def ConfirmDelivery(self):
        pickUpTime = pickUpTimeEnter.get()
        # get pick up time 
        # If the time isn't null, use striptime to change its value to datetime format
        if pickUpTime == "":
        	date = None
        else:
            date = datetime.strptime(pickUpTime, '%Y-%m-%d %H:%M:%S')
        dropOffTime = None
        #conn_delivery = sqlite3.connect('./pronew.db')
        conn_delivery = sqlite3.connect(Database_name)
        delivery_cursor = conn_delivery.cursor()
        order_information = (trackingNo, order_id, date, dropOffTime)
        # insert all the data achieved before into deliveries
        delivery_cursor.execute('INSERT INTO deliveries (trackingNo, oid, pickUpTime, dropOffTime) VALUES (?,?,?,?);', order_information)
        conn_delivery.commit()
        conn_delivery.close()
        # The window should be closed
        r = Tk()
        r.geometry('200x100')
        rlbl = Label(r, text='\n Successful!')
        rlbl.pack()
        # self.ConfirmDeliveryWindow.destroy()
        r.mainloop()

    # Update delivery window define
    def DeliveryUpdate(self):
        self.DeliveryUpdateWindow = tk.Toplevel(master = self, width = 1000, height = 1000)
        self.label = tk.Label(self.DeliveryUpdateWindow, text='Enter Tracking Number:')
        self.label.grid(sticky="W")
        
        # Let user enter an delivery id(trackingNo)
        global IdDelivery
        IdDelivery = tk.Entry(self.DeliveryUpdateWindow)
        IdDelivery.grid(sticky="E")
        self.updateDelivery = tk.Button(self.DeliveryUpdateWindow, text='Update Delivery', command = self.UpdateADelivery)
        self.updateDelivery.grid(columnspan=2, sticky="W")

    # Show all the results from the specific delivery given its tracking number
    # Let user select operation 
    def UpdateADelivery(self):
        self.UpdateDeliveryWindow = tk.Toplevel(master = self.DeliveryUpdateWindow, width = 1000, height = 1000)
        global delivery_id
        global delivery_result
        global OrderCurrent
        delivery_id = IdDelivery.get()
        track_number = int(delivery_id)
        #conn_delivery = sqlite3.connect('./pronew.db')
        conn_delivery = sqlite3.connect(Database_name)
        delivery_cursor = conn_delivery.cursor()
        delivery_cursor.execute('SELECT * FROM deliveries WHERE trackingNo=?;', (track_number,))
        delivery_result = delivery_cursor.fetchall()
        print(delivery_result)
        # fetch all the result from the tracking number
        # loop
        for each in delivery_result:
            self.text = tk.Text(self.UpdateDeliveryWindow, height=3)
            self.text.grid(sticky="W")
            self.text.insert(1.0, each)
        conn_delivery.commit()
        conn_delivery.close()

        self.selectOrderLabel = tk.Label(self.UpdateDeliveryWindow, text='Enter Order ID:')
        self.selectOrderLabel.grid(sticky="W")
        OrderCurrent = tk.Entry(self.UpdateDeliveryWindow)
        OrderCurrent.grid(sticky="E")


        self.btnModify = tk.Button(self.UpdateDeliveryWindow, text="Pick Up", command = self.SelectPickUpTime)
        self.btnModify.grid(columnspan=2, sticky = "W")
        self.btnRemove = tk.Button(self.UpdateDeliveryWindow, text="Remove", command = self.RemoveOrder)
        self.btnRemove.grid(columnspan=2, sticky = "E")
        
        


    # Enter pickup and dropoff time
    def SelectPickUpTime(self):
        self.SelectPickUpWindow = tk.Toplevel(master = self.UpdateDeliveryWindow, width = 1000, height = 1000)
        global updatePickUpTimeEn
        global updateDropOffTimeEn


        self.pickUpLabel = tk.Label(self.SelectPickUpWindow, text='Enter Pickup Time:')
        self.pickUpLabel.grid(sticky="W")
        updatePickUpTimeEn = tk.Entry(self.SelectPickUpWindow)
        updatePickUpTimeEn.grid(sticky="E")

        self.dropOffLabel = tk.Label(self.SelectPickUpWindow, text='Enter Dropoff Time:')
        self.dropOffLabel.grid(sticky="W")
        updateDropOffTimeEn = tk.Entry(self.SelectPickUpWindow)
        updateDropOffTimeEn.grid(sticky="E")

        # click on confirm button to update the data
        self.confirmBtn = tk.Button(self.SelectPickUpWindow, text='Confirm', command = self.UpdateTime)
        self.confirmBtn.grid(columnspan=2, sticky="W")

    # Do database update
    # If user doesn't enter the time, it'll be set to null
    def UpdateTime(self):
        current_oid = int(OrderCurrent.get())
        pickUpTime = updatePickUpTimeEn.get()
        if pickUpTime == "":
            pickUpdate = None
        else:
            pickUpdate = datetime.strptime(pickUpTime, '%Y-%m-%d %H:%M:%S')
        dropOffTime = updateDropOffTimeEn.get()
        if dropOffTime == "":
            dropOffdate = None
        else:
            dropOffdate = datetime.strptime(dropOffTime, '%Y-%m-%d %H:%M:%S')
        
        #conn_delivery = sqlite3.connect('./pronew.db')
        conn_delivery = sqlite3.connect(Database_name)
        delivery_cursor = conn_delivery.cursor()
        delivery_cursor.execute('UPDATE deliveries SET pickUpTime=?, dropOffTime=? WHERE trackingNo=? and oid=?;', (pickUpdate, dropOffdate, delivery_id, current_oid))
        # Once update, shoud it be removed?
        # delivery_cursor.execute('DELETE FROM deliveries WHERE trackingNo=? and oid=?;', (delivery_id, current_order_id))
        conn_delivery.commit()
        conn_delivery.close()
        r = Tk()
        r.geometry('200x100')
        rlbl = Label(r, text='\n Successful!')
        rlbl.pack()
        r.mainloop()
    
    # Remove order
    def RemoveOrder(self):
        current_oid = int(OrderCurrent.get())
        #conn_delivery = sqlite3.connect('./pronew.db')
        conn_delivery = sqlite3.connect(Database_name)
        delivery_cursor = conn_delivery.cursor()
        delivery_cursor.execute('DELETE FROM deliveries WHERE trackingNo=? and oid=?;', (delivery_id, current_oid))
        conn_delivery.commit()
        conn_delivery.close()
        r = Tk()
        r.geometry('200x100')
        rlbl = Label(r, text='\n Successful!')
        rlbl.pack()
        r.mainloop()
       
    def StockUpdate(self):
        self.StockUpWindow = tk.Toplevel(master = self, width = 1000, height = 1000)
        global sidEntry,pidEntry,qtyEntry,prEntry
        sL = tk.Label(self.StockUpWindow, text='Store ID: ') 
        pL = tk.Label(self.StockUpWindow, text='Product ID: ')
        ql = tk.Label(self.StockUpWindow, text='Quantity to be added')
        prl = tk.Label(self.StockUpWindow, text='Unit price alter')
        sL.grid(row=1, sticky="W")
        pL.grid(row=2, sticky="W")
        ql.grid(row=3, sticky="W")
        prl.grid(row=4, sticky="W")
        
        sidEntry = ttk.Entry(self.StockUpWindow) 
        pidEntry = ttk.Entry(self.StockUpWindow)
        qtyEntry = ttk.Entry(self.StockUpWindow)
        prEntry = ttk.Entry(self.StockUpWindow)
        
        sidEntry.grid(row=1, column=1)
        pidEntry.grid(row=2, column=1)
        qtyEntry.grid(row=3, column=1)
        prEntry.grid(row=4, column=1)
        
        
        self.btnA = tk.Button(self.StockUpWindow, text='Confirm',
        	command = self.StockShow)
        self.btnA.grid(columnspan=2, sticky="W")
    	
    
    def StockShow(self):
        self.StockShowWindow = tk.Toplevel(master = self.StockUpWindow)
        sidValue = sidEntry.get()
        pidValue = pidEntry.get()
        qtyValue = qtyEntry.get()
        prValue = prEntry.get()
        #conn_stock = sqlite3.connect('./pronew.db')
        conn_stock = sqlite3.connect(Database_name)
        stock_cursor1 = conn_stock.cursor()
        updata_cursor = conn_stock.cursor()
        sidtake_cursor = conn_stock.cursor()
        sidtake_cursor.execute("SELECT * FROM carries WHERE sid = ?;",(sidValue))
        rows_sid = sidtake_cursor.fetchall()
        stock_cursor1.execute("SELECT * FROM carries WHERE sid = ? AND pid = ?;", (sidValue,pidValue))
        rows_rg1 = stock_cursor1.fetchall()
        newqtyValue = None
        sid_list = []
        for each in rows_sid:
            sid_list. append(each[1])
        
        if (pidValue not in sid_list):
            if (qtyValue == ""):
                newqtyValue = ""
            else:
            
                newqtyValue = int(qtyValue)
            
            updata_cursor.execute("INSERT INTO carries (sid, pid, qty, uprice) VALUES (?,?,?,?);", (sidValue,pidValue,newqtyValue,prValue))
        else:  
            if (qtyValue == ""):
                qtyValue = 0	
        
            for each in rows_rg1:
                newqtyValue = int(qtyValue) + int(each[2])
            if (prValue == ''):
                for each in rows_rg1:
                    prValue = int(each[3])
            updata_cursor.execute("UPDATE carries SET qty=?, uprice=? WHERE sid=? and pid=?;", (newqtyValue, prValue, sidValue, pidValue))
        conn_stock.commit()
        stock_cursor = conn_stock.cursor()
        
        stockShowLbl = tk.Label(self.StockShowWindow,text=("The result is\n"))
        stockShowLbl.pack()
        
        cursorRead = conn_stock.cursor()
        cursorRead. execute("SELECT * FROM carries;")
        names = list(map(lambda x: x[0], cursorRead.description))
        namelb = tk.Label(self.StockShowWindow, text = ("%s   %s   %s   %s") % (names[0],names[1],names[2],names[3]) )
        namelb.pack()
        stock_cursor.execute("SELECT * FROM carries WHERE sid = ? AND pid = ?;", (sidValue,pidValue))
        rows_rg = stock_cursor.fetchall()
        for each in rows_rg:
            stockShowLb = tk.Label(self.StockShowWindow,text=("%s   %s   %s   %s") % (each[0],each[1],each[2],each[3]))
            stockShowLb.pack()
       
        
        
        
        
        
            

class CustomerUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label1 = tk.Label(self, text="Customer User Interface")
        label1.grid(sticky="W")
        
        
        buttonC = tk.Button(self, text='Search for Product', command =  self.SearchForProduct)
        buttonC.grid(sticky="W")
        buttonB = tk.Button(self, text='Place and order(After you fill the basket)', command = lambda:  self.PlaceOrderPage(basket_final))
        buttonB.grid(sticky="W")
        buttonA = tk.Button(self, text='List orders', command = self.ListOrderPage)
        buttonA.grid(sticky="W")
        
        
        
        
        button1 = tk.Button(self, text="Log Out", 
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(sticky="W")
    def SearchForProduct(self):
        global wdEntry
        self.SearchWindow = tk.Toplevel(master = self)
        spl = tk.Label(self.SearchWindow, text="Enter one or more keywords")
        spl.grid(row=1, sticky="W")
        
        wdEntry = ttk.Entry(self.SearchWindow)
        wdEntry.grid(row=1, column=1)
        
        spl1 = tk.Label(self.SearchWindow, text="Please use , to separate")
        spl1.grid(row=2, sticky="W")
        button1 = tk.Button(self.SearchWindow,text="confirm",command = self.SearchResult)
        button1 .grid(sticky = "W")
    
    def SearchResult(self):
        global selectENpid
        self.SearchRW = tk.Toplevel(master = self.SearchWindow)
        label = ttk.Label(self.SearchRW, text="Results", font=LARGE_FONT)
        label.pack(side="top")
        
        wdd = wdEntry.get()
        wddList = wdd.split(",")
        
        
        basket = []
        conn_list = sqlite3.connect(Database_name)
        searchCursor = conn_list.cursor()
        for wd in wddList:
            rows = searchCursor.execute("select pid, name, unit, count(carries.sid), count(case when carries.qty > 0 then 1 end), MIN(carries.uprice), min(case when carries.qty > 0 then carries.uprice end) from products left join carries using (pid) where name like ? group by pid", ('%' + wd + '%',))
        
        self.row_list = rows.fetchall()
        
        label2 = ttk.Label(self.SearchRW, text="PID|product name|unit|# of stores|# of stores has in stock |min price|min price of in stock")
        label2.pack()
        
        
        self.start_index = 0
        self.resListBox = tk.Listbox(self.SearchRW, width=100, height=5)
        self.resListBox.pack()
        for i in range(self.start_index, self.start_index + 5):
            try:
                item = self.row_list[i]
                self.resListBox.insert(END, item)
            except:
                pass
        if (len(self.row_list) > 5):
            nextButton = tk.Button(self.SearchRW, text="Next 5", command=lambda: self.updateIndex2(5))
            nextButton.pack()
            prevButton = tk.Button(self.SearchRW, text="Last 5", command=lambda: self.updateIndex2(-5))
            prevButton.pack()
            
            
        
        
        
        selectlpid = tk.Label(self.SearchRW,text="Please enter the ID of the product for details")
        selectlpid.pack()
        selectENpid = tk.Entry(self.SearchRW)
        selectENpid.pack()
        selectbtpid = tk.Button(self.SearchRW,text="Confirm", command = lambda: self.ShowDetail1(basket))
        selectbtpid.pack()
        
        
        ReturnButton = tk.Button(self.SearchRW, text="Close",
                                  command=lambda: self.SearchRW.destroy())
        ReturnButton.pack()
    def ShowDetail1(self,basket):
        self.detailShowWindow2 = tk.Toplevel(master = self.SearchRW,width=100, height=5)
        global selectENqty,selectENsid
        basket1 = basket
        choice_pid = selectENpid.get()
        conn_list = sqlite3.connect(Database_name)
        detailCursor = conn_list.cursor()
            
        row_detail = detailCursor.execute('''select carries.pid, products.name, unit, cat, stores.name, uprice, qty
                                   from products, stores, carries
                                   where products.pid = ? and products.pid = carries.pid and carries.sid = stores.sid
                                   order by qty=0, uprice''',
                                (choice_pid,))
        for each2 in row_detail.fetchall():
            detaillb1 = tk.Label(self.detailShowWindow2,text=("pid:'%s'\nname:'%s'\nunit:'%s'\ncat:'%s'\nstore name:'%s'\nuprice:'%s'\nqty:'%s'"%(each2[0],each2[1],each2[2],each2[3],each2[4],each2[5],each2[6])))
            detaillb1.grid(sticky = "N")
            
        selectlpid1 = tk.Label(self.detailShowWindow2,text="Would like to add this product to basket?")
        selectlpid1.grid(sticky = "W")
        selectlqty = tk.Label(self.detailShowWindow2,text="Please enter the qty of the product to add")
        selectlqty.grid(sticky = "W")
        selectENqty = tk.Entry(self.detailShowWindow2)
        selectENqty.grid(sticky = "W")
        selectlsid = tk.Label(self.detailShowWindow2,text="Please enter the store to add")
        selectlsid.grid(sticky = "W")
        selectENsid = tk.Entry(self.detailShowWindow2)
        selectENsid.grid(sticky = "W")
        selectbtpiddd = tk.Button(self.detailShowWindow2,text="Confirm", command = lambda: self.AddtoB(basket1))
        selectbtpiddd.grid(sticky = "W")
            
        ReturnButton = tk.Button(self.detailShowWindow2,text="Close", command=lambda: self.detailShowWindow2.destroy())
        ReturnButton.grid(sticky = "W")
    def AddtoB(self,basket1):
        
        global basket_final
        basket_final = basket1
        choice_qty = selectENqty.get()
        
        choice_pid = selectENpid.get()
        choice_sid = selectENsid.get()
        
        conn_list = sqlite3.connect(Database_name)
        addingCursor = conn_list.cursor()
        addingCursor.execute("select uprice from carries where pid = ? and sid = ?;", (choice_pid,choice_sid))
        add_list = addingCursor.fetchone()
        basket_final.append([choice_pid, choice_sid, choice_qty, add_list[0]])
        r = Tk()
        r.geometry('200x100')
        rlbl = Label(r, text='\n Successful!')
        rlbl.pack()
        r.mainloop()
        
        return basket_final
            
            
    def PlaceOrderPage(self,basket_final):
        self.placeWindow = tk.Toplevel(master = self)
        conn_list = sqlite3.connect(Database_name)
        cursor_place1 = conn_list.cursor()
        cursor_place1.execute("select * from orders order by oid DESC limit 1;")
        oid_list = cursor_place1.fetchone()
        oid_rec = oid_list[0]
        if (oid_rec is None):
            oid_rec = 0
            
        page2 = self.controller.get_page(PageTwo)
        customers_cid=page2.idEntry.get()
        #print(customers_cid)
        
        cursor_place2 = conn_list.cursor()
        cursor_place2.execute("select address from customers where cid = ?;",(customers_cid,))
        cursor_list = cursor_place2.fetchone()
        c_address = cursor_list[0]
        
        cursor_place2.execute("insert into orders values (?, ?, DATE('now'), ?);",(oid_rec +1, customers_cid,c_address))
        conn_list.commit()
        for item in basket_final:
            cursor_place2.execute("select qty from carries where pid=? and sid=?;",(item[0], item[1]))
            
            row = cursor_place2.fetchone()
            if int(item[2]) > row[0]:
                situation = tk.Label(self.placeWindow,text="The quantity for " + item[0] + " is greater than what your selected store carries.\n")
                situation.grid(sticky = "N")
                
                ButtonA = tk.Button(self.placeWindow,text="Change qty", command=lambda: self.changQty(basket_final,item,oid_rec,row))
                ButtonA.grid(sticky = "W")
                
                Buttonb = tk.Button(self.placeWindow,text="Delete Item", command=lambda: self.deleteQty(basket_final,item))
                Buttonb.grid(sticky = "W")
            else:
                cursor_place2.execute("insert into olines values (?,?,?,?,?)" , (oid_rec +1,item[1],item[0],item[2],item[3]))
                conn_list.commit()
                situation1 = tk.Label(self.placeWindow,text="Items in basket has been ordered")
                situation1.grid(sticky = "N")
    def changQty(self,basket_final,item,oid_rec,row):
        global changeNqty
        self.changeWindow = tk.Toplevel(master = self.placeWindow)
        situation2 = tk.Label(self.changeWindow,text="Please input the new quantity, new quantity must be equal to or less then " + str(row[0]))
        situation2.grid(sticky = "N")
        changeNqty = tk.Entry(self.changeWindow)
        changeNqty.grid(sticky = "W")
        
        Buttonc = tk.Button(self.changeWindow,text="confirm", command=lambda: self.succQty(basket_final,item,oid_rec))
        Buttonc.grid(sticky = "W")
    def succQty(self,basket_final,item,oid_rec):
        conn_list = sqlite3.connect(Database_name)
        cursor_place = conn_list.cursor()
        item[2] = int(changeNqty.get())
        cursor_place.execute("insert into olines values (?,?,?,?,?)", (oid_rec+1, item[1],item[0],item[2],item[3]))
        conn_list.commit()
        basket_final = []
        r = Tk()
        r.geometry('200x100')
        rlbl = Label(r, text='\n Successful!')
        rlbl.pack()
        r.mainloop()
        return basket_final
	 	  
	 
    def deleteQty(self,basket_final,item):
    	  basket_final = [x for x in basket_final if not item]
    	  return basket_final
                
    
                
                
        
        
        
        
        
    
    def ListOrderPage(self):
        global selecten
        self.listordershow = tk.Toplevel(master = self)
        label = ttk.Label(self.listordershow, text="Your Orders", font=LARGE_FONT)
        label.pack(side="top")
        
        page2 = self.controller.get_page(PageTwo)
        customers_cid=page2.idEntry.get()
        
        #conn_list = sqlite3.connect('./pronew.db')
        conn_list = sqlite3.connect(Database_name)
        clist_cursor = conn_list.cursor()
        clist_cursor.execute("Select oid, odate, sum(qty), round(sum(uprice*qty), 2) from orders left join olines using(oid) where cid = '%s' group by oid, odate order by date(odate) desc;" % customers_cid)
        self.result_list = clist_cursor.fetchall()
        
        self.start_index = 0
        self.resListBox = tk.Listbox(self.listordershow, width=100, height=5)
        self.resListBox.pack()
        
        for i in range(self.start_index, self.start_index + 5):
            try:
                item = self.result_list[i]
                self.resListBox.insert(END, item)
            except:
                pass
        if (len(self.result_list) > 5):
            nextButton = tk.Button(self.listordershow, text="Next 5", command=lambda: self.updateIndex(5))
            nextButton.pack()
            prevButton = tk.Button(self.listordershow, text="Last 5", command=lambda: self.updateIndex(-5))
            prevButton.pack()
        selectlb = tk.Label(self.listordershow,text="Please enter the ID of the order for details")
        selectlb.pack()
        selecten = tk.Entry(self.listordershow)
        selecten.pack()
        selectbt = tk.Button(self.listordershow,text="Confirm", command = self.ShowDetail)
        selectbt.pack()
        
        ReturnButton = tk.Button(self.listordershow, text="Close",
                                  command=lambda: self.listordershow.destroy())
        ReturnButton.pack()
    def ShowDetail(self):
        self.detailShowWindow = tk.Toplevel(master = self.listordershow,width=100, height=5)
        
        selection = selecten.get()
        #conn_detail = sqlite3.connect('./pronew.db')
        conn_detail = sqlite3.connect(Database_name)
        cdetail_cursor1 = conn_detail.cursor()
        cdetail_cursor2 = conn_detail.cursor()
        cdetail_cursor1.execute("select trackingno, pickUpTime, dropOffTime, address from orders left join deliveries using (oid) left join olines using (oid) where oid = '%s' ;" %(selection))
        select_row1 = cdetail_cursor1.fetchone()
        
        detaillb = ttk.Label(self.detailShowWindow,text=("The details are\ntrackingno:'%s'\npickUpTime:'%s'\ndropOffTime:'%s'\naddress:'%s'  \n"%(select_row1[0],select_row1[1],select_row1[2],select_row1[3])))
        detaillb.grid(sticky = "W")
        
        cdetail_cursor2.execute("select sid, stores.name, pid, products.name, qty, unit, uprice from olines left join stores using (sid) left JOIN products using (pid) where oid = '%s'" % (selection))
        select_row2 = cdetail_cursor2.fetchall()
        for each2 in select_row2:
            detaillb1 = tk.Label(self.detailShowWindow,text=("sid:'%s'\nstore name:'%s'\npid:'%s'\nproduct's name:'%s'\nqty:'%s'\nunit:'%s'\nuprice:'%s'"%(each2[0],each2[1],each2[2],each2[3],each2[4],each2[5],each2[6])))
            detaillb1.grid(sticky = "N")
    def updateIndex(self, d_i):
        cur_index = self.start_index
        self.start_index += d_i
        if (self.start_index > len(self.result_list) or self.start_index < 0):
            self.start_index = cur_index
        self.resListBox.delete(0, END)
        for i in range(self.start_index, self.start_index + 5):
            try:
                item = [self.result_list[i][0], self.result_list[i][1],self.result_list[i][2],self.result_list[i][3]]
                self.resListBox.insert(END, item)
            except:
                pass
    def updateIndex2(self, d_i):
        cur_index = self.start_index
        self.start_index += d_i
        if (self.start_index > len(self.row_list) or self.start_index < 0):
            self.start_index = cur_index
        self.resListBox.delete(0, END)
        for i in range(self.start_index, self.start_index + 5):
            try:
                item = [self.row_list[i][0], self.row_list[i][1],self.row_list[i][2],self.row_list[i][3],self.row_list[i][4],self.row_list[i][5],self.row_list[i][6]]
                self.resListBox.insert(END, item)
            except:
                pass


        

               
        
    

        
        
        
        
def main():
    global Database_name
    Database_name = sys.argv[1]
    if not os.path.exists(Database_name):
        print("Unable to find DB, please try again: ")
    else:
    	conn = sqlite3.connect(Database_name)
    	#conn = sqlite3.connect('./pronew.db')
    	c = conn.cursor()
    	c.execute('PRAGMA foreign_keys=ON;') # turns on FKs for the DB for the rest of the connection
    	conn.commit()
    	app = DataBaseapp()
    	app.mainloop()
if __name__ == "__main__":
    main()