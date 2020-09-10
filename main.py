from tkinter import *
from tkinter.messagebox import showerror,showinfo
import requests
import json

def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    parameter = {
        'authorization' : 'IB2mHfPYuTc7LR4keWCM5drSlJOwojKDpAbNgh1tziyG98s6Q39a7he5dGtMg3ElsnIQ1jSfRPJyKqNr',
        'sender_id' : 'FSTSMS',
        'message' : message,
        'language' : 'english',
        'route' : 'p',
        'numbers' : number
    }
    response = requests.get(url, params=parameter)
    abc = response.json()
    print(abc)
    return abc.get('return')

def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    x = send_sms(num, msg)
    if x == True:
        showinfo("Send Success", "Successfully Sent")
    else:
        showerror("Error", "Something Went Wrong")


#GUI Creation
root = Tk()
root.title("Message Sender")
root.geometry("400x550")
font = ("Helvetica", 22, "bold")

textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)

textMsg = Text(root)
textMsg.pack(fill=X)

sendBtn = Button(root, text="Send", command = btn_click)
sendBtn.pack()

root.mainloop()

