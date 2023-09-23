from threading import Thread
from tkinter import *
from nav import Nav
class ContactUs:
    def __init__(this,context):
        this.ctx=context
        this.ctx.contactUsPage=this.contactUsPage
    def contactUsPage(this):
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
        n.nav(canvas,258,0)

        def clicked(event):
            closest = canvas.find_closest(event.x, event.y)
            n.changeNav(closest=closest)

        canvas.bind('<Button>', clicked)