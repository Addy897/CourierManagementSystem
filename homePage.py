from tkinter import *
from math import pi ,sqrt ,tan
import time
from threading import  Thread
class HomePage:
    def __init__(this,context):
            this.ctx=context
            this.txtBoxes=[]
            this.shapes=[]
            this.isAnimating=False
            this.stopThread=False
            this.loggedIn=this.ctx.loggedIn
            this.ctx.homePage=this.homePage
    def homePage(this):
        canvas = Canvas(
            this.ctx.window,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        start=568
        gap=165
        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            81.0,
            1366.0,
            767.0,
            fill="#ECFDFF",
            outline="")

        this.entry_image_1 = PhotoImage(
            file=this.ctx.assets("newUserEntry.png"))
        entry_bg_1 = canvas.create_image(
            1083.5,
            186.0,
            image=this.entry_image_1
        )
        searchBox = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        searchBox.place(
            x=881.0,
            y=158.0,
            width=405.0,
            height=48.0
        )

        canvas.create_rectangle(
            0.0,
            0.0,
            1366.0,
            81.0,
            fill="#BFFFD1",
            outline="")
        about=canvas.create_text(
            start+(gap),
            29.0,
            anchor="nw",
            text="About",
            fill="#191619",
            font=("Vollkorn", 20 * -1)
        )
        Aboutbounds = canvas.bbox(about)  
        AboutlabelW = Aboutbounds[2] - Aboutbounds[0]
        AboutlabelH = Aboutbounds[3] - Aboutbounds[1]
        loginButton=canvas.create_text(
           start+(gap*2),
            29.0,
            anchor="nw",
            text="Login",
            fill="#0CBBC7",
            font=("Vollkorn", 20 * -1)
        )

        products=canvas.create_text(
            start,
            29.0,
            anchor="nw",
            text="Products",
            fill="#191619",
            font=("Vollkorn", 20 * -1)
        )
        Productsbounds = canvas.bbox(products)
        ProductslabelW = Productsbounds[2] - Productsbounds[0]
        ProductslabelH = Productsbounds[3] - Productsbounds[1]
        canvas.create_text(
            141.0,
            246.0,
            anchor="nw",
            text="With stellar one-click orders and unmatched support, see how\n\tC.M.S will make a difference in your life.",
            fill="#868686",
            font=("Vollkorn", 14 * -1)
        )

        canvas.create_text(
            60.0,
            136.0,
            anchor="nw",
            text="A powerful engagement tool",
            fill="#191619",
            font=("Vollkorn", 44 * -1)
        )
        canvas.create_text(
            60.0,
            186.0,
            anchor="nw",
            text="that’s intuitive and simple to use.",
            fill="#191619",
            font=("Vollkorn", 44 * -1)
        )
        this.button_image_1 = PhotoImage(
            file=this.ctx.assets("morebutton.png"))
        
        button_1 = Button(
            image=this.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: kmore(),
            relief="flat"
        )
        button_1.place(
            x=274.0,
            y=296.0,
            width=171.0,
            height=41.0
        )

        canvas.create_text(
            139.0,
            2.0,
            anchor="nw",
            text="C.M.S",
            fill="#000000",
            font=("Iceland", 80 * -1)
        )
        
        this.logo = PhotoImage(
            file=this.ctx.assets("logo.png"))
        canvas.create_image(
            82.0,
            41.0,
            image=this.logo
        )
        def kmore():
            for item in this.ctx.window.winfo_children():
                    item.destroy()
            this.ctx.aboutProjectPage()
        if(this.ctx.loggedIn):
            canvas.itemconfig(loginButton,text=this.ctx.user)
            Loginbounds = canvas.bbox(loginButton)
            LoginlabelW = Loginbounds[2] - Loginbounds[0]
            LoginlabelH = Loginbounds[3] - Loginbounds[1]

        def startAnimation(f):
            if this.isAnimating:
                return
            this.isAnimating=True
            
            for i in range(len(this.shapes)):
                t=Thread(target=this.animateBox,args=(canvas,i,100,))
                t.start()
                t1=Thread(target=this.animateTxt,args=(canvas,f,i,100,))
                t1.start()
        this.run=True
        this.bounds={Productsbounds:[ProductslabelH,ProductslabelW,["Track Delivery","View All"]],\
            Aboutbounds:[AboutlabelH,AboutlabelW,["About Project","Contact Us"]]}
        if(this.ctx.loggedIn):
            this.bounds[Loginbounds]=[LoginlabelW ,LoginlabelH,["Logout"]]
        def resetBounds():   
            
            this.bounds={Productsbounds:[ProductslabelH,ProductslabelW,["Track Delivery","View All"]],\
            Aboutbounds:[AboutlabelH,AboutlabelW,["About Project","Contact Us"]]
            }
            if(this.ctx.loggedIn):
                this.bounds[Loginbounds]=[LoginlabelW ,LoginlabelH,["Logout"]]
            
        def checkHover(x:float,y:float):
            for i in this.bounds.keys():
                x1,y1 =i[0],i[1]
                b=this.bounds[i][1]
                h=this.bounds[i][0]
                if(x>x1 and x<x1+b and y>y1 and y<y1+h):
                    return i
            return False
        def motion(event):
                x, y = event.x, event.y
                bound=checkHover(x,y)
                
                if(bound !=False):
                  
                    h,b=this.bounds[bound][0],this.bounds[bound][1]
                    
                    if(this.run):
                        this.stopThread=False
                        this.isAnimating = False
                        x = bound[0]
                        y = bound[3]
                        h = 25
                        b = 125
                        o = pi/3
                        this.run=False
                        texts=this.bounds[bound][2]
                        this.createTiltedRec(canvas,len(texts), x, y, h, b, o,texts)
                        startAnimation(bound)
                        coords=canvas.coords(this.shapes[-1])
                        this.bounds[bound][0]+=len(this.shapes)*(coords[3]-coords[1])
                        this.bounds[bound][1]+=(coords[6]-coords[0])//2
                        
                        
                else:
                      
                    resetBounds()
                    this.run=True
                    try:
                        this.stopThread=True
                        this.isAnimating=False
                        for i in this.shapes:
                            canvas.delete(i)
                        for j in this.txtBoxes:
                            canvas.delete(j)
                            
                        this.shapes.clear()
                        this.txtBoxes.clear()
                    except:
                        pass
        def clicked(event):
                    closest = canvas.find_closest(event.x, event.y)
                    if(loginButton in closest and not this.ctx.loggedIn):
                        for item in this.ctx.window.winfo_children():
                            item.destroy()
                        this.ctx.loginPage()
                    elif(closest[0] in this.shapes or closest[0] in this.txtBoxes):
                        try:
                            selected=canvas.itemcget(this.txtBoxes[this.shapes.index(closest[0])],"text" )
                        except:
                            selected=canvas.itemcget(closest[0],"text" )
                        if("View All" in selected):
                            for item in this.ctx.window.winfo_children():
                                item.destroy()
                            if(not this.ctx.loggedIn):
                                this.ctx.loginPage()
                                return
                            this.ctx.viewAllPage()
                        elif("Track Delivery" in selected):
                            for item in this.ctx.window.winfo_children():
                                item.destroy()
                            if(not this.ctx.loggedIn):
                                this.ctx.loginPage()
                                return
                            this.ctx.trackOrderPage()
                        elif("About Project" in selected):
                            for item in this.ctx.window.winfo_children():
                                item.destroy()
                            this.ctx.aboutProjectPage()
                        elif("Logout" in selected):
                            this.ctx.loggedIn=False
                            this.ctx.user="LogIn"
                            canvas.itemconfig(loginButton,text=this.ctx.user)
                            try:
                                this.stopThread=True
                                this.isAnimating=False
                                for i in this.shapes:
                                    canvas.delete(i)
                                for j in this.txtBoxes:
                                    canvas.delete(j)
                                    
                                this.shapes.clear()
                                this.txtBoxes.clear()
                            except:
                                pass


        
        labels=[]

        def getResult(event):
            for i in labels:
                canvas.delete(i)
            refId=searchBox.get()
            if(refId==""):
                return
            con=this.ctx.getConnector()
            cur=con.cursor()
            query="use users;"
            cur.execute(query)
            labels.clear()
            try:
                query=f"select status from products where refId='{refId}' and status != 'cancled';"
                cur.execute(query)
                results=cur.fetchall()
                y=searchBox.winfo_rooty()+48
                x=searchBox.winfo_rootx()+100
                for i in  results:
                    lb=canvas.create_text(
                        x,
                        y,
                        text=f"status={i[0]}",
                        font=("Vollkorn",16)
                        )
                    labels.append(lb)
                    y+=30
                canvas.update()
            except Exception as e:
                print(e)
            con.close()
        searchBox.bind("<Return>", getResult) 
        canvas.bind('<Button>', clicked)
        
        canvas.bind('<Motion>', motion)
        canvas.update()    

    def createTiltedRec(this,c:Canvas,n:int,x1:float,y1:float,h:float,b:float,theta:float,texts:list):
        
        for i in range(n):
            y1+=h*i
            
            if(i%2==0):
                x1-=b//2.5
                x2=x1+h/tan(theta)
               #x3,x4=x2+b,x1+b
            else:
                x2=x1+b/2
                x1=x2+h/tan(theta)
                #x4,x4=x2+b,x1+b
            y4=y1
            y3=y2=y1+h
            
            x3,x4=x2+b,x1+b
            point=[x1,y1,x2,y2,x3,y3,x4,y4]
            shape=c.create_polygon(point, outline="black",fill='#EB7EF4', width=1) 
            this.shapes.append(shape)
            txt=c.create_text((point[0]+point[6])//2,(point[1]+point[3])//2,text=texts[i%len(texts)],font=("Iceland", 10))
            this.txtBoxes.append(txt)            
    def animateBox(this,c:Canvas,index:int,speed:float):

        try:
            x1,y1,x2,y2,x3,y3,x4,y4=c.coords(this.shapes[index])
            #c.create_line(x1,y1,x2,y2)
            diff=x2-x1
            if(index%2==0):
                end=int(x1)
                jump=4
                
                start=int(2*x1-x4)
              
            else:
                start=int(x4)
                end=int(x1)
                jump=-4
            for i in range(start,end,jump):
                if(this.stopThread):
                    return
                c.coords(this.shapes[index],i,y1,diff+i,y2,(x3-x2)+diff+i,y3,(x4-x1)+i,y4)
                c.update()
                time.sleep(10/(100*speed))
            #c.coords(this.shapes[index],x1,y1,x2,y2,x3,y3,x4,y4) 

        except Exception as e:
            print("[-] Error In HomePage animateBox:",e)
            return           
    def animateTxt(this,c:Canvas,bounds:tuple,index:int,speed:float):
        try:
            x1,y1= c.coords(this.txtBoxes[index])
             
            b = bounds[2] - bounds[0]
            if(index%2==0):
                end=int(x1)
                jump=4
                start=int(x1-b)
            else:
                start=int(x1+b)
                end=int(x1)
                jump=-4
            for i in range(start,end,jump):
                if(this.stopThread):
                    return
                c.coords(this.txtBoxes[index],i,y1)
                c.update()
                time.sleep(10/(100*speed))
            c.coords(this.txtBoxes[index],x1,y1) 

        except Exception as e:
            print("[-] Error In HomePage animateText:",e)
            return

