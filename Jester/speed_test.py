import tkinter as tk
from tkinter import ttk
import speedtest

class SpeedTestFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.test_button = ttk.Button(self, text="Run Speed Test", command=self.run_speed_test)
        self.test_button.grid(column=0, row=0, padx=5, pady=5)

        self.result_text = tk.Text(self, height=20, width=80)
        self.result_text.grid(column=0, row=1, padx=5, pady=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)

    def run_speed_test(self):
        self.result_text.delete('1.0', tk.END)
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        result = st.results.dict()
        self.result_text.insert(tk.END, f"Download: {result['download'] / 1_000_000:.2f} Mbps\n")
        self.result_text.insert(tk.END, f"Upload: {result['upload'] / 1_000_000:.2f} Mbps\n")
        self.result_text.insert(tk.END, f"Ping: {result['ping']} ms\n")
