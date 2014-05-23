from eve import Eve
from eve.io.sql import SQL, ValidatorSQL
from tables import Users, Stores, HealthAdvisors, MyStores
from flask import request, jsonify, g

app = Eve(validator=ValidatorSQL, data=SQL)

@app.route('/users/register', methods = ['POST'])
def register():
    username = request.form['firstname']
    password = request.form['password']
    if username is None or password is None:
        return jsonify ({'message': 'missing arguments'})
    if Users.query.filter_by(firstname=username).first() is not None:
        return ({'message':'user already exist'})
    user = Users(firstname=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify ({'status':'ok', 'username': username})

@app.route('/stores', methods = ['POST', 'GET'])
def stores(self):
    storename = request.form['storename']
    address = request.form['address']
    contact = request.form['contact']
    if storename is None or address is None or contact is None:
        return jsonify ({'message': 'missing arguments'})
    if Stores.query.filter_by(storename=storename).first() is not None:
        return jsonify ({'message':'store already exist'})
    store = Stores(storename=storename, address=address, contact=contact)
    db.session.add(store)
    db.session.commit()
    return jsonify ({'status':'ok'})

@app.route('/stores/<int:id>/healthadvisors', methods = ['POST'])
def postadvisors(id):
    store = Stores.query.get(id)
    name = request.form['name']
    specialty = request.form['specialty']
    if name is None or specialty is None:
        return jsonify ({'message':'missing arguments'})
    if HealthAdvisors.query.filter_by(name=name).first() is not None:
        return jsonify ({'message': 'health advisor already exist'})
    advisor = HealthAdvisors(name=name, specialty=specialty, store=store._id)
    db.session.add(advisor)
    db.session.commit()
    return jsonify ({'status':'ok'})

@app.route('/stores/<int:id>/healthadvisors')#, methods = ['GET'])
def getadvisors(id):
    advisor = HealthAdvisors.query.filter_by(store=id)
    cols = ['name', 'specialty']
    result = [{col: getattr(d, col) for col in cols} for d in advisor]
    return jsonify(healthadvisors=result)

@app.route('/users/<int:id>/mystore', methods = ['POST'])
def postmystore(id):
    user = Users.query.get(id)
    store = Stores.query.get(id)
    storename = request.form['storename']
    if storename is None:
        return jsonify ({'message': 'missing arguments'})
    if not Stores.query.filter_by(storename=storename).first():
        return jsonify ({'message':'store does not exist'})
    if MyStores.query.filter_by(username=user._id, storename=storename).first() is not None:
         return jsonify ({'message':'store already exist'})
    mystore = MyStores(username=user._id, storename=storename)
    db.session.add(mystore)
    db.session.commit()
    return jsonify ({'status':'ok'})

@app.route('/users/<int:id>/mystore')
def getmystore(id):
    user = MyStores.query.filter_by(username=id) 
    cols = ['storename']
    result = [{col: getattr(d, col) for col in cols} for d in user]
    return jsonify(mystores=result)

db = app.data.driver
db.create_all()
app.run(debug=True)


