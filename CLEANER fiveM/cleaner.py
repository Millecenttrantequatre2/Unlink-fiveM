import os
import time
import sys
from colorama import Fore, Style
 

def print_LIGHTBLUE_EX(message):
    print(Fore.LIGHTBLUE_EX + message + Style.RESET_ALL)
print(F"{Fore.LIGHTBLUE_EX}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print(F"{Fore.LIGHTBLUE_EX}█▀░██▀░██░▄▄░██░▄░█")
time.sleep(0.1)
print(F"{Fore.LIGHTBLUE_EX}██░███░████▄▀█░▀▀░▀")
time.sleep(0.1)
print(F"{Fore.LIGHTBLUE_EX}█▀░▀█▀░▀█░▀▀░████░█")
time.sleep(0.1)
print(F"{Fore.LIGHTBLUE_EX}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
time.sleep(0.1)
def main():                                                      
    files_deleted = [
        "discord.dll",
        "CitizenFX_SubProcess_chrome.bin",
        "CitizenFX_SubProcess_game.bin",
        "CitizenFX_SubProcess_game_372.bin",
        "CitizenFX_SubProcess_game_1604.bin",
        "CitizenFX_SubProcess_game_1868.bin",
        "CitizenFX_SubProcess_game_2060.bin",
        "CitizenFX_SubProcess_game_2189.bin",
        "botan.dll",
        "asi-five.dll",
        "steam.dll",
        "steam_api64.dll",
        "CitizenGame.dll",
        "profiles.dll",
        "cfx_curl_x86_64.dll",
        "CitizenFX.ini",
        "caches.XML",
        "adhesive.dll",
        "cfx_curl_x86_64.dll",
        "steam_api64.dll",
        "profiles.dll"
    ]

    input("Appuyez sur Entrée pour unlink...")

    for file_name in files_deleted:
        print(f"Suppression de {file_name}...")
        sys.stdout.write("En cours")
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.1)
        try:
            os.remove(file_name)
            print(f"\nSuppression de {file_name} terminée.")
        except FileNotFoundError:
            print(f"\nFichier manquant : {file_name}")

    print("Compte unlink bon jeu!")

if __name__ == "__main__":
    main()