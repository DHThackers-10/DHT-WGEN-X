import random
import os
import time
import pyfiglet
from flask import Flask, request, Response

# Define ANSI color codes
R = '\033[91m'  
G = '\033[92m'  
Y = '\033[93m'  
B = '\033[94m'  
P = '\033[95m'  
C = '\033[96m'  
W = '\033[97m'  
N = '\033[0m'   

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def show_banner(text, color):
    clear()
    banner = pyfiglet.figlet_format(text, font="slant")  
    print(f"{color}{banner}{N}")

def dht_hackers_banner():
    show_banner("DHT-HACKERS", R)
    print(f"{C}────────────────────────────────────────────────────────────")
    print(f"{G} THIS TOOL IS PAID! TO USE IT FOR FREE:")
    print(f"{P} SUBSCRIBE TO OUR CHANNEL FOR ETHICAL HACKING TUTORIALS!")
    print(f"{B} 📌 https://youtube.com/@dht-hackers_10")
    print(f"{C}────────────────────────────────────────────────────────────{N}")
    time.sleep(2)
    os.system("termux-open-url https://youtube.com/@dht-hackers_10")
    input(f"{Y}Press Enter after subscribing to continue...{N}")
    clear()

def dht_wgen_x_banner():
    show_banner("DHT-WGEN-X", G)
    print(f"{C}────────────────────────────────────────────────────────────")
    print(f"{P}  🔥 Created by: {R}DHT-HACKERS 🔥")
    print(f"{B}  🎯 Ethical Hacking | Penetration Testing | Cybersecurity")
    print(f"{C}────────────────────────────────────────────────────────────{N}")

# Run banners
dht_hackers_banner()
dht_wgen_x_banner()

# Display credits
print(f"{Y}⚡ Developed by: {G}DHT-HACKERS {N}")
print(f"{B}📌 Follow us for more: {P}https://youtube.com/@dht-hackers_10{N}")
print(f"{C}────────────────────────────────────────────────────────────{N}")

LANGUAGES = {
    "1": ("English", ["king", "queen", "love", "baby", "admin", "123"]),
    "2": ("Urdu (پاکستانی)", ["sheru", "bhai", "safdar", "ali", "jan", "007", "pk"]),
    "3": ("Hindi (हिंदी)", ["singh", "kumar", "raj", "bhaiya", "dev", "sharma"]),
    "4": ("Punjabi (ਪੰਜਾਬੀ)", ["sher", "veer", "sidhu", "gill", "punjabi", "kaka"]),
    "5": ("Arabic (العربية)", ["omar", "abdullah", "al", "bin", "mohd", "arab"]),
    "6": ("Bengali (বাংলা)", ["khan", "akter", "babu", "mim", "bd", "123"]),
}

SEPARATORS = ["", "_", ".", "-", "@", "$"]

LEET_MAP = {
    'a': ['a', '4', '@'], 'e': ['e', '3'], 'i': ['i', '1', '!'],
    'o': ['o', '0'], 's': ['s', '$', '5'], 'g': ['g', '9'], 't': ['t', '7']
}

def leetify(word):
    return ''.join(random.choice(LEET_MAP.get(c, [c])) for c in word)

def generate_combinations(inputs, cultural_words):
    combos = []
    for i in range(10):  # Base pass
        for a in inputs:
            for b in cultural_words:
                for sep in SEPARATORS:
                    combos.append(a + sep + b)
                    combos.append(b + sep + a)
    for i in range(10):  # DOB/suffix mixing
        for a in inputs:
            for b in inputs:
                for sep in SEPARATORS:
                    combos.append(a + sep + b)
    # Light leetify pass
    leet_combos = [leetify(w) for w in combos]
    combos.extend(leet_combos)
    # Filter smart
    smart_filtered = list(set([w for w in combos if 6 <= len(w) <= 16]))
    random.shuffle(smart_filtered)
    return smart_filtered

def main():
    print("=== DHT-WGEN-X-L10N v2: CULTURE-CORE ===")
    for k, v in LANGUAGES.items():
        print(f"[{k.zfill(2)}] {v[0]}")
    lang = input("Select Language: ").strip()
    if lang not in LANGUAGES:
        print("Invalid language selected.")
        return
    lang_name, cultural_words = LANGUAGES[lang]

    print(f"\n[+] Selected Language: {lang_name}")
    name = input("Victim Name: ").strip().lower()
    city = input("City: ").strip().lower()
    dob = input("DOB (e.g. 18-oct-2008): ").strip().lower()
    nick = input("Nicknames (comma separated): ").strip().lower().split(',')

    inputs = [name, city, dob] + nick
    inputs = [w.strip().replace(" ", "").lower() for w in inputs if w.strip()]

    print("\n[+] Generating wordlist (smart + cultural)...")
    final_list = generate_combinations(inputs, cultural_words)

    with open("wordlist.txt", "w", encoding="utf-8") as f:
        for word in final_list:
            f.write(word + "\n")

    print(f"[✓] Wordlist saved to wordlist.txt ({len(final_list)} entries)")

if __name__ == "__main__":
    main()
