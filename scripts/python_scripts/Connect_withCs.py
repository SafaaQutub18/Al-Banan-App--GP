


import socket

host, port = "127.0.0.1", 25001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

global start_recognition
#from SpeechRecognition import convertSpeechToText
start_recognition = sock.recv(1024).decode("UTF-8") # receiveing data in Byte from C#, and converting it to String
#convertSpeechToText(start_recognition,sock) 



def representSign(sign_id): 
    print("safaaaaaaaaaaaaaaaaaaaaaaaaaa",sign_id)
    sock.sendall(str(sign_id).encode("UTF-8"))
    
    