                    # tax_bg_polygen_pr3 start 
                    def responsive_wid(event):
                        dwidth = event.width
                        dheight = event.height
                        dcanvas = event.widget
                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.021
                        y1 = dheight/13
                        y2 = dheight/4 

                        dcanvas.coords("tax_bg_polygen_pr3",x1 +r1,y1,
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
                        dcanvas.coords("add_new_tax_lbl",dwidth/2.3,dheight/9,)
                        

                        # tax_bg_polygen_pr4 start 
                        r1 = 25
                        x1 = dwidth/63
                        x2 = dwidth/1.02
                        y1 = dheight/3.51
                        y2 = dheight/1

                        dcanvas.coords("tax_bg_polygen_pr4",x1 +r1,y1,
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
                        dcanvas.coords("tax_nme_lbl",dwidth/2.3,dheight/1.9,)
                        dcanvas.coords("tax_nme_entry",dwidth/2.3,dheight/1.7,)
                        dcanvas.coords("description_lbl",dwidth/2.3,dheight/1.5,)
                        dcanvas.coords("description_lbl_entry",dwidth/2.3,dheight/1.4,)
                        dcanvas.coords("save_btn",dwidth/2.3,dheight/1.2,)
                        dcanvas.coords("img_label",dwidth/26,dheight/2.5,)