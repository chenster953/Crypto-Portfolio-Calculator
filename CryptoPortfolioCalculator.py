import yfinance as yf
from tkinter import *

root = Tk()
root.title('Portfolio')
root.geometry('350x150')

# Labels

THETA_LABEL = Label(root, text='Theta')
THETA_LABEL.grid(row=0, column=0)
TFUEL_LABEL = Label(root, text='T-Fuel')
TFUEL_LABEL.grid(row=1, column=0)
VET_LABEL = Label(root, text='Vechain')
VET_LABEL.grid(row=2, column=0)
VTHO_LABEL = Label(root, text='Vtho')
VTHO_LABEL.grid(row=3, column=0)
ZIL_LABEL = Label(root, text='Zil')
ZIL_LABEL.grid(row=4, column=0)


# Entry

theta = Entry(root, width=30)
theta.grid(row=0, column=1)
tfuel = Entry(root, width=30)
tfuel.grid(row=1, column=1)
vet = Entry(root, width=30)
vet.grid(row=2, column=1)
vtho = Entry(root, width=30)
vtho.grid(row=3, column=1)
zil = Entry(root, width=30)
zil.grid(row=4, column=1)


def THETA():
    info = theta.get()
    ticker = yf.Ticker("THETA-USD")
    thetaprice = ticker.info['regularMarketPrice']
    THETA = float(info) * float(thetaprice)
    THETA = round(THETA, 4)
    theta_label = Label(root, text=THETA)
    theta_label.grid(row=0, column=4)
    theta.delete(0, END)


def TFUEL():
    info = tfuel.get()
    ticker = yf.Ticker("TFUEL-USD")
    tfuelprice = ticker.info['regularMarketPrice']
    TFUEL = float(info) * float(tfuelprice)
    TFUEL = round(TFUEL, 4)
    tfuel_label = Label(root, text=TFUEL)
    tfuel_label.grid(row=1, column=4)
    tfuel.delete(0, END)


def VET():
    info = vet.get()
    ticker = yf.Ticker("VET-USD")
    vetprice = ticker.info['regularMarketPrice']
    VET = float(info) * float(vetprice)
    VET = round(VET, 4)
    vet_label = Label(root, text=VET)
    vet_label.grid(row=2, column=4)
    vet.delete(0, END)


def VTHO():
    info = vtho.get()
    ticker = yf.Ticker("VTHO-USD")
    vthoprice = ticker.info['regularMarketPrice']
    VTHO = float(info) * float(vthoprice)
    VTHO = round(VTHO, 4)
    vtho_label = Label(root, text=VTHO)
    vtho_label.grid(row=3, column=4)
    vtho.delete(0, END)



def ZIL():
    info = zil.get()
    ticker = yf.Ticker("ZIL-USD")
    zilprice = ticker.info['regularMarketPrice']
    ZIL = float(info) * float(zilprice)
    ZIL = round(ZIL, 4)
    zil_label = Label(root, text=ZIL)
    zil_label.grid(row=4, column=4)
    zil.delete(0, END)


# Buttons

theta_button = Button(root, text='Submit', command=THETA)
theta_button.grid(row=0, column=3)
tfuel_button = Button(root, text='Submit', command=TFUEL)
tfuel_button.grid(row=1, column=3)
vet_button = Button(root, text='Submit', command=VET)
vet_button.grid(row=2, column=3)
vtho_button = Button(root, text='Submit', command=VTHO)
vtho_button.grid(row=3, column=3)
zil_button = Button(root, text='Submit', command=ZIL)
zil_button.grid(row=4, column=3)

root.mainloop()

