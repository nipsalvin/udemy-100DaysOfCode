from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
import random
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
API_KEY = os.getenv('POSTMAN_CAFE_API_KEY')
##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        ## Method 1 ##
        dictionary = {}
        ## Loop through each column in the data record
        for column in self.__table__.columns:
            ## Create a new dictionary entry;
            ## where the key is the name of the column
            ## and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name) #getattr(x, 'y') is equivalent to x.y
        return dictionary
        
        # ## Method 2 (Dictionary Comprehension)##
        # dictionary = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        # return dictionary

# with app.app_context():
#     db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

## HTTP GET - Read Record
### 'GET' is allowed by default on all routes.
@app.route('/random', methods=['GET'])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    # ## Method 1
    # return jsonify(
    #     cafe={
    #         "name": random_cafe.name,
    #         "map_url": random_cafe.map_url,
    #         "img_url": random_cafe.img_url,
    #         "location": random_cafe.location,
    #         "amenities":{
    #             "seats": random_cafe.seats,
    #             "has_toilet": random_cafe.has_toilet,
    #             "has_wifi": random_cafe.has_wifi,
    #             "has_sockets": random_cafe.has_sockets,
    #             "can_take_calls": random_cafe.can_take_calls,
    #             "coffee_price": random_cafe.coffee_price,
    #             }
    #         })
    
    #Simply convert the random_cafe data record to a dictionary of key-value pairs. 
    return jsonify(cafe=random_cafe.to_dict())

@app.route('/all')
def all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    cafes=[cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafes)

@app.route('/search')
def get_cafe_at_location():
    query_location = request.args.get("loc")
    all_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == query_location)).scalars().all()
    query_name = request.args.get('name')
    all_cafes_name = db.session.execute(db.select(Cafe).where(Cafe.name == query_name)).scalars().all()
    if all_cafes:
        return jsonify(cafe = [cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error = {'Not Found': 'Sorry, We do not have a cafe at that location.'}), 404
    # if all_cafes_name:
    #     return jsonify(cafe = [cafe.to_dict() for cafe in all_cafes_name])
    # else:
    #     return jsonify(error = {'Not Found': 'Sorry, We do not have a cafe like that.'}), 404


## HTTP POST - Create Record
@app.route("/add", methods=['GET',"POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'), #This is safer because it will return None if the field is not present or if its value is empty
        # map_url = request.form['map_url'], #This will raise a KeyError exception if the field is not present or if its value is empty.
        map_url = request.form.get('map_url'),
        img_url = request.form.get('img_url'),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    with app.app_context():
        db.session.add(new_cafe)
        db.session.commit()
    return jsonify(response = {
        'success':f'Successfully added the {new_cafe}.'
    })

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    # cafe = db.get_or_404(Cafe, cafe_id) #If no object is found, It returns a 404 error instead of None
    cafe = db.session.get(Cafe, cafe_id) #If no object is found it returns None instead of a 404 error
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(resonse = {'success':'Successfully updated the price.'}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


## HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == API_KEY:
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            cafe_name = cafe.name
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": f"Successfully deleted the {cafe_name} from the database."}), 200
        else:
           return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
