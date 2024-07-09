import tkinter as tk
from tkinter import ttk
import platform
import subprocess
import os
import webbrowser

class I2PDConnectFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.install_button = ttk.Button(self, text="Install i2pd", command=self.install_i2pd)
        self.install_button.grid(column=0, row=0, padx=5, pady=5, sticky='ew')

        self.connect_button = ttk.Button(self, text="Connect to i2pd", command=self.connect_i2pd)
        self.connect_button.grid(column=1, row=0, padx=5, pady=5, sticky='ew')

        self.stop_button = ttk.Button(self, text="Stop i2pd", command=self.stop_i2pd)
        self.stop_button.grid(column=2, row=0, padx=5, pady=5, sticky='ew')

        self.result_text = tk.Text(self, height=20, width=80)
        self.result_text.grid(column=0, row=1, columnspan=3, padx=5, pady=5, sticky='nsew')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def install_i2pd(self):
        os_name = platform.system()
        self.result_text.delete('1.0', tk.END)

        try:
            if os_name == "Linux":
                subprocess.run(["sudo", "apt", "update"], check=True)
                subprocess.run(["sudo", "apt", "install", "-y", "i2pd"], check=True)
                self.result_text.insert(tk.END, "i2pd installed successfully on Linux.\n")
            elif os_name == "Darwin":  # MacOS
                subprocess.run(["brew", "install", "i2pd"], check=True)
                self.result_text.insert(tk.END, "i2pd installed successfully on MacOS.\n")
            else:
                self.result_text.insert(tk.END, f"Unsupported OS: {os_name}\n")
        except subprocess.CalledProcessError as e:
            self.result_text.insert(tk.END, f"Installation failed: {e}\n")

    def connect_i2pd(self):
        self.result_text.delete('1.0', tk.END)

        pid_file = os.path.expanduser("~/Library/Application Support/i2pd/i2pd.pid")

        # Удаление PID-файла, если он существует
        if os.path.exists(pid_file):
            try:
                os.remove(pid_file)
                self.result_text.insert(tk.END, "Removed existing PID file.\n")
            except Exception as e:
                self.result_text.insert(tk.END, f"Failed to remove PID file: {e}\n")
                return

        try:
            process = subprocess.Popen(["i2pd"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                self.result_text.insert(tk.END, "Connected to i2pd service.\n")
                webbrowser.open("http://127.0.0.1:7070/")
            else:
                self.result_text.insert(tk.END, f"Connection failed: {stderr.decode()}\n")
        except Exception as e:
            self.result_text.insert(tk.END, f"Connection failed: {e}\n")

    def stop_i2pd(self):
        self.result_text.delete('1.0', tk.END)

        try:
            process = subprocess.run(["killall", "i2pd"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if process.returncode == 0:
                self.result_text.insert(tk.END, "i2pd service stopped.\n")
            else:
                self.result_text.insert(tk.END, f"Failed to stop i2pd: {process.stderr.decode()}\n")
        except Exception as e:
            self.result_text.insert(tk.END, f"Failed to stop i2pd: {e}\n")
