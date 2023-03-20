from tkinter import*
import pandas as pd
import numpy as np

from sklearn import*
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

win=Tk()
win.config(bg="gray")
win.title("windows application")
win.geometry("1200x1000")

#LogisticRegression
def reg():
    df=pd.read_csv("E:\Python codes\hire_data1.csv")
    
    a=num1.get()
    b=num2.get()
    c=num3.get()
    d=num4.get()
    e=num5.get()
   
    features=df.columns[:5]
    X=df[features]
    Y=df[['Hired']]

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)

    # Convert Y_train and Y_test DataFrames to 1-dimensional arrays
    Y_train = Y_train.values.ravel()
    Y_test = Y_test.values.ravel()
    
    lr=LogisticRegression()
    lr.fit(X_train,Y_train)

    
    y_pred=lr.predict(X_test)

    acc=accuracy_score(Y_test,y_pred)

    out1.set(acc)
    out.set(y_pred)

#DecisionTree
def sec():
    df=pd.read_csv("E:\Python codes\hire_data1.csv")
    
    a=num1.get()
    b=num2.get()
    c=num3.get()
    d=num4.get()
    e=num5.get()
   
    features=df.columns[:5]
    X=df[features]
    Y=df[['Hired']]

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)
    clf=DecisionTreeClassifier()
    clf.fit(X_train,Y_train)
    
    Y_pred=clf.predict(X_test)

    acc=accuracy_score(Y_test,Y_pred)

    out1.set(acc)
    print(Y_pred)
    out.set(Y_pred)

    
frame=Frame(win,bd=10,relief="raised",width=1540,height=50).grid(row=0)
lb=Label(frame,width=150,text="EMPLOYEE HIRING SYSTEM",font=('arial',10,'bold'),fg="Black")
lb.grid(row=0)
frame2=Frame(win,bd=10,relief="raised",width=500,height=400,bg="orange").place(x=560,y=105)
frame3=Frame(win,bd=9,relief="raised",width=350,height=100,bg="orange").place(x=650 ,y=530)

#----------SOLUTION-----------------------------------------------
lb=Label(frame3,text="PREDICTION OUTPUT",width=20).place(x=670,y=550)
lb=Label(frame3,text="ACCURACY SCORE",width=20).place(x=670,y=590)
out=StringVar()
tx8=Entry(frame3,textvariable=out).place(x=850,y=550)
out1=StringVar()
tx9=Entry(frame3,textvariable=out1).place(x=850,y=590)
#------------------------------------------------------------------

lb=Label(frame2,text="PERCENTAGE",width=15).place(x=620,y=200)
lb2=Label(frame2,text="BACKLOG",width=15).place(x=620,y=250)
lb3=Label(frame2,text="INTERNSHIP",width=15).place(x=620,y=300)
lb4=Label(frame2,text="FIRST ROUND",width=15).place(x=620,y=350)
lb5=Label(frame2,text="COMMUNICATION",width=15).place(x=620,y=400)

num1=StringVar()
tx=Entry(frame2,textvariable=num1).place(x=750,y=200)

num2=StringVar()
tx2=Entry(frame2,textvariable=num2).place(x=750,y=250)

num3=StringVar()
tx3=Entry(frame2,textvariable=num3).place(x=750,y=300)

num4=StringVar()
tx4=Entry(frame2,textvariable=num4).place(x=750,y=350)

num5=StringVar()
tx4=Entry(frame2,textvariable=num5).place(x=750,y=400)

btn=Button(frame2,text="LOGISTIC Reg.",command=reg,font=('arial',10,'bold'),width=15,bd=8,relief="raised").place(x=900,y=190)
btn2=Button(frame2,text="Decesion Tree",command=sec,font=('arial',10,'bold'),width=15,bd=8,relief="raised").place(x=900,y=240)
btn2=Button(frame2,text="SVM",font=('arial',10,'bold'),width=15,bd=8,relief="raised").place(x=900,y=290)
btn3=Button(frame2,text="Random Forest",font=('arial',10,'bold'),width=15,bd=8,relief="raised").place(x=900,y=340)
