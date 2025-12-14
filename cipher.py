import base64 as b
import codecs as c
from pycipher import Caesar as C
from pycipher import Atbash as at
import morse_talk as m

COLOR_1 = "\033[35m"
COLOR_2 = "\033[32m"
COLOR_3 = "\033[33m"
COLOR_4 = "\033[34m"
RESET   = "\033[0m"

class Logo:
    def __init__(logo):
        logo._ascii = fr"""{COLOR_3}
                                                 ███            █████                        
                                               ░░░            ░░███                         
                 ████████  █████ ████  ██████  ████  ████████  ░███████    ██████  ████████ 
                ░░███░░███░░███ ░███  ███░░███░░███ ░░███░░███ ░███░░███  ███░░███░░███░░███
                 ░███ ░███ ░███ ░███ ░███ ░░░  ░███  ░███ ░███ ░███ ░███ ░███████  ░███ ░░░ 
                 ░███ ░███ ░███ ░███ ░███  ███ ░███  ░███ ░███ ░███ ░███ ░███░░░   ░███     
                 ░███████  ░░███████ ░░██████  █████ ░███████  ████ █████░░██████  █████    
                 ░███░░░    ░░░░░███  ░░░░░░  ░░░░░  ░███░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░     
                 ░███       ███ ░███                 ░███                                   
                 █████     ░░██████                  █████                                  
                ░░░░░       ░░░░░░                  ░░░░░                                   
                                                                                                        
                                        ╔═════════════════════╗
                                        ║       v0.3.5        ║
                                        ╠═════════════════════╣
                                        ║ Founder: SkyLarping ║
                                        ╚═════════════════════╝{RESET}
"""
        logo._menu = fr"""
{COLOR_3}
                            
                                           ╔═══════════════════════════════╗
                                           ║       Choose an Option:       ║
                                           ╠═══════════════════════════════╣
                                           ║ 1.  Base64(ENCODE)            ║
                                           ║ 2.  Base64(DECODE)            ║
                                           ║ 3.  Base16(DECODE)            ║                          
                                           ║ 4.  Base16(ENCODE)            ║
                                           ║ 5.  ROT13(DECODE)             ║
                                           ║ 6.  ROT13(ENCODE)             ║
                                           ║ 7.  Caesar(ENCODE)            ║
                                           ║ 8.  Caesar(DECODE)            ║
                                           ║ 9.  Morse(ENCODE)             ║
                                           ║ 10. Morse(DECODE)             ║
                                           ║ 11. AtBash(DECODE)            ║
                                           ║ 12. AtBash(ENCODE)            ║
                                           ║ 13. Binary(ENCODE)            ║
                                           ║ 14. Binary(DECODE)            ║
                                           ║ 15- Multi-Layer(Experimental) ║
                                           ╚═══════════════════════════════╝


{RESET}
"""
l = Logo()

print(l._ascii)
print((l._menu))

try:
    option = int(input(f"{COLOR_4}option@pycipher$ "))
except KeyboardInterrupt:
    print("\n[x] Exiting")

match option:

    case 1:
        try:
                msg = input("> [Type your base64] : ")
                decoded = b.b64decode(msg)
                print(f"> Your message is {decoded}")

        except KeyboardInterrupt:
                print("\n[x] Exiting")
    case 2:
        try:
                msg = input("> [Type your message] : ").encode()
                encoded = b.b64encode(msg).decode()
                print(f"> Your base64 is {encoded}")
        except KeyboardInterrupt:
                print("\n[x] Exiting")

    case 3:    
        try:
            msg = input("> [Type your base16] : ")
            decoded_hex = b.b16decode(msg).decode()
            print(f"> Your message is : {decoded_hex}")
        except KeyboardInterrupt:
            print("\n[x] Exiting")
        
    case 4:
        try:
            msg = input("> [Type your message] : ").encode()
            encoded_hex = b.b16encode(msg).decode()
            print(f"> Your base16 is {encoded_hex} ")
        except KeyboardInterrupt:
            print("\n[x] Exiting")
    case 5:        
        try:
                msg = input("> [Type your rot13] : ")
                decoded_rot = c.decode(msg, 'rot13')
                print(f"> Your decrypted rot13 is: {decoded_rot}")
        except KeyboardInterrupt:
                print("\n[x] Exiting")
    case 6:
        try:
                msg = input("> [Type your message] : ")
                encoded_rot = c.encode(msg, 'rot13')
                print(f"> Your rot13 is: {encoded_rot}")
        except KeyboardInterrupt:
                print("\n[x] Exiting")
    case 7:
        try:    
                shift = int(input("> How many shifts: "))
                msg = input("> [Type your message] : ")
                encoded_c = C(shift).encipher(msg)
                print(f"> Your caesar cipher is {encoded_c}")
        except KeyboardInterrupt:
             print("\n[x] Exiting")
    case 8:
        try:
                shift = int(input("> How many shifts: "))
                msg = input("> [Type your caesar]: ")
                decoded_c = C(shift).decipher(msg)
                print(f"> Your message is {decoded_c}")
        except KeyboardInterrupt:
             print("\n[x] Exiting")
    case 9:
        try:
                msg = input("> [Type your message] : ")
                encoded_m = m.encode(msg)
                print(f"> Your morse code is: {encoded_m}")
        except KeyboardInterrupt:
             print("\n[x] Exiting")
    case 10:
        try:
                msg = input("> [Type your morse code] : ")
                decoded_m = m.decode(msg)
                print(f"> Your message is : {decoded_m}")
        except KeyboardInterrupt:
             print("\n[x] Exiting")
    case 11:
        try:
                msg = input("> [Type your atbash code] : ")
                decoded_a = at().decipher(msg)
                print(f"> Your message is : {decoded_a} ")
        except KeyboardInterrupt:
             print("\n[x] Exiting")
    case 12:
        try:
                msg = input("> [Type your message] : ")
                encoded_a = at().encipher(msg)
                print(f"> Your atbash is : {encoded_a}")
        except KeyboardInterrupt:
             print("\n[x] Exiting")
    case 13:
        try:
                msg = input("> [Type your message] : ")
                encoded_b = "".join([format(ord(m), "08b") for m in msg])
                print(f"Your encoded message to binary : {encoded_b}")
        except KeyboardInterrupt:
              print("\n[x] Exiting") 
    case 14:
        try:
                msg = input('> [Type your binaries] : ')
                if len(msg) % 8 == 0:
                   decoded_b = ''.join((chr(int(msg[i:i+8], 2))) for i in range(0,len(msg), 8))
                   print(f"Your decoded message is: {decoded_b}")
                else:
                    raise ValueError("[x] string Must be a Multiple of 8")
        except KeyboardInterrupt:
            print("\n[x] Exiting")
    case 15:
        try:    
             msg = input('> [Type your message] : ')
             options = int(input(fr"""
                                        ╔══════════════════════════════════════╗
                                        ║        Choose a Multi-Layer:         ║
                                        ╠══════════════════════════════════════╣
                                        ║ 1. Binary > Base16 > Base64 > Caesar ║
                                        ║ 2. Binary > Base16 > Base64 > Rot13  ║
                                        ║ 3. Binary > Base16 > Base64 > Morse  ║
                                        ║ 4. Binary > Base16 > Base64 > AtBash ║
                                        ╚══════════════════════════════════════╝


{COLOR_2}option@pycipher{RESET}${COLOR_4} """))
             
             if options == 1:
                  encoded_b = "".join([format((ord(m), "08b")) for m in msg])
                  encoded_h = b.b16encode(encoded_b.encode()).decode()
                  encoded_b64 = b.b64encode(encoded_h.encode()).decode()
                  shift = int(input("How many shifts : "))
                  encoded_c = C(shift).encipher(encoded_b64)
                  print(f"> Your encoded message is: {encoded_c}")
             elif options == 2:
                  encoded_b = "".join([format((ord(m), "08b")) for m in msg])
                  encoded_h = b.b16encode(encoded_b.encode()).decode()
                  encoded_b64 = b.b64encode(encoded_h.encode()).decode()
                  rot13 = c.encode(encoded_b64, 'rot13')
                  print(f"> Your encoded message is: {rot13} ")
             elif options == 3:
                  encoded_b = "".join([format((ord(m), "08b")) for m in msg])
                  encoded_h = b.b16encode(encoded_b.encode()).decode()
                  encoded_b64 = b.b64encode(encoded_h.encode()).decode()
                  morse = m.encode(encoded_b64)
                  print(f"> Your encoded message is {morse}")
             elif options == 4:
                  encoded_b = "".join([format((ord(m), "08b")) for m in msg])
                  encoded_h = b.b16encode(encoded_b.encode()).decode()
                  encoded_b64 = b.b64encode(encoded_h.encode()).decode()
                  atbash = at().encipher(encoded_b64)
                  print(f"> Your encoded message is {atbash}")
             else:
                  print("Invalid Choice!")

        except KeyboardInterrupt:
             print("\n[x] Exiting")
    case _:
        print("[x] Invalid Option, Try Again")
