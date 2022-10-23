#py -m venv venv #create environment in terminal
#.venv\Scripts\activate #activate scripts
#pip install flask flask_squlalchemy
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

#relational databse
#uses tables

app = Flask (__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

app.app_context().push()

#Database Model
#Erase database everytime you create a new field/variable 
class Lugares(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(), nullable = False)
    nombre = db.Column(db.String(), nullable = False)
    direccion = db.Column(db.String(), nullable = False)
    telefono = db.Column(db.String, nullable = False)
    email = db.Column(db.String)
    instagram_url = db.Column(db.String)
    facebook_url = db.Column(db.String)
    opening_hours = db.Column(db.String, nullable = False)
    closing_hours = db.Column(db.String, nullable = False)
    monday = db.Column(db.Boolean, nullable = False)
    tuesday = db.Column(db.Boolean, nullable = False)
    wednesday = db.Column(db.Boolean, nullable = False)
    thursday = db.Column(db.Boolean, nullable = False)
    friday = db.Column(db.Boolean, nullable = False)
    saturday = db.Column(db.Boolean, nullable = False)
    sunday = db.Column(db.Boolean, nullable = False)
    description = db.Column(db.String)
    latitude = db.Column(db.Float, nullable = False)
    longitude = db.Column(db.Float, nullable = False)
    banner_url = db.Column(db.String, nullable = False)
    free_entry = db.Column(db.Boolean, nullable = False)
    parking = db.Column(db.Boolean, nullable = False)
    cash = db.Column(db.Boolean, nullable = False)
    tansfer = db.Column(db.Boolean, nullable = False)
    card = db.Column(db.Boolean, nullable = False)
    qr_pay = db.Column(db.Boolean, nullable = False)
    e_wallet = db.Column(db.Boolean, nullable = False)
    bike = db.Column(db.Boolean, nullable = False)
    car = db.Column(db.Boolean, nullable = False)
    bus = db.Column(db.Boolean, nullable = False)
    pickup_service = db.Column(db.Boolean, nullable = False)
    direction_ref = db.Column(db.String)
    accessible_bathroom = db.Column(db.Boolean, nullable = False) #changed from inclusive_bathroom
    ramp_access = db.Column(db.Boolean, nullable = False)
    wheelchair_available = db.Column(db.Boolean, nullable = False)
    wifi = db.Column(db.Boolean, nullable = False)
    pool = db.Column(db.Boolean, nullable = False)
    playground = db.Column(db.Boolean, nullable = False)
    gym = db.Column(db.Boolean, nullable = False)
    dining = db.Column(db.Boolean, nullable = False)
    tecnaso = db.Column(db.Boolean, nullable = False)
    #foreignkey to merge databases
    #places_images
    #id (int)
    #place_id (int)
    #image_url (string)


    def __init__(self, categoria, nombre, direccion, telefono, email, instagram_url, facebook_url, opening_hours, closing_hours, monday, tuesday, wednesday, thursday, friday, saturday, sunday, description, latitude, longitude, banner_url, free_entry, parking, cash, transfer, card, qr_pay, e_wallet, bike, car, bus, pickup_service, direction_ref, accessible_bathroom, ramp_access, wheelchair_available, wifi, pool, playground, gym, dining, tecnaso):
        self.categoria = categoria
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.instagram_url = instagram_url
        self.facebook_url = facebook_url
        self.opening_hours = opening_hours
        self.closing_hours = closing_hours
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.banner_url = banner_url
        self.free_entry = free_entry
        self.parking = parking
        self.cash = cash
        self.transfer = transfer
        self.card = card
        self.qr_pay = qr_pay
        self.e_wallet = e_wallet
        self.bike = bike
        self.car = car
        self.bus = bus
        self.pickup_service = pickup_service
        self.direction_ref = direction_ref
        self.accessible_bathroom = accessible_bathroom
        self.ramp_access = ramp_access
        self.wheelchair_available = wheelchair_available
        self.wifi = wifi
        self.pool = pool
        self.playground = playground
        self.gym = gym
        self.dining = dining
        self.tecnaso = tecnaso
        

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form/create', methods=['POST', 'GET'])
def create():
    #recibo del formulario el nombre de la categoria 
    categoria = request.form['categoria']
    telefono = request.form['telefono']

    #creo una instancia de mi objeto Form
    form = Lugares(categoria=categoria, wifi=False, telefono=telefono)  
    #Guardo una sesión y envio commit a la base de datos
    db.session.add(form)
    db.session.commit()
    return redirect(url_for('index'))

#command to create database: (py app.py) creates the database
#is created in an instance folder
#once created, from: "sqlite:///data.db" to "sqlite:///instance/data.db" 
#OR put dara.db outside intance folder
if __name__ == '__main__':
    db.create_all()