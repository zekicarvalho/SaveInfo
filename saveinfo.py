import os
import subprocess

print("""
 .d8888b.                        8888888         .d888         
d88P  Y88b                         888          d88P"          
Y88b.                              888          888            
 "Y888b.   8888b. 888  888 .d88b.  888  88888b. 888888 .d88b.  
    "Y88b.    "88b888  888d8P  Y8b 888  888 "88b888   d88""88b 
      "888.d888888Y88  88P88888888 888  888  888888   888  888 
Y88b  d88P888  888 Y8bd8P Y8b.     888  888  888888   Y88..88P 
 "Y8888P" "Y888888  Y88P   "Y88888888888888  888888    "Y88P"  
""")
print(os.system('uname -a'))
print(os.system('df /'))
print(os.system('free'))
entrada = input('Use: "mem", "net", "comandos" ou "backup" para mais detalhes, ou tecle para sair. ')

def save(comando,processo):
    nome = input('Digite um nome do arquivo para backup: ')
    arquivo = open(nome,'w')
    processo = subprocess.getoutput(comando)
    arquivo.write(processo)
    arquivo.close()

if entrada == 'mem':
    print(os.system('df'))
    savemem = input('Deseja salvar dados sobre memoria? Digite "s" ou tecle para sair: ')
    if savemem == 's':
        save('df','mem')
    else:
        print('Até breve!')

elif entrada == 'net':
    print(os.system('netstat'))
    savenet = input('Deseja salvar dados sobre rede? Digite "s" ou tecle para sair: ')
    if savenet == 's':
        save('netstat','netstat')
    else:
        print('Até breve!')

elif entrada == 'comandos':
    print(os.system('ls /usr/bin'))
    savecmd = input('Deseja salvar os comandos disponiveis? Digite "s" ou tecle para sair: ')
    if savecmd == 's':
        save('ls /usr/bin','comandos')
    else:
        print('Até breve!')

elif entrada == 'backup':
    nome = input('Digite um nome do arquivo para backup: ')
    arquivo = open(nome,'w')
    system = subprocess.getoutput('uname -a')
    mem = subprocess.getoutput('df')
    ram = subprocess.getoutput('free')
    lista = list()
    lista.append(system)
    lista.append(mem)
    lista.append(ram)
    arquivo.writelines(lista)
    arquivo.close()
    print('Até breve!')

else:
    print('Até breve!')
