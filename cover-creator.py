from tkinter import *
import tkinter as tk
from datetime import date
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from django.conf import settings

x_pos= 20


root= tk.Tk()

root.title("Cover Letter Creator")
root.iconbitmap(r'icon.ico')

root.resizable(width= False, height=False)
root.geometry('800x600')


canvas1 = tk.Canvas(root, width = 400, height = 800,  relief = 'raised')
canvas1.pack()

#title
label1 = tk.Label(root, text='Cover Letter Creator')
label1.config(font=('helvetica', 16,'bold'))
canvas1.create_window(200, 15, window=label1)

x_start = 50 
#LABELS
#DATA 
label2 = tk.Label(root, justify=RIGHT  , text='Your Name: \n')
label2.config(font=('helvetica', 10,'bold'))
canvas1.create_window(0, 50, window=label2)
##
label3 = tk.Label(root, text='Company Name: \n')
label3.config(font=('helvetica', 10,'bold'))
canvas1.create_window(-10, 80, window=label3)
##
label4 = tk.Label(root, text='Company Address: \n')
label4.config(font=('helvetica', 10,'bold'))
canvas1.create_window(-17, 110, window=label4)
#
label5 = tk.Label(root, text='Cell phone:  \n')
label5.config(font=('helvetica', 10,'bold'))
canvas1.create_window(10, 140, window=label5)
##
label6 = tk.Label(root, text='Email:  \n')
label6.config(font=('helvetica', 10,'bold'))
canvas1.create_window(20, 140+30, window=label6)
##
label7 = tk.Label(root, text='LinkedIn URL:  \n')
label7.config(font=('helvetica', 10,'bold'))
canvas1.create_window(-4, 140+30+30, window=label7)
##
label8 = tk.Label(root, text='Hiring Manager:  \n')
label8.config(font=('helvetica', 10,'bold'))
canvas1.create_window(-10, 140+90, window=label8)
##
label9 = tk.Label(root, text='Target Role:  \n')
label9.config(font=('helvetica', 10,'bold'))
canvas1.create_window(5, 140+90+30, window=label9)
##
label10 = tk.Label(root, text='You Hear about us from:  \n')
label10.config(font=('helvetica', 10,'bold'))
canvas1.create_window(-40, 140+90+60, window=label10)
##
label11 = tk.Label(root, text='Field you apply in:  \n')
label11.config(font=('helvetica', 10,'bold'))
canvas1.create_window(-20, 140+90+90, window=label11)
##
label12 = tk.Label(root, text='Technical Skills :  \n')
label12.config(font=('helvetica', 10,'bold'))
canvas1.create_window(-10, 140+180+30, window=label12)
##
label13 = tk.Label(root, text='Soft Skills :   \n')
label13.config(font=('helvetica', 10,'bold'))
canvas1.create_window(5, 140+180+60, window=label13)
##
label14 = tk.Label(root, text='Education Degree:   \n')
label14.config(font=('helvetica', 10,'bold'))
canvas1.create_window(-15, 140+180+90, window=label14)
##
label15 = tk.Label(root, text='Certification:   \n')
label15.config(font=('helvetica', 10,'bold'))
canvas1.create_window(0,440, window=label15)
##
label16 = tk.Label(root, text='Languages:   \n')
label16.config(font=('helvetica', 10,'bold'))
canvas1.create_window(5, 440+30, window=label16)

#ENTRY
entry0 = tk.Entry (root) 
canvas1.create_window(200, 45, window=entry0, width=300)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 70, window=entry1, width=300)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 100, window=entry2, width=300)

entry3 = tk.Entry (root) 
canvas1.create_window(200, 130, window=entry3, width=300)

entry4 = tk.Entry (root) 
canvas1.create_window(200, 160, window=entry4, width=300)

entry5 = tk.Entry (root) 
canvas1.create_window(200, 190, window=entry5, width=300)

entry6 = tk.Entry (root) 
canvas1.create_window(200, 220, window=entry6, width=300)

entry7 = tk.Entry (root) 
canvas1.create_window(200, 250, window=entry7, width=300)

entry8 = tk.Entry (root) 
canvas1.create_window(200, 280, window=entry8, width=300)

entry9 = tk.Entry (root) 
canvas1.create_window(200, 310, window=entry9, width=300)

entry10 = tk.Entry (root) 
canvas1.create_window(200, 340, window=entry10, width=300)

entry11 = tk.Entry (root) 
canvas1.create_window(200, 370, window=entry11, width=300)

entry12 = tk.Entry (root) 
canvas1.create_window(200, 400, window=entry12, width=300)

entry13= tk.Entry (root) 
canvas1.create_window(200, 430, window=entry13, width=300)

entry14 = tk.Entry (root) 
canvas1.create_window(200, 460, window=entry14, width=300)





def getData ():
    x0 = entry0.get()    
    x1 = entry1.get()
    x2 = entry2.get()
    x3 = entry3.get()
    x4 = entry4.get()
    x5 = entry5.get()
    x6 = entry6.get()
    x7 = entry7.get()
    x8 = entry8.get()
    x9 = entry9.get()
    x10 = entry10.get()
    x11 = entry11.get()
    x12 = entry12.get()
    x13 = entry13.get()
    x14 = entry14.get()
    # print(x0,x1,x2,x3)

    Name = x0
    fileName = str(Name)+str("-CoverLetter.pdf")
    documentTitle = "coverLetter"

    #upper data
    todays_date = str(date.today())
    company_name = x1
    address = x2

    #lower data

    Cell = x3
    Email = x4
    LinkedIn_URL = x5


    #letter data
    Hiring_manager = x6
    if Hiring_manager == "":
        Hiring_manager="Hiring Manager"
    Target_Role = x7
    Site = x8
    if Site == "":
        Site ="Site"

    Job_title = Target_Role
    Industry = x9
    Hard_Skills =x10 
    Soft_Skills = x11
    University_degree  =x12
    Certification = x13
    Languages = x14
    textLines = ['Dear '+ str(Hiring_manager)+",",
    'I am writing regarding your present job opening of '+str(Target_Role)+' as',
    'advertised on '+str(Site)+'.'+ " As a candidate with extensive experience in ",
    str(Industry)+' field and have perivous experience being '+str(Job_title)+".",
    'I am highly skilled in ' + str(Hard_Skills)+ '. ',
    'I am also good in '+str(Soft_Skills) ,
    'My skills has allowed me to build, lead, and work with teams with exceptional',
    'performance.',
    '',
    'The opportunity to join '+str(company_name)+' greatly interests me because',
    "of company culture, possibility to grow with the company, a chance  ",
    'to make a positive impact new challenges.',
    'As a holder of '+str(University_degree)+", ",
    'Im also certified in '+str(Certification)+".",
    "I can competently execute the job responsibilities",
    'therefore, that I would make a valuable asset to your',
    ' team and I hereby offer my resume for your review.',
    '',
    'As my professional summary shows, my qualities, experience ',
    'make me highly suitable for the role of '+str(Job_title)+" in your ",
    "organization. I am regarded for "+str(Hard_Skills)+".",
    'I am also fluent and proficient in '+str(Languages)+".",
    '',
    'Throughout my career, I have always demonstrated the highest levels',
    'of service and commitment to the mission of any organization ',
    'I have worked for.',
    '',
    'Thus, if you are looking for an organized',
    'you are welcome to contact me to arrange an interview. I am eager to',
    'learn more about how your organization can benefit from my ',
    'contribution. I thank you in advance for your time and consideration.',
    'I look forward to hearing from you at your earliest convenience.',
    '',
    '',
    'Best regards,'
    ] 

    # Create document 
    pdf = canvas.Canvas(fileName)
    #font
    # pdfmetrics.registerFont(
    #     TTFont('abc', 'SakBunderan.ttf')
    # )
    # pdf.setFont('abc', 16)

    # Upper Data
    #Date
    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Courier-Bold", 16)
    pdf.drawString(x_pos, 800, todays_date)
    #company name
    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Courier-Bold", 16)
    pdf.drawString(x_pos,780, company_name)
    #Address
    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Courier-Bold", 16)
    pdf.drawString(x_pos,760, address)

    # text data 
    text = pdf.beginText(10, 720)
    text.setTextOrigin(20,720)

    text.setFont("Helvetica", 14)
    text.setFillColor(colors.black)
    for line in textLines:
        text.textLine(line)

    # Lower data
    #name 
    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Courier-Bold", 16)
    pdf.drawString(20,80, Name)
    # mobile number
    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Courier-Bold", 16)
    pdf.drawString(20,65, Cell)
    # email-address 
    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Courier-Bold", 16)
    pdf.drawString(20,50, Email)
    # Linkedin account 
    pdf.setFillColorRGB(0, 0, 0)
    pdf.setFont("Courier-Bold", 16)
    pdf.drawString(20,35, LinkedIn_URL)

    pdf.drawText(text)
    pdf.save()
    # print("File saved")
    label00 = tk.Label(root, text= "File Saved",font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 500, window=label00)




 
def clearData():
	# print("Cleared")
	entry0.delete(0,'end')
	entry1.delete(0,'end')
	entry2.delete(0,'end')
	entry3.delete(0,'end')
	entry4.delete(0,'end')
	entry5.delete(0,'end')
	entry6.delete(0,'end')
	entry7.delete(0,'end')
	entry8.delete(0,'end')
	entry9.delete(0,'end')
	entry10.delete(0,'end')
	entry11.delete(0,'end')
	entry12.delete(0,'end')
	entry13.delete(0,'end')
	entry14.delete(0,'end')


button1 = tk.Button(text='SAVE', command=getData, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 550, window=button1)

button2 = tk.Button(text='CLEAR', command=clearData, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(260, 550, window=button2)

# print(getData())

# label_create()
# entry_create()




root.mainloop()