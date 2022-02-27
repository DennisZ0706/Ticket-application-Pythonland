# Ticket application Pythonland

## The App

Ticket application that allows Pythonland visitors to compose their own tickets. Application is intended to be imported into ticket machines installed in front of the cash office building. So that the staff in the cash office building only have to scan the ticket when the visitors want to enter the park.

The visitor is guided through the ordering process by steps. First they have to fill in how many people are coming and what the age of everyone is. After that, all kinds of extra facilities can be added to the ticket, such as the restaurant or the theater. They can also add a day ticket for cheaper parking.

When all these steps have been performed, the last step is to enter the name of the visitor that will appear on the ticket. Finally, a printable E-ticket is created with a QR-code that can be scanned in the cash office building


## Libraries used

* Tkinter
* PILL, ImageTk Image
* datetime
* qrcode


## Learned skills

* A deeper understanding of functions and arguments
* Work with dates and the datetime module
* Work with different frames in Tkinter
* Work with imported fonts
* Build a progressbarr
* Build an E-ticket
* Build QRcodes

<br>

* Making a plan of action
* Making a planning
* Making a moscow analysis
* Making a GUI design
* Basics of Git and Github
* Keep track of progress with trelloo


## How it works

The ordering process is started by clicking on the "Tickets Bestellen" button. By clicking on the arrows, visitors can be added to the ticket (per age category). Additional facilities can be added by checking the checkboxes.

When a step has been completed, visitors can press "Verder". If the want to go back, they can click "Terug"

After the last step and visitors have entered their name they can press on "Betalen" to pay and get the E-ticket.


## Preview

![screenshot_start](Showcase/screenshot_start.png?raw=true "Start screen")

![screenshot_input_persons](Showcase/screenshot_input_persons.png?raw=true "Fill in persons")

![screenshot_add_parking](Showcase/screenshot_add_parking.png?raw=true "Add daily rate parking")

![screenshot_add_facilities](Showcase/screenshot_add_facilities.png?raw=true "Add theatre")

![screenshot_input_name](Showcase/screenshot_input_name.png?raw=true "Fill in name")

![screenshot_eticket](Showcase/screenshot_eticket.png?raw=true "E-Ticket")