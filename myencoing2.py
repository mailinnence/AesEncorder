from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA
import os
from datetime import datetime
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import time




class myAES():
   
    def __init__(self, keytext, ivtext):
        hash=SHA.new()
        key=hash.digest()
        self.key=key[:16]
        hash.update(ivtext.encode('utf-8'))
        iv=hash.digest()
        self.iv=iv[:16]
 
    def makeEnabled(self,plaintext):
        fillersize=0
        textsize=len(plaintext)
        if textsize%16 !=0:
            fillersize= 16-textsize%16
        filler='0'*fillersize 
        header='%d'%(fillersize)
        gap=16-len(header)
        header +='#'*gap
        return header+plaintext+filler
 
    def enc(self, plaintext):
        plaintext=self.makeEnabled(plaintext)
        aes=AES.new(self.key, AES.MODE_CBC,self.iv)
        encmsg=aes.encrypt(plaintext.encode())
        return encmsg
  
    def dec(self, ciphertext):
        aes=AES.new(self.key, AES.MODE_CBC,self.iv)
        decmsg=aes.decrypt(ciphertext)
        header=decmsg[:16].decode()
        fillersize=int(float(header.split('#')[0]))
        if fillersize !=0:
            decmsg=decmsg[16:-fillersize]
        else:
            decmsg =decmsg[16:]
        return decmsg

        
        
def write():
    now = datetime.now()
    print("encoding : ")
    keytext ='agf7'
    ivtext='mysecretrecord'   
    msg=input()
    print("\n")
    que=input("기본 디렉터리 이외에 공간에 파일을 저장합니까? (기본 디렉터리일 경우 엔터) or (따로 지정한다면 1 을 입력)")
   
    if que=="":
        loc="C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\record\\"
        print("저장할 파일의 이름을 입력하세요 ex) 2022-06-03(14h24m32s).bin  (defalut 현재시간날짜 : ) ")
        fna=input(">>")
        if fna=="":
            fna= str(now.year)+"년_"+str(now.month)+"월_"+ str(now.day)+"일_"+str(now.hour)+"시_"+str(now.minute)+"분_"+str(now.second)+"초" 
        
    elif que=="1":
        print("저장할 위치를 입력하세요. ex)C:\\Users\\maili\\OneDrive\\바탕 화면\\")
        loc=input("defalut : C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\record\\")
        print("저장할 파일의 이름을 입력하세요 ex) 2022-06-03(14h24m32s).bin  (defalut 현재시간날짜 : )")
        fna=input(">>")
        if fna=="":
            fna= str(now.year)+"년_"+str(now.month)+"월_"+ str(now.day)+"일_"+str(now.hour)+"시_"+str(now.minute)+"분_"+str(now.second)+"초" 
  
    myCipher = myAES(keytext, ivtext)
    ciphered = myCipher.enc(msg)
    
    save=loc+str(fna)+".bin"
   
    with open(save, "wb") as f:
        f.write(ciphered)
        f.close()
 
    print("encoding : \n" , ciphered)
    print('\n')
    print(save)
    os.system("pause")
    


def FileEncoding():
    keytext ='agf7'
    ivtext='mysecretrecord'   
    print("\n")
    que=input("암호화 할 파일이 기본 디렉터리에 있습니까?? (yes 경우 엔터) or (no 1 을 입력)")
    file_path = 'C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\record\\'
    file_names = os.listdir(file_path)   
    myCipher = myAES(keytext, ivtext)
    if que=="":
        print("default directory---------------------------------------")
        for i in range(len(file_names)):
            print(file_names[i])
        print("--------------------------------------------------------\n")
        loc="C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\record\\" 
        fna=input("복호화 할 파일의 이름을 입력하세요 ex) 2022-06-03(14h24m32s).txt : ")
        save=loc+fna
        save=loc+str(fna)
        change=save.split('.')
        change[1]=".bin"
        dst="".join(change)
        with open(save, "rt") as f:
            a=f.read()
            ciphered = myCipher.enc(a)
            f.close()
        os.rename(save, dst)
        time.sleep(3)
        with open(dst, "wb") as f:
            f.write(ciphered)
            f.close()
    elif que=="1":
        print("암호할 파일의 이름을 입력하세요 ex) C:\\Users\\maili\\OneDrive\\바탕 화면\\2022-06-03(14h24m32s).txt : )")
        fna=input(">>")
        save=str(fna)
        change=fna.split('.')
        change[1]=".bin"
        dst="".join(change)
        with open(save, "rt") as f:
            a=f.read()
            ciphered = myCipher.enc(a)
            f.close()    
        os.rename(fna, dst)
        time.sleep(3)
        with open(dst, "wb") as f:
            f.write(ciphered)
            f.close()    
    print("encoding : \n" , ciphered)
    print('\n')
    print(save)
    os.system("pause")


def read():
    print("decoding : ")
    keytext ='as7'
    ivtext='mysecretrecord'   
    myCipher = myAES(keytext, ivtext)
    file_path = 'C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\record\\'
    file_names = os.listdir(file_path)
    defalut=input("기본 디렉터리에서 가져옵니까? (기본 디렉터리일 경우 엔터) or (다른 위치의 파일이라면 1 을 입력)")
  
    if defalut=="":
        print("default directory---------------------------------------")
        for i in range(len(file_names)):
            print(file_names[i])
        print("--------------------------------------------------------\n")
        loc="C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\record\\" 
        fna=input("복호화 할 파일의 이름을 입력하세요 ex) 2022-06-03(14h24m32s).bin : ")
        save=loc+fna  
   
    if defalut=="1":
        print("읽어올 파일을 입력하세요. ex)C:\\Users\\maili\\OneDrive\\바탕 화면\\20220603.bin")
        save=input("defalut : C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\2022-06-03(14h24m32s).bin")
  
    with open(save, "rb") as f:
        a=f.read()
        deciphered = myCipher.dec(a)
        f.close()
        print(deciphered)
    print('\n')
    print('\n')   
    os.system("pause")    

    
if __name__=='__main__':
    select = int(input("Choose\n1.encoding \n2.FileEncoding \n3.decoding\n"))
    if select == 1:
        write()
    if select == 2:
        FileEncoding() 
    if select == 3:
        read() 
