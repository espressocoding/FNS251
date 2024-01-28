from tkinter import *
from tkinter import messagebox
import random
########################################################################
tomuseg="QWERTYUIOPASDFGHJKLZXCVBNM"
jijiguseg="qwertyuiopasdfghjklzxcvbnm"
tusgai="!@#$%^&*()_+<>?:;,-="
too="0123456789"
count = 0 
########################################################################-Интэрфэйсийн хэсэг-толгой
root = Tk()
root.title("password checker")
root.geometry("600x400")
root.configure(bg="#3a7ff8")
root.resizable(False,False)

########################################################################-Санамсаргүйгээр хүчирхэг нууц үг үүсгэх 
def autogenerate():
    for i in range(100):
        ans = tomuseg + jijiguseg + tusgai + too
        length = 9
        password = "".join(random.sample(ans,length))
        heading=Label(frame, text= "Санал болгож буй нууц үг:" , fg='#0046a0', bg='#daedd9', font=('Times New Roman',9)).place(x=19, y=154)
        l, j, t, n = 0, 0, 0, 0
        for i in password:
            if (i in tomuseg):
                l+=1
            if (i in jijiguseg):
                j+=1
            if (i in tusgai):
                t+=1
            if (i in too):
                n+=1
        if (l>=1 and j>=1 and t>=1 and n>=1):
            code.delete(0, 'end')
            code.insert(0, password)
            code.place(x=21, y=177)
            screen=Label(root, width=35, height=7,bg='#32ee66')
            screen.place(x=23, y=153)
            tabtab=Label(screen, text="Бид танд дараах нууц үгийг\nсанал болгож байна.\nНууц үгээ мартуузай:)",width=30, height=5,fg='#3a7ff8', bg='white', font=('Times New Roman',9,'bold'))
            tabtab.place(x=19,y=10)
            screen.mainloop()
    
########################################################################-Хэрэглэгчийн оруулсан сул нууц үгийг тоолж дараагын ү/лдийг замчлах хэсэг
def sulkod():
    global count
    if (count <= 3):
        screen=Label(root, width=35, height=7,bg='#fc7e27')
        screen.place(x=23, y=153)
        tabtab=Label(screen, text="Таны сонгосон нууц үг сул буюу\nтайлахад хялбар байгаа тул дахин\nоролдоно уу...",width=30, height=5,fg='#3a7ff8', bg='white', font=('Times New Roman',9,'bold'))
        tabtab.place(x=19,y=10)
        screen.mainloop()
    else:
        count=count-3
        Button(frame, width=16, pady=7, text="АВТОМАТААР\nНУУЦ ҮГ ҮҮСГЭХ", bg='#32ee66', fg='white', border=0, font=('',13,'bold'), command = autogenerate).place(x=93,y=250)
        screen=Label(root, width=35, height=7,bg='red')
        screen.place(x=23, y=153)
        tabtab=Label(screen, text="Та дахин сул нууц үг оруулсан байна.\nТиймээс нууц үг үүсгэх зөвлөмжтэй\nтанилцан дахин оролдоно уу. Эсвэл\nавтоматаар нууц үг үүсгэх сонголтыг\nхийнэ үү.",width=30, height=5,fg='#3a7ff8', bg='white', font=('Times New Roman',9,'bold'))
        tabtab.place(x=19,y=10)
        screen.mainloop()
        
########################################################################- Гараас оруулсан утгыг шалгаж хүчирхэг эсэхийг мэдээллэх хэсэг
def check():
    password=code.get()
    l, j, t, n = 0, 0, 0, 0
    global count
    for i in password:
        if (i in tomuseg):
            l+=1
        if (i in jijiguseg):
            j+=1
        if (i in tusgai):
            t+=1
        if (i in too):
            n+=1
        if (i == ' '):
            messagebox.showerror("Invalid", "Хоосон тэмдэгт болон цэгийг\nашиглаж болохгүйг анхаарна уу!!!")
        if (i == '.'):
            messagebox.showerror("Invalid", "Хоосон тэмдэгт болон цэгийг\nашиглаж болохгүйг анхаарна уу!!!")
        if (len(password) <=7):
            break
    if (l>=1 and j>=1 and t>=1 and n>=1 and len(password) >=8):
        screen=Label(root, width=35, height=7,bg='#32ee66')
        screen.place(x=23, y=153)
        tabtab=Label(screen, text="Таны сонгосoн нууц үг хүчирхэг нууц\nүгийн шалгуурыг хангаж байна...\nтанд амжилт хүсье",width=30, height=5,fg='#3a7ff8', bg='white', font=('Times New Roman',9,'bold'))
        tabtab.place(x=19,y=10)
        screen.mainloop()
    else:
        count=count+1
        sulkod()
########################################################################-Зөвлөмж messagebox-ний код
def zuvlumj():
    zuvlumj = Toplevel(root)
    zuvlumj.title("zuvlumj")
    zuvlumj.geometry('600x400')
    zuvlumj.config(bg='#daedd9')
    Label(zuvlumj, text='Нууц үг үүсгэх зөвлөмж', bg='#daedd9', font=('Calibri(Body)',13,'bold')).pack(expand=True)
    Label(zuvlumj, text='Нууц үг нь багадаа дараах тэмдэгтүүдийг агуулсан байх шаардлагатай:\n-Том үсэг 1 ширхэг\n-Жижиг үсэг 1 ширхэг\n-Тоон тэмдэгт 1 ширхэг\n-Тусгай тэмдэгт 1 ширхэг...\n...зэрэг болно.\nХэрвээ таны оруулсан нууц үгийг сул буюу тайлахад хялбар нууц үг\nгэж тодорхойлсон бол дээрх тэмдэгтүүдээс оруулсан эсэхийг нягтална уу\n\n', bg='#daedd9', font=('Calibri(Body)',11,'bold')).pack(expand=True)
    Label(zuvlumj, text='Мөн Мэдээллийн аюулгүй байдлын цахим веб дэхь\nЗӨВЛӨМЖ -1 ХЭРХЭН ХҮЧИРХЭГ НУУЦ ҮГ ҮҮСГЭХ ВЭ?\nнийтлэлтэй танилцана уу\n"https://www.isd.gov.mn/?id=74"', bg='#daedd9',cursor='hand2', font=('Calibri(Body)',11,'bold')).pack(expand=True)
    zuvlumj.mainloop()
########################################################################-Нүүр хуудасны баруун талын код
heading=Label(root, text='________________________', fg='white', bg="#3a7ff8", font=('Times New Roman', 16, 'bold'))
heading.place(x=20, y=30)
heading=Label(root, text='Welcome to Password Checker', fg='white', bg="#3a7ff8", font=('Times New Roman', 16))
heading.place(x=20, y=20)
heading=Label(root, text='F.NS251-ASSIGNMENT', fg='white', bg='#3a7ff8',font=('Times New Roman', 6, 'bold'))
heading.place(x=20, y=58)
tabtab=Label(root, text= 'Бидний бүтээсэн програм нь таны үүсгэсэн\nнууц үгийн хүчирхэг байдлыг шалгах юм.\n\nМөн таньд хүчирхэг нууц үг үүсгэж\nсанал болгох болно.', width=40, height=5, fg = 'white', bg = '#3a7ff8',font=("Times New Roman",10))
tabtab.place(x=9,y=155)

zaavar = Button(root, text = 'Нууц үг үүсгэх зөвлөмж!!!',bg='#3a7ff8', border=0, cursor='hand2', fg= 'white', font=('Times New Roman', 10, 'italic', 'bold','underline'), command = zuvlumj)
zaavar.place(x=20, y=360)
########################################################################-НҮҮР ХУУДАС-ны зүүн талын код
frame=Frame(root, width=300, height=400, bg='#daedd9')
frame.place(x=300, y=0)

heading=Label(frame, text="_________", fg='#e4d137', bg='#daedd9', font=('',12))
heading.place(x=20, y=36)
heading=Label(frame, text="_________", fg='#0046a0', bg='#daedd9', font=('',12))
heading.place(x=100, y=36)
heading=Label(frame, text="_________", fg='#e94627', bg='#daedd9', font=('',12))
heading.place(x=180, y=36)
heading=Label(frame, text="МОНГОЛ УЛСЫН ШИНЖЛЭХ УХААН\n ТЕХНОЛОГИЙН СУРГУУЛЬ", fg='#0046a0', bg='#daedd9', font=('Times New Roman', 10, 'bold'))
heading.place(x=20, y=18)
heading=Label(frame, text="МЭДЭЭЛЭЛ, ХОЛБООНЫ ТЕХНОЛОГИЙН СУРГУУЛЬ", fg='#0046a0', bg='#daedd9', font=('Times New Roman', 7, 'bold'))
heading.place(x=20, y=58)
heading=Label(frame, text="byTeamLumos", fg='#0046a0', bg='#daedd9', font=('Segoe Script', 14))
heading.place(x=150, y=370)

heading=Label(frame, text= "Нууц үгээ оруулна уу...", fg='#0046a0', bg='#daedd9', font=('Areal',9))
heading.place(x=19, y=154)


########################################################################-Гараас утга оруулах хэсгийн код
def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    code.insert(text='энд бичнэ үү...')

code = Entry(frame, width=20, fg='grey', border=0, bg="white", font=("Times New Roman", 15), show='')
code.place(x=21, y=177)
code.insert(0,'энд бичнэ үү...')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
########################################################################-Нууц үгийг чагтаар нуух код болон Button товчийг check командтай холбож байгаа хэсэг
def show_password():
    if code.cget('show') == '':
        code.config(show='*')
    else:
        code.config(show='')

check_button = Checkbutton(frame, text = '', command= show_password)
check_button.place(x=231, y=177)

Button(frame, width=16, pady=7, text="ШАЛГАХ...", bg='#57a1f8', fg='white', border=0, font=('',13,'bold'), command = check).place(x=93,y=210)


root.mainloop()