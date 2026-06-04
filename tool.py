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

                 __
                / /\
               / / /\
              / / /\ \
             / / /\ \ \
  __________/_/_/__\ \ \__________
 /\ \_______________\ \ \_________\
 \ \ \_______________\ \ \________/
  \ \ \  / / /        \ \ \  / / /
   \ \ \/ / /          \ \ \/ / /
    \ \/ / /            \ \/ / /
     \/ / /              \/ / /
     / / /\              / / /\
    / / /\ \            / / /\ \
   / / /\ \ \          / / /\ \ \
  /_/_/__\ \ \________/_/_/__\ \ \

 \_________\ \ \_______________\_\/
            \ \ \  / / /
             \ \ \/ / /
              \ \/ / /
               \/ / /
                \/_/
      
"""

# =========================
# STARTUP ANIMATION
# =========================

clear()

# Loading Effect
loading_text = "[+] Initializing QR System"

for i in range(4):
    print(Fore.RED + loading_text + "." * i)
    time.sleep(0.3)
    clear()

# Falling Effect
for i in range(15):
    clear()
    print("\n" * (15 - i))
    print(Fore.RED + banner)
    time.sleep(0.04)

time.sleep(0.5)

# Reveal Effect
clear()

for line in banner.splitlines():
    print(Fore.RED + line)
    time.sleep(0.01)

# =========================
# AUTHOR SECTION
# =========================

print("\n")
print(Fore.WHITE + "═" * 70)
print(Fore.RED + f"  AUTHOR : {AUTHOR}")
print(Fore.RED + f"  GITHUB : {GITHUB}")
print(Fore.WHITE + "═" * 70)
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

print(Fore.RED)
qr.print_ascii(invert=True)

print(Style.RESET_ALL)
