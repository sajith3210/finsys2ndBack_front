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