import tkinter as tk
from tkinter import ttk
import socket

class PortScannerFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.ip_label = ttk.Label(self, text="IP Address:")
        self.ip_label.grid(column=0, row=0, padx=5, pady=5)
        
        self.ip_entry = ttk.Entry(self)
        self.ip_entry.grid(column=1, row=0, padx=5, pady=5)

        self.port_range_label = ttk.Label(self, text="Port Range (start-end):")
        self.port_range_label.grid(column=0, row=1, padx=5, pady=5)
        
        self.port_range_entry = ttk.Entry(self)
        self.port_range_entry.grid(column=1, row=1, padx=5, pady=5)

        self.scan_button = ttk.Button(self, text="Scan", command=self.scan_ports)
        self.scan_button.grid(column=0, row=2, columnspan=2, padx=5, pady=5)

        self.result_text = tk.Text(self, height=20, width=80)
        self.result_text.grid(column=0, row=3, columnspan=2, padx=5, pady=5, sticky='nsew')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)

    def scan_ports(self):
        ip = self.ip_entry.get()
        port_range = self.port_range_entry.get()
        start_port, end_port = map(int, port_range.split('-'))
        
        self.result_text.delete('1.0', tk.END)
        
        for port in range(start_port, end_port + 1):
            result = self.scan_port(ip, port)
            self.result_text.insert(tk.END, f"Port {port}: {'Open' if result else 'Closed'}\n")

    def scan_port(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            sock.connect((ip, port))
        except:
            return False
        else:
            sock.close()
            return True
