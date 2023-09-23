import hashlib
from tkinter import *

from nav import Nav


class LoginPage:
    def __init__(this, context):
        this.ctx = context
        this.ctx.loginPage = this.loginPage

    def loginPage(this):
        n = Nav(this.ctx)
        canvas = Canvas(
            this.ctx.window,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)

        this.image_image_1 = PhotoImage(
            file=this.ctx.assets("box.png"))
        image_1 = canvas.create_image(
            1065.0,
            379.0,
            image=this.image_image_1
        )

        this.entry_image_1 = PhotoImage(
            file=this.ctx.assets("loginEntry1.png"))
        entry_bg_1 = canvas.create_image(
            1064.5,
            412.5,
            image=this.entry_image_1
        )
        passw = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            show="*"
        )
        passw.place(
            x=858.0,
            y=386.0,
            width=413.0,
            height=41.0
        )
        entry_bg_2 = canvas.create_image(
            1064.0,
            331.0,
            image=this.entry_image_1
        )
        userName = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        userName.place(
            x=858.0,
            y=304.0,
            width=412.0,
            height=42.0
        )

        this.button_image_1 = PhotoImage(
            file=this.ctx.assets("loginButton.png"))

        button_1 = Button(
            image=this.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: login(),
            relief="flat"
        )
        button_1.place(
            x=852.0,
            y=488.0,
            width=426.83984375,
            height=43.02984619140625
        )

        canvas.create_text(
            1017.0,
            206.0,
            anchor="nw",
            text="Login",
            fill="#000000",
            font=("Iceland", 40 * -1)
        )

        canvas.create_text(
            851.0,
            279.0,
            anchor="nw",
            text="Name or Email",
            fill="#000000",
            font=("Cosmic Sans MS", 20 * -1)
        )

        canvas.create_text(
            851.0,
            362.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Cosmic Sans MS", 20 * -1)
        )

        Fp = canvas.create_text(
            1122.0,
            455.0,
            anchor="nw",
            text="Forgot Password?",
            fill="#000000",
            font=("Cosmic Sans MS", 15 * -1)
        )
        e = canvas.create_text(
            1122.0-270,
            455.0,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Cosmic Sans MS", 15 * -1)
        )
        NewUser = canvas.create_text(
            953.0,
            548.0,
            anchor="nw",
            text="New To C.M.S? Register Here",
            fill="#000000",
            font=("Cosmic Sans MS", 15 * -1)
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
        l = locals()

        def login():
            this.ctx.check_login(l)
            if (this.ctx.loggedIn):
                userName.destroy()
                passw.destroy()
                button_1.destroy()
                canvas.destroy()
                this.ctx.homePage()

        def clicked(event):
            closest = canvas.find_closest(event.x, event.y)
            n.changeNav(closest=closest)
            if Fp in closest:
                for item in this.ctx.window.winfo_children():
                    item.destroy()
                this.forgotPassPage()
            if NewUser in closest:
                userName.destroy()
                passw.destroy()
                button_1.destroy()
                this.ctx.addUserPage1()
                canvas.destroy()

        canvas.bind('<Button>', clicked)
        n.nav(canvas, 258, 0)

    def forgotPassPage(this):
        
        n = Nav(this.ctx)
        canvas = Canvas(
            this.ctx.window,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)

        this.image_image_1 = PhotoImage(
            file=this.ctx.assets("box.png"))
        image_1 = canvas.create_image(
            1065.0,
            379.0,
            image=this.image_image_1
        )

        entry_bg_2 = canvas.create_image(
            1064.0,
            331.0,
            image=this.entry_image_1
        )
        userName = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        userName.place(
            x=858.0,
            y=304.0,
            width=412.0,
            height=42.0
        )

        this.button_image_1 = PhotoImage(
            file=this.ctx.assets("loginButton.png"))

        findAccount = this.ctx.createRoundedTile(
            canvas,
            x=852.0,
            y=488.0,
            width=419.0,
            height=40.0,
            radius=40,
            fill="#2040cF"
        )
        findTxt = canvas.create_text(
            1000.0,
            488.0,
            anchor="nw",
            text="Find Account",
            fill="#000000",
            font=("Vollkorn", 25 * -1)
        )

        canvas.create_text(
            1017.0,
            206.0,
            anchor="nw",
            text="Login",
            fill="#000000",
            font=("Iceland", 40 * -1)
        )

        nameTxt=canvas.create_text(
            851.0,
            279.0,
            anchor="nw",
            text="Name or Email",
            fill="#000000",
            font=("Cosmic Sans MS", 20 * -1)
        )
        e = canvas.create_text(
            1122.0-270,
            455.0,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Cosmic Sans MS", 15 * -1)
        )
        back = canvas.create_text(
            953.0,
            548.0,
            anchor="nw",
            text="Back",
            fill="#000000",
            font=("Cosmic Sans MS", 15 * -1)
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
        if(this.ctx.emailValidated==True):
            this.ctx.emailValidated=False
            entry_bg_1 = canvas.create_image(
                1064.5,
                412.5,
                image=this.entry_image_1
            )
            this.passw = Entry(
                bd=0,
                bg="#FFFFFF",
                highlightthickness=0,
                
            )
            this.passw.place(
                x=858.0,
                y=386.0,
                width=413.0,
                height=41.0
            )
            canvas.create_text(
                851.0,
                362.0,
                anchor="nw",
                text="Confirm Password",
                fill="#000000",
                font=("Cosmic Sans MS", 20 * -1)
            )
            canvas.itemconfigure(findTxt, text="Change Password")
            canvas.itemconfigure(nameTxt, text="New Password")
        l = locals()

        def clicked(event):
            closest = canvas.find_closest(event.x, event.y)
            n.changeNav(closest=closest)
            if back in closest:
                for item in this.ctx.window.winfo_children():
                    item.destroy()
                this.loginPage()
            elif (findAccount in closest or findTxt in closest):
                uname = userName.get()
                
                if(canvas.itemcget(findTxt,"text")=="Change Password"):
                    newPass=this.passw.get()
                    if(newPass!=uname and newPass!=""):
                        this.ctx.show_error(canvas,e,"Passwords Do Not Match")
                        return
                    else:
                       
                        passw=hashlib.sha256((this.name+"#"+newPass).encode()).hexdigest()
                        con = this.ctx.getConnector()
                        cur = con.cursor()
                        query = "use users;"
                        cur.execute(query)
                        query = f'''update user_details set passw="{passw}" where uname="{this.name}";'''
                        cur.execute(query)
                        result = cur.fetchone()
                        con.commit()
                        con.close()
                        for item in this.ctx.window.winfo_children():
                            item.destroy()
                        this.loginPage()
                        return
                
                if (uname != "" and this.ctx.parseChars(uname)):
                    con = this.ctx.getConnector()

                    cur = con.cursor()
                    query = "use users;"
                    cur.execute(query)
                    query = f'''select uname,email from user_details where email="{uname}" or uname="{uname}";'''
                    cur.execute(query)
                    result = cur.fetchone()
                    con.close()
                    if (not result == None):

                        this.ctx.show_error(
                            canvas, e, "Verifying Email", "#004dcf")
                        canvas.update()
                        name, email = result
                        this.name=name
                        result = this.ctx.verifyEmailPage(
                            name, email, this.forgotPassPage, this.forgotPassPage)
                        if (result == False):
                            this.show_error(
                                canvas, e, "Couldn't Verify Your Email")
                            return
                        else:
                            this.ctx.emailValidated = True
                        

                    else:
                        this.ctx.show_error(canvas, e, "Account Not Found!")
                else:
                    this.ctx.show_error(canvas, e, "Invalid Name Or Email")

        canvas.bind('<Button>', clicked)
        n.nav(canvas, 258, 0)
