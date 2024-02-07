import tkinter as tk

class ChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Chat Program")

        self.label = tk.Label(master, text="Hello, what's your name?")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Send", command=self.send_message)
        self.button.pack()

    def send_message(self):
        user_input = self.entry.get()
        self.entry.delete(0, tk.END)

        if user_input.upper() == "QUITPROGRAMNOW":
            self.master.destroy()
            return

        self.label.config(text=f"Hello, {user_input}!")

root = tk.Tk()
app = ChatApp(root)
root.mainloop()
