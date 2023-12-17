from tkinter import Frame, Entry, Button, messagebox


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.alertBtn = None
        self.nameInput = None
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # sonoma 中无法正确显示
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertBtn = Button(self, text='Hello', command=self.hello)
        self.alertBtn.pack()

    def hello(self):
        name = self.nameInput.get() or 'World'
        messagebox.showinfo('Message', 'Hello, %s' % name)


app = App()
app.master.title('Hello World')
app.mainloop()
