from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(255), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

    def save(self):
        db.session.add(self)
        
class Mesa(db.Model):
    __tablename__ = 'mesas'
    id = db.Column(db.Integer, primary_key=True)
    capacidad = db.Column(db.Integer, nullable=False)
    reservas = db.relationship('Reserva', backref='mesa', lazy=True)

class Horario(db.Model):
    __tablename__ = 'horarios'
    id = db.Column(db.Integer, primary_key=True)
    inicio = db.Column(db.Time, nullable=False)
    fin = db.Column(db.Time, nullable=False)
    reservas = db.relationship('Reserva', backref='horario', lazy=True)

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  
    mesa_id = db.Column(db.Integer, db.ForeignKey('mesas.id'), nullable=False)
    horario_id = db.Column(db.Integer, db.ForeignKey('horarios.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
