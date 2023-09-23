from tkinter import *
import hashlib
import random
import smtplib
import time
import configparser


class VerifyEmail:
    def __init__(this,context):
        this.configParser = configparser.ConfigParser()   
        configFilePath = r'Config.txt'
        this.configParser.read(configFilePath)
        this.ctx=context
        this.ctx.addUser=this.addUser
        this.ctx.verifyEmailPage=this.verifyEmailPage
    def addUser(this,l):
        this=this.ctx
        if(not this.parseChars(l['uname'].get())):
            this.show_error(l['canvas'],l['e'],"Invail Character In UserName")
            l['uname'].focus_set()
            return
        if(not this.parseChars(l['city'].get())):
            this.show_error(l['canvas'],l['e'],"Invail Character In City")
            l['city'].focus_set()
            return
        if(len(l['passw'].get())<8):
            this.show_error(l['canvas'],l['e'],"Password Must Be Upto 8 Characters")
            l['passw'].focus_set()
            return
        if(l['passw'].get()!=l['cpassw'].get()):
            this.show_error(l['canvas'],l['e'],"Passwords Do Not Match")
            l['cpassw'].focus_set()
            return
        passw=hashlib.sha256((l['uname'].get()+"#"+l['passw'].get()).encode()).hexdigest()
        con=this.getConnector()
        cur=con.cursor()
        
        this.show_error(l['canvas'],l['e'],"Creating Your Account","#004dcf")
        try:
            query=f'''INSERT into user_details (uname,fname,email,address,phone,pincd,state,city,passw) values ("{l['uname'].get()}",
              "{this.tempData['name']}" ,
              "{this.tempData['email']}",
              "{this.tempData['addr']}",
              "{this.tempData['phone']}",
              "{this.tempData['pincd']}",
              "{l['state'].get()}",
              "{l['city'].get()}",
              "{passw}")
              '''
            cur.execute(query)
            this.loggedIn=True
        except Exception as e:
            print(e)
            this.loggedIn=False
        
        con.commit()
        con.close()
        if(this.loggedIn):
            this.user=l['uname'].get()
            for i in this.tempData.keys():
                this.tempData[i]=""
            for item in this.window.winfo_children():
                    item.destroy()
            this.homePage()
            
    def sendOtp(this,name,email,otp):
        try:
            e,p=this.configParser['DEFAULT']['Email'],this.configParser['DEFAULT']['App_Password']
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            try:
                server.login(e, p)
            except smtplib.SMTPAuthenticationError:
               return False
            header='To:'+email+'\n'+'From:'+e+'\n'+'subject:Verification Code\n'+"Hey, "+name+"\nYour Verification Code is: "
            
            msg=header+otp
            server.sendmail(e, email, msg)
            server.close()
        except:
            return False
    def verifyOtp(this,entered,otp,c,e,n):
     
        if(entered==otp):
            for item in this.ctx.window.winfo_children():
                    item.destroy()
            n()
            
        else:
            this.ctx.show_error(c,e,"Invalid OTP")
    def verifyEmailPage(this,name,email,backFunc,nextFunc):
        otp=str(random.randint(100000,999999))
        print("[+] OTP:",otp)
        sucess=this.sendOtp(name,email,otp)
        if(sucess==False):
           return False
        for item in this.ctx.window.winfo_children():
                    item.destroy()
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
        this.verifyBox = PhotoImage(
            file=this.ctx.assets("box.png"))
        image_1 = canvas.create_image(
            1065.0,
            379.0,
            image=this.verifyBox
        )

        this.entry_image_1 = PhotoImage(
            file=this.ctx.assets("loginEntry1.png"))
        entry_bg_1 = canvas.create_image(
            1064.5,
            412.5,
            image=this.entry_image_1
        )
        otpEntry = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        otpEntry.place(
            x=858.0,
            y=386.0,
            width=413.0,
            height=41.0
        )

        this.button_image_1 = PhotoImage(
            file=this.ctx.assets("verifyButton.png"))
        button_1 = Button(
            image=this.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:this.verifyOtp(otpEntry.get(),otp,canvas,e,nextFunc),
            relief="flat"
        )
        button_1.place(
            x=852.0,
            y=488.0,
            width=426.83984375,
            height=43.02984619140625
        )

        canvas.create_text(
            965.0,
            200.0,
            anchor="nw",
            text="Enter OTP",
            fill="#000000",
            font=("Iceland", 40 * -1)
        )

        canvas.create_text(
            860.0,
            250.0,
            anchor="nw",
            text=f"A OTP of 6 digit has been sent to your email\n{email}\n(check in spam also)",
            fill="#000000",
            font=("Vollkorn", 20 * -1)
        )

        b=canvas.create_text(
            1161.0,
            453.0,
            anchor="nw",
            text="Wrong Email?",
            fill="#000000",
            font=("Vollkorn", 15 * -1)
        )
        e=canvas.create_text(
            1161.0-170.0,
            453.0,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Vollkorn", 15 * -1)
        )
        
        r=canvas.create_text(
            1036.0,
            543.0,
            anchor="nw",
            text="Resend",
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
        this.clickable=True
        def clicked(event):
                    closest = canvas.find_closest(event.x, event.y)
                    this.clickable
                    if b in closest:
                        
                        if(backFunc.__name__=="forgotPassPage"):
                            this.ctx.emailValidated = False
                        for item in this.ctx.window.winfo_children():
                            item.destroy()
                        backFunc()
                    if r in closest and this.clickable:
                        count=0
                        this.clickable=False
                        otp=str(random.randint(100000,999999))
                        sucess=this.sendOtp(name,email,otp)
                        while count<=30:
                            try:
                                time.sleep(1)
                                
                                canvas.itemconfig(r,text="Again Resend in: "+str(30-count))
                                canvas.update()
                                count+=1
                            except:
                                return
                        this.clickable=True
        
        canvas.bind('<Button>', clicked)
        
        this.bg = PhotoImage(
            file=this.ctx.assets("newUserBg.png"))
        image_2 = canvas.create_image(
            407.0,
            379.0,
            image=this.bg
        )
        canvas.update()
    