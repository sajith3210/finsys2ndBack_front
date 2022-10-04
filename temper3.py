if opt_men2.get()=="Today":
                                print("This work perfect")
                                current_asset_treeview.delete(*current_asset_treeview.get_children())
                                sql="SELECT * from app1_accounts1 where acctype=%s and asof=CURRENT_DATE()"
                                current_as='Current Assets'
                                val=(current_as,)
                                p=fbcursor.execute(sql,val)
                                rows=fbcursor.fetchall()
                                for row in rows:              
                                    current_asset_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))

                                total_current_as_sum=0.0
                                for child in current_asset_treeview.get_children():
                                    total_current_as_sum=total_current_as_sum+float(current_asset_treeview.item(child,'values')[1])
                                total_current_asset_sum_lbl['text']='{}'.format(total_current_as_sum)

                                account_reci__treeview.delete(*account_reci__treeview.get_children())
                                sql="SELECT * from app1_accounts1 where acctype=%s and asof=CURRENT_DATE()"
                                account_reci='Account Receivable(Debtors)'
                                val=(account_reci,)
                                p=fbcursor.execute(sql,val)
                                rows=fbcursor.fetchall()
                                for row in rows:              
                                    account_reci__treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))

                                acc_reci_sum=0.0
                                for child in account_reci__treeview.get_children():
                                    acc_reci_sum=acc_reci_sum+float(account_reci__treeview.item(child,'values')[1])
                                sum_account_reci_lbl['text']='{}'.format(acc_reci_sum) 
                                TA_sum=total_current_as_sum+acc_reci_sum
                                total_asset_sum_lbl['text']='{}'.format(TA_sum)

                                current_liabilities_treeview.delete(*current_liabilities_treeview.get_children())
                                sql="SELECT * from app1_accounts1 where acctype=%s and asof=CURRENT_DATE()"
                                current_li='Current Liabilities'
                                val=(current_li,)
                                p=fbcursor.execute(sql,val)
                                rows=fbcursor.fetchall()

                                for row in rows:              
                                    current_liabilities_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))
                                
                                current_liabi_sum=0.0
                                for child in current_liabilities_treeview.get_children():
                                    current_liabi_sum=current_liabi_sum+float(current_liabilities_treeview.item(child,'values')[1])

                                account_payble_treeview.delete(*account_payble_treeview.get_children())
                                sql="SELECT * from app1_accounts1 where acctype=%s and asof=CURRENT_DATE()"
                                account_payb='Account Payble'
                                val=(account_payb,)
                                p=fbcursor.execute(sql,val)
                                rows=fbcursor.fetchall()
                                for row in rows:              
                                    account_payble_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))

                                total_acc_pay_sum=0.0
                                for child in account_payble_treeview.get_children():
                                    total_acc_pay_sum=total_acc_pay_sum+float(account_payble_treeview.item(child,'values')[1])
                                total_account_payb_lbl_sum['text']='{}'.format(total_acc_pay_sum)

                                total_cl=current_liabi_sum + total_acc_pay_sum
                                total_current_liabi_sum['text']="{}".format(total_cl)

                                equity_treeview.delete(*equity_treeview.get_children())
                                sql="SELECT * from app1_accounts1 where acctype=%s and asof=CURRENT_DATE()"
                                eqi='Equity'
                                val=(eqi,)
                                p=fbcursor.execute(sql,val)
                                rows=fbcursor.fetchall()
                                for row in rows:              
                                    equity_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))

                                total_eqi_sum=0.0
                                for child in equity_treeview.get_children():
                                    total_eqi_sum=total_eqi_sum+float(equity_treeview.item(child,'values')[1])
                                total_equity_sum_lbl['text']='{}'.format(total_eqi_sum)
                                liabiliti_equity_sum=total_cl+total_eqi_sum
                                total_liabi_equity_lbl_sum['text']='{}'.format(liabiliti_equity_sum)

                            if opt_men2.get()=="This financial year":
                                print("This work perfect")
                                current_asset_treeview.delete(*current_asset_treeview.get_children())
                                sql="select *  from app1_accounts1 where acctype=%s  and  YEAR(asof)=YEAR(CURRENT_DATE)"
                                current_as='Current Assets'
                                val=(current_as,)
                                p=fbcursor.execute(sql,val)
                                rows=fbcursor.fetchall()
                                for row in rows:              
                                    current_asset_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))








          def date_filter_2():                                
                if opt_men4.get()=="All dates":
                    run_report_treeview.delete(*run_report_treeview.get_children()) 
                    for row in  acctypevalrows:
                        run_report_treeview.insert(parent='',index='end',iid=row,text='',values=(row[8],'','','',row[1],'',row[7] )) 
                if opt_men4.get()=="Today":
                    run_report_treeview.delete(*run_report_treeview.get_children()) 
                    acc_typ_val=acc_treeview.item(acc_treeview.focus())["values"][1]
                    sql="SELECT * from app1_accounts1 where acctype=%s and asof=CURRENT_DATE()"
                    val = (acc_typ_val,)
                    fbcursor.execute(sql,val)
                    acctypevalrows=fbcursor.fetchall()
                    for row in  acctypevalrows:
                        run_report_treeview.insert(parent='',index='end',iid=row,text='',values=(row[8],'','','',row[1],'',row[7] )) 


                if opt_men4.get()=="This month":
                        print("This work perfect")
                        run_report_treeview.delete(*run_report_treeview.get_children()) 
                        acc_typ_val=acc_treeview.item(acc_treeview.focus())["values"][1]
                        sql="select *  from app1_accounts1 where acctype=%s  and  MONTH(asof)=MONTH(now())"  
                        val=(acc_typ_val,)
                        p=fbcursor.execute(sql,val)
                        acctypevalrows=fbcursor.fetchall()
                        for row in acctypevalrows:              
                            run_report_treeview.insert(parent='',index='end',iid=row,text='',values=(row[8],'','','',row[1],'',row[7] ))



                  if opt_men4.get()=="This financial year":
                                print("This work perfect")
                                run_report_treeview.delete(*run_report_treeview.get_children()) 
                                acc_typ_val=acc_treeview.item(acc_treeview.focus())["values"][1]
                                sql="select *  from app1_accounts1 where acctype=%s  and  YEAR(asof)=YEAR(CURRENT_DATE)"
                                val=(acc_typ_val,)
                                p=fbcursor.execute(sql,val)
                                acctypevalrows=fbcursor.fetchall()
                                for row in rows:              
                                    run_report_treeview.insert(parent='',index='end',iid=row,text='',values=(row[8],'','','',row[1],'',row[7] ))




                            from_date_variable
                            to_date_variable
                            from_date_entry
                            to_date_entry




                            def date_filter_2():  
                                if opt_men4.get()=="Custom":
                                    from_d=from_date_entry.get_date()
                                    to_d=to_date_entry.get_date()
                                    # from_d=from_date_variable.get()
                                    # to_d=to_date_variable.get()
                                    fr=from_d.strftime("%Y-%m-%d")
                                    to=to_d.strftime("%Y-%m-%d")
                                    # print("from date is ",from_d)
                                    # print("to date is",to_d)
                                    run_report_treeview.delete(*run_report_treeview.get_children()) 
                                    acc_typ_val=acc_treeview.item(acc_treeview.focus())["values"][1]
                                    sql="select *  from app1_accounts1 where asof BETWEEN %s AND %s AND acctype=%s"
                                    val=(fr,to,acc_typ_val)
                                    p=fbcursor.execute(sql,val)
                                    acctypevalrows=fbcursor.fetchall()
                                    for row in acctypevalrows:              
                                        run_report_treeview.insert(parent='',index='end',iid=row,text='',values=(row[8],'','','',row[1],'',row[7] ))



 def custom_dt(event): 
                                if opt_men4.get()=="Custom":   
                                    from_date_entry['state']=NORMAL
                                    to_date_entry['state']=NORMAL 

                                if opt_men4.get()=="This financial year":
                                    from_date_entry['state']=DISABLED
                                    to_date_entry['state']=DISABLED

                                if opt_men4.get()=="This month":
                                    from_date_entry['state']=DISABLED
                                    to_date_entry['state']=DISABLED

                                if opt_men4.get()=="All dates":
                                    from_date_entry['state']=DISABLED
                                    to_date_entry['state']=DISABLED 

                                if opt_men4.get()=="Today":
                                    from_date_entry['state']=DISABLED
                                    to_date_entry['state']=DISABLED



dcanvas.coords("from_date_lbl",dwidth/2.90,dheight/3.86,)
dcanvas.coords("to_date_lbl",dwidth/1.90,dheight/3.86,)

dcanvas.coords("from_date_entry",dwidth/2.90,dheight/3.36,)
dcanvas.coords("to_date_entry",dwidth/1.90,dheight/3.36,)


from_date_lbl=Label(spcl_rnpt_canvas, text="From",bg="#213b52", fg="White", anchor="nw",font=('Calibri 12'))
from_date_lbl_place=spcl_rnpt_canvas.create_window(0, 0, anchor="nw", window=from_date_lbl, tag=("from_date_lbl"))

to_date_lbl=Label(spcl_rnpt_canvas, text="To",bg="#213b52", fg="White", anchor="nw",font=('Calibri 12'))
To_date_lbl_place=spcl_rnpt_canvas.create_window(0, 0, anchor="nw", window=to_date_lbl, tag=("to_date_lbl"))

from_date_variable=StringVar()
to_date_variable=StringVar()

from_date_entry=DateEntry(spcl_rnpt_canvas,state=DISABLED , selectmode='day',textvariable=from_date_variable)
from_date_entry_place=spcl_rnpt_canvas.create_window(0, 0, anchor="nw", window=from_date_entry, tag=("from_date_entry"))

to_date_entry=DateEntry(spcl_rnpt_canvas,state=DISABLED ,selectmode='day',textvariable=to_date_variable)
to_date_entry_place=spcl_rnpt_canvas.create_window(0, 0, anchor="nw", window=to_date_entry, tag=("to_date_entry"))





                        payment_sum_lbl=Label(strt_rcon_canvas, text=ser_chr_var,bg="#213b52", fg="White", anchor="nw",font=('Calibri 11'))
                        payment_sum_lbl_place=strt_rcon_canvas.create_window(0, 0, anchor="nw", window=payment_sum_lbl, tag=("payment_sum_lbl"))
                        deposit_sum_lbl=Label(strt_rcon_canvas, text=interest_ear_var,bg="#213b52", fg="White", anchor="nw",font=('Calibri 11'))
                        deposit_sum_lbl_place=strt_rcon_canvas.create_window(0, 0, anchor="nw", window=deposit_sum_lbl, tag=("deposit_sum_lbl"))
                        diffrence_sum_lbl=Label(strt_rcon_canvas, text=diffrence_bal,bg="#213b52", fg="White", anchor="nw",font=('Calibri 11'))
                        diffrence_sum_lbl_place=strt_rcon_canvas.create_window(0, 0, anchor="nw", window=diffrence_sum_lbl, tag=("diffrence_sum_lbl"))




payment_lbl=Label(strt_rcon_canvas, text="PAYMENTS",bg="#213b52", fg="White", anchor="nw",font=('Calibri 11 bold'))
                        payment_sum_lbl_place=strt_rcon_canvas.create_window(0, 0, anchor="nw", window=payment_lbl, tag=("payment_lbl"))


deposit_lbl=Label(strt_rcon_canvas, text='DEPOSITS',bg="#213b52", fg="White", anchor="nw",font=('Calibri 11'))
deposit_lbl_place=strt_rcon_canvas.create_window(0, 0, anchor="nw", window=deposit_lbl, tag=("deposit_lbl"))

diffrence_lbl=Label(strt_rcon_canvas, text='DIFFRENCE',bg="#213b52", fg="White", anchor="nw",font=('Calibri 11'))
                        diffrence_lbl_place=strt_rcon_canvas.create_window(0, 0, anchor="nw", window=diffrence_lbl, tag=("diffrence_lbl"))







print("Print company id is ",cid[0],"Acct type id is ",actypid[0],"Expense id is",exp_id[0])
sql="update app1_expenseaccount set account=%s,begbal=%s,endbal=%s,enddate=%s,dat=%s,serchar=%s,expacc=%s,cid_id=%s,expaccountypid_id=%s where expenseid=%s" #ADDING VALUE INT APP1_ADDTAX1 TABLE
val=(Accnt_variable.get(),begining_balance_va,ending_balance_va,end_dt_variable.get(),date_variable.get(),servise_charge_va,exp_acc_variable.get(),cid[0],actypid[0],exp_id[0])
fbcursor.execute(sql,val)
finsysdb.commit()

sql="update app1_incomeaccount set dat1=%s,intear=%s,incacc=%s,cid_id=%s,expenceincomeid_id=%s where incomeid=%s" #ADDING VALUE INT APP1_ADDTAX1 TABLE
val=(incom_ac_date_variable.get(),interest_earn_va,income_acc_variable.get(),cid[0],exp_id[0],incom_id[0])







