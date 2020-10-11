from tkinter import *
import random

def reg():
   root = Tk()
   root.geometry('650x600')
   root.title("Registration Form")


   Fullname=StringVar()
   Email=StringVar()
   var = IntVar()
   c=StringVar()
   var1= IntVar()
   def subclick():
        label_0.destroy()
        label_1.destroy()
        entry_1.destroy()
        label_2.destroy()
        entry_2.destroy()
        label_3.destroy()
        label_4.destroy()
        label_5.destroy()
        b1.destroy()
        c1.destroy()
        c2.destroy()
        r1.destroy()
        r2.destroy()
        droplist.destroy()
        main()
        
     




   def database():
      name1=Fullname.get()
      email=Email.get()
      gender=var.get()
      country=c.get()
      prog=var1.get()
      conn = sqlite3.connect('Form.db')
      with conn:
         cursor=conn.cursor()
      cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
      cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
      conn.commit()
   
   
             
   label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
   label_0.place(x=90,y=53)
  

   label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
   label_1.place(x=80,y=130)

   entry_1 = Entry(root,textvar=Fullname)
   entry_1.place(x=240,y=130)

   label_2 = Label(root, text="Email",width=20,font=("bold", 10))
   label_2.place(x=68,y=180)

   entry_2 = Entry(root,textvar=Email)
   entry_2.place(x=240,y=180)

   label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
   label_3.place(x=70,y=230)

   r1=Radiobutton(root, text="Male",padx = 5, variable=var, value=1)
   r1.place(x=235,y=230)
   r2=Radiobutton(root, text="Female",padx = 20, variable=var, value=2)
   r2.place(x=290,y=230)

   label_4 = Label(root, text="country",width=20,font=("bold", 10))
   label_4.place(x=70,y=280)

   list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

   droplist=OptionMenu(root,c, *list1)
   droplist.config(width=15)
   c.set('select your country') 
   droplist.place(x=240,y=280)

   label_5 = Label(root, text="Programming",width=20,font=("bold", 10))
   label_5.place(x=85,y=330)
   var2= IntVar()
   c1=Checkbutton(root, text="java", variable=var1)
   c1.place(x=235,y=330)
  
   c2=Checkbutton(root, text="python", variable=var2)
   c2.place(x=290,y=330)

   b1=Button(root, text='Submit',width=20,bg='brown',fg='white',command=subclick)
   b1.place(x=180,y=380)



reg()

def main():
   questions = [
      "1.How many Keywords are there in C Programming language ?",
      "2.Which of the following functions takes A console Input in Python ?",
      "3.Which of the following is the capital of India ?",
      "4.Which of The Following is must to Execute a Python Code ?",
      "5.The Taj Mahal is located in  ?",
      "6.The append Method adds value to the list at the  ?",
      "7.Which of the following is not a costal city of india ?",
      "8.Which of The following is executed in browser(client side) ?",
      "9.Which of the following keyword is used to create a function in Python ?",
      "10.To Declare a Global variable in python we use the keyword ?",
      ]

   answers_choice = [
       ["23","32","33","43",],
       ["get()","input()","gets()","scan()",],
       ["Mumbai","Delhi","Chennai","Lucknow",],
       ["TURBO C","Py Interpreter","Notepad","IDE",],
       ["Patna","Delhi","Benaras","Agra",],
       ["custom location","end","center","beginning",],
       ["Bengluru","Kochin","Mumbai","vishakhapatnam",],
       ["perl","css","python","java",], 
       ["function","void","fun","def",],
       ["all","var","let","global",],
   ]    

   answers = [1,1,1,1,3,1,0,1,3,3] 

   user_answer = []

   indexes = []
   def gen():
       global indexes
       while(len(indexes) < 5):
            x = random.randint(0,9)
            if x in indexes:
                continue
            else:
                indexes.append(x)
            #print(indexes)



   def showresult(score):
        lblQuestion.destroy()
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        r5.destroy()
        r6.destroy()

        def persentage(score):
            a=(score/25)*100
        
            b=str(a)+"%"
            per=Label(text=b,
                    font = ("Gabriola",16),
                    background = "#ffffff",)
            per.place(x=280,y=370)


    
        labelimage = Label(
            root,
            background = "#ffffff",
            border = 0,
        )
        labelimage.pack(pady=(50,30))
        labelresulttext = Label(
            root,
            font = ("Gabriola",20,"bold"),
            background = "#ffffff",
        )
        labelresulttext.pack()
        questext=Label(text="Total Question= 5",
                    font = ("Gabriola",16),
                    background = "#ffffff",)
        questext.place(x=200,y=310)

        tmtext=Label(text="Total Marks= 25",
                    font = ("Gabriola",16),
                    background = "#ffffff",)
        tmtext.place(x=200,y=340)
  

        pertext=Label(text="Persentage=",
                    font = ("Gabriola",16),
                    background = "#ffffff",)
        pertext.place(x=200,y=370)
    
        markstext=Label(text="Your Marks=",
                    font = ("Gabriola",16),
                    background = "#ffffff",)
        markstext.place(x=200,y=400)

    
        persentage(score)   
        if score >= 20:
           img = PhotoImage(file="good.png")
           labelimage.configure(image=img)
           labelimage.image = img
           labelresulttext.configure(text="You Are Excellent !!")
           marks=Label(text=score,
                    font = ("Gabriola",16),
                    background = "#ffffff",)
           marks.place(x=290,y=400)
        elif (score >= 10 and score < 20):
           img = PhotoImage(file="bad.png")
           labelimage.configure(image=img)
           labelimage.image = img
           labelresulttext.configure(text="You Can Be Better !!")
           marks=Label(text=score,
                    font = ("Gabriola",16),
                    background = "#ffffff",)
           marks.place(x=290,y=400)
        else:
           img = PhotoImage(file="bad.png")
           labelimage.configure(image=img)
           labelimage.image = img
           labelresulttext.configure(text="You Should Work Hard !!")
           marks=Label(text=score,
                    font = ("Gabriola",16),
                    background = "#ffffff",)
           marks.place(x=290,y=400)
     




   def calc():
       global indexes,user_answer,answers
       x = 0
       score = 0
       for i in indexes:
           if user_answer[x] == answers[i]:
               score = score + 5
           x += 1
       print(score)
       showresult(score)            

   ques = 1
   def selected():
       global radiovar,user_answer
       global lblQuestion,r1,r2,r3,r4,r5,r6
       global ques
       x = radiovar.get()
       user_answer.append(x)
       radiovar.set(-1)
       if ques < 5:
           lblQuestion.config(text= questions[indexes[ques]])
           r1['text'] = answers_choice[indexes[ques]][0]
           r2['text'] = answers_choice[indexes[ques]][1]
           r3['text'] = answers_choice[indexes[ques]][2]
           r4['text'] = answers_choice[indexes[ques]][3]
           ques += 1
       else:
           print(indexes)
           print(user_answer)
         
           calc()


       
   def nextb():
        skip=0 
        skip +=1
        print(skip)
    
        global ques
        ques += 1
        selected()
     
   def preb():
        global ques
        ques -= 2
        selected()

   def sartQuiz():
       global lblQuestion,r1,r2,r3,r4,r5,r6
       lblQuestion=Label( 
           root,
           text=questions[indexes[0]],
           font=("Gabriola",16),
           width=500,
           justify="center",
           wraplength=400,
           background="#ffffff"
           )
       lblQuestion.pack(pady=(100,30 ))
       global radiovar
       radiovar=IntVar()
       radiovar.set(-1)

       r1=Radiobutton(
       root,
       text=answers_choice[indexes[0]][0],
       font=("Gabriola",12),
       value=0,
       variable=radiovar,
       command=selected,
       background="#ffffff"
         )
       r1.pack(pady=5)
       r2=Radiobutton(
            root,
            text=answers_choice[indexes[0]][1],
            font=("Gabriola",12),
            value=1,
            variable=radiovar,
            command=selected,
            background="#ffffff"
            )
       r2.pack(pady=5)

       r3=Radiobutton(
            root,
            text=answers_choice[indexes[0]][2],
            font=("Gabriola",12),
            value=2,
            variable=radiovar,
            command=selected,
            background="#ffffff"
            )
       r3.pack(pady=5)

       r4=Radiobutton(
            root,
            text=answers_choice[indexes[0]][3],
            font=("Gabriola",12),
            value=3,
            variable=radiovar,
            command=selected,
            background="#ffffff"
            )
       r4.pack(pady=5)



       global ques
       r5=Button(root,
                  text="Next>>",
                  font=("Gabriola",12,"bold"),
                  #background=""
                  command=nextb,
                 )
       r5.place(x=490,y=400)
       r6=Button(root,
                  text="<<Previous",
                  font=("Gabriola",12,"bold"),
                  #background=""
                  command=preb,
                  )
       r6.place(x=410,y=400)





   def startmsg():
        labelimage.destroy()
        labeltext.destroy()
        lblinstruction.destroy()
        b1.destroy()
        lblRule.destroy()
        gen()
        sartQuiz()


 
   root=Tk()
   root.title("Quizstar")
   root.geometry("650x600")
   root.config(background="#ffffff")
   root.resizable(0,0)   


   img1=PhotoImage(file="hat1.png")
   labelimage=Label(
        root,
        image=img1,
        background="#ffffff",bd=0
      )
   labelimage.pack(pady=(50,0))

   labeltext=Label(
       root,
       text="Quizstar",
       font=("Gabriola",26,"bold"),
       background="#ffffff"
      )
   labeltext.pack()

   b1 = Button(text = "START QUIZ >>",activeforeground = "white",
                activebackground = "maroon", background="green",
                font=("Gabriola",12,"bold"),border=(0),
                command=startmsg)
   b1.pack(pady=(40,0))

   lblinstruction=Label(root,text="Read The Instruction And \n Click Start Once You Are Read",
   font=("Gabriola",15,"bold"),
   background="#ffffff",
   justify="center"
    )
   lblinstruction.pack(pady=(30,0))

   lblRule=Label(root,
              text="This Quiz Contains 15 Questions\n You will get 2 minutes to solve a question Once you select \nfinal choice hence think before you select",
              font=("Cambria",12),
              width=100,
              background="black",
              foreground="yellow"
              )
   lblRule.pack(side="bottom")


   root.mainloop()










