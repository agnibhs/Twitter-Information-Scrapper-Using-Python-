# Main Program

'''from tkinter import *
window = Tk()
window.title("Twitter Information")
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
window.mainloop()'''

from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests

window = Tk()
window.title("Twitter")
window.geometry('500x400')
window.configure(bg='#07e7f7')

lbl = Label(window,text="Enter the Account name",font=("Algerian",20),bg='#07e7f7',fg='#141452')

lbl.grid(column=0, row=1)

txt = Entry(window, width=40)
txt.grid(column=0, row=2)


def clicked():
    handle = txt.get()
    temp = requests.get('https://twitter.com/' + '@' + handle)
    bs = BeautifulSoup(temp.text, 'lxml')
    try:
        follow_box = bs.find('li', {'class': 'ProfileNav-item ProfileNav-item--followers'})
        followers = follow_box.find('a').find('span', {'class': 'ProfileNav-value'})
        a = "Follower = " + followers.get('data-count')
        lbl_2 = Label(window, text=a,bg="yellow",font=("Arial Black",14))
        lbl_2.grid(column=0, row=6)
    except:
        a = -1

    try:
        following_box = bs.find('li', {'class': 'ProfileNav-item ProfileNav-item--following'})
        following = following_box.find('a').find('span', {'class': 'ProfileNav-value'})
        b = "Following = " + following.get('data-count')
        lbl_3 = Label(window, text=b,bg="yellow",font=("Arial Black",14))
        lbl_3.grid(column=0, row=7)

    except:
        b = -1

    try:
        favorite_box = bs.find('li', {'class': 'ProfileNav-item ProfileNav-item--favorites'})
        favorite = favorite_box.find('a').find('span', {'class': 'ProfileNav-value'})
        c = "Post liked = " + favorite.get('data-count')
        lbl_4 = Label(window, text=c, bg="yellow",font=("Arial Black",14))
        lbl_4.grid(column=0, row=8)
    except:
        c = -1

    try:
        tweet_box = bs.find('li', {'class': 'ProfileNav-item ProfileNav-item--tweets is-active'})
        tweets = tweet_box.find('a').find('span', {'class': 'ProfileNav-value'})
        d = "Tweets = " + tweets.get('data-count')
        lbl_5 = Label(window, text=d,bg="yellow",font=("Arial Black",14))
        lbl_5.grid(column=0, row=9)
    except:
        d = -1

    if a == -1 and b == -1 and c == -1 and d == -1:
        messagebox.showerror("Error", "Account name not found \nPlease Enter Correct Account Name")


btn_1 = Button(window, text="Submit", font=("times new roman",10), command=clicked)
btn_1.grid(column=0, row=3)
btn_1.config(bg='navy', fg='white', bd=8)


def delete():
    txt.delete(first=0, last=100)

btn_2 = Button(window, text="Clear",font=("times new roman",10), command=delete)
btn_2.grid(column=0, row=4)
btn_2.config(bg='navy', fg='white', bd=8)

def destroy():
    window.destroy()


btn_3 = Button(window, text="Quit", font=("times new roman",10), command=destroy)
btn_3.grid(column=0, row=5)
btn_3.config(bg='navy', fg='yellow', bd=8)

window.mainloop()