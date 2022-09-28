def all_dates():
    current_asset_treeview.delete(*current_asset_treeview.get_children())
    sql="select *  from app1_accounts1 where acctype=%s"
    current_as='Current Assets'
    val=(current_as,)
    p=fbcursor.execute(sql,val)
    rows=fbcursor.fetchall()
    for row in rows:              
        current_asset_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))

    account_reci__treeview.delete(*account_reci__treeview.get_children())
    sql="select *  from app1_accounts1 where acctype=%s"
    account_reci='Account Receivable(Debtors)'
    val=(account_reci,)
    p=fbcursor.execute(sql,val)
    rows=fbcursor.fetchall()
    for row in rows:              
        account_reci__treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))

    current_liabilities_treeview.delete(*tv.current_liabilities_treeview())
    sql="select *  from app1_accounts1 where acctype=%s"
    current_li='Current Liabilities'
    val=(current_li,)
    p=fbcursor.execute(sql,val)
    rows=fbcursor.fetchall()
    for row in rows:              
        current_liabilities_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))

    account_payble_treeview.delete(*tv.account_payble_treeview())
    sql="select * from app1_accounts1 where acctype=%s"
    account_payb='Account Payble'
    val=(account_payb,)
    p=fbcursor.execute(sql,val)
    rows=fbcursor.fetchall()
    for row in rows:              
        account_payble_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))

    equity_treeview.delete(*equity_treeview.get_children())
    sql="select * from app1_accounts1 where acctype=%s"
    eqi='Equity'
    val=(eqi,)
    p=fbcursor.execute(sql,val)
    rows=fbcursor.fetchall()
    for row in rows:              
        equity_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],)) 


def this_month():
    print("This work perfect")
    current_asset_treeview.delete(*tv.get_children())
    sql="select *  from app1_accounts1 where acctype=%s  and  MONTH(asof)=MONTH(now())"
    current_as='Current Assets'
    val=(current_as,)
    p=fbcursor.execute(sql,val)
    rows=fbcursor.fetchall()
    for row in rows:              
        current_asset_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))

    account_reci__treeview.delete(*tv.get_children())
    sql="select *  from app1_accounts1 where acctype=%s  and  MONTH(asof)=MONTH(now())"
    account_reci='Account Receivable(Debtors)'
    val=(account_reci,)
    p=fbcursor.execute(sql,val)
    rows=fbcursor.fetchall()
    for row in rows:              
        account_reci__treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))

    current_liabilities_treeview.delete(*tv.get_children())
    sql="select *  from app1_accounts1 where acctype=%s  and  MONTH(asof)=MONTH(now())"
    current_li='Current Liabilities'
    val=(current_li,)
    p=fbcursor.execute(sql,val)
    rows=fbcursor.fetchall()
    for row in rows:              
        current_liabilities_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))
    

    account_payble_treeview.delete(*tv.get_children())
    sql="select * from app1_accounts1 where acctype=%s and  MONTH(asof)=MONTH(now())"
    account_payb='Account Payble'
    val=(account_payb,)
    p=fbcursor.execute(sql,val)
    rows=fbcursor.fetchall()
    for row in rows:              
        account_payble_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],))

    equity_treeview.delete(*tv.get_children())
    sql="select * from app1_accounts1 where acctype=%s and  MONTH(asof)=MONTH(now())"
    eqi='Equity'
    val=(eqi,)
    p=fbcursor.execute(sql,val)
    rows=fbcursor.fetchall()
    for row in rows:              
        equity_treeview.insert(parent='', index='end',iid=row,text='', values=(row[1],row[7],)) 