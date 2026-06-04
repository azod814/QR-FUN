```python
import os
import time
import qrcode
from colorama import Fore, Style, init

init(autoreset=True)

# =========================
# SETTINGS
# =========================

AUTHOR = "azod08"
GITHUB = "https://github.com/azod08"

IMAGE_URL = "https://i.pinimg.com/originals/2a/2f/a0/2a2fa0db3179d4b4ec39d1a8a1eeda7d.jpg?nii=t"

# =========================
# CLEAR SCREEN
# =========================

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# =========================
# ASCII BANNER
# =========================

banner = r"""

───▄█▌─▄─▄─▐█▄
───██▌▀▀▄▀▀▐██
───██▌─▄▄▄─▐██
───▀██▌▐█▌▐██▀
▄██████─▀─██████▄

      MASK

"""

# =========================
# STARTUP ANIMATION
# =========================

clear()

boot_text = """
╔══════════════════════════════╗
║      MASK QR GENERATOR       ║
╚══════════════════════════════╝

[+] Connecting...
[+] Loading Components...
[+] Initializing QR Engine...
[+] Access Granted...

"""

# Typewriter Boot Screen
for char in boot_text:
    print(Fore.RED + char, end="", flush=True)
    time.sleep(0.015)

time.sleep(0.8)
clear()

# Typewriter Banner
for char in banner:
    print(Fore.RED + char, end="", flush=True)
    time.sleep(0.0015)

print("\n")

# =========================
# AUTHOR SECTION
# =========================

print(Fore.WHITE + "═" * 60)
print(Fore.RED + f" Author : {AUTHOR}")
print(Fore.RED + f" GitHub : {GITHUB}")
print(Fore.WHITE + "═" * 60)
print()

# =========================
# QR CODE
# =========================

qr = qrcode.QRCode(
    version=1,
    box_size=2,
    border=1
)

qr.add_data(IMAGE_URL)
qr.make(fit=True)

print(Fore.RED + "[+] Scan QR Code Below\n")

qr.print_ascii(invert=True)

print(Style.RESET_ALL)
```
