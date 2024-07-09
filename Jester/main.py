import tkinter as tk
from tkinter import ttk
from port_scanner import PortScannerFrame
from network_ping import NetworkPingFrame
from speed_test import SpeedTestFrame
from i2pd_connect import I2PDConnectFrame
from ssh_connect import SSHConnectFrame

class NetworkToolApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jester Tool")
        self.geometry("800x600")

        tabControl = ttk.Notebook(self)

        self.port_scanner_frame = PortScannerFrame(tabControl)
        tabControl.add(self.port_scanner_frame, text='Port Scanner')

        self.network_ping_frame = NetworkPingFrame(tabControl)
        tabControl.add(self.network_ping_frame, text='Network Ping')

        self.speed_test_frame = SpeedTestFrame(tabControl)
        tabControl.add(self.speed_test_frame, text='Speed Test')

        self.i2pd_connect_frame = I2PDConnectFrame(tabControl)
        tabControl.add(self.i2pd_connect_frame, text='I2PD Connect')

        self.ssh_connect_frame = SSHConnectFrame(tabControl)
        tabControl.add(self.ssh_connect_frame, text='SSH Connect')

        tabControl.pack(expand=1, fill="both")

if __name__ == "__main__":
    app = NetworkToolApp()
    app.mainloop()



