import tkinter
from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA
import os
from datetime import datetime
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import time

window=tkinter.Tk()
window.title("AES-encoding")
window.geometry("900x620+100+100")
window.resizable(True, True) 



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





class main: 
    def firstpage(self):
        #버튼으로 지우는 함수
        def moveencoding():
            #place 지우는 함수
            fbutton1.place_forget()
            fbutton2.place_forget()
            #pack 지우는 함수
            flabel.pack_forget()
            flabel4.pack_forget()
            main().encoding()          
 
        def movedecoding():
            #place 지우는 함수
            fbutton1.place_forget()
            fbutton2.place_forget()
            #pack 지우는 함수
            flabel.pack_forget()
            flabel4.pack_forget()
            main().decoding()         
         
        #메뉴바 초기화--------------------------------------------------------------
        menubar=tkinter.Menu(window)

        menu_1=tkinter.Menu(menubar, tearoff=0)
        window.config(menu=menubar)
        #-----------------------------------------------------------------------        
        
        
     
        flabel4=tkinter.Label(window, height=3)
        flabel4.pack()

        image=tkinter.PhotoImage(file="./main.png" ,height=430)
        flabel=tkinter.Label(window, image=image)
        flabel.pack()

        fbutton1 = tkinter.Button(window, width=15 , text="Encoding" ,command=moveencoding )
        fbutton1.pack()

        fbutton2 = tkinter.Button(window, width=15 , text="decoding" ,command=movedecoding)
        fbutton2.pack()

        fbutton1.place(x=200, y=480)
        fbutton2.place(x=560, y=480)
        window.mainloop()
    
    
    
    def encoding(self):
        def movefristpage():
            EPlaintext.pack_forget()
            Encodingtext.pack_forget()
            Eencbutton.pack_forget()
            Esavebutton.pack_forget()
            Enone.pack_forget()
            Enone1.pack_forget()
            Enone2.pack_forget()
            Etext.pack_forget()
            Etext1.pack_forget()
            main().firstpage()
            
            
        #메뉴바 설정--------------------------------------------------------------
        menubar=tkinter.Menu(window)

        menu_1=tkinter.Menu(menubar, tearoff=0)
        menu_1.add_command(label="초기화")
        menu_1.add_command(label="저장")
        menu_1.add_command(label="다른이름으로 저장")
        menubar.add_cascade(label="파일", menu=menu_1)

        menu_2=tkinter.Menu(menubar, tearoff=0)
        menu_2.add_command(label="글자크기")
        menubar.add_cascade(label="설정", menu=menu_2)
        
        menu_3=tkinter.Menu(menubar, tearoff=0)
        menu_3.add_command(label="첫페이지로 돌아가기" ,command=movefristpage)
        menubar.add_cascade(label="끝내기", menu=menu_3)        
        
        window.config(menu=menubar)
        #-----------------------------------------------------------------------
        
        
        #한칸띄우기-----------------------------
        EPlaintext=tkinter.Label(window, text="Plain text", width=10)
        EPlaintext.pack()
        #-----------------------------------
        
       
        #텍스트-------------------------------
    
        Etext=tkinter.Text(window,width=120,height=28)
        plaintext="aaa"
        Etext.insert(tkinter.CURRENT, plaintext)
        Etext.pack()
        #------------------------------------

        #한칸띄우기-----------------------------
        Encodingtext=tkinter.Label(window, text="Encoding text", width=10)
        Encodingtext.pack()
        #------------------------------------

        #암호문-------------------------------
        Etext1=tkinter.Text(window,width=120,height=10,)
        endntext=""
        Etext1.insert(tkinter.CURRENT, endntext )
        Etext1.pack()
        #------------------------------------
        
        #한칸띄우기-----------------------------
        Enone=tkinter.Label(window, text="")
        Enone.pack()
        #------------------------------------  
              
        #암호화,저장 암호-------------------------------
        Enone1=tkinter.Label(window, width="3")
        Enone1.pack(side="right")
        
        Esavebutton=tkinter.Button(window, width=15 , text="save")    
        Esavebutton.pack(side="right")
        
        Enone2=tkinter.Label(window, width="3")
        Enone2.pack(side="right")        
        
        Eencbutton=tkinter.Button(window, width=15 , text="encoding")    
        Eencbutton.pack(side="right")
        #------------------------------------ 
        

        
        
        
    def decoding(self):
        def movefristpage():
            Encodingtext.pack_forget()
            Dtext.pack_forget()
            done1.pack_forget()
            input.pack_forget()
            done1.pack_forget()
            Dbutton.pack_forget()
            plainlabel.pack_forget() 
            input.pack_forget() 
            main().firstpage()
        
        #메뉴바 설정--------------------------------------------------------------
        menubar=tkinter.Menu(window)

        menu_1=tkinter.Menu(menubar, tearoff=0)
        menu_1.add_command(label="다른이름으로 저장")
        menubar.add_cascade(label="파일", menu=menu_1)

        menu_2=tkinter.Menu(menubar, tearoff=0)
        menu_2.add_command(label="글자크기")
        menubar.add_cascade(label="설정", menu=menu_2)
        
        menu_3=tkinter.Menu(menubar, tearoff=0)
        menu_3.add_command(label="첫페이지로 돌아가기" ,command=movefristpage)
        menubar.add_cascade(label="끝내기", menu=menu_3)        
        
        window.config(menu=menubar)
        #-----------------------------------------------------------------------
        
        
        
        
        #-----------------------------
        Encodingtext=tkinter.Label(window, text="Decoding text", width=10)
        Encodingtext.pack()
        #------------------------------------        
        
        #텍스트-------------------------------
        Dtext=tkinter.Text(window,width=120,height=35)
        decodingtext=""
        Dtext.insert(tkinter.CURRENT, decodingtext)
        Dtext.pack()
        #------------------------------------
        
        #설명용 라벨------------------------------
        plainlabel=tkinter.Label(window, text="디코딩할 파일을 입력해 주세요\n ex C:\\Users\\gildong\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\record\\secret.bin) ")
        plainlabel.pack()
        #------------------------------------------
       
        #파일립력-------------------------------
        input=tkinter.Text(window,width=80,height=1)
        decodingtext=""
        input.insert(tkinter.CURRENT, decodingtext)
        #------------------------------------
        
        #디코딩실행버튼---------------------------------
        Dbutton = tkinter.Button(window, width=15, text="Decoding")
        #------------------------------------------
        
        #칸 맟추기용 라벨------------------------------
        done1=tkinter.Label(window, text="",width=5)
        #------------------------------------------
        
        #위젯 위치 설정------------------------------
        done1.pack(side="right")
        Dbutton.pack(side="right")
        input.pack(side="right") 
        #----------------------------------------

        
if __name__=='__main__':        
    main().firstpage()


