from flask import Flask, render_template, request, redirect,  url_for

app = Flask(__name__)  

Fname=None
Lname=None
Age=None
Gfname=None
Glname=None
Air=None
category=None
deck=None
room=None
place=None
spot=None
confirm=None
COUNT = 5
counter=0


@app.route("/reservation.html") 
def my_home(): 
    return render_template('reservation.html') 



@app.route('/submit_reservation', methods=['POST', 'GET'])
def submit_reservation():
    if request.method == 'POST':
        data = request.form.to_dict()
        global Fname 
        global Lname 
        Fname = data["Fname"]
        Lname = data["Lname"]
        if ((str(data["Fname"])=="Alexandre") and (str(data["Lname"])=="Petrenko")) or ((str(data["Fname"])=="Arnaud") and (str(data["Lname"])=="Dury")) or ((str(data["Fname"])=="ElHachemi") and (str(data["Lname"])=="AliKacem")) or ((str(data["Fname"])=="May") and (str(data["Lname"])=="Haydar")) or ((str(data["Fname"])=="Hesham") and (str(data["Lname"])=="Hallal")) or ((str(data["Fname"])=="Serge") and (str(data["Lname"])=="Boroday")) or ((str(data["Fname"])=="Nicolas") and (str(data["Lname"])=="Gorse")) or ((str(data["Fname"])=="Etienne") and (str(data["Lname"])=="Bergeron")):
            return redirect('setAge.html')
        else:
            return redirect('rejection.html')
    else:
        return 'something went wrong. Try again!'
    
@app.route("/rejection.html") 
def rejection(): 
    global counter
    counter += 1
    if counter >= COUNT:
        return render_template('HTTPflood.html')
    return render_template('rejection.html') 
    
@app.route("/setAge.html") 
def Age(): 
    return render_template('setAge.html') 

@app.route('/submit_setAge', methods=['POST', 'GET'])
def submit_setAge():
    if request.method == 'POST':
        data = request.form.to_dict()
        global Age 
        Age = data["Age"]
        if int(data["Age"]) <= 14:
            return redirect('guardian.html')
        else:
            global Gfname
            Gfname=None
            global Glname
            Glname=None 
            return redirect('setCategory.html')
    else:
        return 'something went wrong. Try again!'


@app.route("/guardian.html") 
def guardian(): 
    return render_template('guardian.html') 

@app.route('/submit_guardian', methods=['POST', 'GET'])
def submit_guardian():
    if request.method == 'POST':
        data = request.form.to_dict()
        global Gfname
        global Glname
        Gfname = data["Gfname"]
        Glname = data["Glname"]
        if ((str(data["Gfname"])=="Alexandre") and (str(data["Glname"])=="Petrenko")) or ((str(data["Gfname"])=="Arnaud") and (str(data["Glname"])=="Dury")) or ((str(data["Gfname"])=="ElHachemi") and (str(data["Glname"])=="AliKacem")) or ((str(data["Gfname"])=="May") and (str(data["Glname"])=="Haydar")) or ((str(data["Gfname"])=="Hesham") and (str(data["Glname"])=="Hallal")) or ((str(data["Gfname"])=="Serge") and (str(data["Glname"])=="Boroday")) or ((str(data["Gfname"])=="Nicolas") and (str(data["Glname"])=="Gorse")) or ((str(data["Gfname"])=="Etienne") and (str(data["Glname"])=="Bergeron")):
            return redirect('setCategory.html')
        else:
            return redirect('rejection.html')
    else:
        return 'something went wrong. Try again!'
    
@app.route("/setCategory.html") 
def category(): 
    return render_template('setCategory.html') 

@app.route('/submit_setCategory', methods=['POST', 'GET'])
def submit_setCategory():
    if request.method == 'POST':
        data = request.form.to_dict()
        global Air
        global category
        global deck
        Air = data["Air"]
        category = data["category"]
        deck = data["deck"]
        if (str(data["deck"]) == "Lower") and (str(data["category"]) == "Luxury"):
            global room
            room=None
            global spot
            spot=None
            return redirect('bedroomSports.html')
        elif (str(data["deck"]) == "Upper") and (int(data["Air"]) < 10000):
            return redirect('notEnoughAM.html')
        elif (str(data["deck"]) == "Upper") and (str(data["category"]) == "Luxury") and (int(data["Air"]) >= 10000):
            global place
            place=None
            spot=None
            return redirect('roomType.html')
        elif (str(data["deck"]) == "Upper") and (str(data["category"]) == "Tourist") and (int(data["Air"]) >= 10000):
            place=None
            room=None
            return redirect('windowAlley.html')
        elif (str(data["deck"]) == "Lower") and (str(data["category"]) == "Tourist"):
            place=None
            room=None
            return redirect('windowAlley.html')
    else:
        return 'something went wrong. Try again!'
    
@app.route("/notEnoughAM.html") 
def notEnough():
    global counter
    counter += 1
    if counter >= COUNT:
        return render_template('HTTPflood.html')
    return render_template('notEnoughAM.html')  

@app.route("/roomType.html") 
def room(): 
    return render_template('roomType.html') 

@app.route('/submit_roomType', methods=['POST', 'GET'])
def submit_roomType():
    if request.method == 'POST':
        data = request.form.to_dict()
        global room
        room = data["room"]
        return redirect('flightDetails.html')
    else:
        return 'something went wrong. Try again!'

@app.route("/bedroomSports.html") 
def bedroomSports(): 
    return render_template('bedroomSports.html') 

@app.route('/submit_bedroomSports', methods=['POST', 'GET'])
def submit_bedroomSports():
    if request.method == 'POST':
        data = request.form.to_dict()
        global place
        place = data["place"]
        return redirect('flightDetails.html')
    else:
        return 'something went wrong. Try again!'
    
@app.route("/windowAlley.html") 
def windowAlley(): 
    return render_template('windowAlley.html') 

@app.route('/submit_windowAlley', methods=['POST', 'GET'])
def submit_windowAlley():
    if request.method == 'POST':
        data = request.form.to_dict()
        global spot
        spot = data["spot"]
        return redirect('flightDetails.html')
    else:
        return 'something went wrong. Try again!'
    
    
@app.route("/flightDetails.html") 
def details(): 
    return render_template('flightDetails.html',Fname=Fname, Lname=Lname, Age=Age, Gfname=Gfname, Glname=Glname, Air=Air, category=category, deck=deck, room=room, place=place, spot=spot)

@app.route('/submit_details', methods=['POST', 'GET'])
def submit_details():
    if request.method == 'POST':
        data = request.form.to_dict()
        global confirm
        confirm = data["confirm"]
        if (str(data["confirm"]) == "New Reservation"):
            return redirect('reservation.html')
        else:
            return redirect('final.html')
    else:
        return 'something went wrong. Try again!'
    
@app.route("/final.html") 
def final(): 
    return render_template('final.html') 
