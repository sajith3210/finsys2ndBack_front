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