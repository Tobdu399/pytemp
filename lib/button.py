from lib.misc import tkinter


class Button(tkinter.Button):
    def __init__(self, root, x, y, width, height, text, command):
        super().__init__(text=text, command=command, bg="#57e34d", activebackground="#57e34d",
                         font=("Ubuntu", 13), relief="flat", overrelief="groove")

        self.root = root
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        self.place(x=self.x, y=self.y, width=self.width, height=self.height)


if __name__ == "__main__":
    exit()
