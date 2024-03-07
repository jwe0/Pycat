import os, sys, hashlib, threading, time, binascii, os;from Crypto.Hash import MD4 ;from datetime import datetime; from pyfiglet import Figlet; from pystyle import Colorate, Colors, Center


cracked = False


class Bruteforcer:
    def __init__(self, target, wordlist, password, line, starttime, algorithm=None):
        self.target = target
        self.password = password
        self.algorithm = algorithm
        self.line = line
        self.start = starttime
        self.wordlist = wordlist


    def hash_bruteforce(self):
        global cracked
        



        starttime = time.time()

        # Sha hashing

        if self.algorithm == "sha1":
            hashed_pass = hashlib.sha1(self.password.encode()).hexdigest()
        elif self.algorithm == "sha224":
            hashed_pass = hashlib.sha224(self.password.encode()).hexdigest()
        elif self.algorithm == "sha256":
            hashed_pass = hashlib.sha256(self.password.encode()).hexdigest()
        elif self.algorithm == "sha384":
            hashed_pass = hashlib.sha384(self.password.encode()).hexdigest()
        elif self.algorithm == "sha512":
            hashed_pass = hashlib.sha512(self.password.encode()).hexdigest()
        elif self.algorithm == "sha3_224":
            hashed_pass = hashlib.sha3_224(self.password.encode()).hexdigest()
        elif self.algorithm == "sha3_256":
            hashed_pass = hashlib.sha3_256(self.password.encode()).hexdigest()
        elif self.algorithm == "sha3_384":
            hashed_pass = hashlib.sha3_3844(self.password.encode()).hexdigest()
        elif self.algorithm == "sha3_512":
            hashed_pass = hashlib.sha3_512(self.password.encode()).hexdigest()



        # MD hashing
        elif self.algorithm == "md4":
            hashed_pass = MD4.new(self.password.encode('utf-16le')).hexdigest()
        elif self.algorithm == "md5":
            hashed_pass = hashlib.md5(self.password.encode()).hexdigest()


        # Shake hashing

        elif self.algorithm == "shake_128":
            hashed_pass = hashlib.shake_128(self.password.encode()).hexdigest(16)
        elif self.algorithm == "shake_256":
            hashed_pass = hashlib.shake_256(self.password.encode()).hexdigest(16)



        




        elif self.algorithm == "ntlm":
            hashed_pass = MD4.new(self.password.encode('utf-16le')).digest().hex() 
        else:
            print("[!] Unrecognised hash")
        if str(hashed_pass) == str(self.target):
            
            if cracked != True:
                cracked = True
            
                print(f"""
\n[+] Status.............. Cracked    
[+] Original hash....... {self.target}
[+] Algorithm........... {self.algorithm}
[+] Cracked hash........ {self.password}
[+] Wordlist used....... {self.wordlist}
[+] Start time.......... {self.start}
[+] End time............ {datetime.now().strftime('%H:%M:%S')}
[+] Time taken.......... {int(time.time() - starttime)}s
[+] Line................ {self.line}
""")




        exit()


class Main:
    def clear_s():
        os.system("cls") if os.name == "nt" else os.system("clear")

    
    def title(name):
        f = Figlet(font='calvin_s')
        return f.renderText(name)

    def loading_screen(total, current):
        percent = int((current / total) * 100)
        if percent == 10:
            print("Status [ █▒▒▒▒▒▒▒▒▒ 10% ] ", end='\r')
        elif percent == 20:
            print("Status [ ██▒▒▒▒▒▒▒▒ 20% ] ", end='\r')
        elif percent == 30:
            print("Status [ ███▒▒▒▒▒▒▒ 30% ] ", end='\r')
        elif percent == 40:
            print("Status [ ████▒▒▒▒▒▒ 40% ] ", end='\r')
        elif percent == 50:
            print("Status [ █████▒▒▒▒▒ 50% ] ", end='\r')
        elif percent == 60:
            print("Status [ ██████▒▒▒▒ 60% ] ", end='\r')
        elif percent == 70:
            print("Status [ ███████▒▒▒ 70% ] ", end='\r')
        elif percent == 80:
            print("Status [ ████████▒▒ 80% ] ", end='\r')
        elif percent == 90:
            print("Status [ █████████▒ 90% ] ", end='\r')
        elif percent == 100:
            print("Status [ ██████████ 100% ] ", end='\r')



    def Main():
        line_num = 0

        if sys.argv[1] == "-a":
            print("[+] Available Algorithms\n")
            for algorithm in [algs for algs in hashlib.algorithms_available]:
                print("[+] {}".format(algorithm))
        else:
        
            
            #Main.clear_s()
            art = """
                   .-.
                  / /
                 / |
   |\     ._ ,-""  `.
   | |,,_/  7        ;   ╔═╗╦ ╦╔═╗╔═╗╔╦╗
 `;=     ,=(     ,  /    ╠═╝╚╦╝║  ╠═╣ ║
  |`q  q  ` |    \_,|    ╩   ╩ ╚═╝╩ ╩ ╩   
 .=; <> _ ; /  ,/'/ |
';|\,j_ \;=\ ,/   `-'
    `--'_|\  )
   ,' | /  ;'          Made by Josh Webb
  (,,/ (,,/     
        
        """
            print(Colorate.Horizontal(Colors.red_to_purple, art))
            print(f"[+] Dehashing {sys.argv[1]}")
            print(f"[+] Algorithm {sys.argv[2]}")
            print(f"[+] Wordlist {sys.argv[3]}")
            hash = sys.argv[1]
            algorithm = sys.argv[2]
            wordlist = sys.argv[3]
            print()


            passwords = [line for line in open(wordlist).read().splitlines()]

            for password in passwords:
                
                line_num += 1

                Main.loading_screen(len(passwords), line_num)

                crack = Bruteforcer(hash, wordlist, password, line_num, datetime.now().strftime('%H:%M:%S'), algorithm)
                threading.Thread(target=crack.hash_bruteforce).start()

        



if __name__ == "__main__":
    Main.Main()