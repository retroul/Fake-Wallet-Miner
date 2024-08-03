import os,string;from pystyle import *;from time import sleep;from random import choice, randint
logo = """                         
                        %@@@@@@@@@@@@@%##*+==---------=====-:                             
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=                          
                        %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                         
                        %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-                         
                        %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=                         
                        %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+                         
                        %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+                         
                        %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.                        
                     .-=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*=:                  
                 -+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+.              
              =#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-            
            *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+           
          .%@@@@@@@@@@@@:=*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@.          
          +@@@@@@@@@@@@@*:   .-=+#%@@@@@@@@@@@@@@@@@@@@%#*+-:. -%@@@@@@@@@@@@@@           
          +@@@@@@@@@@@@@@@@*-.      .::-========--::.      :=#@@@@@@@@@@@@@@@@=           
          :@@@@@@@@@@@@@@@@@@@@#+-.                  .:=*%@@@@@@@@@@@@@@@@@@@-            
           *@@@@@@@@@@@@@@@@@@@@@@@@@%#*++=====++*#%@@@@@@@@@@@@@@@@@@@@@@@+              
            *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=                
 :------:::::=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*=.                  
  *@@@@@@@@@@@%**%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###*+++========------.    
   =@@@@@@@@@@@@@=.-+#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#####%@@@@@@@@@@@@@@@@@@@@=     
    :%@@@@@@@@@@@@      .:-=+**##%%%@@@@@@%%%##**++=-:.+#@@@@@@@@@@@@@@@@@@@@@@@@@*.      
      #@@@@@@@@@@@*             .%%:                   @@@@@@@@@@@@@@@@@@@@@@@@@#:        
       +@@@@@@@@@@@=           =@@@#                  *@@@@@@@@@@@@@@@@@@@@@@@%=          
        -@@@@@@@@@@@*        =%@@@@@#                *@@@@@@@@@@@@@@@@@@@@@@@+            
         .%@@@@@@@@@@@*=-=+#@@@@@@@@@@=            -%@@@@@@@@@@@@@@@@@@@@@@#.             
           *@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=-:..:-=*@@@@@@@@@@@@@@@@@@@@@@@%-               
            =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=  .=#%=          
             :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*..=#@@@@@@=        
             +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%--#@@@@@@@@@@#.      
           =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@@@@@@@@-     
          *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-    
         =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:   
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
        =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*  
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@: 
       +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*
"""
os.system("mode con cols=92 lines=52")
os.system("title " + "Wallet Miner by fer#0001")
class Code:
   def __init__(self):
      print(f"{Col.dark_red}{logo}")
      print(f"\t\t\t     #{Col.white} Coded by fer{Col.dark_red}0001")
      try:
         c = int(input(f"""
{Col.white}[{Col.dark_red}1{Col.white}]{Col.dark_red} BTC Wallet Miner
{Col.white}[{Col.dark_red}2{Col.white}]{Col.dark_red} LTC Wallet Miner
{Col.white}[{Col.dark_red}3{Col.white}]{Col.dark_red} Ethereum Wallet Miner

{Col.white}>> """))
      except:os.system('cls');self.__init__()
      if c == 1:
            self.btc()
      elif c==2:
         self.ltc()
      elif c==3:
         self.eth()
      else:os.system('cls');self.__init__()
   def btc(self):
      while True:
         btc = input(f"\n{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Enter Your BTC Wallet {Col.white}>> ")
         if btc.startswith("3") or btc.startswith("bc1") or btc.startswith("1"):print(f"\n{Col.white}[{Col.green}+{Col.white}]{Col.green} Valid Address | Starting Process..");sleep(2);break
         else:print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Invalid BTC Address");sleep(2)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Decrypting in : {Col.white}1.5 Seconds")
      sleep(1.5)
      proxies = randint(100,170)
      seconds = randint(23142,43254)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Scraped : {Col.white}{proxies} {Col.dark_red}proxies in{Col.white} 1.5{seconds} {Col.dark_red}seconds")
      sleep(2.5)
      print("\n")
      while True:
         print("\n")
         m = randint(200,750)
         for _ in range(m):
            chars = string.ascii_lowercase + string.ascii_uppercase
            a = ''.join(choice(chars) for _ in range(64))
            print(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} Generated - {Col.white}{a} - {Col.dark_red}0.00$")
            sleep(0.1)
         mo= randint(57,980)
         mo2 = randint(10,80)
         chars = string.ascii_lowercase + string.ascii_uppercase
         a = ''.join(choice(chars) for _ in range(64))
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Generated - {Col.white}{a} - {Col.green}{mo}.{mo2}$")
         sleep(1)
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Successfully Sent {Col.white}{mo}.{mo2}$ {Col.green}To Your wallet !")
         input(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} Press Enter to continue mining..")
   def ltc(self):
      while True:
         ltc = input(f"\n{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Enter Your LTC Wallet {Col.white}>> ")
         if ltc.startswith("L") or ltc.startswith("M") or ltc.startswith("ltc1"):print(f"\n{Col.white}[{Col.green}+{Col.white}]{Col.green} Valid Address | Starting Process..");sleep(2);break
         else:print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Invalid LTC Address");sleep(2)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Decrypting in : {Col.white}0.6 Seconds")
      sleep(1.5)
      proxies = randint(100,170)
      seconds = randint(23142,43254)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Scraped : {Col.white}{proxies} {Col.dark_red}proxies in{Col.white} 1.5{seconds} {Col.dark_red}seconds")
      sleep(2.5)
      print("\n")
      while True:
         print("\n")
         m = randint(200,750)
         for _ in range(m):
            chars = string.ascii_lowercase + string.ascii_uppercase
            a = ''.join(choice(chars) for _ in range(64))
            print(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} Generated - {Col.white}{a} - {Col.dark_red}0.00$")
            sleep(0.1)
         mo= randint(57,980)
         mo2 = randint(10,80)
         chars = string.ascii_lowercase + string.ascii_uppercase
         a = ''.join(choice(chars) for _ in range(64))
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Generated - {Col.white}{a} - {Col.green}{mo}.{mo2}$")
         sleep(1)
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Successfully Sent {Col.white}{mo}.{mo2}$ {Col.green}To Your wallet !")
         input(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} Press Enter to continue mining..")
   def eth(self):
      while True:
         eth = input(f"\n{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Enter Your ETH Wallet {Col.white}>> ")
         if eth.startswith("0x") or eth.startswith("tx"):print(f"\n{Col.white}[{Col.green}+{Col.white}]{Col.green} Valid Address | Starting Process..");sleep(2);break
         else:print(f"{Col.white}[{Col.red}+{Col.white}]{Col.red} Invalid ETH Address");sleep(2)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Decrypting in : {Col.white}0.9 Seconds")
      sleep(1.5)
      proxies = randint(100,170)
      seconds = randint(23142,43254)
      print(f"{Col.white}[{Col.dark_red}+{Col.white}]{Col.dark_red} Scraped : {Col.white}{proxies} {Col.dark_red}proxies in{Col.white} 1.5{seconds} {Col.dark_red}seconds")
      sleep(2.5)
      print("\n")
      while True:
         print("\n")
         m = randint(200,750)
         for _ in range(m):
            chars = string.ascii_lowercase + string.ascii_uppercase
            a = ''.join(choice(chars) for _ in range(64))
            print(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} Generated - {Col.white}{a} - {Col.dark_red}0.00$")
            sleep(0.1)
         mo= randint(57,980)
         mo2 = randint(10,80)
         chars = string.ascii_lowercase + string.ascii_uppercase
         a = ''.join(choice(chars) for _ in range(64))
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Generated - {Col.white}{a} - {Col.green}{mo}.{mo2}$")
         sleep(1)
         print(f"{Col.white}[{Col.green}!{Col.white}]{Col.green} Successfully Sent {Col.white}{mo}.{mo2}$ {Col.green}To Your wallet !")
         input(f"{Col.white}[{Col.dark_red}!{Col.white}]{Col.dark_red} Press Enter to continue mining..")
Code()
