from tkinter import *
from Application import Application

# Creating a window from the application class
def main():
    root = Tk()
    root.title("Pokemon Battle")
    root.geometry("670x500")

    app = Application(root)
    root.mainloop()

main()