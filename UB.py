import subprocess
#from tkinter import *
from tkinter import filedialog
from colorama import Fore, init, Back
#from os import path
init(autoreset=True)
print(Fore.CYAN + """
   __  _______ ____     ____  ____  ____  ______
  / / / / ___// __ )   / __ )/ __ \/ __ \/_  __/
 / / / /\__ \/ __  |  / __  / / / / / / / / /   
/ /_/ /___/ / /_/ /  / /_/ / /_/ / /_/ / / /   
\____//____/_____/  /_____/\____/\____/ /_/ 
""")
print("""
!!!Advertencias!!!
#Se borraran todos los datos del dispositivo USB
#Asegurese de que este en la carpeta del ISO EJEMPLO NOMBRE-DEL-ISO.iso
#La direcion de la memoria se escibe /dev/sdb asegurase de que este bien
""")
op = input("DESEA-CONTINUAR[s/n]\n")
if op == "s":
    memoria = input("DIRECION-MEMORIA\n")

    subprocess.call(["sudo","umount",memoria])    
    subprocess.call(["sudo","mkfs.vfat","-F","32","-n","USB-BOOT",memoria])

    
    file = filedialog.askopenfilename(filetypes = (("CD files","*.iso"),("all files","*.*")))    

    subprocess.run(["sudo","dd","if="+file,"of="+memoria])

print ("COMPLETADO")