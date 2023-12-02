from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title('Criminal Management System')

        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM',font=('times new roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1360,height=70)

        # NCR LOGO
        img_logo=Image.open('images/ncrlogo.png')
        image_logo=img_logo.resize((60,60))
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=10,y=5,width=60,height=60)

        # IMG-FRAME 1
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1366,height=130)
        
        img1=Image.open('images/police1.png')
        img1=img1.resize((455,160))
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=455,height=160)

        # IMG-FRAME 2
        img_2=Image.open('images/police2.png')
        img_2=img_2.resize((455,160))
        self.photo2=ImageTk.PhotoImage(img_2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=455,y=0,width=455,height=155)

        # IMG-FRAME 2
        img_3=Image.open('images/police3.png')
        img_3=img_3.resize((455,160))
        self.photo3=ImageTk.PhotoImage(img_3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=910,y=0,width=455,height=155)

        # MAIN FRAME
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=200,width=1345,height=495)

        # UPPER-FRAME
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information',font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=4,width=1322,height=235)

        #Label Entry
        #CASE ID
        caseid=Label(upper_frame,text='Case ID:',font=('arial',9,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,width=22,text='Case ID:',font=('arial',9,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        # Criminal No
        lbl_criminal_no=Label(upper_frame,text='Criminal NO:',font=('arial',9,'bold'),bg='white')
        lbl_criminal_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        lbl_criminal_no=ttk.Entry(upper_frame,width=22,font=('arial',9,'bold'))
        lbl_criminal_no.grid(row=0,column=3,padx=2,pady=7)

        # Criminal Name
        lbl_Name=Label(upper_frame,text='Criminal Name:',font=('arial',9,'bold'),bg='white')
        lbl_Name.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_Name=ttk.Entry(upper_frame,width=22,font=('arial',9,'bold'))
        txt_Name.grid(row=1,column=1,padx=2,pady=7)

        # Criminal NickName
        lbl_nickname=Label(upper_frame,text='NickName:',font=('arial',9,'bold'),bg='white')
        lbl_nickname.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_nickname=ttk.Entry(upper_frame,width=22,font=('arial',9,'bold'))
        txt_nickname.grid(row=1,column=3,padx=2,pady=7)

        # Father Name
        lbl_fatherName=Label(upper_frame,text='Father Name:',font=('arial',9,'bold'),bg='white')
        lbl_fatherName.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_fatherName=ttk.Entry(upper_frame,width=22,font=('arial',9,'bold'))
        txt_fatherName.grid(row=2,column=1,padx=2,pady=7)
        
        # Date of Crime
        lbl_dateOfCrime=Label(upper_frame,text='Date of Crime:',font=('arial',9,'bold'),bg='white')
        lbl_dateOfCrime.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_dateOfCrime=ttk.Entry(upper_frame,width=22,font=('arial',9,'bold'))
        txt_dateOfCrime.grid(row=2,column=3,padx=2,pady=7)
        
        
        # Address
        lbl_Address=Label(upper_frame,text='Address:',font=('arial',9,'bold'),bg='white')
        lbl_Address.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_Address=ttk.Entry(upper_frame,width=22,font=('arial',9,'bold'))
        txt_Address.grid(row=3,column=1,padx=2,pady=7)
                
        
        # Age
        lbl_Age=Label(upper_frame,text='Age:',font=('arial',9,'bold'),bg='white')
        lbl_Age.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_Age=ttk.Entry(upper_frame,width=22,font=('arial',9,'bold'))
        txt_Age.grid(row=3,column=3,padx=2,pady=7)
        
        
        # Occupation
        lbl_occupation=Label(upper_frame,text='Occupation:',font=('arial',9,'bold'),bg='white')
        lbl_occupation.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_occupation=ttk.Entry(upper_frame,width=22,font=('arial',9,'bold'))
        txt_occupation.grid(row=4,column=1,padx=2,pady=7)

        # BirthMark
        lbl_birthmark=Label(upper_frame,text='Birth Mark:',font=('arial',9,'bold'),bg='white')
        lbl_birthmark.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_birthmark=ttk.Entry(upper_frame,width=22,font=('arial',9,'bold'))
        txt_birthmark.grid(row=4,column=3,padx=2,pady=7)

        # Crime Type
        lbl_crimeType=Label(upper_frame,text='Crime Type:',font=('arial',9,'bold'),bg='white')
        lbl_crimeType.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_crimeType=ttk.Entry(upper_frame,width=22,font=('arial',9,'bold'))
        txt_crimeType.grid(row=0,column=5,padx=2,pady=7)

        # Arrest Date
        lbl_arrestDate=Label(upper_frame,text='Arrest Date:',font=('arial',9,'bold'),bg='white')
        lbl_arrestDate.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_arrestDate=ttk.Entry(upper_frame,width=22,font=('arial',9,'bold'))
        txt_arrestDate.grid(row=1,column=5,padx=2,pady=7)

        # Gender
        lbl_gender=Label(upper_frame,text='Gender:',font=('arial',9,'bold'),bg='white')
        lbl_gender.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        # Radio Button for gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=603,y=75,width=134,height=30)

        male=Radiobutton(radio_frame_gender,text='Male',value='male',font=("arial",9,"bold"),bg='white')
        male.grid(row=0,column=0,pady=0,padx=2,sticky=W)

        female=Radiobutton(radio_frame_gender,text='Female',value='female',font=("arial",9,"bold"),bg='white')
        female.grid(row=0,column=1,pady=0,padx=2,sticky=W)

        # Wanted
        lbl_wanted=Label(upper_frame,text='Most Wanted:',font=('arial',9,'bold'),bg='white')
        lbl_wanted.grid(row=3,column=4,sticky=W,padx=2,pady=7)

        # Radio Button for wanted
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=603,y=110,width=134,height=30)

        yes=Radiobutton(radio_frame_wanted,text='Yes',value='yes',font=("arial",9,"bold"),bg='white')
        yes.grid(row=0,column=0,pady=0,padx=2,sticky=W)

        no=Radiobutton(radio_frame_wanted,text='No',value='no',font=("arial",9,"bold"),bg='white')
        no.grid(row=0,column=1,pady=0,padx=2,sticky=W)

        # Buttons
        button_frame=Frame(Main_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=15,y=193,width=514,height=42)

        # Add Button
        btn_add=Button(button_frame,text='Save Record',font=('arial',13,"bold"),width=11,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=3)

        # Update Button
        btn_update=Button(button_frame,text='Update',font=('arial',13,"bold"),width=11,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=3)

        # Delete Button
        btn_delete=Button(button_frame,text='Delete',font=('arial',13,"bold"),width=11,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=3)

        # Clear Button
        btn_clear=Button(button_frame,text='Clear',font=('arial',13,"bold"),width=11,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=3)


        # DOWN-FRAME
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=250,width=1322,height=235)

        # SEARCH-FRAME
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Criminal Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=3,y=0,width=1312,height=50)

if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
