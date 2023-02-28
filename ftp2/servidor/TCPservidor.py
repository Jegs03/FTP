from socket import *
import os 
usr='admin'
psw='123'
cred=0
PATH=os.getcwd()
print(PATH)
print(os.listdir(PATH+'/archivos'))
servidorPuerto = 13000
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
print("El servidor está listo para recibir mensajes")
j=1
while j:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    print("Conexión establecida con ", clienteDireccion)
    mensaje = str( conexionSocket.recv(1024), "utf-8" )
    print(mensaje)
    if mensaje[0]=='h':
        mensajeRespuesta="""
        u ususario y contraseña
        l lista de archivos disponibles 
        r [nombre archivo] descargar un archivo
        c cerrar el servidor
        h ayuda
        """
        conexionSocket.send(bytes(str(mensajeRespuesta), "utf-8"))
    if mensaje[0]=='u' and not cred:
        credMens=str(mensaje).split('|')
        if credMens[1]==usr and credMens[2]==psw:
            cred=1
            mensajeRespuesta='200 estas conectado'
            conexionSocket.send(bytes(str(mensajeRespuesta), "utf-8"))
        else:
            mensajeRespuesta='400 credenciales erroneas'
            conexionSocket.send(bytes(str(mensajeRespuesta), "utf-8"))
    elif mensaje[0]=='u' and cred:
            mensajeRespuesta='200 estas conectado'
            conexionSocket.send(bytes(str(mensajeRespuesta), "utf-8"))
    if cred:
        if mensaje[0]=='c':
            mensajeRespuesta='220 servidor apagado'
            conexionSocket.send(bytes(str(mensajeRespuesta), "utf-8"))
            conexionSocket.close()
            j=0        
        if mensaje[0]=='l':
            list=os.listdir(PATH+'/archivos')
            mensajeRespuesta=''
            for k in list:
                mensajeRespuesta=mensajeRespuesta+k+'\n'
            mensajeRespuesta=mensajeRespuesta+'230 lista de directorios'
            print("Mensaje recibido de ", clienteDireccion)
            print(mensajeRespuesta)
            conexionSocket.send(bytes(str(mensajeRespuesta), "utf-8"))
        elif mensaje[0]=='r':
            nombre=mensaje[2:]
            print(nombre)
            list=os.listdir(PATH+'/archivos')
            if nombre in list:
                f=open(PATH+'/archivos/'+nombre,'r')
                texto=f.read()
                mensajeRespuesta=f'240 archivo {nombre} creado'+'|'+nombre+'|'+texto
                conexionSocket.send(bytes(str(mensajeRespuesta), "utf-8"))
                f.close()
            else:
                mensajeRespuesta='404 el archivo no existe'
                conexionSocket.send(bytes(str(mensajeRespuesta), "utf-8"))
    else:
        if mensaje[0]=='c':
            mensajeRespuesta='220 servidor apagado'
            conexionSocket.send(bytes(str(mensajeRespuesta), "utf-8"))
            conexionSocket.close()
            j=0
        else:
            mensajeRespuesta='401 no tienes las credenciales adecuadas'
            conexionSocket.send(bytes(str(mensajeRespuesta), "utf-8"))

    conexionSocket.close()