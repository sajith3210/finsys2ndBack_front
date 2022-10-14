 def rnrpt():
                        def responsive_wid(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget

                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/13
                            y2 = dheight/5            

                            dcanvas.coords("bsheet_polygen_pr",x1 +r1,y1,
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
                            dcanvas.coords("bsheet_llb",dwidth/2.8,dheight/11,)
                            

                            # bsheet_polygen_pr2  start 
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/1.78
                            y2 = dheight/4

                            dcanvas.coords("bsheet_polygen_pr2",x1 +r1,y1,
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
                            dcanvas.coords("run_rpt_lbl",dwidth/12,dheight/3.86,)  
                            dcanvas.coords("opt_men2",dwidth/12,dheight/3.36,)  
                            dcanvas.coords("run_rpt_btn",dwidth/1.30,dheight/2,)  
                            dcanvas.coords("back_btn",dwidth/1.15,dheight/2,)  
                             

                            # bsheet_polygen_pr3  start 
                            r1 = 25
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/0.30
                            y2 = dheight/1.70

                            dcanvas.coords("bsheet_polygen_pr3",x1 +r1,y1,
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
                            dcanvas.coords("acc_canvas3",dwidth/20,dheight/1.65,) 
                    
                            
                        # acc_canvas forget widget
                         
                        acc_canvas.pack_forget()
                        acc_sr_Scroll.pack_forget()
                        global acc_canvas2,acc_sr_Scroll2
                        acc_canvas2 = Canvas(accou_fr,height=700,bg="#386491",scrollregion=(0,0,700,3000))
                        acc_sr_Scroll2 = Scrollbar(accou_fr,orient=VERTICAL)
                        acc_sr_Scroll2.pack(fill=Y,side="right")
                        acc_sr_Scroll2.config(command=acc_canvas2.yview)
                        acc_canvas2.bind("<Configure>", responsive_wid)
                        acc_canvas2.config(yscrollcommand=acc_sr_Scroll2.set)
                        acc_canvas2.pack(fill=X)
                        acc_canvas2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bsheet_polygen_pr"),smooth=True,)
                        bsheet_llb=Label(acc_canvas2, text="BALANCE SHEET",bg="#213b52", fg="White", anchor="nw",font=('Calibri 20 bold'))
                        bsheet_llb_place = acc_canvas2.create_window(0, 0, anchor="nw", window=bsheet_llb, tag=("bsheet_llb"))
                        acc_canvas2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bsheet_polygen_pr2"),smooth=True,)
                        
                        run_rpt_lbl=Label(acc_canvas2, text="Report period",bg="#213b52", fg="White", anchor="nw",font=('Calibri 12'))
                        run_rpt_lbl_place=acc_canvas2.create_window(0, 0, anchor="nw", window=run_rpt_lbl, tag=("run_rpt_lbl"))
                        OptionList2=['All dates','Custom','Today','This month','This financial year']
                        variable2 = StringVar()
                        variable2.set(OptionList2[0])
                        opt_men2 = OptionMenu(acc_canvas2,variable2, *OptionList2)
                        opt_men2.config(bg="#213b52",width=30)
                        opt_men2_place=acc_canvas2.create_window(0, 0, anchor="nw", window=opt_men2, tag=("opt_men2"))
                        run_rpt_btn=Button(acc_canvas2,bg="#213b52",text="Run Report",fg="white",width=15,)
                        run_rpt_place=acc_canvas2.create_window(0, 0, anchor="nw", window=run_rpt_btn, tag=("run_rpt_btn"))
                        def bsheet_back():
                           acc_canvas2.pack_forget()
                           acc_sr_Scroll3.pack_forget()
                           acc_sr_Scroll2.pack_forget()
                           acc_canvas.pack(fill=X)
                        #    acc_sr_Scroll.pack(fill=Y,side="right")
                        back_btn=Button(acc_canvas2,bg="#213b52",text="←Back",fg="white",width=15,command=bsheet_back)
                        back_btn_place=acc_canvas2.create_window(0, 0, anchor="nw", window=back_btn, tag=("back_btn"))
                        acc_canvas2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bsheet_polygen_pr3"),smooth=True,) #213b52


                        acc_canvas3= Canvas(acc_canvas2,height=1600,width=1200, bg="white",)
                        acc_canvas3_place=acc_canvas2.create_window(0, 0, anchor="nw", window=acc_canvas3, tag=("acc_canvas3"))
                        

                        # acc_canvas3 responsive function 
                        def responsive_wid(event):
                            dwidth = event.width
                            dheight = event.height
                            dcanvas = event.widget

                            r1 = 0
                            x1 = dwidth/63
                            x2 = dwidth/1.021
                            y1 = dheight/145  
                            y2 = dheight/12           

                            dcanvas.coords("bsheet_polygen_pr4",x1 +r1,y1,
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
                            dcanvas.coords("company_name_lbl",dwidth/3,dheight/23,)
                            dcanvas.coords("logo_label",dwidth/10,dheight/17,)
                            dcanvas.coords("bsheetline1",dwidth/21,dheight/7,dwidth/1.055,dheight/7,)
                            dcanvas.coords("bsheetline2",dwidth/21,dheight/6.10,dwidth/1.055,dheight/6.10,)
                            dcanvas.coords("total_lbl",dwidth/1.20,dheight/6.8,) 
                            dcanvas.coords("asset_lbl",dwidth/10,dheight/5.20,) 
                            dcanvas.coords("current_asset_lbl",dwidth/9.60,dheight/4.60,)  
                            dcanvas.coords("bank_lbl",dwidth/9,dheight/4.20,) 
                            dcanvas.coords("account_reci_lbl",dwidth/9,dheight/3.93,) 
                            dcanvas.coords("bsheetline3",dwidth/21,dheight/3.73,dwidth/1.055,dheight/3.73,)
                            dcanvas.coords("bsheetline4",dwidth/21,dheight/3.43,dwidth/1.055,dheight/3.43,)
                            dcanvas.coords("total_account_reci_lbl",dwidth/9,dheight/3.61,)
                            dcanvas.coords("bsheetline5",dwidth/21,dheight/3.13,dwidth/1.055,dheight/3.13,)
                            dcanvas.coords("total_current_asset_lbl",dwidth/9,dheight/3.30,)
                            dcanvas.coords("bsheetline6",dwidth/21,dheight/2.83,dwidth/1.055,dheight/2.83,)
                            dcanvas.coords("liability_eq_lbl",dwidth/10,dheight/2.53,)
                            dcanvas.coords("bsheetline7",dwidth/21,dheight/2.73,dwidth/1.055,dheight/2.73,)
                            dcanvas.coords("total_asset_lbl",dwidth/10,dheight/3.11,)
                            dcanvas.coords("current_liability_lbl",dwidth/9.60,dheight/2.33,)
                            dcanvas.coords("account_payb_lbl",dwidth/9,dheight/2.13,) 
                            dcanvas.coords("bsheetline8",dwidth/21,dheight/2.03,dwidth/1.055,dheight/2.03,)
                            dcanvas.coords("bsheetline9",dwidth/21,dheight/1.93,dwidth/1.055,dheight/1.93,)
                            dcanvas.coords("total_account_payb_lbl",dwidth/9,dheight/1.98,)
                            dcanvas.coords("bsheetline10",dwidth/21,dheight/1.83,dwidth/1.055,dheight/1.83,) 
                            
                            dcanvas.coords("total_current_liabi_lbl",dwidth/9.60,dheight/1.88,)
                            dcanvas.coords("equity_lbl",dwidth/9.60,dheight/1.78,)
                            dcanvas.coords("profit_for_yr_lbl",dwidth/9,dheight/1.68,)
                            dcanvas.coords("bsheetline11",dwidth/21,dheight/1.60,dwidth/1.055,dheight/1.60,) 
                            dcanvas.coords("bsheetline12",dwidth/21,dheight/1.52,dwidth/1.055,dheight/1.52,) 
                            dcanvas.coords("total_equity_lbl",dwidth/9.60,dheight/1.56,)
                            dcanvas.coords("total_liabilities_eqity_lbl",dwidth/9.60,dheight/1.49,)


                        acc_sr_Scroll3 = Scrollbar(accou_fr,orient=VERTICAL)
                        acc_sr_Scroll3.pack(fill=Y,side="right")
                        acc_sr_Scroll3.config(command=acc_canvas3.yview) 
                        acc_canvas3.config(yscrollcommand=acc_sr_Scroll3.set)
                        acc_canvas3.bind("<Configure>", responsive_wid)

                        sql = 'select * from auth_user where username=%s'
                        val = (nm_ent.get(),)
                        fbcursor.execute(sql,val)
                        u_id = fbcursor.fetchone()

                        sql = 'select * from app1_company where id_id=%s'
                        val = (u_id[0],)
                        fbcursor.execute(sql,val)
                        c_id = fbcursor.fetchone()

                        acc_canvas3.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bsheet_polygen_pr4"),smooth=True,) #213b52
                        company_name_lbl=Label(acc_canvas3, text=c_id[1],bg='#213b52', fg="white", anchor="nw",font=('Calibri 21 bold'))
                        company_name_lbl_place=acc_canvas3.create_window(0, 0, anchor="nw", window=company_name_lbl, tag=("company_name_lbl"))
                        data = StringIO(c_id[8]).read()
                        company_logo=Image.open(data)
                        resize=company_logo.resize((84,84),Image.ANTIALIAS)
                        photo = ImageTk.PhotoImage(resize)
                        logo_label = Label(acc_canvas3, image=photo,)
                        logo_label.photo = photo
                        logo_label_place=acc_canvas3.create_window(0, 0, anchor="nw", window=logo_label, tag=("logo_label"))


    account_payble_treeview=ttk.Treeview(acc_canvas3,height=4,columns=(1,2,),style='mystyle115.Treeview')
    account_payble_treeview.column("#0",width=0,stretch=NO)
    account_payble_treeview.column("#1",anchor=CENTER,width=220)
    account_payble_treeview.column('#2',anchor=CENTER,width=220)
    account_payble_treeview.heading("#0",text='',anchor=CENTER)
    account_payble_treeview.heading('1',text='Particulars')
    account_payble_treeview.heading('2',text='Amount')


     def display_currentasset():
            p=fbcursor.execute("select * from app1_accounts1")
            rows=fbcursor.fetchall()
            for row in rows:              
            current_asset_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))




 def responsive_wid(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget

        r1 = 0
        x1 = dwidth/63
        x2 = dwidth/1.021
        y1 = dheight/145  
        y2 = dheight/12         
        dcanvas.coords("total_current_asset_lbl",dwidth/9,dheight/2.15,)                    
 



                    # New category tab add tax button function 
    def accounttablefetch():
        p=fbcursor.execute("select * from app1_accounts1")
        rows=fbcursor.fetchall()
                        # print(rows)
        return rows

p=fbcursor.execute("select name ,balance from app1_accounts1 where acctype=%s")
val=('Account Payble',)
rows=fbcursor.fetchall(p,val)









sql="select *  from app1_accounts1 where acctype=%s"
current_as='Current Assets'

 p=fbcursor.execute(sql,val)
 rows=fbcursor.fetchall()




sql="select *  from app1_accounts1 where acctype=%s"
current_as='Current Assets'
val=(current_as,)
p=fbcursor.execute(sql,val)
rows=fbcursor.fetchall()


#account recivable sum
total_equity_sum="select sum(Equity) as ba from app1_accounts1 WHERE acctype=%s"                   
tem='Equity'
val=(tem,)
fbcursor.execute(total_acc_pay_sum,val)
total_eqi_sum=fbcursor.fetchone()


total_asset_sum_lbl=Label(acc_canvas3, text=TA_sum, fg="black", anchor="nw",font=('Calibri 10 '))
total_asset_sum_lbl_place=acc_canvas3.create_window(0, 0, anchor="nw", window=total_asset_sum_lbl, tag=("total_asset_sum_lbl")) 

sum_equity_and_liabili=total_current_lia_sum[0]+total_eqi_sum[0]
total_liabi_equity_lbl=Label(acc_canvas3, text=sum_equity_and_liabili, fg="black", anchor="nw",font=('Calibri 10 '))
total_asset_sum_lbl_place=acc_canvas3.create_window(0, 0, anchor="nw", window=total_liabi_equity_lbl, tag=("total_liabi_equity_lbl"))






def edit_rnrpt_back():
    acc_canvas4.pack_forget()
    acc_sr_Scroll4.pack_forget()
    acc_canvas.pack(fill=X)
    if edit_rnrpt_combo.get()=="Edit":
    print("dropdown work")
    acc_canvas.pack_forget()
    acc_sr_Scroll.pack_forget()

edit_rnrpt_combo=ttk.Combobox(acc_canvas,font=('arial 10'),background="#213b52",foreground='white')
edit_rnrpt_combo['values']=('Edit','Make Inactive','Run Report')
edit_rnrpt_combo.current(0)

acc_typ=acctypvariab.get()
det_typ_var=dettypvariab.get()
nam_vari=name_variab.get()
de_vari=descri_variab.get()
sb_ac_var=sub_Account_variab.get()
def_var=defcode_variab .get()
ba_var=bal_variab.get()
as_of_date_var=as_of_date_variab.get()



 OptionList2=['All dates','Custom','Today','This month','This financial year']
variable2 = StringVar()
variable2.set(OptionList2[0])
opt_men2 = OptionMenu(acc_canvas2,variable2, *OptionList2)
opt_men2.config(bg="#213b52",width=30)
opt_men2_place=acc_canvas2.create_window(0, 0, anchor="nw", window=opt_men2, tag=("opt_men2"))

if OptionMenu.get()=="All dates"

current_asset_treeview
current_liabilities_treeview
account_reci__treeview
account_payble_treeview
equity_treeview

opt_men2=ttk.Combobox(acc_canvas2,font=('arial 10'),background="#213b52",foreground='white')
opt_men2.['values']=('All dates','Custom','Today','This month','This financial year')
opt_men2.current(0)
opt_men2.bind("<<ComboboxSelected>>",filter_date)

edit_rnrpt_combo=ttk.Combobox(acc_canvas,font=('arial 10'),background="#213b52",foreground='white')
edit_rnrpt_combo['values']=('Edit','Make Inactive','Run Report')
edit_rnrpt_combo.current(0)

edit_rnrpt_combo.bind("<<ComboboxSelected>>",edit_rnrpt)
edit_menn_place=acc_canvas.create_window(0, 0, anchor="nw", window=edit_rnrpt_combo, tag=("edit_rnrpt_combo"))








      def filter_tb():











                        acc_treeview.delete(*acc_treeview.get_children())
                        fil_val=acc_filter_entry.get()
                        sq_str='"%{}%"'.format(fil_val)
                        if fil_val=="":
                            displayaccounttab()
                        else:
                            sql="select * from app1_accounts1 where name Like {}".format(sq_str)
                            # fbcursor.execute("select * from app1_accounts1 where name Like '% %'".format(fil_val))
                            fbcursor.execute(sql)
                            fech=fbcursor.fetchall()
                            print("fech isdf is isi si si si s",fech)
                            for row in fech:
                                acc_treeview.insert(parent='', index='end',iid=row,text='', values=(row[3],row[1],row[2],row[6],row[7],''))





total_ca_sum="select sum(balance) as ba from app1_accounts1 WHERE acctype=%s and MONTH(asof)=MONTH(now())" #account recivable sum
tem='Current Assets'
val=(tem,)
fbcursor.execute(account_reci_sum,val)
total_current_as_sum=fbcursor.fetchone()
total_current_asset_sum_lbl=Label(acc_canvas3, text=total_current_as_sum, fg="black", anchor="nw",font=('Calibri 10 '))


total_current_as_sum=0.0
for child in current_asset_treeview.get_children():
    total_current_as_sum=total_current_as_sum+float(current_asset_treeview.item(child,'values')[1])
total_current_asset_sum_lbl['text']='{}'.format(total_current_as_sum) 

 total_current_as_sum+acc_reci_sum

 total_cl=total_current_liabi_sum + total_acc_pay_sum

liabiliti_equity_sum=total_cl+total_eqi_sum


total_current_as_sum=0.0
for child in current_asset_treeview.get_children():
    total_current_as_sum=total_current_as_sum+float(current_asset_treeview.item(child,'values')[1])

total_current_asset_sum_lbl['text']='{}'.format(total_current_as_sum)


acc_reci_sum=0.0
for child in account_reci__treeview.get_children():
    acc_reci_sum=acc_reci_sum+float(account_reci__treeview.item(child,'values')[1])
sum_account_reci_lbl['text']='{}'.format(acc_reci_sum) 

TA_sum=total_current_as_sum+acc_reci_sum
total_asset_sum_lbl['text']='{}'.format(TA_sum)

current_liabi_sum=0.0
for child in current_liabilities_treeview.get_children():
    current_liabi_sum=current_liabi_sum+float(current_liabilities_treeview.item(child,'values')[1]) 

total_acc_pay_sum=0.0
for child in account_payble_treeview.get_children():
    total_acc_pay_sum=total_acc_pay_sum+float(account_payble_treeview.item(child,'values')[1])
total_account_payb_lbl_sum['text']='{}'.format(total_acc_pay_sum) 


total_cl=current_liabi_sum + total_acc_pay_sum
total_current_liabi_sum['text']="{}".format(total_cl)


total_eqi_sum=0.0
for child in equity_treeview.get_children():
    total_eqi_sum=total_eqi_sum+float(equity_treeview.item(child,'values')[1])
total_equity_sum_lbl['text']='{}'.format(total_eqi_sum)

liabiliti_equity_sum=total_cl+total_eqi_sum
total_liabi_equity_lbl_sum['text']='{}'.format(liabiliti_equity_sum)




"select * from app1_accounts1 where acctype=%s"
from_date_entry=DateEntry(acc_canvas5,selectmode='day',textvariable=from_variable)
from_date_entry_place=acc_canvas5.create_window(0, 0, anchor="nw", window=from_date_entry, tag=("from_date_entry"))


to_date_entry=DateEntry(acc_canvas5,selectmode='day',textvariable=to_variable)
to_date_entry_place=acc_canvas5.create_window(0, 0, anchor="nw", window=to_date_entry, tag=("to_date_entry"))

acc_typ_val=acc_treeview.item(acc_treeview.focus())["values"][1]
bal_val=acc_treeview.item(acc_treeview.focus())["values"][4]


rcon_canvas.pack_forget()
rcon_sr_Scroll.pack_forget()

strt_rcon_canvas = Canvas(recon_fr,height=700,bg="#386491",scrollregion=(0,0,700,1200))
strt_rcon_Scroll = Scrollbar(recon_fr,orient=VERTICAL)













