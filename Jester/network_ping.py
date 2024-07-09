import tkinter as tk
from tkinter import ttk
import subprocess

class NetworkPingFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.ping_button = ttk.Button(self, text="Ping Google", command=self.ping_google)
        self.ping_button.grid(column=0, row=0, padx=5, pady=5)

        self.result_text = tk.Text(self, height=20, width=80)
        self.result_text.grid(column=0, row=1, padx=5, pady=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)

    def ping_google(self):
        self.result_text.delete('1.0', tk.END)
        process = subprocess.Popen(["ping", "-c", "4", "google.com"], stdout=subprocess.PIPE)
        output, error = process.communicate()
        self.result_text.insert(tk.END, output.decode())

