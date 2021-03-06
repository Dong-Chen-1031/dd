def rbVideo():  #點選選項按鈕後處理函式
    global getvideo
    labelMsg.config(text="")
    getvideo = videorb.get()
        
def clickDown():  #按「下載影片」鈕後處理函式
    global getvideo, strftype, listradio
    labelMsg.config(text="")
    if(url.get()==""):  #若未輸入網址就顯示提示訊息
        labelMsg.config(text="網址欄位必須輸入！")
        return

    if(path.get()==""):
        pathdir = 'download'
    else:
        pathdir = path.get()
        pathdir = pathdir.replace("\\", "\\\\")  #將「\」轉換為「\\」
    if not os.path.isdir(pathdir):  #如果資料夾不存在就建立
        os.mkdir(pathdir)

    try:
        yt = YouTube(url.get())
        yt.streams.filter(subtype='mp4', res=getvideo, progressive=True).first().download(pathdir)  #下載mp4影片
        labelMsg.config(text="下載完成！")
    except:
        labelMsg.config(text="影片無法下載！")
        
import tkinter as tk
from pytube import YouTube
import os

win=tk.Tk()
win.geometry("560x280")  #設定主視窗解析度
win.title("下載Youtube影片")
getvideo = "360p"  #影片格式
videorb = tk.StringVar()  #選項按鈕值
url = tk.StringVar()  #影片網址
path = tk.StringVar()  #存檔資料夾

label1=tk.Label(win, text="Youtube網址：")
label1.place(x=123, y=30)
entryUrl = tk.Entry(win, textvariable=url)
entryUrl.config(width=45)
entryUrl.place(x=220, y=30)

label2=tk.Label(win, text="存檔路徑(預設為download資料夾)：")
label2.place(x=10, y=70)
entryPath = tk.Entry(win, textvariable=path)
entryPath.config(width=45)
entryPath.place(x=220, y=70)

btnDown = tk.Button(win, text="下載影片", command=clickDown)
btnDown.place(x=200, y=110)

rb1 = tk.Radiobutton(win, text='360p, mp4', variable=videorb, value='360p', command=rbVideo)
rb1.place(x=200, y=150)
rb1.select()
rb2 = tk.Radiobutton(win, text='720p, mp4', variable=videorb, value='720p', command=rbVideo)
rb2.place(x=200, y=180)

labelMsg = tk.Label(win, text="", fg="red")  #訊息標籤
labelMsg.place(x=200, y=220)
    
win.mainloop()