import customtkinter
import json
import tkinter as tk
import time

print("###########################\nTHIS ZONE IS FOR DEBBUGGING\n###########################")

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
<<<<<<< HEAD

        # Widgets

=======
        
        # Widgets
        
>>>>>>> 17f67c06083ba1eeb2acbf178b4475824d91ab76
        self.label = customtkinter.CTkLabel(self, font=("Arial", 32), text="Login System")
        self.label.grid(padx=235, pady=(50, 30))

        self.keyCheckerText = self.label = customtkinter.CTkLabel(self, text="", font=("Arial", 20))
        self.label.grid(padx=0, pady=(10, 20))

        self.keyInserBox = self.entry = customtkinter.CTkEntry(self, placeholder_text="Key here", width=190)
        self.entry.grid(padx=0, pady=0)

        self.button = customtkinter.CTkButton(master=self, command=self.login, text="Login", width=80)
        self.button.grid(padx=0, pady=50)

    def login(self):
        self.correct = "Correct! Welcome."
        self.incorrect = "Incorrect key."
<<<<<<< HEAD

        # Checker

        print(self.entry.get())
        with open("data.json", "r") as r:
=======
        print(self.entry.get()) # reading the input
        with open("data.json", "r") as r: # reading the key json file
>>>>>>> 17f67c06083ba1eeb2acbf178b4475824d91ab76
            data = json.load(r)
            for item in data: # checker
                if item['key'] == self.entry.get(): # if valid
                    self.keyCheckerText.configure(text="Correct! Welcome.")
                    print(self.correct)
                    self.keyInserBox.delete(0, tk.END)

                elif self.entry.get() == "": # if no given key
                    self.keyCheckerText.configure(text="No given key.")
                    print("No given key.")

<<<<<<< HEAD
                else:
                    self.keyCheckerText.configure(text="Incorrect key. Make sure you don't put spaces.")
=======
                else: # if invalid
                    self.keyCheckerText.configure(text="Incorrect key.")
>>>>>>> 17f67c06083ba1eeb2acbf178b4475824d91ab76
                    print(self.incorrect)
                    self.keyInserBox.delete(0, tk.END)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Appearance

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        # Window {geometry, center calc}

        window_x = int((App.winfo_screenwidth(self) - 700) / 2)
        window_y = int((App.winfo_screenheight(self) - 400) / 2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.geometry(f"700x400+{window_x}+{window_y}")
        self.title("Key Test")
        self.resizable(False, False)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


<<<<<<< HEAD
if __name__ == "__main__":
    try:
        app = App()
        app.mainloop()
    except KeyboardInterrupt:
        print("Canceled by user.")
=======

app = App()
app.mainloop()
>>>>>>> 17f67c06083ba1eeb2acbf178b4475824d91ab76
