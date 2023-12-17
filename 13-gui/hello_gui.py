import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 创建一个 Label
        self.helloLabel = tk.Label(self, text="Hello World")
        self.helloLabel.pack(side=tk.TOP)
        # 创建按钮，并且点击后退出程序
        self.quitButton = tk.Button(self, text="Quit", command=self.master.quit)
        self.quitButton.pack(side=tk.BOTTOM)


root = tk.Tk()
app = App(master=root)
# 设置程序窗口标题
app.master.title("Hello World")
# 主消息循环
app.mainloop()
#
# import tkinter as tk
#
#
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.label = tk.Label(self, text="Hello", font="Helvetica 12 bold", highlightcolor="red")
#         self.label.pack()
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World (click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")
#
#     def say_hi(self):
#         self.label.text = "hi there, everyone!"
#
#
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()
