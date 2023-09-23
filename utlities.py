
import hashlib
from tkinter import Canvas


class Utilites:
    def __init__(this,context) -> None:
        this.ctx=context
        context.assets=this.assets
        context.show_error=this.show_error
        context.parseChars=this.parseChars
        context.check_login=this.check_login
        context.createRoundedTile=this.createRoundedTile
    def assets(this,path: str):
        return f"./assets/{path}"
    def show_error(this,c:Canvas,i,msg:str,fill="#F10909"):
        return  c.itemconfig(i,
                    text=msg,
                    fill=fill,
                )
    def parseChars(this,text:str):
        bad_chars="=\'\\\"<>-?}{()[]#$%^&*-=+`~" 
        for i in text:
            if (i in bad_chars):
                return False
        return True
    def check_login(this,l:dict):
        email=l["userName"].get()
        passw=l['passw'].get()
        if(len(email)==0 or len(passw)==0):
            this.show_error(l['canvas'],l['e'],"Please Enter Name And Password")
            l['userName'].focus_set()
        if(not this.parseChars(email) or not this.parseChars(passw)):
          this.show_error(l['canvas'],l['e'],"Please Enter Valid Chars")
          l['passw'].itemconifg(text="")
          l['passw'].focus_set()
        con=this.ctx.getConnector()
        cur=con.cursor()
        query=f'''select passw , uname ,eid from user_details where uname="{email}" or email="{email}";'''
        cur.execute(query)
        result=cur.fetchone()
        con.close()
        if(result==None):
            this.show_error(l['canvas'],l['e'],"Invalid UserName or Email")
            return
        passw=hashlib.sha256((result[1]+"#"+passw).encode()).hexdigest()
        
        if(result[0]!=passw):
            
            this.show_error(l['canvas'],l['e'],"Invalid Password")
        else:
            this.ctx.loggedIn=True
            this.ctx.user=result[1]
            this.ctx.uid=result[2]
    def createRoundedTile(this,canvas:Canvas,x,y,height,width,radius=40,fill="#DB4343"):
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
        return canvas.create_polygon(points,fill=fill,smooth=True)