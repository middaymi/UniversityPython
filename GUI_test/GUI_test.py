import tkinter
# from tkinter import *


def test():
    tkinter._test()


def sayHello(event):
    print("Yet another helloWorld!")


if __name__ == "__main__":
    # test()
    main_frame = tkinter.Tk()

    # btn = tkinter.Button(main_frame, text="Нажми меня", width=30, height=10, bg="white", fg="black")
    # btn.bind("<Button-1>", sayHello)
    # btn.pack(side="right")

    tkinter.Button(main_frame, text="1").grid(row=1, column=1)
    tkinter.Button(main_frame, text="2").grid(row=1, column=2)
    tkinter.Button(main_frame, text="3").grid(row=2, column=1, columnspan=2)

    main_frame.mainloop()
