import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
import datetime
import qrcode

from data import *
from fonts_app import *
 
    
root = tk.Tk()
root.iconbitmap('Img/Logo2.ico')
root.title('Bestellen Tickets "Pythonland"')
root.configure(bg='#d4e783')
root.geometry('1200x900+300+5')
root.resizable(False, False)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
frame5 = tk.Frame(root)
frame6 = tk.Frame(root)
frame7 = tk.Frame(root)
frame8 = tk.Frame(root)
frame9 = tk.Frame(root)

# Input variables for E-ticket
time_now = datetime.datetime.now()
ticketnumber = 0

# Input variables for use checkboxes
var_parking = IntVar()
var_restaurant = IntVar()
var_theatre = IntVar()
var_facepaint = IntVar()
var_confirmation = IntVar()

#======================================== IMAGES ========================================

logo1 = ImageTk.PhotoImage(Image.open('Img/logo1.jpg'))
logo2 = ImageTk.PhotoImage(Image.open('Img/Logo_wit.jpg'))
image_pythonland = ImageTk.PhotoImage(Image.open('Img/Snake.jpg'))

image_tickets = ImageTk.PhotoImage(Image.open('Img/Tickets1.jpg'))
image_parking = ImageTk.PhotoImage(Image.open('Img/Parkeren1.jpg'))
image_restaurant = ImageTk.PhotoImage(Image.open('Img/Restaurant1.jpg'))
image_theatre = ImageTk.PhotoImage(Image.open('Img/Theater1.jpg'))
image_facepaint = ImageTk.PhotoImage(Image.open('Img/Schmink1.jpg'))
image_ice = ImageTk.PhotoImage(Image.open('Img/IJs1.jpg'))

progress_tickets = ImageTk.PhotoImage(Image.open('Img/Tickets2.jpg'))
progress_parking = ImageTk.PhotoImage(Image.open('Img/Parkeren2.jpg'))
progress_restaurant = ImageTk.PhotoImage(Image.open('Img/Restaurant2.jpg'))
progress_theatre = ImageTk.PhotoImage(Image.open('Img/Theater2.jpg'))
progress_facepaint = ImageTk.PhotoImage(Image.open('Img/Schmink2.jpg'))
progress_ice = ImageTk.PhotoImage(Image.open('Img/IJs2.jpg'))

arrow_left = ImageTk.PhotoImage(Image.open('Img/Pijl1.jpg'))
arrow_right = ImageTk.PhotoImage(Image.open('Img/Pijl2.jpg')) 
                                   
#=================================== STANDARD FORMAT ====================================
                                      
for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7):
    frame.configure(bg='#d4e783')
    frame.grid(row=0,column=0,sticky='nsew')  

#Logo
for frame in (frame2, frame3, frame4, frame5, frame6, frame7):
    Frame_logo = Label(frame, image=logo1, borderwidth=0)
    Frame_logo.place(x=980, y=-5) 

#Title receipt
    receipt_title = Label(frame, text= "Kassabon", font= font_title3, 
                     bg= font_title3_bg, fg= font_title3_color)
    receipt_title.place(x=910, y=178)

# Images progressbar
for frame in (frame2, frame3, frame4, frame5, frame6, frame7):
    Progress_image1 = Label(frame, image=progress_tickets, borderwidth=0)
    Progress_image2 = Label(frame, image=progress_parking, borderwidth=0)
    Progress_image3 = Label(frame, image=progress_restaurant, borderwidth=0)
    Progress_image4 = Label(frame, image=progress_theatre, borderwidth=0)
    Progress_image5 = Label(frame, image=progress_facepaint, borderwidth=0)
    Progress_image6 = Label(frame, image=progress_ice, borderwidth=0)

    Progress_image1.place(x=300, y=760)
    Progress_image2.place(x=400, y=760)
    Progress_image3.place(x=500, y=760)
    Progress_image4.place(x=600, y=760)
    Progress_image5.place(x=700, y=760)
    Progress_image6.place(x=800, y=760)

#================================== GENERAL FUNCTIONS ==================================
                                    
# Function to change frame
                                 
def show_frame(frame):
    frame.tkraise()

# Function to calculate total price

def calculate_total():

    global total_price

    total_price = (total_entrance - total_benefit + total_parking 
    + total_restaurant + total_theatre + total_facepaint  + total_donation)
                   
# Function to keep receipt up to date by a frame change

def update_receipt(visitorlist, pricelist):

    parking_no = "Totaal parkeren     nee"
    parking_yes = "Totaal parkeren     ja"
    restaurant_no = "Totaal restaurant   nee"
    restaurant_yes = "Totaal restaurant   ja"
    theatre_no = "Totaal theater      nee"
    theatre_yes = "Totaal theater      ja"
    facepaint_no = "Totaal schminken    nee"
    facepaint_yes = "Totaal schminken    ja"
    confirmation_no = "Totaal donatie      nee"
    confirmation_yes = "Totaal donatie      ja"

    visitorlist.delete(0, END)
    visitorlist.insert(END, 'Totaal kleinkind    ' + str(number_toddle) + 'x') 
    visitorlist.insert(END, 'Totaal kind         ' + str(number_child) + 'x')
    visitorlist.insert(END, 'Totaal volwassenen  ' + str(number_adult) + 'x')
    visitorlist.insert(END, 'Totaal senior       ' + str(number_senior) + 'x')
    visitorlist.insert(END, '' + '\n')
    visitorlist.insert(END, 'Totaal entree')
    visitorlist.insert(END, '' + '\n')
    visitorlist.insert(END, 'Totaal korting')
    visitorlist.insert(END, '' + '\n')

    if number_car == 0:
        visitorlist.insert(END, parking_no)
        visitorlist.insert(END, '' + '\n')

    if number_car !=0:
        visitorlist.insert(END, parking_yes)
        visitorlist.insert(END, '' + '\n')
    
    if var_restaurant.get() == 0:
        visitorlist.insert(END, restaurant_no)
        visitorlist.insert(END, '' + '\n')

    if var_restaurant.get() == 1:
        visitorlist.insert(END, restaurant_yes)
        visitorlist.insert(END, '' + '\n')
    
    if var_theatre.get() == 0:
        visitorlist.insert(END, theatre_no)
        visitorlist.insert(END, '' + '\n')

    if var_theatre.get() == 1:
        visitorlist.insert(END, theatre_yes)
        visitorlist.insert(END, '' + '\n')
    
    if number_facepaint == 0:
        visitorlist.insert(END, facepaint_no)
        visitorlist.insert(END, '' + '\n')

    if number_facepaint != 0:
        visitorlist.insert(END, facepaint_yes)
        visitorlist.insert(END, '' + '\n')
    
    if var_confirmation.get() == 0:
        visitorlist.insert(END, confirmation_no)
        visitorlist.insert(END, '' + '\n')
        visitorlist.insert(END, '' + '\n')

    if var_confirmation.get() == 1:
        visitorlist.insert(END, confirmation_yes)
        visitorlist.insert(END, '' + '\n')
        visitorlist.insert(END, '' + '\n')
    
    
    visitorlist.insert(END, 'Totaal prijs')

    pricelist.delete(0, END)
    pricelist.insert(END, "\N{euro sign} {:.2f}".format(total_toddle))
    pricelist.insert(END, "\N{euro sign} {:.2f}".format(total_child))
    pricelist.insert(END, "\N{euro sign} {:.2f}".format(total_adult))
    pricelist.insert(END, "\N{euro sign} {:.2f}".format(total_senior))
    pricelist.insert(END, '' + '\n')
    pricelist.insert(END, "\N{euro sign} {:.2f}".format(total_entrance))
    pricelist.insert(END, '' + '\n')
    pricelist.insert(END,"- " "\N{euro sign} {:.2f}".format(total_benefit))
    pricelist.insert(END, '' + '\n')
    pricelist.insert(END, "\N{euro sign} {:.2f}".format(total_parking))
    pricelist.insert(END, '' + '\n')
    pricelist.insert(END, "\N{euro sign} {:.2f}".format(total_restaurant))
    pricelist.insert(END, '' + '\n')
    pricelist.insert(END, "\N{euro sign} {:.2f}".format(total_theatre))
    pricelist.insert(END, '' + '\n')
    pricelist.insert(END, "\N{euro sign} {:.2f}".format(total_facepaint))
    pricelist.insert(END, '' + '\n')
    pricelist.insert(END, "\N{euro sign} {:.2f}".format(total_donation))
    pricelist.insert(END, '' + '\n')
    pricelist.insert(END, '' + '\n')
    pricelist.insert(END, "\N{euro sign} {:.2f}".format(total_price))

# Functie for filling in data E-ticket

def eticket():

    ticket_name2.config(text=name_visitor.title())
    ticket_number2.config(text="%05d"%ticketnumber)

    ticket_toddle2.config(text=str(number_toddle) + " x")
    ticket_child2.config(text=str(number_child) + " x")
    ticket_adult2.config(text=str(number_adult) + " x")
    ticket_senior2.config(text=str(number_senior) + " x")
    ticket_discount2.config(text=str(total_discount) + " x") 

    ticket_toddle3.config(text='\N{euro sign} '+
                                 "{:.2f}".format(total_toddle).replace(".", ","))
    ticket_child3.config(text='\N{euro sign} '+
                            "{:.2f}".format(total_child).replace(".", ","))
    ticket_adult3.config(text='\N{euro sign} '+
                                  "{:.2f}".format(total_adult).replace(".", ","))
    ticket_senior3.config(text='\N{euro sign} '+
                              "{:.2f}".format(total_senior).replace(".", ","))
    ticket_discount3.config(text='-  \N{euro sign} '+
                               "{:.2f}".format(total_benefit).replace(".", ","))
    ticket_entrance3.config(text='\N{euro sign} '+
                              "{:.2f}".format(total_entrance-total_benefit).replace(".", ","))
    ticket_arrangement5.config(text='\N{euro sign} '+
                                  "{:.2f}".format(total_price-(total_entrance-total_benefit)).replace(".", ","))
    ticket_total5.config(text='\N{euro sign} '+
                              "{:.2f}".format(total_price).replace(".", ","))

    if number_car > 0:
        ticket_parking2.config(text="Ja")
        ticket_parking3.config(text="Aantal auto's")
        ticket_parking4.config(text=str(number_car))

    else:
        ticket_parking2.config(text="nee")
        ticket_parking3.config(text= '')
        ticket_parking4.config(text= '')
        
    if var_restaurant.get() == 1:
        ticket_restaurant2.config(text="Ja")
        ticket_restaurant3.config(text="Aantal personen")
        ticket_restaurant4.config(text=str(number_visitors))

    else:
        ticket_restaurant2.config(text="nee")
        ticket_restaurant3.config(text="")
        ticket_restaurant4.config(text="")

    if var_theatre.get() == 1:
        ticket_theatre2.config(text="Ja")
        ticket_theatre3.config(text="Aantal personen")
        ticket_theatre4.config(text=str(number_visitors))
        ticket_time_theatre2.config(text=str(time_theatre))

    else:
        ticket_theatre2.config(text="nee")
        ticket_theatre3.config(text="")
        ticket_theatre4.config(text="")
        ticket_time_theatre2.config(text="geen")
        
    if number_facepaint > 0:
        ticket_facepaint2.config(text="Ja")
        ticket_facepaint3.config(text="Aantal personen")
        ticket_facepaint4.config(text=str(number_facepaint))

    else:
        ticket_facepaint2.config(text="nee")
        ticket_facepaint3.config(text="")
        ticket_facepaint4.config(text="")
        
    if var_confirmation.get() == 1:
        ticket_donation2.config(text="Ja")
        ticket_donation3.config(text="Aantal personen")
        ticket_donation4.config(text=str(number_visitors))
         
    else:
        ticket_donation2.config(text="nee")
        ticket_donation3.config(text="")
        ticket_donation4.config(text="")
    
    ticket_parking5.config(text='\N{euro sign} '+
                            "{:.2f}".format(total_parking).replace(".", ","))
    ticket_restaurant5.config(text='\N{euro sign} '+
                              "{:.2f}".format(total_restaurant).replace(".", ","))
    ticket_theatre5.config(text='\N{euro sign} '+
                             "{:.2f}".format(total_theatre).replace(".", ","))
    ticket_facepaint5.config(text='\N{euro sign} '+
                             "{:.2f}".format(total_facepaint).replace(".", ","))
    ticket_donation5.config(text='\N{euro sign} '+
                           "{:.2f}".format(total_donation).replace(".", ","))

# Function to build qrcode

def build_code():

    global ticket_QRcode
    global qr_parking
    global qr_restaurant
    global qr_theatre
    global qr_facepaint
    global qr_donation

    if number_car > 0:
        qr_parking = 'Parkeren Dagtarief: ja  ' + str(number_car) + ' x'

    else:
        qr_parking = 'Parkeren Dagtarief: nee'
        
    if var_restaurant.get() == 1:
        qr_restaurant = 'Restaurant: ja  ' + str(number_visitors) + ' x'

    else:
        qr_restaurant = 'Restaurant: nee'

    if var_theatre.get() == 1:
        qr_theatre = '3D-Theater: ja  '  + str(number_visitors) + ' x'  

    else:
        qr_theatre = '3D-Theater: nee'

        
    if number_facepaint > 0:
        qr_facepaint = 'Schminken: ja  '  + str(number_facepaint) + ' x'  

    else:
        qr_facepaint= 'Schminken: nee'
        
    if var_confirmation.get() == 1:
        qr_donation = 'Donatie gratis ijsje: ja  '  + str(number_visitors) + ' x'  

    else:
        qr_donation = 'Donatie gratis ijsje: nee'
    
    qr = qrcode.make('Entree \n \n'
                         'Aantal kleinkind: ' + str(number_toddle) + '\n'
                         'Aantal kind: ' + str(number_child) + '\n'
                         'Aantal volwassenen: ' + str(number_adult) + '\n'
                         'Aantal senioren: ' + str(number_senior) + '\n' + '\n'
                         'Totaal: ' + str(number_visitors) + '\n' + '\n'
                         'Arrangement \n \n'
                         + qr_parking + '\n'
                         + qr_restaurant + '\n'
                         + qr_theatre + '\n'
                         + qr_facepaint + '\n'
                         + qr_donation+ '\n' + '\n'
                         'Tijd 3D-theater: '+ time_theatre)
                            
                        
    qr.save('Qr/Qr'+ str("%05d"%ticketnumber) + '.png')

    img = Image.open('Qr/Qr'+ str("%05d"%ticketnumber) + '.png')

    resized = img.resize((250, 250), Image.ANTIALIAS)

    QRcode_update1 = ImageTk.PhotoImage(resized) 

    ticket_QRcode.config(image=QRcode_update1)
    ticket_QRcode.photo_ref = QRcode_update1

#=================================== FRAME1 WELCOME =====================================

frame1_title = tk.Label(frame1, text='Welkom in Pythonland', font=font_title1, 
                        bg=font_title1_bg, fg=font_title1_color)
frame1_title.place(x=18, y=40)

frame1_image = Label(frame1, image=image_pythonland, borderwidth=0)
frame1_image.place(x=500, y=200)

#==================================== FRAME2 TICKETS ====================================

frame2_title = tk.Label(frame2, text='Tickets', font=font_title1, bg=font_title1_bg, 
                        fg=font_title1_color)
frame2_title.place(x=40, y=30)

frame2_image = Label(frame2, image=image_tickets, borderwidth=0)
frame2_image.place(x=860, y=30)

progressbar2 = ttk.Progressbar(frame2, orient=HORIZONTAL, value=16.67, length=600, 
                               mode='determinate')
progressbar2.place(x=285, y=860)

# Labels for description age groups visitors + age limits
description_toddle = Label(frame2, text='- Kleine kinderen jonger dan ' + 
                         str(LIMIT_TODDLE) + ' jaar:', font=font1, bg=font1_bg, 
                         fg=font1_color)
description_child = Label(frame2, text='- Kinderen vanaf ' + str(LIMIT_TODDLE) + 
                    ' jaar t/m ' + str(LIMIT_CHILD) + ' jaar:', font=font1, bg=font1_bg, 
                    fg=font1_color)
description_adult = Label(frame2, text='- Volwassenen vanaf ' + str(LIMIT_CHILD) +
                          ' t/m ' + str(LIMIT_ADULT) + ' jaar:', font=font1, 
                          bg=font1_bg, fg=font1_color)
description_senior = Label(frame2, text='- Senioren vanaf ' + str(LIMIT_ADULT) +
                      ' jaar en ouder:', font=font1, bg=font1_bg, fg=font1_color)
description_discount = Label(frame2, text='- Korting per ' + str(LIMIT_DISCOUNT) +
                       'e betalende bezoeker:', font=font2, bg=font2_bg, 
                       fg=font2_color)

description_toddle.place(x=10, y=238)
description_child.place(x=10, y=338)
description_adult.place(x=10, y=438)
description_senior.place(x=10, y=538)
description_discount.place(x=10, y=638)

# Labels for entrance fees and visitor age groups
entrance_toddle = Label(frame2, text='\N{euro sign} '+
                         "{:.2f}".format(PRICE_TODDLE).replace(".", ","),
                         font=font2, bg=font2_bg, fg=font2_color)
entrance_child = Label(frame2, text='\N{euro sign} '+
                    "{:.2f}".format(PRICE_CHILD).replace(".", ","), 
                    font=font2, bg=font2_bg, fg=font2_color)
entrance_adult = Label(frame2, text='\N{euro sign} '+
                          "{:.2f}".format(PRICE_ADULT).replace(".", ","),
                          font=font2, bg=font2_bg, fg=font2_color)
entrance_senior = Label(frame2, text='\N{euro sign} '+
                      "{:.2f}".format(PRICE_SENIOR).replace(".", ","), 
                      font=font2, bg=font2_bg, fg=font2_color)
entrance_discount = Label(frame2, text='\N{euro sign} '+
                       "{:.2f}".format(PRICE_DISCOUNT).replace(".", ","),
                       font=font2, bg=font2_bg, fg=font2_color)

entrance_toddle.place(x=500, y=240)
entrance_child.place(x=500, y=340)
entrance_adult.place(x=500, y=440)
entrance_senior.place(x=500, y=540)
entrance_discount.place(x=500, y=640)

# Labels for entering visitor numbers by age group
input_toddle = Listbox(frame2, width=3, height=1, font=font3, justify='center')
input_toddle.insert(END, number_toddle)
input_child = Listbox(frame2, width=3, height=1, font=font3, justify='center')
input_child.insert(END, number_child)
input_adult = Listbox(frame2, width=3, height=1, font=font3, justify='center')
input_adult.insert(END, number_adult)
input_senior = Listbox(frame2, width=3, height=1, font=font3, justify='center')
input_senior.insert(END, number_senior)
input_discount = Listbox(frame2, width=3, height=1, font=font3, justify='center')
input_discount.insert(END, 0)

input_toddle.place(x=696, y=238)
input_child.place(x=696, y=338)
input_adult.place(x=696, y=438)
input_senior.place(x=696, y=538)
input_discount.place(x=696, y=638)

#Labels receipt
visitorlist_2 = Listbox(frame2, font=font_checkout1, width=27, height=23)
visitorlist_2.place(x=860, y=230)

pricelist_2 = Listbox(frame2, font=font_checkout2, width=15, height=23, justify='right')
pricelist_2.place(x=1050, y=230)

update_receipt(visitorlist_2, pricelist_2)
    
# Function to calculate costs tickets

def calculate_entrance():

    global total_entrance

    global number_toddle
    global number_child
    global number_adult
    global number_senior
    global number_visitors

    number_visitors = (number_toddle + number_child + number_adult 
                       + number_senior)

    total_entrance = (total_toddle + total_child + total_adult 
                    + total_senior)

    if number_visitors == 25:
        messagebox.showerror("Maximaal aantal bezoekers ",
                                    "Voor groepen groter dan 25 personen vragen wij u "
                                    "zich te melden bij één van onze kassa's")
        toddle_plus.configure(state=DISABLED)
        child_plus.configure(state=DISABLED)
        adult_plus.configure(state=DISABLED)
        senior_plus.configure(state=DISABLED)

    else:
        toddle_plus.configure(state=NORMAL)
        child_plus.configure(state=NORMAL)
        adult_plus.configure(state=NORMAL)
        senior_plus.configure(state=NORMAL)

# Function to calculate discount

def calculate_discount():

    global total_discount
    global total_benefit

    if PRICE_TODDLE == 0:

        total_discount = (number_child + number_adult + number_senior) // 5
        total_benefit = total_discount * PRICE_DISCOUNT

        input_discount.delete(0,END)
        input_discount.insert(END, total_discount)
    
    else:

        total_discount = (number_toddle + number_child + number_adult + number_senior) // 5
        total_benefit = total_discount * PRICE_DISCOUNT

        input_discount.delete(0,END)
        input_discount.insert(END, total_discount)

# Functions for adding and removing visitors per button

def toddle_up():
    global number_toddle
    number_toddle = number_toddle + 1
    input_toddle.delete(0, END)
    input_toddle.insert(END, number_toddle)

    global total_toddle
    total_toddle = number_toddle * PRICE_TODDLE

    calculate_entrance()
    calculate_discount()
    calculate_total()

    update_receipt(visitorlist_2, pricelist_2)
    update_receipt(visitorlist_2, pricelist_2)

    input_discount.delete(0,END)
    input_discount.insert(END, total_discount)

def toddle_down():
    global number_toddle
    number_toddle = number_toddle - 1
    if number_toddle < 0: 
        number_toddle = 0
    input_toddle.delete(0, END)
    input_toddle.insert(END, number_toddle)

    global total_toddle
    total_toddle = number_toddle * PRICE_TODDLE

    calculate_entrance()
    calculate_discount()
    calculate_total()

    update_receipt(visitorlist_2, pricelist_2)
    update_receipt(visitorlist_2, pricelist_2)
    

def child_up():
    global number_child
    number_child = number_child + 1
    input_child.delete(0, END)
    input_child.insert(END, number_child)

    global total_child
    total_child = number_child * PRICE_CHILD
    
    calculate_entrance()
    calculate_discount()
    calculate_total()

    update_receipt(visitorlist_2, pricelist_2)
    update_receipt(visitorlist_2, pricelist_2)


def child_down():
    global number_child
    number_child = number_child - 1
    if number_child < 0: 
        number_child = 0
    input_child.delete(0, END)
    input_child.insert(END, number_child)

    global total_child
    total_child = number_child * PRICE_CHILD

    calculate_entrance()
    calculate_discount()
    calculate_total()
    
    update_receipt(visitorlist_2, pricelist_2)
    update_receipt(visitorlist_2, pricelist_2)


def adult_up():
    global number_adult
    number_adult = number_adult + 1
    input_adult.delete(0, END)
    input_adult.insert(END, number_adult)

    global total_adult
    total_adult = number_adult * PRICE_ADULT

    calculate_entrance()
    calculate_discount()
    calculate_total()

    update_receipt(visitorlist_2, pricelist_2)
    update_receipt(visitorlist_2, pricelist_2)


def adult_down():
    global number_adult
    number_adult = number_adult - 1
    if number_adult < 0: 
        number_adult = 0
    input_adult.delete(0, END)
    input_adult.insert(END, number_adult)

    global total_adult
    total_adult = number_adult * PRICE_ADULT

    calculate_entrance()
    calculate_discount()
    calculate_total()

    update_receipt(visitorlist_2, pricelist_2)
    update_receipt(visitorlist_2, pricelist_2)


def senior_up():
    global number_senior
    number_senior = number_senior + 1
    input_senior.delete(0, END)
    input_senior.insert(END, number_senior)

    global total_senior
    total_senior = number_senior * PRICE_SENIOR

    calculate_entrance()
    calculate_discount()
    calculate_total()

    update_receipt(visitorlist_2, pricelist_2)
    update_receipt(visitorlist_2, pricelist_2)


def senior_down():
    global number_senior
    number_senior = number_senior - 1
    if number_senior < 0: 
        number_senior = 0
    input_senior.delete(0, END)
    input_senior.insert(END, number_senior)

    global total_senior
    total_senior = number_senior * PRICE_SENIOR

    calculate_entrance()
    calculate_discount()
    calculate_total()

    update_receipt(visitorlist_2, pricelist_2)
    update_receipt(visitorlist_2, pricelist_2)

# Buttons for visitors input
toddle_min = tk.Button(frame2, image = arrow_left, borderwidth=0, 
                command=toddle_down)
toddle_plus = tk.Button(frame2, image = arrow_right, borderwidth=0, 
                 command=toddle_up)
child_min = tk.Button(frame2, image = arrow_left, borderwidth=0, 
           command=child_down)
child_plus = tk.Button(frame2, image = arrow_right, borderwidth=0, 
            command=child_up)
adult_min = tk.Button(frame2, image = arrow_left, borderwidth=0, 
                 command=adult_down)
adult_plus = tk.Button(frame2, image = arrow_right, borderwidth=0, 
                  command=adult_up)
senior_min = tk.Button(frame2, image = arrow_left, borderwidth=0, 
             command=senior_down)
senior_plus = tk.Button(frame2, image = arrow_right, borderwidth=0, 
              command=senior_up)

toddle_min.place(x=620, y=230)
toddle_plus.place(x=770, y=230)
child_min.place(x=620, y=330)
child_plus.place(x=770, y=330)
adult_min.place(x=620, y=430)
adult_plus.place(x=770, y=430)
senior_min.place(x=620, y=530)
senior_plus.place(x=770, y=530)

#=================================== FRAME3 PARKING =====================================
                                            
frame3_title = tk.Label(frame3, text='Parkeren', font=font_title1, bg=font_title1_bg, 
                        fg=font_title1_color)
frame3_title.place(x=40, y=30)

frame3_image = Label(frame3, image=image_parking, borderwidth=0)
frame3_image.place(x=860, y=30)

progressbar3 = ttk.Progressbar(frame3, orient=HORIZONTAL, value=33.33, length=600, 
                               mode='determinate')
progressbar3.place(x=285, y=860)

#Labels voor beschrijving dagtarief + uurtarief
daily_rate_1 = Label(frame3, text='Voor het gebruik van ons parkeerterrein bieden we',
                   font=font1, bg=font1_bg, fg=font1_color)
daily_rate_2 = Label(frame3, text='nu eenmalig een dagtarief aan van:',
                   font=font1, bg=font1_bg, fg=font1_color)
hourly_rate_1 = Label(frame3, text='Indien u hier geen gebruik van wilt maken kunt',
                   font=font1, bg=font1_bg, fg=font1_color)
hourly_rate_2 = Label(frame3, text='u ook met uw parkeerticket betalen bij de',
                   font=font1, bg=font1_bg, fg=font1_color)
hourly_rate_3 = Label(frame3, text='parkeerautomaat. Dan betaalt u per uur:',
                   font=font1, bg=font1_bg, fg=font1_color)

daily_rate_1.place(x=20, y=238)
daily_rate_2.place(x=20, y=288)
hourly_rate_1.place(x=20, y=338)
hourly_rate_2.place(x=20, y=438)
hourly_rate_3.place(x=20, y=488)

# Labels for prices daily rate + hourly rate
price_daily_rate = Label(frame3, text='\N{euro sign} '+
                        "{:.2f}".format(CAR_DAILY_RATE).replace(".", ","),
                        font=font2, bg=font2_bg, fg=font2_color)
price_houry_rate = Label(frame3, text='\N{euro sign} '+
                        "{:.2f}".format(CAR_HOURLY_RATE).replace(".", ","),
                        font=font2, bg=font2_bg, fg=font2_color)

price_daily_rate.place(x=695, y=288)
price_houry_rate.place(x=695, y=488)

# Labels to conform daily rate
confirm_daily_1 = Label(frame3, text='Ja wij willen gebruik maken van het dag-',
                                font=font2, bg=font2_bg, fg=font2_color)
confirm_daily_2 = Label(frame3, text="tarief met het volgend aantal auto's",
                                font=font2, bg=font2_bg, fg=font2_color)

confirm_daily_1.place(x=60, y=598)
confirm_daily_2.place(x=60, y=648)

#Label input cars
input_car = Listbox(frame3, width=3, height=1,  font=font3, justify='center')
input_car.insert(END, number_car)
input_car.configure(state=DISABLED)
input_car.place(x=715, y=620)

#Labels for receipt
visitorlist_3 = Listbox(frame3, font=font_checkout1, width=27, height=23)
visitorlist_3.place(x=860, y=230)

pricelist_3 = Listbox(frame3, font=font_checkout2, width=15, height=23, justify='right')
pricelist_3.place(x=1050, y=230)

update_receipt(visitorlist_3, pricelist_3)

# Function to calculate use daily rate

def calculate_parking():

    global total_parking
    global number_car

    if var_parking.get() == 1:

        input_car.configure(state=NORMAL)
        car_min.configure(state=NORMAL)
        car_plus.configure(state=NORMAL)
        input_car.delete(0, END)
        input_car.insert(END, number_car)

        total_parking = number_car * CAR_DAILY_RATE

    elif var_parking.get() == 0:

        number_car = 0
        total_parking = 0

        input_car.delete(0, END)
        input_car.insert(END, number_car)

        input_car.configure(state=DISABLED)
        car_min.configure(state=DISABLED)
        car_plus.configure(state=DISABLED)

        calculate_total()
        update_receipt(visitorlist_3, pricelist_3)
        update_receipt(visitorlist_3, pricelist_3)

# Functions for adding or removing cars

def car_up():

    global number_car
    number_car = number_car + 1
    input_car.delete(0, END)
    input_car.insert(END, number_car)

    global total_car
    total_car = number_car * CAR_DAILY_RATE

    calculate_parking()
    calculate_total()
    update_receipt(visitorlist_3, pricelist_3)
    update_receipt(visitorlist_3, pricelist_3)  

def car_down():
    
    global number_car
    number_car = number_car - 1
    if number_car < 0: 
        number_car = 0
    input_car.delete(0, END)
    input_car.insert(END, number_car)

    calculate_parking()
    calculate_total()
    update_receipt(visitorlist_3, pricelist_3)
    update_receipt(visitorlist_3, pricelist_3)

# Checkbutton for adding daily rate to the package
Check_parking = Checkbutton(frame3, bg="#d4e783", variable=var_parking, 
                             command=calculate_parking)
Check_parking.place(x=20, y=598)

# Buttons for input cars
car_min = tk.Button(frame3, image = arrow_left, borderwidth=0, 
                     command=car_down, state=DISABLED)
car_plus = tk.Button(frame3, image = arrow_right, borderwidth=0, 
                      command=car_up, state=DISABLED)

car_min.place(x=635, y=610)
car_plus.place(x=785, y=610)

#================================== FRAME4 RESTAURANT ===================================

frame4_title = tk.Label(frame4, text='Restaurant', font=font_title1, bg=font_title1_bg, 
                        fg=font_title1_color)
frame4_title.place(x=40, y=30)

frame4_image = Label(frame4, image=image_restaurant, borderwidth=0)
frame4_image.place(x=860, y=30)

progressbar4 = ttk.Progressbar(frame4, orient=HORIZONTAL, value=50, length=600, 
                               mode='determinate')
progressbar4.place(x=285, y=860)

#Labels for description restaurant
restaurant1 = Label(frame4, text='Om uw onbezorgde dag compleet te maken kunt u met',
                    font=font1, bg=font1_bg, fg=font1_color)
restaurant2 = Label(frame4, text='uw gezin of familie eenmalig* komen eten in ons',
                    font=font1, bg=font1_bg, fg=font1_color)
restaurant3 = Label(frame4, text='"All you can eat Restaurant". Voor het gebruik van',
                    font=font1, bg=font1_bg, fg=font1_color)
restaurant4 = Label(frame4, text='ons restaurant rekenen we de volgendende prijzen :',
                    font=font1, bg=font1_bg, fg=font1_color)

restaurant1.place(x=20, y=238)
restaurant2.place(x=20, y=278)
restaurant3.place(x=20, y=318)
restaurant4.place(x=20, y=358)

#Labels for description age groups restaurant + age limits
restaurant_toddle = Label(frame4, text='- Kleine kinderen jonger dan ' + 
                         str(LIMIT_TODDLE) + ' jaar:', font=font1, bg=font1_bg, 
                         fg=font1_color)
restaurant_child = Label(frame4, text='- Kinderen vanaf ' + str(LIMIT_TODDLE) + 
                    ' jaar t/m ' + str(LIMIT_CHILD) + ' jaar:', font=font1, bg=font1_bg, 
                    fg=font1_color)
restaurant_adult = Label(frame4, text='- Volwassenen vanaf ' + str(LIMIT_CHILD) +
                          ' t/m ' + str(LIMIT_ADULT) + ' jaar:', font=font1, 
                          bg=font1_bg, fg=font1_color)
restaurant_senior = Label(frame4, text='- Senioren vanaf ' + str(LIMIT_ADULT) +
                      ' jaar en ouder:', font=font1, bg=font1_bg, fg=font1_color)

restaurant_toddle.place(x=20, y=418)
restaurant_child.place(x=20, y=478)
restaurant_adult.place(x=20, y=538)
restaurant_senior.place(x=20, y=598)

#Labels for prices restaurant
charge_toddle = Label(frame4, text='\N{euro sign} '+
                         "{:.2f}".format(RESTAURANT_TODDLE).replace(".", ","),
                         font=font2, bg=font2_bg, fg=font2_color)
charge_child = Label(frame4, text='\N{euro sign} '+
                    "{:.2f}".format(RESTAURANT_CHILD).replace(".", ","),
                    font=font2, bg=font2_bg, fg=font2_color)
charge_adult = Label(frame4, text='\N{euro sign} '+
                          "{:.2f}".format(RESTAURANT_ADULT).replace(".", ","),
                          font=font2, bg=font2_bg, fg=font2_color)
charge_senior = Label(frame4, text='\N{euro sign} '+
                      "{:.2f}".format(RESTAURANT_SENIOR).replace(".", ","),
                      font=font2, bg=font2_bg, fg=font2_color)

charge_toddle.place(x=720, y=418)
charge_child.place(x=720, y=478)
charge_adult.place(x=720, y=538)
charge_senior.place(x=720, y=598)

#Labels for conforming restaurant
confirm_restaurant = Label(frame4, text='Ja wij willen komen eten in het Restaurant',
                                font=font2, bg=font2_bg, fg=font2_color)
confirm_restaurant.place(x=60, y=648)

#Labels for receipt
visitorlist_4 = Listbox(frame4, font=font_checkout1, width=27, height=23)
visitorlist_4.place(x=860, y=230)

pricelist_4 = Listbox(frame4, font=font_checkout2, width=15, height=23, justify='right')
pricelist_4.place(x=1050, y=230)

update_receipt(visitorlist_4, pricelist_4)

# Function for calculating costs restaurant

def calculate_restaurant():

    global total_restaurant

    if var_restaurant.get() == 1:

        total_restaurant = (number_toddle * RESTAURANT_TODDLE + 
        number_child * RESTAURANT_CHILD + number_adult * RESTAURANT_ADULT + 
        number_senior * RESTAURANT_SENIOR)

        calculate_total()
        update_receipt(visitorlist_4, pricelist_4)
        update_receipt(visitorlist_4, pricelist_4)

    elif var_restaurant.get() == 0:
        total_restaurant = 0

        calculate_total()
        update_receipt(visitorlist_4, pricelist_4)
        update_receipt(visitorlist_4, pricelist_4)

#Checkbutton for adding restaurant to package
check_restaurant = Checkbutton(frame4, bg='#d4e783' , variable=var_restaurant, 
                               command=calculate_restaurant)
check_restaurant.place(x=20, y=648)

#================================== FRAME5 3D-theatre ===================================

frame5_title = tk.Label(frame5, text='3D-theater', font=font_title1, bg=font_title1_bg, 
                        fg=font_title1_color)
frame5_title.place(x=40, y=30)

frame5_image = Label(frame5, image=image_theatre, borderwidth=0)
frame5_image.place(x=860, y=30)

progressbar5 = ttk.Progressbar(frame5, orient=HORIZONTAL, value=66.66, length=600, 
                               mode='determinate')
progressbar5.place(x=285, y=860)

#Labels for description theatre
theatre1 = Label(frame5, text='Kom op slangen-safari in ons 3D-theater. Kies een',
                 font=font1, bg=font1_bg, fg=font1_color)
theatre2 = Label(frame5, text='tijdstip en kom met de gehele familie slangen vangen',
                 font=font1, bg=font1_bg, fg=font1_color)
theatre3 = Label(frame5, text='als jullie durven. Voor een bezoek aan ons 3D-theater',
                 font=font1, bg=font1_bg, fg=font1_color)
theatre4 = Label(frame5, text='rekenen we de volgendende prijzen :',
                 font=font1, bg=font1_bg, fg=font1_color)

theatre1.place(x=20, y=238)
theatre2.place(x=20, y=278)
theatre3.place(x=20, y=318)
theatre4.place(x=20, y=358)

# Labels for description age groups 3D-theatre + age limits
theatre_toddle = Label(frame5, text='- Kleine kinderen jonger dan ' + 
                         str(LIMIT_TODDLE) + ' jaar:', font=font1, bg=font1_bg, 
                         fg=font1_color)
theatre_child = Label(frame5, text='- Kinderen vanaf ' + str(LIMIT_TODDLE) + 
                    ' jaar t/m ' + str(LIMIT_CHILD) + ' jaar:', font=font1, bg=font1_bg, 
                    fg=font1_color)
theatre_adult = Label(frame5, text='- Volwassenen vanaf ' + str(LIMIT_CHILD) +
                          ' t/m ' + str(LIMIT_ADULT) + ' jaar:', font=font1, 
                          bg=font1_bg, fg=font1_color)
theatre_senior = Label(frame5, text='- Senioren vanaf ' + str(LIMIT_ADULT) +
                      ' jaar en ouder:', font=font1, bg=font1_bg, fg=font1_color)

theatre_toddle.place(x=20, y=418)
theatre_child.place(x=20, y=478)
theatre_adult.place(x=20, y=538)
theatre_senior.place(x=20, y=598)

#Labels for prices 3D-theatre
cost_toddle = Label(frame5, text='\N{euro sign} '+
                          "{:.2f}".format(THEATRE_TODDLE).replace(".", ","),
                          font=font2, bg=font2_bg, fg=font2_color)
cost_child = Label(frame5, text='\N{euro sign} '+
                    "{:.2f}".format(THEATRE_CHILD).replace(".", ","),
                    font=font2, bg=font2_bg, fg=font2_color)
cost_adult = Label(frame5, text='\N{euro sign} '+
                           "{:.2f}".format(THEATRE_ADULT).replace(".", ","),
                           font=font2, bg=font2_bg, fg=font2_color)
cost_senior = Label(frame5, text='\N{euro sign} '+
                       "{:.2f}".format(THEATRE_SENIOR).replace(".", ","),
                       font=font2, bg=font2_bg, fg=font2_color)

cost_toddle.place(x=720, y=418)
cost_child.place(x=720, y=478)
cost_adult.place(x=720, y=538)
cost_senior.place(x=720, y=598)

#Labels for confirming 3D-theatre
confirm_theatre_1 = Label(frame5, text='Ja wij willen op safari in het 3D-theater',
                            font=font2, bg=font2_bg, fg=font2_color)
confirm_theatre_2 = Label(frame5, text='Tijd:',
                            font=font2, bg=font2_bg, fg=font2_color)

confirm_theatre_1.place(x=60, y=648)
confirm_theatre_2.place(x=640, y=648)

#Labels for receipt
visitorlist_5 = Listbox(frame5, font=font_checkout1, width=27, height=23)
visitorlist_5.place(x=860, y=230)

pricelist_5 = Listbox(frame5, font=font_checkout2, width=15, height=23, justify='right')
pricelist_5.place(x=1050, y=230)

update_receipt(visitorlist_5, pricelist_5)

# Function for calculating costs 3D-theatre

def calculate_theatre():

    global total_theatre

    if var_theatre.get() == 1:

        total_theatre = (number_toddle * THEATRE_TODDLE + 
                          number_child * THEATRE_CHILD + 
                          number_adult * THEATRE_ADULT 
                          + number_senior * THEATRE_SENIOR)

        cover_theatre.lower()
        calculate_total()
        update_receipt(visitorlist_5, pricelist_5)
        update_receipt(visitorlist_5, pricelist_5)

    elif var_theatre.get() == 0:
        total_theatre = 0

        calculate_total()
        update_receipt(visitorlist_5, pricelist_5)
        update_receipt(visitorlist_5, pricelist_5)
        cover_theatre.lift()

# Checkbutton for adding 3D-theatre to package
check_theatre = Checkbutton(frame5, bg='#d4e783', variable=var_theatre, 
                            command=calculate_theatre)
check_theatre.place(x=20, y=648)

# Code voor creëeren en plaatsen optiemenu om tijd te kiezen voor 3D-theater

hour = int(time_now.strftime("%I"))

options = [ 
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
]

if hour == 10:
    options.pop(0)

if hour == 11:
    for i in range(2):
        options.pop(0)

if hour == 12:
    for i in range(3):
        options.pop(0)

if hour == 1:
    for i in range(4):
        options.pop(0)

if hour == 2:
    for i in range(5):
        options.pop(0)
    
if hour == 3:
    for i in range(6):
        options.pop(0)
    
if hour == 4:
    for i in range(7):
        options.pop(0)
    
clicked = StringVar()
clicked.set(options[0])

period = OptionMenu(frame5, clicked, *options)
period.configure(font=font_option1, bg=font_option1_bg, activebackground=font_option1_bg)
period.place(x=720, y=640)
menu = frame5.nametowidget(period.menuname)
menu.config(font=font_option2, bg=font_option2_bg)

# Cover for hiding time slot if 3D theater is not desired
cover_theatre = Label(frame5, text="                      ",
                                font='Arial 24', bg='#d4e783')
cover_theatre.place(x=600, y=640)

#=================================== FRAME6 FACEPAINT ===================================
                                            
frame6_title = tk.Label(frame6, text='Schminken', font=font_title1, bg=font_title1_bg, 
                        fg=font_title1_color)
frame6_title.place(x=40, y=30)

frame6_image = Label(frame6, image=image_facepaint, borderwidth=0)
frame6_image.place(x=860, y=30)

progressbar6 = ttk.Progressbar(frame6, orient=HORIZONTAL, value=83.33, length=600, 
                               mode='determinate')
progressbar6.place(x=285, y=860)

# Labels for description facepaint
facepaint1 = Label(frame6, text='Laat jezelf schminken tot slang om niet opgegeten',
                                font=font1, bg=font1_bg, fg=font1_color)
facepaint2 = Label(frame6, text='te worden. Een erg leuke toevoeging aan de dag',
                                font=font1, bg=font1_bg, fg=font1_color)
facepaint3 = Label(frame6, text='voor de allerkleinsten. Voor het schminken rekenen',
                                font=font1, bg=font1_bg, fg=font1_color)
facepaint4 = Label(frame6, text='we het volgende vaste bedrag per persoon:',
                                font=font1, bg=font1_bg, fg=font1_color)

facepaint1.place(x=20, y=238)
facepaint2.place(x=20, y=288)
facepaint3.place(x=20, y=338)
facepaint4.place(x=20, y=388)

# Labels for prices facepaint
charge_facepaint = Label(frame6, text='\N{euro sign} '+
                        "{:.2f}".format(PRICE_FACEPAINT).replace(".", ","),
                        font=font2, bg=font2_bg, fg=font2_color)
charge_facepaint.place(x=695, y=388)

# Labels for confirm facepaint
confirm_facepaint_1 = Label(frame6, text='Ja wij willen het volgend aantal personen',
                                font=font2, bg=font2_bg, fg=font2_color)
confirm_facepaint_2 = Label(frame6, text='laten schminken:',
                                font=font2, bg=font2_bg, fg=font2_color)

confirm_facepaint_1.place(x=60, y=598)
confirm_facepaint_2.place(x=60, y=648)

# Label for input number facepaint
input_facepaint = Listbox(frame6, width=3, height=1, font=font3, justify='center')
input_facepaint.insert(END, number_facepaint)
input_facepaint.configure(state= DISABLED)
input_facepaint.place(x=715, y=620)

# Labels for receipt
visitorlist_6 = Listbox(frame6, font=font_checkout1, width=27, height=23)
visitorlist_6.place(x=860, y=230)

pricelist_6 = Listbox(frame6, font=font_checkout2, width=15, height=23, justify='right')
pricelist_6.place(x=1050, y=230)

update_receipt(visitorlist_6, pricelist_6)

# Function for calculating costs facepaint

def calculate_facepaint():

    global number_facepaint
    global total_facepaint
    
    global number_visitors
    

    if var_facepaint.get() == 1:

        input_facepaint.configure(state=NORMAL)
        facepaint_min.configure(state=NORMAL)
        facepaint_plus.configure(state=NORMAL)
        input_facepaint.delete(0, END)
        input_facepaint.insert(END, number_facepaint)

        total_facepaint = number_facepaint * PRICE_FACEPAINT

        if number_facepaint == number_visitors:
            facepaint_plus.configure(state=DISABLED)

    elif var_facepaint.get() == 0:

        number_facepaint = 0
        total_facepaint = 0

        input_facepaint.delete(0, END)
        input_facepaint.insert(END, number_facepaint)

        input_facepaint.configure(state=DISABLED)
        facepaint_min.configure(state=DISABLED)
        facepaint_plus.configure(state=DISABLED)

        calculate_total()
        update_receipt(visitorlist_6, pricelist_6)
        update_receipt(visitorlist_6, pricelist_6)

# Function for add or remove visitors for face painting 

def facepaint_up():

    global number_facepaint

    number_facepaint = number_facepaint + 1
    input_facepaint.delete(0, END)
    input_facepaint.insert(END, number_facepaint)

    global total_facepaint
    total_facepaint = number_facepaint * PRICE_FACEPAINT

    if number_senior != 0 and (number_facepaint - number_toddle 
                                - number_child - number_adult) == 1:
        messagebox.showerror("Wordt het zo'n dag",
                                    "Weet je wel heel zeker dat opa en oma " 
                                    "ook geschminkt willen worden? ;)")

    calculate_facepaint()
    calculate_total()
    update_receipt(visitorlist_6, pricelist_6)
    update_receipt(visitorlist_6, pricelist_6)  
    
def facepaint_down():
    
    global number_facepaint
    number_facepaint = number_facepaint - 1
    if number_facepaint < 0: 
        number_facepaint = 0
    input_facepaint.delete(0, END)
    input_facepaint.insert(END, number_facepaint)

    calculate_facepaint()
    calculate_total()
    update_receipt(visitorlist_6, pricelist_6)
    update_receipt(visitorlist_6, pricelist_6)

# Check button for adding facepaint to package
Check_schminken = Checkbutton(frame6, bg='#d4e783', variable=var_facepaint, 
                              command=calculate_facepaint)
Check_schminken.place(x=20, y=598)

# Buttons for input facepaint
facepaint_min = tk.Button(frame6, image = arrow_left, borderwidth=0, 
                          command=(facepaint_down), state=DISABLED)
facepaint_plus = tk.Button(frame6, image = arrow_right, borderwidth=0, 
                           command=(facepaint_up), state=DISABLED)

facepaint_min.place(x=635, y=610)
facepaint_plus.place(x=785, y=610)

#================================= FRAME 7 CONFIRMATION =================================
                                            
frame7_title = tk.Label(frame7, text='Bevestigen', font=font_title1, bg=font_title1_bg, 
                        fg=font_title1_color)
frame7_title.place(x=40, y=30)

frame7_image = Label(frame7, image=image_ice, borderwidth=0)
frame7_image.place(x=860, y=30)

progressbar7 = ttk.Progressbar(frame7, orient=HORIZONTAL, value=100, length=600, 
                               mode='determinate')
progressbar7.place(x=285, y=860)

#Labels for description confirmation
confirmation1 = Label(frame7, text='Voordat we uw bestelling kunnen afronden hebben we',
                                font=font1, bg=font1_bg, fg=font1_color)
confirmation2 = Label(frame7, text='alleen nog uw naam nodig. Deze komt op het E-ticket',
                                font=font1, bg=font1_bg, fg=font1_color)
confirmation3 = Label(frame7, text='en kan gebruikt worden indien u uw E-ticket verliest',
                                font=font1, bg=font1_bg, fg=font1_color)

confirmation1.place(x=20, y=238)
confirmation2.place(x=20, y=278)
confirmation3.place(x=20, y=318)

#Labels for visitor's first and last name
confirm_firstname = Label(frame7, text='Voornaam:',
                                font=font2, bg=font2_bg, fg=font2_color)
confirm_lastname = Label(frame7, text='Achternaam:',
                                font=font2, bg=font2_bg, fg=font2_color)

confirm_firstname.place(x=60, y=368)
confirm_lastname.place(x=60, y=428)

#Labels for description + confirmation donation
confirm_donation_1 = Label(frame7, text='Ja wij willen een eenmalige donatie aan stichting',
                               font=font2, bg=font2_bg, fg=font2_color)
confirm_donation_2 = Label(frame7, text='Carnivora doen en hiermee voor iedereen een ijsje',
                               font=font2, bg=font2_bg, fg=font2_color)
confirm_donation_3 = Label(frame7, text='verdienen in de ijssalon. Carnivora is een stich-',
                               font=font2, bg=font2_bg, fg=font2_color)
confirm_donation_4 = Label(frame7, text='ting die zich inzet voor bedreigde slangensoorten.',
                               font=font2, bg=font2_bg, fg=font2_color)

confirm_donation_1.place(x=60, y=498)
confirm_donation_2.place(x=60, y=548)
confirm_donation_3.place(x=60, y=598)
confirm_donation_4.place(x=60, y=648)

#Labels for price donation
cost_donation = Label(frame7, text='\N{euro sign} '+
                      "{:.2f}".format(DONATION).replace(".", ","),
                      font=font2, bg=font2_bg, fg=font2_color)
cost_donation.place(x=720, y=573)

# Labels for inputfields visitor's first and last name
input_firstname = Entry(frame7, width=20, font=font3, justify='left')
input_firstname.focus()
input_firstname.place(x=300, y=368)

input_lastname = Entry(frame7, width=20, font=font3, justify='left')
input_lastname.place(x=300, y=428)

#Labels for receipt
visitorlist_7 = Listbox(frame7, font=font_checkout1, width=27, height=23)
visitorlist_7.place(x=860, y=230)

pricelist_7 = Listbox(frame7, font=font_checkout2, width=15, height=23, justify='right')
pricelist_7.place(x=1050, y=230)

update_receipt(visitorlist_7, pricelist_7)

# Function to calculate costs donation

def calculate_donation():

    global total_donation

    if var_confirmation.get() == 1:
        total_donation = DONATION

        calculate_total()
        update_receipt(visitorlist_7, pricelist_7)
        update_receipt(visitorlist_7, pricelist_7)

    elif var_confirmation.get() == 0:
        total_donation = 0

        calculate_total()
        update_receipt(visitorlist_7, pricelist_7)
        update_receipt(visitorlist_7, pricelist_7)

# Checkbutton for adding donation to package
check_donation = Checkbutton(frame7, bg='#d4e783', variable=var_confirmation, 
                            command=calculate_donation)
check_donation.place(x=20, y=498)

#================================ FRAME 8 CODE E-ticket =================================

frame8.configure(bg='#ffffff')
frame8.grid(row=0,column=0,sticky='nsew') 

frame2_title = tk.Label(frame8, text="E-Ticket", font=font_title2, bg=font_title2_bg, 
                        fg=font_title2_color)
frame2_title.place(x=30, y=15)

frame8_logo = Label(frame8, image=logo2, borderwidth=0)
frame8_logo.place(x=500, y=-25) 

#Labels for adress Pythonland
ticket_adress1 = Label(frame8, text="Pythonland", 
                      font=font8b, bg=font8b_bg, fg=font8b_color)
ticket_adress2 = Label(frame8, text="Schweitzerlaan 3", 
                      font=font8, bg=font8_bg, fg=font8_color)
ticket_adress3 = Label(frame8, text="9728 NR Groningen", 
                      font=font8, bg=font8_bg, fg=font8_color)
ticket_adress4 = Label(frame8, text="tel 050 541 3842", 
                      font=font8, bg=font8_bg, fg=font8_color)

ticket_adress1.place(x=515, y=165)
ticket_adress2.place(x=515, y=185)
ticket_adress3.place(x=515, y=205)
ticket_adress4.place(x=515, y=225)

#Labels for info visitor
ticket_name1 = Label(frame8, text="Naam:", 
                     font=font12b, bg=font12b_bg, fg=font12b_color)
ticket_number1 = Label(frame8, text="ticketnummer:", 
                       font=font12b, bg=font12b_bg, fg=font12b_color)
ticket_date1 = Label(frame8, text="Datum:", 
                      font=font12b, bg=font12b_bg, fg=font12b_color)
ticket_time1 = Label(frame8, text="Tijdstip:", 
                     font=font12b, bg=font12b_bg, fg=font12b_color)

ticket_name2 = Label(frame8, text="", 
                     font=font12, bg=font12_bg, fg=font12_color)
ticket_number2 = Label(frame8, text="", 
                       font=font12b, bg=font12b_bg, fg=font12b_color)
ticket_date2 = Label(frame8, text=(time_now.strftime("%x")), 
                      font=font12, bg=font12_bg, fg=font12_color)
ticket_time2 = Label(frame8, text=(time_now.strftime("%X")), 
                     font=font12, bg=font12_bg, fg=font12_color)

ticket_name1.place(x=30, y=165)
ticket_number1.place(x=30, y=195)
ticket_date1.place(x=30, y=225)
ticket_time1.place(x=30, y=255)

ticket_name2.place(x=240, y=165)
ticket_number2.place(x=240, y=195)
ticket_date2.place(x=240, y=225)
ticket_time2.place(x=240, y=255)

#Labels for entrance visitors
ticket_toddle1 = Label(frame8, text="Aantal kleine kinderen:", 
                          font=font10, bg=font10_bg, fg=font10_color)
ticket_child1 = Label(frame8, text="Aantal kinderen:", 
                     font=font10, bg=font10_bg, fg=font10_color)
ticket_adult1 = Label(frame8, text="Aantal volwassenen:", 
                           font=font10, bg=font10_bg, fg=font10_color)
ticket_senior1 = Label(frame8, text="Aantal senioren:", 
                       font=font10, bg=font10_bg, fg=font10_color)
ticket_discount1 = Label(frame8, text="Korting", 
                        font=font10, bg=font10_bg, fg=font10_color)
ticket_entrance1 = Label(frame8, text="Totaal Entree", 
                       font=font10b, bg=font10b_bg, fg=font10b_color)

ticket_toddle2 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_child2 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_adult2 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_senior2 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_discount2 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)

ticket_toddle3 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_child3 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_adult3 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_senior3 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_discount3 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_entrance3 = Label(frame8, text="", font=font12, bg=font12_bg, fg=font12_color)

ticket_toddle1.place(x=30, y=305)
ticket_child1.place(x=30, y=325)
ticket_adult1.place(x=30, y=345)
ticket_senior1.place(x=30, y=365)
ticket_discount1.place(x=30, y=390)
ticket_entrance1.place(x=30, y=420)

ticket_toddle2.place(x=460, y=305)
ticket_child2.place(x=460, y=325)
ticket_adult2.place(x=460, y=345)
ticket_senior2.place(x=460, y=365)
ticket_discount2.place(x=460, y=390)

ticket_toddle3.place(x=590, y=305)
ticket_child3.place(x=590, y=325)
ticket_adult3.place(x=590, y=345)
ticket_senior3.place(x=590, y=365)
ticket_discount3.place(x=575, y=390)
ticket_entrance3.place(x=590, y=420)

#Labels for additions to package
ticket_parking1 = Label(frame8, text="Parkeren Dagtarief", 
                         font=font10, bg=font10_bg, fg=font10_color)
ticket_restaurant1 = Label(frame8, text="Restaurant", 
                           font=font10, bg=font10_bg, fg=font10_color)
ticket_theatre1 = Label(frame8, text="3D-theater", 
                          font=font10, bg=font10_bg, fg=font10_color)
ticket_facepaint1 = Label(frame8, text="Schminken", 
                          font=font10, bg=font10_bg, fg=font10_color)
ticket_donation1= Label(frame8, text="Donatie gratis ijsje", 
                       font=font10, bg=font10_bg, fg=font10_color)
ticket_package1 = Label(frame8, text="Totaal Toevoegingen", 
                            font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_total1 = Label(frame8, text="Totaal Prijs", 
                       font=font12b, bg=font12b_bg, fg=font12b_color)

ticket_parking2 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_restaurant2 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_theatre2 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_facepaint2 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_donation2 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)

ticket_parking3 = Label(frame8, text="", font=font10, bg=font10_bg, fg=font10_color)
ticket_restaurant3 = Label(frame8, text="", font=font10, bg=font10_bg, fg=font10_color)
ticket_theatre3 = Label(frame8, text="", font=font10, bg=font10_bg, fg=font10_color)
ticket_facepaint3 = Label(frame8, text="", font=font10, bg=font10_bg, fg=font10_color)
ticket_donation3 = Label(frame8, text="", font=font10, bg=font10_bg, fg=font10_color)

ticket_parking4 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_restaurant4 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_theatre4 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_facepaint4 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_donation4 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)

ticket_parking5 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_restaurant5 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_theatre5 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_facepaint5 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_donation5 = Label(frame8, text="", font=font10b, bg=font10b_bg, fg=font10b_color)
ticket_arrangement5 = Label(frame8, text="", font=font12, bg=font12_bg, fg=font12_color)
ticket_total5 = Label(frame8, text="", font=font12b, bg=font12b_bg, fg=font12b_color)

ticket_parking1.place(x=30, y=460)
ticket_restaurant1.place(x=30, y=480)
ticket_theatre1.place(x=30, y=500)
ticket_facepaint1.place(x=30, y=520)
ticket_donation1.place(x=30, y=540)
ticket_package1.place(x=30, y=570)
ticket_total1.place(x=30, y=610)

ticket_parking2.place(x=240, y=460)
ticket_restaurant2.place(x=240, y=480)
ticket_theatre2.place(x=240, y=500)
ticket_facepaint2.place(x=240, y=520)
ticket_donation2.place(x=240, y=540)

ticket_parking3.place(x=300, y=460)
ticket_restaurant3.place(x=300, y=480)
ticket_theatre3.place(x=300, y=500)
ticket_facepaint3.place(x=300, y=520)
ticket_donation3.place(x=300, y=540)

ticket_parking4.place(x=460, y=460)
ticket_restaurant4.place(x=460, y=480)
ticket_theatre4.place(x=460, y=500)
ticket_facepaint4.place(x=460, y=520)
ticket_donation4.place(x=460, y=540)

ticket_parking5.place(x=590, y=460)
ticket_restaurant5.place(x=590, y=480)
ticket_theatre5.place(x=590, y=500)
ticket_facepaint5.place(x=590, y=520)
ticket_donation5.place(x=590, y=540)
ticket_arrangement5.place(x=590, y=570)
ticket_total5.place(x=590, y=610)

#Labels for time 3D-theatre
ticket_time_theatre1 = Label(frame8, text="Tijd 3D-Theater:", 
                            font=font12, bg=font12_bg, fg=font12_color)
ticket_time_theatre2 = Label(frame8, text="", 
                            font=font12b, bg=font12b_bg, fg=font12b_color)

ticket_time_theatre1.place(x=330, y=760)
ticket_time_theatre2.place(x=370, y=790)

#Labels for openinghours Pythonland
ticket_openinghours1 = Label(frame8, text="Openingstijden", 
                               font=font8b, bg=font8b_bg, fg=font8b_color)
ticket_openinghours2 = Label(frame8, text="maandag", 
                               font=font8, bg=font8_bg, fg=font8_color)
ticket_openinghours3 = Label(frame8, text="dinsdag", 
                               font=font8, bg=font8_bg, fg=font8_color)
ticket_openinghours4 = Label(frame8, text="woensdag", 
                               font=font8, bg=font8_bg, fg=font8_color)
ticket_openinghours5 = Label(frame8, text="donderdag", 
                               font=font8, bg=font8_bg, fg=font8_color)
ticket_openinghours6 = Label(frame8, text="vrijdag", 
                               font=font8, bg=font8_bg, fg=font8_color)
ticket_openinghours7 = Label(frame8, text="zaterdag", 
                               font=font8, bg=font8_bg, fg=font8_color)
ticket_openinghours8 = Label(frame8, text="zondag", 
                               font=font8, bg=font8_bg, fg=font8_color)

ticket_openinghours9 = Label(frame8, text=TIMES_MONDAY, 
                               font=font8b, bg=font8b_bg, fg=font8b_color)
ticket_openinghours10 = Label(frame8, text=TIMES_TUESDAY, 
                                font=font8b, bg=font8b_bg, fg=font8b_color)
ticket_openinghours11 = Label(frame8, text=TIMES_WEDNESDAY, 
                                font=font8b, bg=font8b_bg, fg=font8b_color)
ticket_openinghours12 = Label(frame8, text=TIMES_THURSDAY, 
                                font=font8b, bg=font8b_bg, fg=font8b_color)
ticket_openinghours13 = Label(frame8, text=TIMES_FRIDAY, 
                                font=font8b, bg=font8b_bg, fg=font8b_color)
ticket_openinghours14= Label(frame8, text=TIMES_SATURDAY, 
                               font=font8b, bg=font8b_bg, fg=font8b_color)
ticket_openinghours15= Label(frame8, text=TIMES_SUNDAY, 
                               font=font8b, bg=font8b_bg, fg=font8b_color)

ticket_openinghours1.place(x=515, y=700)
ticket_openinghours2.place(x=515, y=720)
ticket_openinghours3.place(x=515, y=740)
ticket_openinghours4.place(x=515, y=760)
ticket_openinghours5.place(x=515, y=780)
ticket_openinghours6.place(x=515, y=800)
ticket_openinghours7.place(x=515, y=820)
ticket_openinghours8.place(x=515, y=840)

ticket_openinghours9.place(x=590, y=720)
ticket_openinghours10.place(x=590, y=740)
ticket_openinghours11.place(x=590, y=760)
ticket_openinghours12.place(x=590, y=780)
ticket_openinghours13.place(x=590, y=800)
ticket_openinghours14.place(x=590, y=820)
ticket_openinghours15.place(x=590, y=840)

#Labels for ticketrequirements
ticket_requirements1 = Label(frame8, text="- Dit E-ticket is alleen geldig op de dag "
                            "van aanschaf op bovengenoemde datum", 
                            font=font7, bg=font7_bg, fg=font7_color)
ticket_requirements2 = Label(frame8, text="- Bij verlies kunt u zich met een geldig "
                            "legitimatiebewijs melden in het kassagebouw", 
                            font=font7, bg=font7_bg, fg=font7_color)
ticket_requirements3 = Label(frame8, text="- Op verzoek dient het ticket te worden "
                            "getoond", 
                            font=font7, bg=font7_bg, fg=font7_color)
ticket_requirements4 = Label(frame8, text="- Het ticket is niet inwisselbaar voor geld, " 
                            "een ander ticket of anderszins inwisselbaar", 
                            font=font7, bg=font7_bg, fg=font7_color)
ticket_requirements5 = Label(frame8, text="- Met het betreden van het park gaat u akkoord " 
                            "met het parkregelement", 
                            font=font7, bg=font7_bg, fg=font7_color)

ticket_requirements1.place(x=20, y=888)
ticket_requirements2.place(x=20, y=905)
ticket_requirements3.place(x=20, y=922)
ticket_requirements4.place(x=20, y=939)
ticket_requirements5.place(x=20, y=956)

#Label for QRcode
ticket_QRcode = Label(frame8, image=QRcode, borderwidth=0)
ticket_QRcode.place(x=60, y=640)

#============================ FUNCTIONS FOR CHANGING FRAMES ============================= 
                              
def frame1_next():

    show_frame(frame2)

    input_toddle.delete(0, END)
    input_child.delete(0, END)
    input_adult.delete(0, END)
    input_senior.delete(0, END)

    input_toddle.insert(0, number_toddle)
    input_child.insert(0, number_child)
    input_adult.insert(0, number_adult)
    input_senior.insert(0, number_senior)

    update_receipt(visitorlist_2, pricelist_2)
    update_receipt(visitorlist_2, pricelist_2)

def frame2_back():

    show_frame(frame1)

    global number_toddle
    number_toddle = 0
    global number_child
    number_child = 0
    global number_adult
    number_adult = 0
    global number_senior
    number_senior = 0

    global total_toddle
    total_toddle = 0
    global total_child
    total_child = 0
    global total_adult
    total_adult = 0
    global total_senior
    total_senior = 0

    calculate_entrance()
    calculate_discount()
    calculate_total()
    update_receipt(visitorlist_2, pricelist_2)
    update_receipt(visitorlist_2, pricelist_2)

def frame2_next():

    global number_visitors

    number_visitors = number_toddle + number_child + number_adult + number_senior 

    if  number_visitors == 0:
        messagebox.showerror("Geen Invoer",
                                    "Klik op de pijlen om bezoekers aan uw ticket " 
                                    "in te voeren")

        show_frame(frame2)

    elif  number_child == 0 and number_adult == 0 and number_senior == 0:
        messagebox.showerror("Geen Invoer ",
                                    "Vraag je ouders het ticket te bestellen")

        show_frame(frame2)

    elif  number_child != 0 and number_adult == 0 and number_senior == 0:
        messagebox.showerror("Geen Invoer",
                                    "Vraag je ouders het ticket te bestellen of meld " 
                                    "je bij één van onze kassa's om een ticket te bestellen")

        show_frame(frame2)

    else:
        show_frame(frame3)

        update_receipt(visitorlist_3, pricelist_3)
        update_receipt(visitorlist_3, pricelist_3)

def frame3_back():

    show_frame(frame2)

    global number_car
    number_car = 0

    global total_parking 
    total_parking = 0

    input_car.delete(0, END)
    input_car.insert(0, number_car)
    
    var_parking.set(0)

    input_car.configure(state=DISABLED)
    car_min.configure(state=DISABLED)
    car_plus.configure(state=DISABLED)

    calculate_parking()
    calculate_total()
    update_receipt(visitorlist_3, pricelist_3)
    update_receipt(visitorlist_3, pricelist_3)

def frame3_next():

    show_frame(frame4)

    update_receipt(visitorlist_4, pricelist_4)
    update_receipt(visitorlist_4, pricelist_4)

def frame4_back():

    show_frame(frame3)

    var_restaurant.set(0)

    calculate_restaurant()
    calculate_total()
    update_receipt(visitorlist_4, pricelist_4)
    update_receipt(visitorlist_4, pricelist_4)

def frame4_next():

    show_frame(frame5)

    update_receipt(visitorlist_5, pricelist_5)
    update_receipt(visitorlist_5, pricelist_5)

def frame5_back():

    show_frame(frame4)

    var_theatre.set(0)
    clicked.set(options[0])

    calculate_theatre
    calculate_total()
    update_receipt(visitorlist_4, pricelist_4)
    update_receipt(visitorlist_4, pricelist_4)

def frame5_next():

    show_frame(frame6)

    global time_theatre

    time_theatre = clicked.get()
    
    if var_theatre.get() == 0:
        time_theatre = "geen"

    update_receipt(visitorlist_6, pricelist_6)
    update_receipt(visitorlist_6, pricelist_6)

def frame6_back():

    show_frame(frame5)

    global number_facepaint
    number_facepaint = 0

    global total_facepaint 
    total_facepaint = 0

    input_facepaint.delete(0, END)
    input_facepaint.insert(0, number_facepaint)
    
    var_facepaint.set(0)

    input_facepaint.configure(state=DISABLED)
    facepaint_min.configure(state=DISABLED)
    facepaint_plus.configure(state=DISABLED)

    calculate_facepaint()
    calculate_total()
    update_receipt(visitorlist_6, pricelist_6)
    update_receipt(visitorlist_6, pricelist_6)

def frame6_next():

    show_frame(frame7)

    update_receipt(visitorlist_7, pricelist_7)
    update_receipt(visitorlist_7, pricelist_7)

def frame7_back():

    show_frame(frame6)

    var_confirmation.set(0)
    input_firstname.delete(0, END)
    input_lastname.delete(0, END)

    calculate_donation()
    calculate_total()
    update_receipt(visitorlist_7, pricelist_7)
    update_receipt(visitorlist_7, pricelist_7)

def frame7_next():

    global firstname_visitor
    global lastname_visitor
    global name_visitor

    global ticketnumber
    ticketnumber = ticketnumber + 1

    global QRcode
    
    firstname_visitor = input_firstname.get()
    firstname_visitor = firstname_visitor.lower()
    firstname_visitor = firstname_visitor.strip()

    lastname_visitor = input_lastname.get()
    lastname_visitor = lastname_visitor.lower()
    lastname_visitor = lastname_visitor.strip()

    name_visitor = firstname_visitor + " " + lastname_visitor 

    if firstname_visitor == "" or lastname_visitor =="":
        messagebox.showerror("Geen Invoer",
                                    "Voor uw voor- en achternaam in")
        show_frame(frame7)

    else:
        
        root.geometry('706x1000+300+0')

        eticket()
        build_code()

        show_frame(frame8)

# Function to restart app

def frame8_next():

    global number_toddle
    number_toddle = 0
    global number_child
    number_child = 0
    global number_adult
    number_adult = 0
    global number_senior
    number_senior = 0

    global total_toddle
    total_toddle = 0
    global total_child
    total_child = 0
    global total_adult
    total_adult = 0
    global total_senior
    total_senior = 0

    global number_car
    number_car = 0
    global total_parking 
    total_parking = 0

    global number_facepaint
    number_facepaint = 0
    global total_facepaint 
    total_facepaint = 0

    var_parking.set(0)
    var_restaurant.set(0)
    var_theatre.set(0)
    clicked.set(options[0])
    var_facepaint.set(0)
    var_confirmation.set(0)
    
    input_toddle.delete(0, END)
    input_child.delete(0, END)
    input_adult.delete(0, END)
    input_senior.delete(0, END)

    input_toddle.insert(0, number_toddle)
    input_child.insert(0, number_child)
    input_adult.insert(0, number_adult)
    input_senior.insert(0, number_senior)

    input_car.delete(0, END)
    input_car.insert(0, number_car)

    input_facepaint.delete(0, END)
    input_facepaint.insert(0, number_facepaint)

    input_firstname.delete(0, END)
    input_firstname.focus()
    input_lastname.delete(0, END)
    
    input_car.configure(state=DISABLED)
    car_min.configure(state=DISABLED)
    car_plus.configure(state=DISABLED)
    
    input_facepaint.configure(state=DISABLED)
    facepaint_min.configure(state=DISABLED)
    facepaint_plus.configure(state=DISABLED)

    calculate_entrance()
    calculate_discount()
    calculate_parking()
    calculate_restaurant()
    calculate_theatre()
    calculate_facepaint()
    calculate_donation()
    calculate_total()

    root.geometry('1200x900')

    show_frame(frame1)

# Buttons to change frames
frame1_button = Button(frame1, text ='Tickets Bestellen', font =font_button1, 
                       bg=font_button1_bg, fg=font_button1_color, relief=RAISED, bd=12, 
                       command=frame1_next)
frame1_button.grid(row=0, column=0, padx=330, pady=700)

frame2_button2 = Button(frame2, text ='Verder', font =font_button2, bg=font_button2_bg, 
                        fg=font_button2_color, relief=RAISED, bd=6, command=frame2_next)
frame2_button2.place(x=960, y=770)

frame2_button1 = Button(frame2, text ='Terug', font =font_button2, bg=font_button2_bg, 
                        fg=font_button2_color, relief=RAISED, bd=6, command=frame2_back)
frame2_button1.place(x=40, y=770)

frame3_button1 = Button(frame3, text ='Terug', font =font_button2, bg=font_button2_bg, 
                        fg=font_button2_color, relief=RAISED, bd=6, command=frame3_back)
frame3_button1.place(x=40, y=770)

frame3_button2 = Button(frame3, text ='Verder', font =font_button2, bg=font_button2_bg, 
                        fg=font_button2_color, relief=RAISED, bd=6, command=frame3_next)
frame3_button2.place(x=960, y=770)

frame4_button1 = Button(frame4, text ='Terug', font =font_button2, bg=font_button2_bg, 
                        fg=font_button2_color, relief=RAISED, bd=6, command=frame4_back)
frame4_button1.place(x=40, y=770)

frame4_button2 = Button(frame4, text ='Verder', font =font_button2, bg=font_button2_bg, 
                        fg=font_button2_color, relief=RAISED, bd=6, command=frame4_next)
frame4_button2.place(x=960, y=770)

frame5_button1 = Button(frame5, text ='Terug', font =font_button2, bg=font_button2_bg, 
                        fg=font_button2_color, relief=RAISED, bd=6, command=frame5_back)
frame5_button1.place(x=40, y=770)

frame5_button2 = Button(frame5, text ='Verder', font =font_button2, bg=font_button2_bg, 
                        fg=font_button2_color, relief=RAISED, bd=6, command=frame5_next)
frame5_button2.place(x=960, y=770)

frame6_button1 = Button(frame6, text ='Terug', font =font_button2, bg=font_button2_bg, 
                        fg=font_button2_color, relief=RAISED, bd=6, command=frame6_back)
frame6_button1.place(x=40, y=770)

frame6_button2 = Button(frame6, text ='Verder', font =font_button2, bg=font_button2_bg, 
                        fg=font_button2_color, relief=RAISED, bd=6, command=frame6_next)
frame6_button2.place(x=960, y=770)

frame7_button1 = Button(frame7, text ='Terug', font =font_button2, bg=font_button2_bg, 
                        fg=font_button2_color, relief=RAISED, bd=6, command=frame7_back)
frame7_button1.place(x=40, y=770)

frame7_button2 = Button(frame7, text ='Betalen', font =font_button2, bg=font_button2_bg, 
                        fg=font_button2_color, relief=RAISED, bd=6, command=frame7_next)
frame7_button2.place(x=960, y=770)

frame8_button = Button(frame8, text ='Print', font =font_button2, bg=font_button2_bg, 
                       fg=font_button2_color, relief=RAISED, bd=6, command=frame8_next)
frame8_button.place(x=515, y=880)

show_frame(frame1)

root.mainloop()

