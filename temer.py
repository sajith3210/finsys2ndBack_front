def edit_reconcile_statement():
                        def responsive_wid(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget

                            try:
                                #rcn_polygen_pr_2
                                r1 = 25
                                x1 = dwidth/63
                                x2 = dwidth/1.021
                                y1 = dheight/4
                                y2 = dheight/0.59            

                                dcanvas.coords("rcn_polygen_pr2",x1 +r1,y1,
                                x1 + r1,y1,
                                x2 - r1,y1,
                                x2 - r1,y1,     
                                x2,y1,     
                                #--------------------
                                x2,y1 + r1,     
                                x2,y1 + r1,     
                                x2,y2 - r1,     
                                x2,y2 - r1,     
                                x2,y2,
                                #--------------------
                                x2 - r1,y2,     
                                x2 - r1,y2,     
                                x1 + r1,y2,
                                x1 + r1,y2,
                                x1,y2,
                                #--------------------
                                x1,y2 - r1,
                                x1,y2 - r1,
                                x1,y1 + r1,
                                x1,y1 + r1,
                                x1,y1,
                                )
                                dcanvas.coords("open_st_lbl",dwidth/2.75,dheight/3,)
                                dcanvas.coords("which_acct_lbl",dwidth/4,dheight/2.60,)
                                dcanvas.coords("Account_lbl",dwidth/4,dheight/2.30,)
                                dcanvas.coords("Account_men",dwidth/4,dheight/1.97,)
                                dcanvas.coords("ad_follow_info_lbl",dwidth/4,dheight/1.74,)
                                dcanvas.coords("beg_bal_lbl",dwidth/4,dheight/1.60,)
                                dcanvas.coords("end_bal_lbl",dwidth/2.65,dheight/1.60,)
                                dcanvas.coords("end_date_lbl",dwidth/2,dheight/1.60,) 
                                dcanvas.coords("beg_bal_entry",dwidth/4,dheight/1.40,)
                                dcanvas.coords("end_bal_entry",dwidth/2.65,dheight/1.40,)
                                
                                dcanvas.coords("enter_the_servi_lbl",dwidth/4,dheight/1.20,)
                                dcanvas.coords("date_lbl",dwidth/4,dheight/1.10,)
                                
                                dcanvas.coords("servise_chr_lbl",dwidth/2.65,dheight/1.10,)
                                dcanvas.coords("expence_ac_lbl",dwidth/2,dheight/1.10,)
                                dcanvas.coords("servise_chrg_entry",dwidth/2.65,dheight/1,)
                                dcanvas.coords("exp_account_men",dwidth/2,dheight/1,)
                                dcanvas.coords("strt_rec_btn",dwidth/2.65,dheight/0.67,)
                                dcanvas.coords("income_date_lbl",dwidth/4,dheight/0.80,)
                                dcanvas.coords("interest_earn_lbl",dwidth/2.65,dheight/0.80,)
                                dcanvas.coords("income_ac_lbl",dwidth/2,dheight/0.80,)
                                dcanvas.coords("interest_earn_lbl_entry",dwidth/2.65,dheight/0.73,)
                                dcanvas.coords("income_account_men",dwidth/2,dheight/0.73,)
                            except:
                                pass
                            try:
                                dcanvas.coords("end_date_entry",dwidth/2,dheight/1.40,)
                                dcanvas.coords("date_lbl_entry",dwidth/4,dheight/1,)
                                dcanvas.coords("icome_date_entry",dwidth/4,dheight/0.73,)
                                
                            except:
                                pass
                         
                    strt_rcon_canvas.pack_forget()
                    strt_rcon_Scroll.pack_forget()
                    edit_recon_canvas = Canvas(recon_fr,height=700,bg="#386491",scrollregion=(0,0,700,1200))
                    edit_recon_scroll = Scrollbar(recon_fr,orient=VERTICAL)
                    edit_recon_scroll.pack(fill=Y,side="right")
                    edit_recon_scroll.config(command=edit_recon_canvas.yview)
                    edit_recon_canvas.bind("<Configure>", responsive_wid)
                    edit_recon_canvas.config(yscrollcommand=edit_recon_scroll.set)
                    edit_recon_canvas.pack(fill=X)
                    edit_recon_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("rcn_polygen_pr"),smooth=True,)
                    
                    rcon_lbl=Label(edit_recon_canvas, text="RECONCILED",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    rcon_lbl_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=rcon_lbl, tag=("rcon_lbl"))

                    edit_recon_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("rcn_polygen_pr2"),smooth=True,)
                    open_st_lbl=Label(edit_recon_canvas, text="Open your statement and we'll get started.",bg="#213b52", fg="White", anchor="nw",font=('Calibri 11'))

                    open_st_lbl_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=open_st_lbl, tag=("open_st_lbl"))
                    which_acct_lbl=Label(edit_recon_canvas, text="Which account do you want to reconcile?",bg="#213b52", fg="White", anchor="nw",font=('Calibri 15 bold'))

                    which_acct_lbl_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=which_acct_lbl, tag=("which_acct_lbl"))
                    Account_lbl=Label(edit_recon_canvas, text="Account",bg="#213b52", fg="White", anchor="nw",font=('Calibri 11'))
                    Account_lbl_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=Account_lbl, tag=("Account_lbl"))

                    ac_sql="select accountname from app1_accountype"
                    ex=fbcursor.execute(ac_sql)
                    
                    ac=fbcursor.fetchall()
                    # print('table is',ac)
                    # alist=ac[1]
                    Account_List=[]
                    for x in ac:
                        for k in x:
                            Account_List.append(k)
                            
                    global Account_variable,beg_bal_varia,end_bal_varia,ser_chrg_varia,exp_account_variable,date_varia,end_dt_vari, int_ear_varia,incom_ac_date_varia,income_account_variable
                    beg_bal_variable=beg_bal_entry.get()
                    end_bal_variable=end_bal_entry.get()
                    servise_chrg_variable=servise_chrg_entry.get()
                    date_variable=StringVar()
                    end_dt_variable=StringVar()
                    # end_dt_varia=StringVar()
                    interest_ear_variable=interest_earn_lbl_entry.get()
                    incom_ac_date_variable=StringVar()

                    Accnt_variable = StringVar()
                    Accnt_variable.set(Account_List[0])
                    Account_men = OptionMenu(edit_recon_canvas,Accnt_variable, *Account_List)
                    Account_men.config(bg="#213b52",width=30,fg='white')
                    Account_men_place=rcon_canvas.create_window(0, 0, anchor="nw", window=Account_men, tag=("Account_men"))

                    ad_follow_info_lbl=Label(edit_recon_canvas, text="Add the following information",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    ad_follow_info_lbl_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=ad_follow_info_lbl, tag=("ad_follow_info_lbl"))

                    beg_bal_lbl=Label(edit_recon_canvas, text="Beginning balance*",bg="#213b52", fg="White", anchor="nw",font=('Calibri 12'))
                    beg_bal_lbl_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=beg_bal_lbl, tag=("beg_bal_lbl"))

                    end_bal_lbl=Label(edit_recon_canvas, text="Ending balance*",bg="#213b52", fg="White", anchor="nw",font=('Calibri 12'))
                    end_bal_lbl_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=end_bal_lbl, tag=("end_bal_lbl"))
                    end_date_lbl=Label(edit_recon_canvas, text="Ending date*",bg="#213b52", fg="White", anchor="nw",font=('Calibri 12'))
                    end_date_lbl_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=end_date_lbl, tag=("end_date_lbl"))
                    beg_bal_entry=Entry(edit_recon_canvas,font=('Calibri 8'),)
                    beg_bal_entry.insert(0,beg_bal_varia.get())
                    beg_bal_entry_place=edit_recon_canvas.create_window(0, 0, anchor="nw",width=130 , window=beg_bal_entry, tag=("beg_bal_entry"))
                    end_bal_entry=Entry(edit_recon_canvas,font=('Calibri 8'),)
                    end_bal_entry.insert(0,end_bal_varia.get())
                    end_bal_entry_place=edit_recon_canvas.create_window(0, 0, anchor="nw",width=130 , window=end_bal_entry, tag=("end_bal_entry"))
                    enter_the_servi_lbl=Label(edit_recon_canvas, text="Enter the service charge or interest earned, if necessary",bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    enter_the_servi_lbl_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=enter_the_servi_lbl, tag=("enter_the_servi_lbl"))
                    date_lbl=Label(edit_recon_canvas, text="Date",bg="#213b52", fg="White", anchor="nw",font=('Calibri 12'))
                    date_lbl_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=date_lbl, tag=("date_lbl"))
                    servise_chr_lbl=Label(edit_recon_canvas, text="Servise Charge",bg="#213b52", fg="White", anchor="nw",font=('Calibri 12'))
                    servise_chr_lbl_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=servise_chr_lbl, tag=("servise_chr_lbl"))
                    expence_ac_lbl=Label(edit_recon_canvas, text="Expense Account",bg="#213b52", fg="White", anchor="nw",font=('Calibri 12'))
                    expence_ac_lbl_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=expence_ac_lbl, tag=("expence_ac_lbl"))
                    servise_chrg_entry=Entry(edit_recon_canvas,font=('Calibri 8'),)
                    servise_chrg_entry.insert(0,ser_chrg_varia.get())
                    servise_chrg_place=edit_recon_canvas.create_window(0, 0, anchor="nw",width=130 , window=servise_chrg_entry, tag=("servise_chrg_entry"))
                    
                    exp_account_list=['Advertising/Promotional','Bank Charges','Business Licenses and Permits','Charitable Contributions','Computer and Internet Expense',
                    'Continuing Education','Depreciation Expense','Dues and Subscriptions','Housekeeping Charges','Insurance Expense','Insurance Expense-General Liability Insurance',
                    'Insurance Expense-Health Insurance','Insurance Expense-Professional Liability','Interest Expense','Meals and Entertainment','Office Supplies',
                    'Postage ang Delivery','Printing and Reproduction','Professional Fees','Purchases','Rent Expense','Repair and Maintenance','Small Tools and Equipments','Swachh Bharath Cess Expense',
                    'Taxes-Property','Telephone Expense','Travel Expense','Uncategorised Expenses','Utilities','Ask My Accountant','CGST write-off','GST write-off','IGST write-off','Miscelleneous Expense',
                    'Political Contribution','Reconcilation Discrepancies','SGST write-off','Tax write-off','Vehicle Expenses','Deferred GST Input Credit','Deferred IGST','Deferred Krishi Kalyan Cess Input Cedit',
                    'Deferred Service Tax Input Credit','Deferred SGST','Deferred VAT Input Credit','GST Refund','Inventory Asset','Krishi Kalyan Cess Refund','Prepaid Insurance','Service Tax Refund','TDS Receivable','Uncategorised Asset','Accumulated Depreciation',
                    'Buildings and Improvements','Furniture and Equipments','Land','Leasehold Improvements','Vehicles','CGST Payable','CST Payable','CST Suspense','GST Payable','GST Suspense','IGST Payable','Input CGST','Input CGST Tax RCM','Input IGST','Input IGST Tax RCM',
                    'Input Krishi Kalyan Cess','Input Krishi Kalyan Cess RCM','Input Service Tax','Input Service Tax RCM','Input SGST','Input SGST Tax RCM','Input VAT','Input VAT 14%','Input VAT 4%','Input VAT 5%','Krishi Kalyan Cess Payable','Krishi Kalyan Cess Suspense',
                    'Output CGST','Output CGST Tax RCM','Output CST 2%','Output IGST','Output IGST Tax RCM','Output Krishi Kalyan Cess','Output Krishi Kalyan Cess RCM','Output Service Tax','Output Service Tax RCM','Output SGST','Output VAT 14%','Output VAT 4%','Output VAT 5%',
                    'Service Tax Payable','Service Tax Suspense','SGST Payable','Swachh Bharat Cess Payable','Swachh Bharat Cess Suspense','TDS Payable','VAT Payable','VAT Suspense','Opening Balance Equity','Retained Earnings','Billable Expense Income','Consulting Income','Products Sales','Sales',
                    'Sales-Hardware','Sales-Software','Sales-Support and Maintenance','Sales Discounts','Sales of Product Income','Uncategorised Income','Cost of Sales','Equipments Rental for Jobs','Freight and Shipping Cost','Merchant Account Fees','Purchase-Hardware for Resale','Purchase-Software for Resale',
                    'Sub-contracted Services','Tools and Craft Supplies','Finance Charge Income','Insurance Proceeds Received','Interest Income','Proceeds from Sale of Asset','Shipping and Delivery Income',
                    ]
                    exp_acc_variable = StringVar()
                    exp_acc_variable.set(exp_account_list[0])
                    exp_account_men=OptionMenu(edit_recon_canvas,exp_acc_variable, *exp_account_list)
                    exp_account_men.config(bg="#213b52",width=28,fg='white')
                    exp_account_men_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=exp_account_men, tag=("exp_account_men"))
                    strt_rec_btn=Button(edit_recon_canvas,bg="#213b52",text="Save",fg="white",width=15,command='')
                    strt_rec_btn_place=edit_recon_canvas.create_window(0, 0, anchor="nw", window=strt_rec_btn, tag=("strt_rec_btn"))
                    end_date_entry=DateEntry(edit_recon_canvas,selectmode='day',textvariable=end_dt_variable)
                    end_date_entry_place=edit_recon_scroll.create_window(0, 0, anchor="nw", window=end_date_entry, tag=("end_date_entry"))
                    date_lbl_entry=DateEntry(edit_recon_scroll,selectmode='day',textvariable=date_variable)
                    date_lbl_entry_place=edit_recon_scroll.create_window(0, 0, anchor="nw", window=date_lbl_entry, tag=("date_lbl_entry"))
                    income_date_lbl=Label(edit_recon_scroll, text="Date",bg="#213b52", fg="White", anchor="nw",font=('Calibri 12'))
                    income_date_lbl_place=edit_recon_scroll.create_window(0, 0, anchor="nw", window=income_date_lbl, tag=("income_date_lbl"))
                    interest_earn_lbl=Label(edit_recon_scroll, text="Interest earned",bg="#213b52", fg="White", anchor="nw",font=('Calibri 12'))
                    interest_earn_lbl_place=edit_recon_scroll.create_window(0, 0, anchor="nw",width=130 , window=interest_earn_lbl, tag=("interest_earn_lbl"))
                    income_ac_lbl=Label(edit_recon_scroll, text="Interest account",bg="#213b52", fg="White", anchor="nw",font=('Calibri 12'))
                    income_ac_lbl_place=edit_recon_scroll.create_window(0, 0, anchor="nw", window=income_ac_lbl, tag=("income_ac_lbl"))
                    interest_earn_lbl_entry=Entry(edit_recon_scroll,font=('Calibri 8'),)
                    interest_earn_lbl_entry.insert(0,int_ear_varia.get())
                    interest_earn_lbl_entry_place=edit_recon_scroll.create_window(0, 0, anchor="nw", window=interest_earn_lbl_entry, tag=("interest_earn_lbl_entry"))
                    income_account_list=['Finance Charge Income','Insurance Proceeds Received','Interest Income','Proceeds From Sale of Asset','Shipping and Delivery Income','Billable Expense Income',
                    'Consulting Income',
                    ]
                    income_acc_variable = StringVar()
                    income_acc_variable.set(income_account_list[0])
                    income_account_men=OptionMenu(edit_recon_scroll,income_acc_variable, *income_account_list)
                    income_account_men.config(bg="#213b52",width=28,fg='white')
                    income_account_men_place=edit_recon_scroll.create_window(0, 0, anchor="nw", window=income_account_men, tag=("income_account_men"))
                    icome_date_entry=DateEntry(edit_recon_scroll,selectmode='day',textvariable=incom_ac_date_variable)
                    income_date_entry_place=edit_recon_scroll.create_window(0, 0, anchor="nw", window=icome_date_entry, tag=("icome_date_entry")) 



global Accnt_variable,
begining_balance_va=beg_bal_entry.get(),
ending_balance_va=end_bal_entry.get(),
servise_charge_va=servise_chrg_entry.get(),
exp_acc_variable,
date_variable
end_dt_variable
interest_earn_va=interest_earn_lbl_entry.get()
incom_ac_date_variable,
income_acc_variable

exp_id    #Last row fetch variable Expense table
incom_id   #Last row fetch variable income table
actypid    #Account type variable fetch specific row 

sql="select * from auth_user where username=%s"
val=(nm_ent.get(),)
fbcursor.execute(sql,val)
u_id=fbcursor.fetchone()

sql="select * from app1_company where id_id=%s"
val=(u_id[0],)
fbcursor.execute(sql,val)
cid=fbcursor.fetchone()

sql="update app1_expenseaccount set account=%s,begbal=%s,endbal=%s,enddate=%s,dat=%s,serchar=%s,expacc=%s,cid_id=%s,expaccountypid_id=%s where expenseid=%s" #ADDING VALUE INT APP1_ADDTAX1 TABLE
val=(Accnt_variable,begining_balance_va,ending_balance_va,end_dt_variable,date_variable,servise_charge_va,exp_acc_variable,c_id[0],acc_typ,exp_id)
fbcursor.execute(sql,val)
finsysdb.commit()


sql="update app1_incomeaccount set dat1=%s,intear=%s,incacc=%s,cid_id=%s,expenceincomeid_id=%s, where incomeid=%s" #ADDING VALUE INT APP1_ADDTAX1 TABLE
val=(incom_ac_date_variable,interest_earn_va,income_acc_variable,c_id[0],exp_id[0],incom_id)
fbcursor.execute(sql,val)
finsysdb.commit()
messagebox.showinfo("Update","Update successfully")

sql="update app1_expenseaccount set cid_id=%s,expaccountypid_id=%s , account=%s,begbal=%s,endbal=%s,enddate=%s,dat=%s,serchar=%s,expacc=%s, where expenseid=%s" #ADDING VALUE INT APP1_ADDTAX1 TABLE
val=(cid[0],actypid[0],Accnt_variable,begining_balance_va,ending_balance_va,end_dt_variable,date_variable,servise_charge_va,exp_acc_variable,exp_id[0])
val=()
