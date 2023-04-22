import socket
import time
import sys
import json
import os
import keyboard
import requests
from art import *
import getpass
import uuid
import hashlib
import getmac as gma
from ipwhois import IPWhois
from pygame import mixer  # Load the popular external library

def rgb_inline(r,g,b):
    return f"\033[38;2;{str(r)};{str(g)};{str(b)}m"

r = 125
g = 115
b = 158
os.system("cls")
os.system('mode 80,20')
tool_name = "Astolfo"
main_clr = rgb_inline(r,g,b)
red = rgb_inline(255,0,0)
white = rgb_inline(255,255,255)
startup_s = requests.get("https://cdn.discordapp.com/attachments/1037207555195273248/1099264831527333898/Nya_Cute_Anime_Girl_Noise_-_Sound_Effect_for_editing.mp3")
error_s = requests.get("https://cdn.discordapp.com/attachments/1037207555195273248/1099265507766567023/Error_Sound_Effects_No_Copyright.mp3")
os.system(f'title {tool_name}')
path = f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Astolfo"
print(f"{white}Loading {main_clr}{tool_name}...")
try:
    os.mkdir(path)
    print("folder created successfully")
    time.sleep(5)  # sleep for 5 seconds
except OSError as error:
    print("folder: 'Astolfo' already exists")
    
try:
    os.mkdir(f"{path}\\txt")
    print("folder created successfully")
    time.sleep(5)  # sleep for 5 seconds
except OSError as error:
    print("folder: 'txt' already exists")

try:
    os.mkdir(f"{path}\\sound")
    print("folder created successfully")
    time.sleep(5)  # sleep for 5 seconds
except OSError as error:
    print("folder: 'sound' already exists")

if startup_s.status_code == 200:
    with open(f"{path}\sound\startup.mp3", "wb") as file:
        file.write(startup_s.content)
    print("startup.mp3 download successful")
else:
    print(f"Error downloading startup.mp3. Status code: {startup_s.status_code}")

if error_s.status_code == 200:
    with open(f"{path}\sound\error.mp3", "wb") as file:
        file.write(error_s.content)
    print("error.mp3 download successful")
else:
    print(f"Error downloading error.mp3. Status code: {error_s.status_code}")


time.sleep(5)
file = requests.get(url='https://pastebin.com/raw/qwQ37qud')
stripped = file.text[:500].split('\r\n')
for i in range(len(stripped)):
    if hashlib.sha256((os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode()))).encode()).hexdigest() == stripped[i]:
        mixer.init()
        mixer.music.load(f'{path}\sound\startup.mp3')
        mixer.music.play()
        def is_pressed():
            if keyboard.is_pressed("q"):
                return False
            else:
                return True

        def ping(ip):
            try:
                # Try connecting to the host on port 80
                with socket.create_connection((ip, 80), timeout=5) as conn:
                    print(f"{white}{ip} is {main_clr}online")
            except:
                # If the connection fails, assume the host is down
                print(f"{white}{ip} is {red}offline")

        def tcp_ping(ip, port):
            try:
                # Create a TCP socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)  # Set a timeout for socket operations

                # Attempt to connect to the IP address and port
                sock.connect((ip, port))

                # If the connection is successful, print a success message
                print(f"{white}{ip}:{port} is {main_clr}online")
            except Exception as e:
                # If an exception occurs, print an error message
                print(f"{white}{ip}:{port} is {red}offline ({e})")
            finally:
                # Close the socket
                sock.close()

        def faded(text):
            os.system(""); faded = ""
            fade = r
            for line in text.splitlines():
                faded += (f"{rgb_inline(fade,g,b)}{line}\033[0m\n")
                if not fade == 255:
                    fade += 15
                    if fade > 255:
                        fade = 255
            return faded

        def banner(string):
            if string == "main":
                print(f"{main_clr}               Type 'help' to see all commands")
                print(faded(text2art(f"     {tool_name}","cybermedium")))
            if string == "help":
                print(faded(f"""
                {white}╔════════════════════{main_clr}════════════════════╗
                {white}║  tcp-ping - basic t{main_clr}cp pinger (fast).   ║
                {white}║  ping - basic pinge{main_clr}r using socket.     ║
                {white}║  lookup - basic ip {main_clr}lookup using ipwhois║
                {white}╚═══════╦════════════{main_clr}═══════════╦════════╝
                {white}╔═══════╩════════════{main_clr}═══════════╩════════╗
                {white}║  spass - save a pas{main_clr}sword to a txt file ║
                {white}║  xxxxxx - xxxxxxxxx{main_clr}xxxxxxxxxxxxxxxx    ║
                {white}║  xxxxxx - xxxxxxxxx{main_clr}xxxxxxxxxxxxxxxx    ║
                {white}╚════════════════════{main_clr}════════════════════╝
                """))
            if string == "tcp-ping":
                print(f"{main_clr}                      Hold 'q' to stop pinging")
                print(faded(text2art(f"     TCP Ping","cybermedium")))
            if string == "ping":
                print(f"{main_clr}                      Hold 'q' to stop pinging")
                print(faded(text2art(f"        Ping","cybermedium")))
            if string == "lookup":
                print(faded(text2art(f"        IP lookup","cybermedium")))
            if string == "spass":
                print(faded(text2art(f"        Password","cybermedium")))

        while True:
            os.system('cls')
            os.system('mode 80,20')
            os.system(f'title {tool_name} Multi Tool')
            banner("main")
            cmd = input(f"{main_clr}[{white}{tool_name}{main_clr}]{white}~{main_clr}$ ")
            if cmd == "cls" or cmd == "clear":
                os.system('cls')
            if cmd == "help":
                os.system('cls')
                os.system('mode 80,20')
                os.system(f'title {tool_name} Multi Tool')
                banner("help")
                cmd = input(f"{main_clr}[{white}{tool_name}{main_clr}]{white}~{main_clr}$ ")
            if cmd == "tcp-ping":
                os.system('cls')
                os.system('mode 80,20')
                os.system(f'title {tool_name} Multi Tool')
                banner("tcp-ping")
                ip = input(f"{main_clr}[{white}IP{main_clr}]{white}~{main_clr}$ ")
                port = input(f"{main_clr}[{white}PORT{main_clr}]{white}~{main_clr}$ ")
                while is_pressed():
                    os.system('cls')
                    banner("tcp-ping")
                    for _ in range(13):
                        tcp_ping(ip,int(port))
            if cmd == "ping":
                os.system('cls')
                os.system('mode 80,20')
                os.system(f'title {tool_name} Multi Tool')
                banner("ping")
                ip = input(f"{main_clr}[{white}IP{main_clr}]{white}~{main_clr}$ ")
                while is_pressed():
                    os.system('cls')
                    banner("ping")
                    for _ in range(13):
                        ping(ip,)

            if cmd == "spass":
                os.system('cls')
                os.system('mode 80,20')
                os.system(f'title {tool_name} Multi Tool')
                banner("spass")
                website = input(f"{main_clr}[{white}website{main_clr}]{white}~{main_clr}$ ")
                password = input(f"{main_clr}[{white}password{main_clr}]{white}~{main_clr}$ ")
                if website != "" or password != "":
                    with open(f"{path}\\txt\password.txt", "a") as f:
                        f.write("---------------\n")
                        f.write(f"{website}\n")
                        f.write(f"{password}\n")
                        f.write("---------------\n")
                
            if cmd == "lookup":
                os.system('cls')
                os.system('mode 80,20')
                os.system(f'title {tool_name} Multi Tool')
                banner("lookup")
                ip_address = input(f"{main_clr}[{white}IP{main_clr}]{white}~{main_clr}$ ")
                os.system("cls")
                ip = IPWhois(ip_address)
                result = ip.lookup_rdap()
                print(f"{white}IP address:{main_clr}", result['query'])
                print(f"{white}ASN:{main_clr}", result['asn'])
                print(f"{white}ASN CIDR:{main_clr}", result['asn_cidr'])
                print(f"{white}ASN Country Code:{main_clr}", result['asn_country_code'])
                print(f"{white}ISP Name:{main_clr}", result['asn_description'])
                print(f"{white}Network Name:{main_clr}", result['network']['name'])
                print(f"{white}Network CIDR:{main_clr}", result['network']['cidr'])
                print(f"{white}Network Country Code:{main_clr}", result['network']['country'])
                cmd = input(f"{main_clr}[{white}PRESS ENTER{main_clr}]{white}...")  
else:
    os.system("cls")
    mixer.init()
    mixer.music.load(f'{path}\sound\error.mp3')
    mixer.music.play()
    print(f"{white}please send this to {main_clr}! Reload#0001{white} on discord!{main_clr}")
    print(hashlib.sha256((os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode()))).encode()).hexdigest())
    input(f"{main_clr}[{white}PRESS ENTER AFTER COPPIED{main_clr}]{white}...")
