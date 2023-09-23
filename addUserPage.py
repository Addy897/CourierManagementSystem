from mapBox import *
from tkinter import *

from nav import Nav

class UserPage:
    def __init__(this,context) -> None:
        this.ctx=context
        this.ctx.addUserPage1=this.addUserPage1
        this.ctx.addUserPage2=this.addUserPage2
    def addUserPage1(this):
        
        n=Nav(this.ctx)
        canvas = Canvas(
            this.ctx.window,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        this.image_image_1 = PhotoImage(
            file=this.ctx.assets("registerBox.png"))
        image_1 = canvas.create_image(
            1080.0,
            372.0,
            image=this.image_image_1
        )

        this.entry_image_1 = PhotoImage(
            file=this.ctx.assets("newUserEntry.png"))
        pincdEntryBg = canvas.create_image(
            1083.5,
            572.0,
            image=this.entry_image_1
        )
        pincd = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        pincd.insert(0,this.ctx.tempData['pincd'])
        pincd.place(
            x=881.0,
            y=542.0,
            width=405.0,
            height=48.0
        )
        phoneEntryBg = canvas.create_image(
            1083.5,
            472.0,
            image=this.entry_image_1
        )
        phone = Entry(
            bd=0,
            bg="#FFFFFF",
            text=this.ctx.tempData['phone'],
            highlightthickness=0
        )
        phone.insert(0,this.ctx.tempData['phone'])
        phone.place(
            x=881.0,
            y=442.0,
            width=405.0,
            height=48.0
        )

        
        addrEntryBg = canvas.create_image(
            1083.5,
            378.0,
            image=this.entry_image_1
        )
        addr = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        addr.insert(0,this.ctx.tempData['addr'])
        addr.place(
            x=881.0,
            y=349.0,
            width=405.0,
            height=48.0
        )

        emailEntryBg = canvas.create_image(
            1083.5,
            284.0,
            image=this.entry_image_1
        )
        email = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        email.insert(0,this.ctx.tempData['email'])
        email.place(
            x=881.0,
            y=254.0,
            width=405.0,
            height=48.0
        )

        fnameEntryBg = canvas.create_image(
            1083.5,
            186.0,
            image=this.entry_image_1
        )
        fname = Entry(
            bd=0,
            bg="#FFFFFF",
            
            highlightthickness=0
        )
        fname.insert(0,this.ctx.tempData['name'])
        fname.place(
            x=881.0,
            y=156.0,
            width=405.0,
            height=48.0
        )

        this.button_image_1 = PhotoImage(
            file=this.ctx.assets("nextButton.png"))
        button_1 = Button(
            image=this.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: this.checkDetails(l),
            relief="flat"
        )
        button_1.place(
            x=878.0,
            y=649.0,
            width=419.0,
            height=50.0
        )

        canvas.create_text(
            874.0,
            48.0,
            anchor="nw",
            text="Register",
            fill="#000000",
            font=("Iceland", 40 * -1)
        )

        canvas.create_text(
            874.0,
            98.0,
            anchor="nw",
            text="Welcome onboard with us!",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        canvas.create_text(
            877.0,
            133.0,
            anchor="nw",
            text="Full Name",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        canvas.create_text(
            878.0,
            319.0,
            anchor="nw",
            text="Address",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        canvas.create_text(
            877.0,
            414.0,
            anchor="nw",
            text="Phone No.",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        canvas.create_text(
            877.0,
            516.0,
            anchor="nw",
            text="Pincode",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        canvas.create_text(
            877.0,
            231.0,
            anchor="nw",
            text="E-Mail",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        login=canvas.create_text(
            1068.0,
            612.0,
            anchor="nw",
            text="Already Have An Account? Login.",
            fill="#000000",
            font=("Vollkorn", 15 * -1)
        )
        e=canvas.create_text(
            1068.0-170,
            612.0,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Vollkorn", 15 * -1)
        )
        canvas.create_rectangle(
            757.0,
            67.0,
            759.0,
            714.0,
            fill="#000000",
            outline="")

        this.image_image_2 = PhotoImage(
            file=this.ctx.assets("newUserBg.png"))
        image_2 = canvas.create_image(
            407.0,
            379.0,
            image=this.image_image_2
        )
        this.locButtonImg = PhotoImage(
            file=this.ctx.assets("loc.png"))
        button_2 = Button(
            image=this.locButtonImg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: this.ctx.window.after(0,gmap),
            relief="flat"
        )
        button_2.place(
            x=960.0,
            y=319.0,
            width=18.0,
            height=22.0
        )
        l=locals()
        def gmap():
            try:
                app=MapBox(this.ctx.window)
                address=app.start()
                addr.delete(0,END)
                addr.insert(0,address.address)
                this.ctx.tempData['addr']=addr
                this.ctx.tempData['city']=address.city
                this.ctx.tempData['state']=address.state if address.state is not None else address.district
                this.ctx.tempData['pincd']=address.postal
                pincd.delete(0,END)
                pincd.insert(0,address.postal)
            except:
                pass
        
        def clicked(event):
                    closest = canvas.find_closest(event.x, event.y)
                    n.changeNav(closest=closest)
                    if login in closest:
                        canvas.destroy()
                        this.ctx.loginPage()
                        
                        
        canvas.bind('<Button>', clicked)
        
        n.nav(canvas,258,0)
        canvas.update()   
    def addUserPage2(this):
        
        n=Nav(this.ctx)
        canvas = Canvas(
            this.ctx.window,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        this.image_image_1 = PhotoImage(
            file=this.ctx.assets("registerBox.png"))
        image_1 = canvas.create_image(
            1080.0,
            372.0,
            image=this.image_image_1
        )

        this.entry_image_1 = PhotoImage(
            file=this.ctx.assets("newUserEntry.png"))
        cpasswEntryBg = canvas.create_image(
            1083.5,
            572.0,
            image=this.entry_image_1
        )
        cpassw = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        cpassw.place(
            x=881.0,
            y=542.0,
            width=405.0,
            height=48.0
        )
        
        passwEntryBg = canvas.create_image(
            1083.5,
            472.0,
            image=this.entry_image_1
        )
        passw = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        passw.place(
            x=881.0,
            y=442.0,
            width=405.0,
            height=48.0
        )

        
        stateEntryBg = canvas.create_image(
            1083.5,
            378.0,
            image=this.entry_image_1
        )
        state = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        
        state.place(
            x=881.0,
            y=348.0,
            width=405.0,
            height=48.0
        )
        state.insert(0,str(this.ctx.tempData['state']))
        citylEntryBg = canvas.create_image(
            1083.5,
            284.0,
            image=this.entry_image_1
        )
        city = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        
        city.place(
            x=881.0,
            y=254.0,
            width=405.0,
            height=48.0
        )
        city.insert(0,str(this.ctx.tempData['city']))
        unameEntryBg = canvas.create_image(
            1083.5,
            186.0,
            image=this.entry_image_1
        )
        uname = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        uname.place(
            x=881.0,
            y=156.0,
            width=405.0,
            height=48.0
        )

        this.button_image_1 = PhotoImage(
            file=this.ctx.assets("signupButton.png"))
        button_1 = Button(
            image=this.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: this.ctx.addUser(l),
            relief="flat"
        )
        button_1.place(
            x=878.0,
            y=649.0,
            width=419.0,
            height=50.0
        )

        canvas.create_text(
            874.0,
            48.0,
            anchor="nw",
            text="Register",
            fill="#000000",
            font=("Iceland", 40 * -1)
        )

        canvas.create_text(
            874.0,
            98.0,
            anchor="nw",
            text="Welcome onboard with us!",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        canvas.create_text(
            877.0,
            133.0,
            anchor="nw",
            text="UserName",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        canvas.create_text(
            878.0,
            319.0,
            anchor="nw",
            text="State",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        canvas.create_text(
            877.0,
            414.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        canvas.create_text(
            877.0,
            516.0,
            anchor="nw",
            text="Confirm Password",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        canvas.create_text(
            877.0,
            231.0,
            anchor="nw",
            text="City",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        back=canvas.create_text(
            1068.0,
            612.0,
            anchor="nw",
            text="Go Back",
            fill="#000000",
            font=("Vollkorn", 15 * -1)
        )
        e=canvas.create_text(
            1068.0-170,
            612.0,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Vollkorn", 15 * -1)
        )
        canvas.create_rectangle(
            757.0,
            67.0,
            759.0,
            714.0,
            fill="#000000",
            outline="")

        this.image_image_2 = PhotoImage(
            file=this.ctx.assets("newUserBg.png"))
        image_2 = canvas.create_image(
            407.0,
            379.0,
            image=this.image_image_2
        )
        l=locals()
        def clicked(event):
                    closest = canvas.find_closest(event.x, event.y)
                    n.changeNav(closest=closest)
                    if back in closest:
                        canvas.destroy()
                        this.addUserPage1()
                        
                        
        canvas.bind('<Button>', clicked)
       
        canvas.update()
        
        n.nav(canvas,285,0)       
    def checkDetails(this,l):
        i=l["e"]
        c=l['canvas']
        this.ctx.tempData['name']=name=l['fname'].get()
        this.ctx.tempData['email']=email=l['email'].get()
        this.ctx.tempData['addr']=addr=l['addr'].get()
        this.ctx.tempData['phone']=phone=l['phone'].get()
        this.ctx.tempData['pincd']=pincd=l['pincd'].get()
        if(len(name)>0 and len(email)>0 and len(addr)>0 and len(phone)==10 and phone.isdigit() and len(pincd)==6 and pincd.isdigit()):
            if("@" not in email):
                this.ctx.show_error(c,i,"Invalid Email")
                l['email'].focus_set()
                return
            if(not this.ctx.parseChars(name)):
                this.ctx.show_error(c,i,"Invalid Name")
                l['name'].focus_set()
                return
            validAddr=convert_coordinates_to_address(convert_address_to_coordinates(addr)[0],convert_address_to_coordinates(addr)[1]).country

            validAddr=validAddr!="India"
            if(not this.ctx.parseChars(addr) or validAddr):
                this.ctx.show_error(c,i,"Invalid Address")
                l['addr'].focus_set()
                return
            this.ctx.show_error(c,i,"Verifying Email","#004dcf")
            c.update()
            result=this.ctx.verifyEmailPage(name,email,this.addUserPage1,this.addUserPage2)
            if(result==False):
                this.show_error(c,i,"Email Does Not Exist")
                l['email'].focus_set()
                return
            
        elif(len(name)==0):
            this.ctx.show_error(c,i,"Enter Name")
            l['name'].focus_set()
            return
        elif(len(addr)==0):
            this.ctx.show_error(c,i,"Enter Address")
            l['addr'].focus_set()
            return
        elif(len(email)==0):
            this.ctx.show_error(c,i,"Enter Email")
            l['email'].focus_set()
            return
        elif(len(phone)!=10 or not phone.isdigit()):
            this.ctx.show_error(c,i,"Enter Valid Phone No.")
            l['phone'].focus_set()
            return
        
        elif(len(pincd)!=6 or not pincd.isdigit()):
            this.ctx.show_error(c,i,"Enter Valid Pincode")
            l['pincd'].focus_set()
            return
