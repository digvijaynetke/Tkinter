import tkinter as tk
from tkinter import scrolledtext, ttk
import scapy.all as scapy
from scapy.layers import http
import threading
import time

class RetroNIDS:
    def __init__(self, master):
        self.master = master
        master.title("Retro NIDS")
        master.configure(bg='black')

        self.create_widgets()
        self.sniffing = False

    def create_widgets(self):
        # Log display
        self.log = scrolledtext.ScrolledText(self.master, bg='black', fg='green', font=('Courier', 10))
        self.log.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Start button
        self.start_button = tk.Button(self.master, text="Start", command=self.start_sniffing,
                                      bg='darkgreen', fg='white', font=('Courier', 10))
        self.start_button.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        # Stop button
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_sniffing,
                                     bg='darkred', fg='white', font=('Courier', 10), state='disabled')
        self.stop_button.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        # Configure grid
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

    def log_message(self, message):
        self.log.insert(tk.END, f"{message}\n")
        self.log.see(tk.END)

    def start_sniffing(self):
        self.sniffing = True
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')
        self.log_message("Starting network sniffing...")
        threading.Thread(target=self.sniff_packets, daemon=True).start()

    def stop_sniffing(self):
        self.sniffing = False
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')
        self.log_message("Stopping network sniffing...")

    def sniff_packets(self):
        scapy.sniff(prn=self.process_packet, store=False, stop_filter=lambda _: not self.sniffing)

    def process_packet(self, packet):
        if packet.haslayer(http.HTTPRequest):
            url = packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()
            self.log_message(f"HTTP Request: {url}")

            if packet.haslayer(scapy.Raw):
                payload = packet[scapy.Raw].load.decode(errors='ignore')
                keywords = ['username', 'user', 'login', 'password', 'pass']
                for keyword in keywords:
                    if keyword in payload.lower():
                        self.log_message(f"Possible sensitive info in payload: {payload}")
                        break

        # Simple port scan detection (very basic)
        elif packet.haslayer(scapy.TCP):
            if packet[scapy.TCP].flags == 2:  # SYN flag
                self.log_message(f"Possible port scan detected from {packet[scapy.IP].src}")

        # Add more intrusion detection rules here

if __name__ == "__main__":
    root = tk.Tk()
    nids = RetroNIDS(root)
    root.mainloop()