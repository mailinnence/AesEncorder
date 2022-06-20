# 메인 로고 사진
# C:\\Users\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\main.png
# defalut path set
# C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\filedefalutpath.txt
# 개인저장장소 2022/06/07
# C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\record\\

from urllib import parse
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
            fbutton1.pack_forget()
            fbutton2.pack_forget()
            #pack 지우는 함수
            flabel.pack_forget()
            flabel4.pack_forget()
            flabel5.pack_forget()
            flabel6.pack_forget()
            foption.pack_forget()
            main().encoding()          
        def movedecoding():
            #place 지우는 함수
            fbutton1.pack_forget()
            fbutton2.pack_forget()
            #pack 지우는 함수
            flabel.pack_forget()
            flabel4.pack_forget()
            flabel5.pack_forget()
            flabel6.pack_forget()
            foption.pack_forget()
            main().decoding()    
        def movepathoption():
            #place 지우는 함수
            fbutton1.pack_forget()
            fbutton2.pack_forget()
            #pack 지우는 함수
            flabel.pack_forget()
            flabel4.pack_forget()
            flabel5.pack_forget()
            flabel6.pack_forget()
            foption.pack_forget()
            main().pathset()         
         
        #메뉴바 초기화
        menubar=tkinter.Menu(window)
        menu_1=tkinter.Menu(menubar, tearoff=0)
        window.config(menu=menubar)    
        #한칸띄우기 용 위젯
        flabel4=tkinter.Label(window, height=3)
        flabel5=tkinter.Label(window, width=10 )
        flabel6=tkinter.Label(window, width=10 )
        flabel4.pack()
        #이미지로고
        image=tkinter.PhotoImage(file="C:\\Users\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\main.png" ,height=430)
        flabel=tkinter.Label(window, image=image)
        flabel.pack()
        #encorder 페이지로 이동
        fbutton1 = tkinter.Button(window, width=15 , text="Encoding" ,command=moveencoding )
        fbutton1.configure(font=(40))
        flabel5.pack(side="left")
        fbutton1.pack(side="left")
        #decorder 페이지로 이동
        fbutton2 = tkinter.Button(window, width=15 , text="Decoding" ,command=movedecoding)
        fbutton2.configure(font=(40))
        flabel6.pack(side="right")
        fbutton2.pack(side="right")
        #defalut path 설정 페이지로 이동        
        foption= tkinter.Button(window, width=15 , text="PathOption" ,command=movepathoption)
        foption.configure(font=(40))
        foption.pack()
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
            ivtext.pack_forget()
            ivtextinput.pack_forget()
            main().firstpage()
        def initialization(): 
            Etext.delete("1.0","end")
            Etext1.delete("1.0","end")
        #메뉴바 설정
        menubar=tkinter.Menu(window)
        menu_1=tkinter.Menu(menubar, tearoff=0)
        menu_1.add_command(label="초기화" ,command=initialization)
        menubar.add_cascade(label="설정", menu=menu_1)
        menu_3=tkinter.Menu(menubar, tearoff=0)
        menu_3.add_command(label="첫페이지로 돌아가기" ,command=movefristpage)
        menubar.add_cascade(label="끝내기", menu=menu_3)        
        window.config(menu=menubar)
        #한칸띄우기
        EPlaintext=tkinter.Label(window, text="Plain text", width=10)
        EPlaintext.configure(font=(40))
        EPlaintext.pack()
        #평문텍스트
        Etext=tkinter.Text(window,width=77,height=17 )
        Etext.configure(font=(40))
        Etext.pack()
        #한칸띄우기
        Encodingtext=tkinter.Label(window, text="Encoding text", width=10)
        Encodingtext.configure(font=(40))
        Encodingtext.pack()
        #암호문텍스트
        Etext1=tkinter.Text(window,width=120,height=10)
        Etext1.pack()
        #한칸띄우기
        Enone=tkinter.Label(window, text="")
        Enone.pack()  
        #임시 바이트 함수
        global ciphered
        def enc(argument1,argument2):
            Etext1.delete("1.0","end")
            keytext ='aesencoding'
            ivtext=argument2   
            msg=parse.quote(argument1)
            myCipher = myAES(keytext, ivtext)
            global ciphered
            ciphered = myCipher.enc(msg)
            Etext1.insert(tkinter.CURRENT, str(ciphered))
        def savefilegui():
        #메뉴바 초기화
            menubar=tkinter.Menu(window)
            menu_1=tkinter.Menu(menubar, tearoff=0)
            window.config(menu=menubar)
            #저장 창 만들기
            EPlaintext.pack_forget()
            Encodingtext.pack_forget()
            Eencbutton.pack_forget()
            Esavebutton.pack_forget()
            Enone.pack_forget()
            Enone1.pack_forget()
            Enone2.pack_forget()
            Etext.pack_forget()
            Etext1.pack_forget()
            ivtext.pack_forget()
            ivtextinput.pack_forget()
            #경로지정텍스트
            filepathlabel=tkinter.Label(window, text="파일을 저장할 위치와 이름을 입력해 주세요\n ex C:\\\\Users\\\\gildong\\\\OneDrive\\\\secret.bin ")
            filepathlabel.pack()                
            #경로지정
            filepathinput=tkinter.Text(window,width=70,height=2)
            filepathinput.pack()
            with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\filedefalutpath.txt", "rt") as f:
                a=f.read()
                f.close()
                filepathinput.insert(tkinter.CURRENT, a)
            #한칸띄우기
            Enone3=tkinter.Label(window, text="")
            Enone3.pack()
            def savefilepath(path,ciphered):
                path=path[0:-1]
                try:
                    with open(path, "wb") as f:
                        f.write(ciphered)
                        f.close()
                        print(ciphered)
                    errorlabel.config(text="파일이 정상적으로 저장되었습니다")    
                except:
                    errorlabel.config(text="파일이 없거나 경로가 올바르지 않습니다")
            #경로에 저장하기 버튼
            Esavefilebutton = tkinter.Button(window, width=15, text="저장하기" , command=lambda:savefilepath(filepathinput.get("1.0","end"),ciphered))    
            Esavefilebutton.pack()
            #한칸띄우기
            Enone4=tkinter.Label(window, text="")
            Enone4.pack()
            def ReturnEnc():
                filepathlabel.pack_forget()
                filepathinput.pack_forget()
                Enone3.pack_forget()
                Enone4.pack_forget()
                Enone5.pack_forget()
                Esavefilebutton.pack_forget()
                Esavereturnbutton.pack_forget()
                errorlabel.pack_forget()
                main().encoding()                
            #돌아가기 버튼
            Esavereturnbutton = tkinter.Button(window, width=15, text="돌아가기" , command=ReturnEnc)    
            Esavereturnbutton.pack()
            #한칸띄우기
            Enone5=tkinter.Label(window, text="")
            Enone5.pack()
            #예외처리
            errorlabel=tkinter.Label(window, text="")
            errorlabel.pack()                    
        #ivtext,암호화,저장 암호
        Enone1=tkinter.Label(window, width="3")
        Enone1.pack(side="right")
        Esavebutton = tkinter.Button(window, width=15, text="save" ,command=savefilegui)    
        Esavebutton.pack(side="right")
        Enone2=tkinter.Label(window, width="3")
        Enone2.pack(side="right")                
        Eencbutton=tkinter.Button(window, width=15 , text="encoding" , command=lambda: enc(Etext.get("1.0","end"),ivtextinput.get("1.0","end")))    
        Eencbutton.pack(side="right")
        ivtext=tkinter.Label(window, text="ivtext를 입력해주세요")
        ivtext.pack(side="right")
        ivtextinput=tkinter.Text(window,width=30,height=2,)
        ivtextinput.pack(side="right")
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
            done2.pack_forget() 
            ivtext.pack_forget() 
            ivtextinput.pack_forget() 
            main().firstpage()        
        def initialization():
            input.delete("1.0","end")
            Dtext.delete("1.0","end")
            with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\filedefalutpath.txt", "rt") as f:
                a=f.read()
                f.close()
                input.insert(tkinter.CURRENT, a) 
            file_names = os.listdir(a)
            for name in file_names:
                src = os.path.join(a, name)
                result = src.split('\\\\')
                result = result[-1]+"\n"      
                Dtext.insert(tkinter.CURRENT, result)  
        #메뉴바 설정
        menubar=tkinter.Menu(window)
        menu_1=tkinter.Menu(menubar, tearoff=0)
        menu_1.add_command(label="초기화" ,command=initialization)
        menubar.add_cascade(label="설정", menu=menu_1) 
        menu_3=tkinter.Menu(menubar, tearoff=0)
        menu_3.add_command(label="첫페이지로 돌아가기" ,command=movefristpage)
        menubar.add_cascade(label="끝내기", menu=menu_3)
        window.config(menu=menubar)
        #복호화 설명 라벨
        Encodingtext=tkinter.Label(window, text="Decoding text", width=10)
        Encodingtext.pack()
        #복호화된 문장 보여주는 텍스트
        Dtext=tkinter.Text(window,width=77,height=24)
        Dtext.configure(font=(40))
        Dtext.pack()
        #파일 경로 설명 라벨
        plainlabel=tkinter.Label(window, text="디코딩할 파일을 입력해 주세요\n ex C:\\\\Users\\\\gildong\\\\OneDrive\\\\바탕 화면\\\\program\\\\CompletedProject\\\\encoingdecoding\\\\record\\\\secret.bin) ")
        plainlabel.pack()
        #칸 맟추기용 라벨
        done2=tkinter.Label(window, text="",width=5)
        #ivtext 입력기
        ivtext=tkinter.Label(window, text="ivtext를 입력해주세요")
        ivtextinput=tkinter.Text(window,width=30,height=2)
        #파일입력
        input=tkinter.Text(window,width=40,height=1)
        with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\filedefalutpath.txt", "rt") as f:
            a=f.read()
            f.close()
            input.insert(tkinter.CURRENT, a)
        file_names = os.listdir(a)
        for name in file_names:
            src = os.path.join(a, name)
            result = src.split('\\\\')
            result = result[-1]+"\n"      
            Dtext.insert(tkinter.CURRENT, result)   
        def loadfilpath(path , argument2 ):
            path=path[0:-1]
            Dtext.delete("1.0","end")
            try:
                with open(path, "rb") as f:
                    a=f.read()
                    f.close()
                keytext ='aesencoding'
                ivtext=argument2 
                msg=a
                myCipher = myAES(keytext, ivtext)
                deciphered = myCipher.dec(msg)
                deciphered = parse.unquote(str(deciphered))
                Dtext.insert(tkinter.CURRENT, deciphered[2:-1])
            except:
                plainlabel.config(text="파일이 없거나 ivtext가 틀렸거나 경로가 올바르지 않습니다")
        #디코딩실행버튼
        Dbutton = tkinter.Button(window, width=15, text="Decoding" ,command=lambda:loadfilpath(input.get("1.0","end"),ivtextinput.get("1.0","end")))
        done1=tkinter.Label(window, text="",width=5)
        #위젯 위치 설정
        done1.pack(side="right")
        Dbutton.pack(side="right")
        input.pack(side="right")
        done2.pack(side="left") 
        ivtextinput.pack(side="left")
        ivtext.pack(side="left")
    def pathset(self):
        def pathsetreturn():
            pone.pack_forget()
            pathsetlabel.pack_forget()
            pathsettext.pack_forget()
            pone2.pack_forget()
            pathsetbutton.pack_forget()
            pone1.pack_forget()
            pathreturnbutton.pack_forget()
            pone3.pack_forget()
            currentpath1.pack_forget()
            currentpath2.pack_forget()
            main().firstpage()
        def pathsetsave(path):
            with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\filedefalutpath.txt", "wt") as f:
                path=path[0:-1]
                f.write(path)
                f.close()
                pathsetlabel.config(text="저장되었습니다")
                currentpath1.config(text="현재의 defalut path ")
                currentpath2.config(text=path )
        pone=tkinter.Label(window)
        pone1=tkinter.Label(window)
        pone2=tkinter.Label(window)
        pone3=tkinter.Label(window)
        #파일경로 기본 지정 설명 라벨
        pathsetlabel=tkinter.Label(window, text="defalut path를 입력해 주세요\n ex C:\\\\Users\\\\gildong\\\\program\\\\record\\\\ ")
        pathsetlabel.configure(font=(1))
        pathsettext=tkinter.Text(window,width=60,height=2)
        pathsetbutton = tkinter.Button(window, width=15 , text="저장하기" ,command=lambda:pathsetsave(pathsettext.get("1.0","end")))
        pathsetbutton.configure(font=(40))
        pathreturnbutton = tkinter.Button(window, width=15 , text="돌아가기" , command=pathsetreturn)
        pathreturnbutton.configure(font=(40))
        with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\filedefalutpath.txt", "rt") as f:
            path1=f.read()
            f.close()
        if path1=="":   
            currentpath1=tkinter.Label(window, text="현재의 defalut path 는 지정되지 않았습니다")      
        if path1!="":   
            currentpath1=tkinter.Label(window, text="현재의 defalut path ")        
            currentpath1.configure(font=(40)) 
            currentpath2=tkinter.Label(window, text=path1)
        pone.pack()
        pathsetlabel.pack()
        pathsettext.pack()
        pone2.pack()
        pathsetbutton.pack()
        pone1.pack()
        pathreturnbutton.pack()
        pone3.pack()
        currentpath1.pack()
        currentpath2.pack()





if __name__=='__main__':        
    main().firstpage()
    
    
    
    
#----------------------------
# 메인 로고 사진
# C:\\Users\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\main.png
# defalut path set
# C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\filedefalutpath.txt
# 개인저장장소 2022/06/07
# C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\record\\

from urllib import parse
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
            fbutton1.pack_forget()
            fbutton2.pack_forget()
            #pack 지우는 함수
            flabel.pack_forget()
            flabel4.pack_forget()
            flabel5.pack_forget()
            flabel6.pack_forget()
            foption.pack_forget()
            main().encoding()          
        def movedecoding():
            #place 지우는 함수
            fbutton1.pack_forget()
            fbutton2.pack_forget()
            #pack 지우는 함수
            flabel.pack_forget()
            flabel4.pack_forget()
            flabel5.pack_forget()
            flabel6.pack_forget()
            foption.pack_forget()
            main().decoding()    
        def movepathoption():
            #place 지우는 함수
            fbutton1.pack_forget()
            fbutton2.pack_forget()
            #pack 지우는 함수
            flabel.pack_forget()
            flabel4.pack_forget()
            flabel5.pack_forget()
            flabel6.pack_forget()
            foption.pack_forget()
            main().pathset()         
         
        #메뉴바 초기화
        menubar=tkinter.Menu(window)
        menu_1=tkinter.Menu(menubar, tearoff=0)
        window.config(menu=menubar)    
        #한칸띄우기 용 위젯
        flabel4=tkinter.Label(window, height=3)
        flabel5=tkinter.Label(window, width=10 )
        flabel6=tkinter.Label(window, width=10 )
        flabel4.pack()
        #이미지로고
        image=tkinter.PhotoImage(file="C:\\Users\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\main.png" ,height=430)
        flabel=tkinter.Label(window, image=image)
        flabel.pack()
        #encorder 페이지로 이동
        fbutton1 = tkinter.Button(window, width=15 , text="Encoding" ,command=moveencoding )
        fbutton1.configure(font=("", 16, ""))
        flabel5.pack(side="left")
        fbutton1.pack(side="left")
        #decorder 페이지로 이동
        fbutton2 = tkinter.Button(window, width=15 , text="Decoding" ,command=movedecoding)
        fbutton2.configure(font=("", 16, ""))
        flabel6.pack(side="right")
        fbutton2.pack(side="right")
        #defalut path 설정 페이지로 이동        
        foption= tkinter.Button(window, width=15 , text="PathOption" ,command=movepathoption)
        foption.configure(font=("", 16, ""))
        foption.pack()
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
            ivtext.pack_forget()
            ivtextinput.pack_forget()
            main().firstpage()
        def initialization(): 
            Etext.delete("1.0","end")
            Etext1.delete("1.0","end")
        #메뉴바 설정
        menubar=tkinter.Menu(window)
        menu_1=tkinter.Menu(menubar, tearoff=0)
        menu_1.add_command(label="초기화" ,command=initialization)
        menubar.add_cascade(label="설정", menu=menu_1)
        menu_3=tkinter.Menu(menubar, tearoff=0)
        menu_3.add_command(label="첫페이지로 돌아가기" ,command=movefristpage)
        menubar.add_cascade(label="끝내기", menu=menu_3)        
        window.config(menu=menubar)
        #한칸띄우기
        EPlaintext=tkinter.Label(window, text="Plain text", width=10)
        EPlaintext.configure(font=("", 16, ""))
        EPlaintext.pack()
        #평문텍스트
        Etext=tkinter.Text(window,width=77,height=17 )
        Etext.configure(font=("", 16, ""))
        Etext.pack()
        #한칸띄우기
        Encodingtext=tkinter.Label(window, text="Encoding text", width=10)
        Encodingtext.configure(font=("", 16, ""))
        Encodingtext.pack()
        #암호문텍스트
        Etext1=tkinter.Text(window,width=120,height=10)
        Etext1.pack()
        #한칸띄우기
        Enone=tkinter.Label(window, text="")
        Enone.pack()  
        #임시 바이트 함수
        global ciphered
        def enc(argument1,argument2):
            Etext1.delete("1.0","end")
            keytext ='aesencoding'
            ivtext=argument2   
            msg=parse.quote(argument1)
            myCipher = myAES(keytext, ivtext)
            global ciphered
            ciphered = myCipher.enc(msg)
            Etext1.insert(tkinter.CURRENT, str(ciphered))
        def savefilegui():
        #메뉴바 초기화
            menubar=tkinter.Menu(window)
            menu_1=tkinter.Menu(menubar, tearoff=0)
            window.config(menu=menubar)
            #저장 창 만들기
            EPlaintext.pack_forget()
            Encodingtext.pack_forget()
            Eencbutton.pack_forget()
            Esavebutton.pack_forget()
            Enone.pack_forget()
            Enone1.pack_forget()
            Enone2.pack_forget()
            Etext.pack_forget()
            Etext1.pack_forget()
            ivtext.pack_forget()
            ivtextinput.pack_forget()
            #경로지정텍스트
            filepathlabel=tkinter.Label(window, text="파일을 저장할 위치와 이름을 입력해 주세요\n ex C:\\\\Users\\\\gildong\\\\OneDrive\\\\secret.bin ")
            filepathlabel.pack()                
            #경로지정
            filepathinput=tkinter.Text(window,width=70,height=2)
            filepathinput.pack()
            with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\filedefalutpath.txt", "rt") as f:
                a=f.read()
                f.close()
                filepathinput.insert(tkinter.CURRENT, a)
            #한칸띄우기
            Enone3=tkinter.Label(window, text="")
            Enone3.pack()
            def savefilepath(path,ciphered):
                path=path[0:-1]
                try:
                    with open(path, "wb") as f:
                        f.write(ciphered)
                        f.close()
                        print(ciphered)
                    errorlabel.config(text="파일이 정상적으로 저장되었습니다")    
                except:
                    errorlabel.config(text="파일이 없거나 경로가 올바르지 않습니다")
            #경로에 저장하기 버튼
            Esavefilebutton = tkinter.Button(window, width=15, text="저장하기" , command=lambda:savefilepath(filepathinput.get("1.0","end"),ciphered))    
            Esavefilebutton.pack()
            #한칸띄우기
            Enone4=tkinter.Label(window, text="")
            Enone4.pack()
            def ReturnEnc():
                filepathlabel.pack_forget()
                filepathinput.pack_forget()
                Enone3.pack_forget()
                Enone4.pack_forget()
                Enone5.pack_forget()
                Esavefilebutton.pack_forget()
                Esavereturnbutton.pack_forget()
                errorlabel.pack_forget()
                main().encoding()                
            #돌아가기 버튼
            Esavereturnbutton = tkinter.Button(window, width=15, text="돌아가기" , command=ReturnEnc)    
            Esavereturnbutton.pack()
            #한칸띄우기
            Enone5=tkinter.Label(window, text="")
            Enone5.pack()
            #예외처리
            errorlabel=tkinter.Label(window, text="")
            errorlabel.pack()                    
        #ivtext,암호화,저장 암호
        Enone1=tkinter.Label(window, width="3")
        Enone1.pack(side="right")
        Esavebutton = tkinter.Button(window, width=15, text="save" ,command=savefilegui)    
        Esavebutton.pack(side="right")
        Enone2=tkinter.Label(window, width="5")
        Enone2.pack(side="right")                
        Eencbutton=tkinter.Button(window, width=15 , text="encoding" , command=lambda: enc(Etext.get("1.0","end"),ivtextinput.get("1.0","end")))    
        Eencbutton.pack(side="right")
        ivtext=tkinter.Label(window, text="ivtext를 입력해주세요")
        ivtext.pack(side="right")
        ivtextinput=tkinter.Text(window,width=30,height=2,)
        ivtextinput.pack(side="right")
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
            done2.pack_forget() 
            ivtext.pack_forget() 
            ivtextinput.pack_forget() 
            main().firstpage()        
        def initialization():
            input.delete("1.0","end")
            Dtext.delete("1.0","end")
            with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\filedefalutpath.txt", "rt") as f:
                a=f.read()
                f.close()
                input.insert(tkinter.CURRENT, a) 
            file_names = os.listdir(a)
            for name in file_names:
                src = os.path.join(a, name)
                result = src.split('\\\\')
                result = result[-1]+"\n"      
                Dtext.insert(tkinter.CURRENT, result)  
        #메뉴바 설정
        menubar=tkinter.Menu(window)
        menu_1=tkinter.Menu(menubar, tearoff=0)
        menu_1.add_command(label="초기화" ,command=initialization)
        menubar.add_cascade(label="설정", menu=menu_1) 
        menu_3=tkinter.Menu(menubar, tearoff=0)
        menu_3.add_command(label="첫페이지로 돌아가기" ,command=movefristpage)
        menubar.add_cascade(label="끝내기", menu=menu_3)
        window.config(menu=menubar)
        #복호화 설명 라벨
        Encodingtext=tkinter.Label(window, text="Decoding text", width=10)
        Encodingtext.pack()
        #복호화된 문장 보여주는 텍스트
        Dtext=tkinter.Text(window,width=77,height=24)
        Dtext.configure(font=("", 16, ""))
        Dtext.pack()
        #파일 경로 설명 라벨
        plainlabel=tkinter.Label(window, text="디코딩할 파일을 입력해 주세요\n ex C:\\\\Users\\\\gildong\\\\OneDrive\\\\바탕 화면\\\\program\\\\CompletedProject\\\\encoingdecoding\\\\record\\\\secret.bin) ")
        plainlabel.pack()
        #칸 맟추기용 라벨
        done2=tkinter.Label(window, text="",width=5)
        #ivtext 입력기
        ivtext=tkinter.Label(window, text="ivtext를 입력해주세요")
        ivtextinput=tkinter.Text(window,width=30,height=2)
        #파일입력
        input=tkinter.Text(window,width=40,height=1)
        with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\filedefalutpath.txt", "rt") as f:
            a=f.read()
            f.close()
            input.insert(tkinter.CURRENT, a)
        file_names = os.listdir(a)
        for name in file_names:
            src = os.path.join(a, name)
            result = src.split('\\\\')
            result = result[-1]+"\n"      
            Dtext.insert(tkinter.CURRENT, result)   
        def loadfilpath(path , argument2 ):
            path=path[0:-1]
            Dtext.delete("1.0","end")
            try:
                with open(path, "rb") as f:
                    a=f.read()
                    f.close()
                keytext ='aesencoding'
                ivtext=argument2 
                msg=a
                myCipher = myAES(keytext, ivtext)
                deciphered = myCipher.dec(msg)
                deciphered = parse.unquote(str(deciphered))
                Dtext.insert(tkinter.CURRENT, deciphered[2:-1])
            except:
                plainlabel.config(text="파일이 없거나 ivtext가 틀렸거나 경로가 올바르지 않습니다")
        #디코딩실행버튼
        Dbutton = tkinter.Button(window, width=15, text="Decoding" ,command=lambda:loadfilpath(input.get("1.0","end"),ivtextinput.get("1.0","end")))
        done1=tkinter.Label(window, text="",width=5)
        #위젯 위치 설정
        done1.pack(side="right")
        Dbutton.pack(side="right")
        input.pack(side="right")
        done2.pack(side="left") 
        ivtextinput.pack(side="left")
        ivtext.pack(side="left")
    def pathset(self):
        def pathsetreturn():
            pone.pack_forget()
            pathsetlabel.pack_forget()
            pathsettext.pack_forget()
            pone2.pack_forget()
            pathsetbutton.pack_forget()
            pone1.pack_forget()
            pathreturnbutton.pack_forget()
            pone3.pack_forget()
            currentpath1.pack_forget()
            currentpath2.pack_forget()
            main().firstpage()
        def pathsetsave(path):
            with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\filedefalutpath.txt", "wt") as f:
                path=path[0:-1]
                f.write(path)
                f.close()
                pathsetlabel.config(text="저장되었습니다")
                currentpath1.config(text="현재의 defalut path ")
                currentpath2.config(text=path )
        pone=tkinter.Label(window)
        pone1=tkinter.Label(window)
        pone2=tkinter.Label(window)
        pone3=tkinter.Label(window)
        #파일경로 기본 지정 설명 라벨
        pathsetlabel=tkinter.Label(window, text="defalut path를 입력해 주세요\n ex C:\\\\Users\\\\gildong\\\\program\\\\record\\\\ ")
        pathsetlabel.configure(font=(1))
        pathsettext=tkinter.Text(window,width=60,height=2)
        pathsetbutton = tkinter.Button(window, width=15 , text="저장하기" ,command=lambda:pathsetsave(pathsettext.get("1.0","end")))
        pathsetbutton.configure(font=(40))
        pathreturnbutton = tkinter.Button(window, width=15 , text="돌아가기" , command=pathsetreturn)
        pathreturnbutton.configure(font=(40))
        with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\program\\CompletedProject\\encoingdecoding\\AES-EncorderProgram\\filedefalutpath.txt", "rt") as f:
            path1=f.read()
            f.close()
        if path1=="":   
            currentpath1=tkinter.Label(window, text="현재의 defalut path 는 지정되지 않았습니다")      
        if path1!="":   
            currentpath1=tkinter.Label(window, text="현재의 defalut path ")        
            currentpath1.configure(font=(40)) 
            currentpath2=tkinter.Label(window, text=path1)
        pone.pack()
        pathsetlabel.pack()
        pathsettext.pack()
        pone2.pack()
        pathsetbutton.pack()
        pone1.pack()
        pathreturnbutton.pack()
        pone3.pack()
        currentpath1.pack()
        currentpath2.pack()





if __name__=='__main__':        
    main().firstpage()




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



