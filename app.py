from tkinter import Tk
from aboutProjectPage import AboutProject
from cancelOrderPage import CancelOrder
from contactUsPage import ContactUs
from loginPage import LoginPage
from placeOrderPage import PlaceOrder
from reportOrder import ReportOrder
from setupSql import setupSql
from homePage import  HomePage
from addUserPage import UserPage
from trackOrderPage import TrackOrder
from utlities import Utilites
from verifyEmailPage import VerifyEmail
from viewAllPage import ViewAll
from viewOrdersPage import ViewOrders

class App:
    def __init__(this):
        this.getConnector=setupSql(this).getConnector
        this.loggedIn=False
        this.emailValidated = False
        this.user="LogIn"
        this.uid=-1
        this.tempData={"name":"","email":"","phone":"","addr":"","pincd":"","city":"","state":""}
        this.window = Tk()
        this.window.title("C.M.S")
        this.window.geometry("1366x768")
        this.window.configure(bg = "#FFFFFF")
       
        HomePage(this)
        LoginPage(this)
        UserPage(this)
        ViewAll(this)
        TrackOrder(this)
        PlaceOrder(this)
        Utilites(this)
        VerifyEmail(this)
        ViewOrders(this)
        CancelOrder(this)
        ReportOrder(this)
        AboutProject(this)
        ContactUs(this)
            
    def run(this):
        this.homePage()
        this.window.resizable(False, False)
        this.window.mainloop()
    
    
                
        
a=App()
a.run()                
    
