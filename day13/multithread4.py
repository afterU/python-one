import threading
import tkinter
from time import sleep

def main():
    class DownLoad_Task(threading.Thread):
        def run(self):
            sleep(10)
            tkinter.messagebox.showinfo('提示','下载完成')
            button1.config(state=tkinter.NORMAL)

    def download():
        button1.config(state=tkinter.DISABLED)
        DownLoad_Task(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)


    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载',command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于',command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == '__main__':
    main()