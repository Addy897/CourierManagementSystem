from tkinter import Event, PhotoImage, Tk, Canvas
class Nav:
    def __init__(this,context) -> None:
        this.ctx=context

    def nav(this,canvas:Canvas,x,y):
        this.canvas=canvas
        width=280
        rec=this.createNavRec(canvas=canvas,x=x,y=y,height=40,width=width)
        gap=48
        start=x+width//4
       
        this.homeImageLoc = PhotoImage(
            file=this.ctx.assets("home.png"))
        this.homeImg = canvas.create_image(
            start,y+20,
            image=this.homeImageLoc
        )
        this.productImageLoc = PhotoImage(
            file=this.ctx.assets("product.png"))
        this.productImg = canvas.create_image(
           start+gap,y+20,
            image=this.productImageLoc
        )
        this.aboutImageLoc = PhotoImage(
            file=this.ctx.assets("about.png"))
        this.aboutImg = canvas.create_image(
            start+(gap*2),y+20,
            image=this.aboutImageLoc
        )
        this.contactImageLoc = PhotoImage(
            file=this.ctx.assets("tone.png"))
        this.contactImg = canvas.create_image(
           start+(gap),y+20,
            image=this.contactImageLoc,
            state='hidden'
        )
        this.loginImageLoc = PhotoImage(
            file=this.ctx.assets("user.png"))
        this.loginImg = canvas.create_image(
           start+(gap*3),y+20,
            image=this.loginImageLoc
        )
       
        this.backImageLoc = PhotoImage(
            file=this.ctx.assets("back.png"))
        this.backImg = canvas.create_image(
            start,y+20,
            image=this.backImageLoc,
            state='hidden'

        ) 
        this.viewAllImageLoc = PhotoImage(
            file=this.ctx.assets("all.png"))
        this.viewAllImg = canvas.create_image(
            start+gap,y+20,
            image=this.viewAllImageLoc,
            state='hidden'

        )   
        this.trackImageLoc = PhotoImage(
            file=this.ctx.assets("track.png"))
        this.trackImg = canvas.create_image(
            start+(gap*2),y+20,
            image=this.trackImageLoc,
            state='hidden'

        )   
        this.projImageLoc = PhotoImage(
            file=this.ctx.assets("proj.png"))
        this.projImg = canvas.create_image(
            start+(gap*2),y+20,
            image=this.projImageLoc,
            state='hidden'

        )
        def onHover(event):
            closest=canvas.find_closest(event.x,event.y)
            if(this.homeImg in closest):
                this.homeImageLoc = PhotoImage(file=this.ctx.assets("homeW.png"))
            elif(this.productImg in closest):
                this.productImageLoc = PhotoImage(file=this.ctx.assets("productW.png"))  

            elif(this.aboutImg in closest):
                this.aboutImageLoc = PhotoImage(file=this.ctx.assets("aboutW.png"))    
            elif(this.contactImg in closest):
                this.contactImageLoc = PhotoImage(file=this.ctx.assets("toneW.png"))    
            elif(this.loginImg in closest):
                this.loginImageLoc = PhotoImage(file=this.ctx.assets("userW.png"))    
            
            else:
                this.homeImageLoc = PhotoImage(file=this.ctx.assets("home.png"))
                this.productImageLoc = PhotoImage(file=this.ctx.assets("product.png"))
                this.aboutImageLoc = PhotoImage(file=this.ctx.assets("about.png"))
                this.loginImageLoc = PhotoImage(file=this.ctx.assets("user.png"))
                this.contactImageLoc = PhotoImage(file=this.ctx.assets("tone.png"))
            canvas.itemconfig(this.homeImg,image=this.homeImageLoc)
            canvas.itemconfig(this.productImg,image=this.productImageLoc)
            canvas.itemconfig(this.aboutImg,image=this.aboutImageLoc)
            canvas.itemconfig(this.contactImg,image=this.contactImageLoc)
            canvas.itemconfig(this.loginImg,image=this.loginImageLoc)
        canvas.bind("<Motion>",onHover)
    def changeNav(this,closest):
            if(this.homeImg in closest):
                this.ctx.tempData={"name":"","email":"","phone":"","addr":"","pincd":"","city":"","state":""}
                for item in this.ctx.window.winfo_children():
                    item.destroy()
                this.canvas.destroy()
                this.ctx.homePage()
            elif(this.loginImg in closest):
                if(not this.ctx.loggedIn):
                    for item in this.ctx.window.winfo_children():
                        item.destroy()
                    this.canvas.destroy()
                    this.ctx.loginPage()
                else:
                    this.ctx.loggedIn=False
                    this.ctx.user="Login"
                    for item in this.ctx.window.winfo_children():
                        item.destroy()
                    this.canvas.destroy()
                    this.ctx.loginPage()
            elif(this.productImg in closest):
                if(this.ctx.loggedIn):
                    this.updateNav("product")
                else:
                    for item in this.ctx.window.winfo_children():
                        item.destroy()
                    this.canvas.destroy()
                    this.ctx.loginPage()
            elif(this.backImg in closest):
                this.updateNav("reset")
            elif (this.aboutImg in closest):
                this.updateNav("about")
            elif(this.viewAllImg in closest):
                for item in this.ctx.window.winfo_children():
                    item.destroy()
                this.canvas.destroy()
                this.ctx.viewAllPage()
            elif(this.trackImg in closest):
                for item in this.ctx.window.winfo_children():
                    item.destroy()
                this.canvas.destroy()
                this.ctx.trackOrderPage()
            elif(this.contactImg in closest):
                for item in this.ctx.window.winfo_children():
                    item.destroy()
                this.canvas.destroy()
                this.ctx.contactUsPage()
            elif(this.projImg in closest):
                for item in this.ctx.window.winfo_children():
                    item.destroy()
                this.canvas.destroy()
                this.ctx.aboutProjectPage()

    def show(this,elemt:list,hide:str):
        for i in elemt:
           this.canvas.itemconfig(i,state=hide)
    def updateNav(this,to:str):
        if("product" in to):
            this.show([this.aboutImg,this.homeImg,this.productImg,this.loginImg,this.contactImg],'hidden')
            this.show([this.backImg,this.viewAllImg,this.trackImg],'normal')
        elif("about" in to):
            this.show([this.aboutImg,this.homeImg,this.productImg,this.trackImg,this.loginImg,this.contactImg],'hidden')
            this.show([this.backImg,this.contactImg,this.projImg],'normal')
        elif("reset" in to):
            this.show([this.aboutImg,this.homeImg,this.productImg,this.loginImg,this.contactImg],'normal')
            this.show([this.backImg,this.viewAllImg,this.contactImg,this.trackImg,this.projImg],'hidden')
    def createNavRec(this,canvas:Canvas,x,y,height,width,radius=40):
        x2=x+width
        y2=y+height
        points=[x,y,
                x+radius,y,
                x2-radius,y,
                x2,y,
                x2,y+radius,
                x2,y2-radius,
                x2,y2,
                x2-radius,y2,
                x+radius,y2,
                x,y2,
                x,y2-radius,
                x,y+radius,
                ]
        return canvas.create_polygon(points,fill="#2BCCFF",smooth=True)

        
