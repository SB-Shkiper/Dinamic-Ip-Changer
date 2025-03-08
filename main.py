#The script expects the "CookieAuthentication" value in torrc to be 1
import sys
import time
import os
import colorama
from stem.control import Controller
from stem import Signal
from threading import Thread
from colorama import Fore

colorama.init()
logo = Fore.WHITE + r"""
  ___ ____     ____ _                                 
 |_ _|  _ \   / ___| |__   __ _ _ __   __ _  ___ _ __ 
  | || |_) | | |   | '_ \ / _` | '_ \ / _` |/ _ \ '__|
  | ||  __/  | |___| | | | (_| | | | | (_| |  __/ |   
 |___|_|      \____|_| |_|\__,_|_| |_|\__, |\___|_|   
                                      |___/           
""" + Fore.RESET

print(logo)
colorama.deinit()

class DinamicIP:
    def __init__(self, count, interval, port):
        self.count = count
        self.interval = interval
        self.running = False
        self.port = port

    def change_ip(self):
        with Controller.from_port(port=self.port) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)

    def log_message(self, message):
        print(message)

    def run_script(self):
        i = 0
        while self.running and (self.count == 0 or i < self.count):
            self.change_ip()
            self.log_message(f"IP Changed. Waiting {self.interval} seconds")
            time.sleep(self.interval)
            i += 1

    def start_script(self):
        if not self.running:
            self.running = True
            self.thread = Thread(target=self.run_script)
            self.thread.start()

    def stop_script(self):
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()


def read_config(file_path):
    config = {}
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write('Count=0\n')
            file.write('Interval=5\n')
            file.write('ControllerPort=9050\n')
        print(f"Config file '{file_path}' created with default values.")

    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.split('=')
                config[key.strip()] = value.strip().strip('"')
    return config


if __name__ == '__main__':
    config_file_path = 'config.txt'
    config = read_config(config_file_path)

    count = int(config.get('Count', 0))
    interval = int(config.get('Interval', 10))
    port = int(config.get('ControllerPort', 9050))

    dinamic_ip = DinamicIP(count, interval, port)
    dinamic_ip.start_script()

    try:
        while dinamic_ip.running:
            time.sleep(1)
    except KeyboardInterrupt:
        dinamic_ip.stop_script()
        print("Script stopped.")
