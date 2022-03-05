from tkinter import *
import pyautogui as keyboard
import time

def spammer():
    rmsg.place(x=330,y=275)
    print(words.get("1.0","end"))
    wordslist=words.get("1.0","end").split('\n')
    time.sleep(float(betw_s_m.get()))
    i=0
    if dada:
        while i<len(wordslist):
            keyboard.write(f"{wordslist[i]} {i}")
            keyboard.press("enter")
            time.sleep(float(betw_msg.get()))
            i+=1
    else:
        while i<len(wordslist):
            keyboard.write("{wordslist[i]}")
            keyboard.press("enter")
            time.sleep(float(betw_msg.get()))
            i+=1
    rmsg.place_forget()

def checkvarsdef():
    try:
        float(betw_msg.get())
    except ValueError:
        errormsg.place(x=330,y=130)
    else:
        errormsg.place_forget() #destroy
    try:
        float(betw_s_m.get())
    except ValueError:
        errors_m.place(x=330,y=150)
    else:
        errors_m.place_forget() #destroy

def main():
    window = Tk()

    global rmsg
    global dada
    global betw_msg
    global betw_s_m
    global words
    global errors_m
    global errormsg
    dada=IntVar()
    #see_iter=BooleanVar()
    #see_iter.set(True)
    window.title("Spammer by Plaza52(twilight#6866)")
    window.geometry("700x347") #700x347
    window.resizable(width=False, height=False)
    window["bg"] = "black"

    
    info = Label(window,
        font=("Arial Bold",15),
        text="""  Enter(copy) text in text shield,
after juct click button START""",
        bg="black",
        fg="white"
    )
    info.place(x=315,y=0)
    
    words = Text(window,
        width=40,
        height=20,
        bg="gray",
        fg="white",
        bd=0
    )
    words.place(x=0,y=0)
    words.focus()

    
    START = Button(
        text="START",
        width=7,
        height=3,
        bg="gray",
        fg="white",
        highlightcolor="black",
        command=spammer
    )
    START.place(x=475,y=200)

    
    see_iterw = Checkbutton(
        text="See iterator after string",
        variable=dada,
        bg="black",
        fg="gray",
    )
    see_iterw.pack()
    see_iterw.place(x=325, y=50)

    
    betw_msg = Entry(window,
        width=10,
        bg="gray",
        fg="white",
    )
    betw_msg.place(x=330,y=70)

    betw_msginfo = Label(window,
        text="Time between msg (Float)",
        bg="black",
        fg="white"
    )
    betw_msginfo.place(x=420,y=70)


    betw_s_m = Entry(window,
        width=10,
        bg="gray",
        fg="white",
    )
    betw_s_m.place(x=330,y=100)

    betw_s_minfo = Label(window,
        text="Time between START and first msg (Float)",
        bg="black",
        fg="white"
    )
    betw_s_minfo.place(x=420,y=100)

    errormsg = Label(
        text=f"Please enter value in 1st text shield",
        fg="red",
        bg="black"
    )
    errors_m = Label(
        text=f"Please enter value in 2nd text shield",
        fg="red",
        bg="black"
    )

    checkvars = Button(
        text="CHECK VALUES",
        fg="white",
        bg="gray",
        width=14,
        height=3,
        command=checkvarsdef
    )
    checkvars.place(x=330,y=200)

    rmsg = Label(
        text=f"Spammer started, wait for start script",
        bg="black",
        fg="red",
    )
    
    window.mainloop()
    

if __name__=="__main__":
    main()
