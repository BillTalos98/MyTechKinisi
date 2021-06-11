import tkinter as tk

class window():

    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("400x600")
        self.window.configure(background="#FFFFFF")

    def photo(self,path,x,y,x_stat,y_stat):
        self.canvas=tk.Canvas(self.window,width=x,height=y,bd=0)
        self.photo=tk.PhotoImage(file=path)
        self.canvas.create_image(x/2,y/2, anchor="center", image=self.photo)
        self.canvas.pack()
        self.canvas.place(relx=x_stat,rely=y_stat)
        return self

    def app_button(self, text, x_stat, y_stat):
        self.button = tk.Button(self.window, text=text)
        self.button.pack()
        self.button.place(relx=x_stat, rely=y_stat)
        return self

    def click(self):
        self.entry.delete(0,"end")
        self.entry.insert(0,"")


    def foregoing(self,text):
        self.entry.insert(0,text)

    def add_input(self,x,y,w,h):
        self.entry=tk.Entry(self.window,cursor="xterm",font=("calibri",10),justify="center")
        self.entry.pack()
        self.entry.place(relx=x,y=y,width=w,height=h)





    def run(self):
        run=self.window.mainloop()
        return run