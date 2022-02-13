import tkinter
import tkinter.colorchooser

def ChooseColor():
    r = tkinter.colorchooser.askcolor(title='顏色選擇器')
    print('十六進位色碼',r[1])
    print('rgb色碼',r[0])
    label1.config(text='十六進位色碼：'+str(r[1]))
    label2.config(text='rgb色碼：'+str(r[0]))


win1 = tkinter.Tk()
win高 = win1.winfo_screenheight()
win寬 = win1.winfo_screenwidth()
x = (win寬-250)/2
y = (win高-300)/2
win1.geometry('%dx%d+%d+%d' %(250,200,x,y))

button1 = tkinter.Button(win1, text='顏色選擇',command=ChooseColor)
button1.pack()
label1=tkinter.Label(win1, text="")
label1.pack()
label2=tkinter.Label(win1, text="")
label2.pack()


win1.mainloop()