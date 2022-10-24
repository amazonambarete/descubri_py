#py -m venv venv #create environment in terminal
#.venv\Scripts\activate #activate scripts
#pip install flask flask_squlalchemy
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
#relational databse
#uses tables

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.app_context().push()

#Database Model
#Erase database everytime you create a new field/variable 
class Lugares(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(), nullable = False)
    name = db.Column(db.String(), nullable = False)
    description = db.Column(db.String)
    banner_url = db.Column(db.String, nullable = False)
    direction = db.Column(db.String(), nullable = False)
    direction_ref = db.Column(db.String)
    latitude = db.Column(db.Float, nullable = False)
    longitude = db.Column(db.Float, nullable = False)
    bike = db.Column(db.Boolean, nullable = False)
    car = db.Column(db.Boolean, nullable = False)
    bus = db.Column(db.Boolean, nullable = False)
    pickup_service = db.Column(db.Boolean, nullable = False)
    phone_number = db.Column(db.String, nullable = False)
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
    free_entry = db.Column(db.Boolean, nullable = False)
    parking = db.Column(db.Boolean, nullable = False)
    cash = db.Column(db.Boolean, nullable = False)
    transfer = db.Column(db.Boolean, nullable = False)
    card = db.Column(db.Boolean, nullable = False)
    qr_pay = db.Column(db.Boolean, nullable = False)
    e_wallet = db.Column(db.Boolean, nullable = False)
    accessible_bathroom = db.Column(db.Boolean, nullable = False) 
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

    def __init__(self, category, name, direction, phone_number, email, instagram_url, facebook_url, opening_hours, closing_hours, monday, tuesday, wednesday, thursday, friday, saturday, sunday, description, latitude, longitude, banner_url, free_entry, parking, cash, transfer, card, qr_pay, e_wallet, bike, car, bus, pickup_service, direction_ref, accessible_bathroom, ramp_access, wheelchair_available, wifi, pool, playground, gym, dining, tecnaso):
        self.category = category
        self.name = name
        self.direction = direction
        self.direction_ref = direction_ref
        self.phone_number = phone_number
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
    return "este es el Homepage"

@app.get('/registro')
def show_form():
    #recibo del formulario el nombre de la categoria 
   #recibo del formulario el nombre de la categoria 
    #recibo del formulario el nombre de la categoria 
    #query por el id del negocio
    #un endpoint que me traiga todo
    results = db.session.query(Lugares).all()
    json_list = [i.to_dict() for i in results]
    return json_list

@app.post('/registro')
def submit_form(): 

    payment_methods = request.form.getlist('payment_method')
    transport_available = request.form.getlist('transport_available')
    inclusive_features = request.form.getlist('inclusive_features')
    ammenities = request.form.getlist('ammenities')
    weekdays = request.form.getlist('weekday')
    category = request.form['category']
    name = request.form['name']
    description = request.form['description']
    banner_url = request.form['banner_url']    
    direction = request.form['direction']
    direction_ref = request.form['direction_ref']
    latitude = request.form['latitude'] 
    longitude = request.form['longitude']
    phone_number = request.form['phone_number']
    email = request.form['email']
    instagram_url = request.form['instagram_url']
    facebook_url = request.form['facebook_url']
    opening_hours = request.form['opening_hours']
    closing_hours = request.form['closing_hours']
    monday = 'monday' in weekdays
    tuesday = 'tuesday' in weekdays
    wednesday = 'wednesday' in weekdays
    thursday = 'thursday' in weekdays
    friday = 'friday' in weekdays
    saturday = 'saturday' in weekdays
    sunday = 'sunday' in weekdays
    free_entry = request.form['free_entry'] == '1'
    parking = request.form['free_entry'] == '1'
    cash = 'cash' in payment_methods
    transfer = 'transfer' in payment_methods
    card = 'card' in payment_methods
    qr_pay = 'qr_pay' in payment_methods          
    e_wallet = 'e_wallet' in payment_methods
    bike = 'bike' in transport_available
    car = 'car' in transport_available
    bus = 'bus' in transport_available
    pickup_service = 'pickup_service' in transport_available  
    accessible_bathroom = 'accessible_bathroom' in inclusive_features
    ramp_access = 'ramp_access' in inclusive_features
    wheelchair_available = 'wheelchair_available' in inclusive_features
    wifi = 'wifi' in ammenities
    pool = 'pool' in ammenities
    playground = 'playground' in ammenities
    gym = 'gym' in ammenities
    dining = 'dining' in ammenities
    tecnaso = 'tecnaso' in ammenities
    
    #creo una instancia de mi objeto Lugares
    new_place = Lugares(category=category, name=name, direction=direction, direction_ref=direction_ref, latitude=latitude, longitude=longitude, phone_number=phone_number, email=email, instagram_url=instagram_url, facebook_url=facebook_url, opening_hours=opening_hours, closing_hours=closing_hours, monday=monday, tuesday=tuesday, wednesday=wednesday, thursday=thursday, friday=friday, saturday=saturday, sunday=sunday, description=description, banner_url=banner_url, free_entry=free_entry, parking=parking, cash=cash, transfer=transfer, card=card, qr_pay=qr_pay, e_wallet=e_wallet, bike=bike, car=car, bus=bus, pickup_service=pickup_service, accessible_bathroom=accessible_bathroom, ramp_access=ramp_access, wheelchair_available=wheelchair_available, wifi=wifi, pool=pool, playground=playground, gym=gym, dining=dining, tecnaso=tecnaso)  
    #Guardo una sesión y envio commit a la base de datos
    db.session.add(new_place)
    db.session.commit()
    #return redirect(url_for('index'))
    #return json que diga datos agregados correctamente
    return "ahora volvemos a la pagina de inicio caso quieras registrar otro local o punto turístico"

#command to create database: (py app.py) creates the database
#is created in an instance folder
#once created, from: "sqlite:///data.db" to "sqlite:///instance/data.db" 
#OR put dara.db outside intance folder
if __name__ == '__main__':
    db.create_all()