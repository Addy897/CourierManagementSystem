import sqlite3 as mysql
class setupSql:
    def __init__(this,context):
            this.ctx=context
            this.ctx.getConnector=this.getConnector
            this.setup()
    def setup(this):
        try:
            connector=this.getConnector()
            cursor=connector.cursor()
            #query="create database if not exists users;"
            #cursor.execute(query)
            #query="use users;"
            #cursor.execute(query)
            query="create table if not exists user_details(eid  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , fname varchar(100) not null ,email varchar(100) not null unique,uname varchar(100) not null unique ,address varchar(50) not null,phone int(10) not null,pincd int(6) not null,state varchar(20) not null,city varchar(20) not null,passw varchar(64) not null);"
            cursor.execute(query)
            query="create table if not exists products(pid  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,sname varchar(100) not null, rname varchar(100) not null ,saddr varchar(100) not null ,raddr varchar(100) not null  ,spno int(10) not null,rpno int(10) not null,pDate Date not null,rDate Date not null,image varchar(100) not null,status varchar(64) not null,refId varchar(64) not null unique,uid int not null);"
            cursor.execute(query)
            query="create table if not exists reports(rid  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,rname varchar(100) not null, reason varchar(100) not null ,refId varchar(64) not null,uid int not null);"
            cursor.execute(query)
            
            connector.close()
        except Exception as e:
            print(e)
            return
        
    def getConnector(this):
        return mysql.connect('cms.db')
