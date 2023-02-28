from socket import *
import os
PATH=os.getcwd()
servidorNombre = "127.0.0.1" 
servidorPuerto = 13000
clienteSocket = socket(AF_INET, SOCK_STREAM)
clienteSocket.connect((servidorNombre,servidorPuerto))
mensaje = input("Ingrese un mensaje(para ayuda ingrese h):")
if mensaje=='u':
    usr=input("Ingrese un usuario:")
    pas=input("Ingrese un contraseña:")
    mensaje=mensaje+'|'+usr+'|'+pas
clienteSocket.send(bytes(mensaje, "utf-8"))
mensajeRespuesta = clienteSocket.recv(1024)
if mensaje[0] =='r' and mensajeRespuesta[0]!='4' :
    res=str(mensajeRespuesta, "utf-8").split('|')
    print(res)
    k=open(PATH+'/archivos/'+res[1],'w')
    k.write(res[2])
    print("Respuesta:\n"+res[0])
else:
    print("Respuesta:\n" + str(mensajeRespuesta, "utf-8"))
clienteSocket.close()