import tkinter as tk
from tkinter import ttk
import paramiko

class SSHConnectFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.ip_label = ttk.Label(self, text="IP Address:")
        self.ip_label.grid(column=0, row=0, padx=5, pady=5)
        
        self.ip_entry = ttk.Entry(self)
        self.ip_entry.grid(column=1, row=0, padx=5, pady=5)

        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.grid(column=0, row=1, padx=5, pady=5)
        
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(column=1, row=1, padx=5, pady=5)

        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.grid(column=0, row=2, padx=5, pady=5)
        
        self.password_entry = ttk.Entry(self, show='*')
        self.password_entry.grid(column=1, row=2, padx=5, pady=5)

        self.connect_button = ttk.Button(self, text="Connect", command=self.connect_ssh)
        self.connect_button.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

        self.result_text = tk.Text(self, height=20, width=80)
        self.result_text.grid(column=0, row=4, columnspan=2, padx=5, pady=5)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)

    def connect_ssh(self):
        ip = self.ip_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        self.result_text.delete('1.0', tk.END)
        
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, username=username, password=password)
            stdin, stdout, stderr = ssh.exec_command('ls')
            self.result_text.insert(tk.END, stdout.read().decode())
            ssh.close()
        except Exception as e:
            self.result_text.insert(tk.END, str(e))
