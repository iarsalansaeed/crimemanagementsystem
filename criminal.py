from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        #variable
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthMark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()

        #from tkinter import StringVar
        ## List of variable names
        #variables = [
        #    "var_case_id", "var_criminal_no", "var_name", "var_nickname",
        #    "var_arrest_date", "var_date_of_crime", "var_address", "var_age",
        #    "var_occupation", "var_birthMark", "var_crime_type", "var_father_name",
        #    "var_gender", "var_wanted"
        #]
        #
        ## Creating StringVar instances using a loop
        #for var_name in variables:
        #    globals()[var_name] = StringVar()




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

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('arial',9,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        # Criminal No
        lbl_criminal_no=Label(upper_frame,text='Criminal NO:',font=('arial',9,'bold'),bg='white')
        lbl_criminal_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        lbl_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('arial',9,'bold'))
        lbl_criminal_no.grid(row=0,column=3,padx=2,pady=7)

        # Criminal Name
        lbl_Name=Label(upper_frame,text='Criminal Name:',font=('arial',9,'bold'),bg='white')
        lbl_Name.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',9,'bold'))
        txt_Name.grid(row=1,column=1,padx=2,pady=7)

        # Criminal NickName
        lbl_nickname=Label(upper_frame,text='NickName:',font=('arial',9,'bold'),bg='white')
        lbl_nickname.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=('arial',9,'bold'))
        txt_nickname.grid(row=1,column=3,padx=2,pady=7)

        # Father Name
        lbl_fatherName=Label(upper_frame,text='Father Name:',font=('arial',9,'bold'),bg='white')
        lbl_fatherName.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_fatherName=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=22,font=('arial',9,'bold'))
        txt_fatherName.grid(row=2,column=1,padx=2,pady=7)
        
        # Date of Crime
        lbl_dateOfCrime=Label(upper_frame,text='Date of Crime:',font=('arial',9,'bold'),bg='white')
        lbl_dateOfCrime.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_dateOfCrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=('arial',9,'bold'))
        txt_dateOfCrime.grid(row=2,column=3,padx=2,pady=7)
        
        
        # Address
        lbl_Address=Label(upper_frame,text='Address:',font=('arial',9,'bold'),bg='white')
        lbl_Address.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_Address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',9,'bold'))
        txt_Address.grid(row=3,column=1,padx=2,pady=7)
                
        
        # Age
        lbl_Age=Label(upper_frame,text='Age:',font=('arial',9,'bold'),bg='white')
        lbl_Age.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_Age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',9,'bold'))
        txt_Age.grid(row=3,column=3,padx=2,pady=7)
        
        
        # Occupation
        lbl_occupation=Label(upper_frame,text='Occupation:',font=('arial',9,'bold'),bg='white')
        lbl_occupation.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_occupation=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('arial',9,'bold'))
        txt_occupation.grid(row=4,column=1,padx=2,pady=7)

        # BirthMark
        lbl_birthmark=Label(upper_frame,text='Birth Mark:',font=('arial',9,'bold'),bg='white')
        lbl_birthmark.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_birthmark=ttk.Entry(upper_frame,textvariable=self.var_birthMark,width=22,font=('arial',9,'bold'))
        txt_birthmark.grid(row=4,column=3,padx=2,pady=7)

        # Crime Type
        lbl_crimeType=Label(upper_frame,text='Crime Type:',font=('arial',9,'bold'),bg='white')
        lbl_crimeType.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_crimeType=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=('arial',9,'bold'))
        txt_crimeType.grid(row=0,column=5,padx=2,pady=7)

        # Arrest Date
        lbl_arrestDate=Label(upper_frame,text='Arrest Date:',font=('arial',9,'bold'),bg='white')
        lbl_arrestDate.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=('arial',9,'bold'))
        txt_arrestDate.grid(row=1,column=5,padx=2,pady=7)

        # Gender
        lbl_gender=Label(upper_frame,text='Gender:',font=('arial',9,'bold'),bg='white')
        lbl_gender.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        # Radio Button for gender
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=603,y=75,width=134,height=30)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=("arial",9,"bold"),bg='white')
        male.grid(row=0,column=0,pady=0,padx=2,sticky=W)
        self.var_gender.set('Male')

        female=Radiobutton(radio_frame_gender,text='Female',value='female',font=("arial",9,"bold"),bg='white')
        female.grid(row=0,column=1,pady=0,padx=2,sticky=W)

        # Wanted
        lbl_wanted=Label(upper_frame,text='Most Wanted:',font=('arial',9,'bold'),bg='white')
        lbl_wanted.grid(row=3,column=4,sticky=W,padx=2,pady=7)

        # Radio Button for wanted
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=603,y=110,width=134,height=30)

        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=("arial",9,"bold"),bg='white')
        yes.grid(row=0,column=0,pady=0,padx=2,sticky=W)
        self.var_wanted.set('Yes')

        no=Radiobutton(radio_frame_wanted,text='No',value='no',font=("arial",9,"bold"),bg='white')
        no.grid(row=0,column=1,pady=0,padx=2,sticky=W)

        # Buttons
        button_frame=Frame(Main_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=15,y=193,width=514,height=42)

        # Add Button
        btn_add=Button(button_frame,command=self.add_data,text='Save Record',font=('arial',13,"bold"),width=11,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=3)

        # Update Button
        btn_update=Button(button_frame,command=self.update_data,text='Update',font=('arial',13,"bold"),width=11,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=3)

        # Delete Button
        btn_delete=Button(button_frame,text='Delete',font=('arial',13,"bold"),width=11,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=3)

        # Clear Button
        btn_clear=Button(button_frame,text='Clear',font=('arial',13,"bold"),width=11,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=3)
        
        # bg crime pic
        img_crime=Image.open('images/background.jpg')
        img_crime=img_crime.resize((455,200))
        self.photocrime=ImageTk.PhotoImage(img_crime)

        self.img_crime=Label(upper_frame,image=self.photocrime)
        self.img_crime.place(x=850,y=0,width=455,height=200)

        # DOWN-FRAME
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=250,width=1322,height=240)

        # SEARCH-FRAME
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Criminal Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=3,y=0,width=1312,height=60)
        
        search_by=Label(search_frame,text='Search By:',font=('arial',9,'bold'),bg='red',fg='white')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        combo_search_box=ttk.Combobox(search_frame, font=('arial',9,'bold'), width=18, state='readonly')
        combo_search_box['value']=('Select Option','Case ID','Criminal No')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)
        
        search_txt=ttk.Entry(search_frame,width=22,font=('arial',9,'bold'))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        # search Button
        btn_search=Button(search_frame,text='Search',font=('arial',13,"bold"),width=11,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,sticky=W,padx=5)

        # all Button
        btn_all=Button(search_frame,text='Show All',font=('arial',13,"bold"),width=11,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,sticky=W,padx=5)


        crimeagency=Label(search_frame,text='NATIONAL CRIME AGENCY:',font=('arial',18,'bold'),bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=20,)

        #table
        table_frame=Frame(down_frame,bd=2, relief=RIDGE)
        table_frame.place(x=3,y=60,width=1312,height=155)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.xview)
        

#        self.criminal_table.heading('1',text='Case ID')
#        self.criminal_table.heading('2',text='Crime No')
#        self.criminal_table.heading('3',text='Criminal Name')
#        self.criminal_table.heading('4',text='NickName')
#        self.criminal_table.heading('5',text='ArrestDate')
#        self.criminal_table.heading('6',text='CrimeOfDate')
#        self.criminal_table.heading('7',text='Address')
#        self.criminal_table.heading('8',text='Age')
#        self.criminal_table.heading('9',text='Occupation')
#        self.criminal_table.heading('10',text='Birth Mark')
#        self.criminal_table.heading('11',text='Crime Type')
#        self.criminal_table.heading('12',text='Father Name')
#        self.criminal_table.heading('13',text='Gender')
#        self.criminal_table.heading('14',text='Wanted')
#        self.criminal_table['show']='headings'
#        self.criminal_table.column('1',width=90)
#        self.criminal_table.column('2',width=90)
#        self.criminal_table.column('3',width=90)
#        self.criminal_table.column('4',width=90)
#        self.criminal_table.column('5',width=90)
#        self.criminal_table.column('6',width=90)
#        self.criminal_table.column('7',width=90)
#        self.criminal_table.column('8',width=90)
#        self.criminal_table.column('9',width=90)
#        self.criminal_table.column('10',width=90)
#        self.criminal_table.column('11',width=90)
#        self.criminal_table.column('12',width=90)
#        self.criminal_table.column('13',width=90)
#        self.criminal_table.column('14',width=90)
#        self.criminal_table.pack(fill=BOTH,expand=1)

        # The above steps done here using clean code and loop.
        headings = ['Case ID', 'Crime No', 'Criminal Name', 'NickName', 'ArrestDate', 'CrimeOfDate', 'Address', 'Age', 'Occupation', 'Birth Mark', 'Crime Type', 'Father Name', 'Gender', 'Wanted']
        for i, heading in enumerate(headings, start=1):
            self.criminal_table.heading(str(i), text=heading)


        self.criminal_table['show']='headings'
        for i in range(1, 15):
            self.criminal_table.column(str(i), width=90)

        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()
    #Add function
# Add function
    def add_data(self):
        if self.var_name.get() == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                # Print all variables for debugging
                print("Case ID:", self.var_case_id.get())
                print("Criminal No:", self.var_criminal_no.get())
                print("Name:", self.var_name.get())
                print("Nickname:", self.var_nickname.get())
                print("Arrest Date:", self.var_arrest_date.get())
                print("Date of Crime:", self.var_date_of_crime.get())
                print("Address:", self.var_address.get())
                print("Age:", self.var_age.get())
                print("Occupation:", self.var_occupation.get())
                print("Birth Mark:", self.var_birthMark.get())
                print("Crime Type:", self.var_crime_type.get())
                print("Father's Name:", self.var_father_name.get())
                print("Gender:", self.var_gender.get())
                print("Wanted:", self.var_wanted.get())

                conn = mysql.connector.connect(host='localhost', user='root', password='arsalan123', database='cms')
                if conn.is_connected():
                    print("Connected to the database.")
                else:
                    print("Failed to connect to the database.")

                my_cursor = conn.cursor()
                my_cursor.execute('INSERT INTO criminal1 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_case_id.get(),
                    self.var_criminal_no.get(),
                    self.var_name.get(),
                    self.var_nickname.get(),
                    self.var_arrest_date.get(),
                    self.var_date_of_crime.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_occupation.get(),
                    self.var_birthMark.get(),
                    self.var_crime_type.get(),
                    self.var_father_name.get(),
                    self.var_gender.get(),
                    self.var_wanted.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Criminal record has been added')
            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}')

    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='arsalan123', database='cms')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from criminal1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,even):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        #self.var_case_id.set(data[0])
        #self.var_criminal_no.set(data[1])
        #self.var_name.set(data[2])
        #self.var_nickname.set(data[3])
        #self.var_arrest_date.set(data[4])
        #self.var_date_of_crime.set(data[5])
        #self.var_address.set(data[6])
        #self.var_age.set(data[7])
        #self.var_occupation.set(data[8])
        #self.var_birthMark.set(data[9])
        #self.var_crime_type.set(data[10])
        #self.var_father_name.set(data[11])
        #self.var_gender.set(data[12])
        #self.var_wanted.set(data[13])

        variables = [
            self.var_case_id, self.var_criminal_no, self.var_name, self.var_nickname,
            self.var_arrest_date, self.var_date_of_crime, self.var_address, self.var_age,
            self.var_occupation, self.var_birthMark, self.var_crime_type, self.var_father_name,
            self.var_gender, self.var_wanted
        ]

        for i, variable in enumerate(variables):
            variable.set(data[i])

    def update_data(self):
        if self.var_name.get() == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure to update this criminal record')
                if update>0:
                    conn = mysql.connector.connect(host='localhost', user='root', password='arsalan123', database='cms')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update criminal1 set Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateOfcrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where Case_id=%s',(
                        self.var_criminal_no.get(),
                        self.var_name.get(),
                        self.var_nickname.get(),
                        self.var_arrest_date.get(),
                        self.var_date_of_crime.get(),
                        self.var_address.get(),
                        self.var_age.get(),
                        self.var_occupation.get(),
                        self.var_birthMark.get(),
                        self.var_crime_type.get(),
                        self.var_father_name.get(),
                        self.var_gender.get(),
                        self.var_wanted.get(),
                        self.var_case_id.get()
                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record successfully updated')    
            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}')

if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
