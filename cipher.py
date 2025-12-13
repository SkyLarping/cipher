import base64 as b
import codecs as c

COLOR_1 = "\033[31m"
COLOR_2 = "\033[32m"
RESET   = "\033[0m"

class Logo:
    def __init__(logo):
        logo._ascii = fr"""{COLOR_1}
 ▄▄▄▄ ▓██   ██▓ ▄████▄   ██▓ ██▓███   ██░ ██ ▓█████  ██▀███  
▓█████▄▒██  ██▒▒██▀ ▀█  ▓██▒▓██░  ██▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
▒██▒ ▄██▒██ ██░▒▓█    ▄ ▒██▒▓██░ ██▓▒▒██▀▀██░▒███   ▓██ ░▄█ ▒
▒██░█▀  ░ ▐██▓░▒▓▓▄ ▄██▒░██░▒██▄█▓▒ ▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
░▓█  ▀█▓░ ██▒▓░▒ ▓███▀ ░░██░▒██▒ ░  ░░▓█▒░██▓░▒████▒░██▓ ▒██▒
░▒▓███▀▒ ██▒▒▒ ░ ░▒ ▒  ░░▓  ▒▓▒░ ░  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
▒░▒   ░▓██ ░▒░   ░  ▒    ▒ ░░▒ ░      ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
 ░    ░▒ ▒ ░░  ░         ▒ ░░░        ░  ░░ ░   ░     ░░   ░ 
 ░     ░ ░     ░ ░       ░            ░  ░  ░   ░  ░   ░     
      ░░ ░     ░                                             
                                                                v0.1.1 (beta)
                                                                Made by Sky{RESET}
"""

l = Logo()
print(l._ascii)

try:

    option = int(input(f"{COLOR_2}Options :\n\n1)Decoding a base64\n\n2)Encoding a base64\n\n3)Decoding a base16\n\n4)Encoding to base16\n\n5)Decoding a rot13\n\n6)Encoding to rot13\n\n[cipher]:  "))

except KeyboardInterrupt:
    print("[-] Exiting")

match option:

    case 1:
       try:
            msg = input("[+] Type your encrypted message : ")
            decoded = b.b64decode(msg)
            print(f"[+] Your message is {decoded}")

       except KeyboardInterrupt:
            print("\n[-] Exiting")
    case 2:
        try:
            msg_1 = input("[+] Type your message : ").encode()
            encoded = b.b64encode(msg_1)
            print(f"[+] Your encrypted message is {encoded}")
        except KeyboardInterrupt:
            print("\n[-] Exiting")
    case 3:
        try:
            msg_2 = input("[+] Type your cipher : ")
            decoded_hex = b.b16decode(msg_2).decode()
            print(f"[+] Your decrypted message is : {decoded_hex}")
        except KeyboardInterrupt:
            print("\n[-] Exiting")
    case 4:
        try:
            msg_3 = input("[+] Type your message : ").encode()
            encoded_hex = b.b16encode(msg_3)
            print(f"[+] Your encrypted message is {encoded_hex} ")
        except KeyboardInterrupt:
            print("\n[-] Exiting")
    case 5:
        try:
            msg_4 = input("[+] Type your cipher : ")
            decoded_rot = c.decode(msg_4, 'rot13')
            print(f"[+] Your decrypted cypher is: {decoded_rot}")
        except KeyboardInterrupt:
            print("\n[-] Exiting")
    case 6:
        try:
            msg_5 = input("[+] Type your message : ")
            encoded_rot = c.encode(msg_5, 'rot13')
            print(f"[+] Your encrypted message is: {encoded_rot}")
        except KeyboardInterrupt:
            print("\n[-] Exiting")
    case _:
        print("[-] Invalid Option, Try Again")