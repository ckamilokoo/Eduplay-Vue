from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Profesor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.String(1000), nullable=False)
    cursos = db.relationship('Curso', backref='profesor', lazy=True)

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    profesor_id = db.Column(db.Integer, db.ForeignKey('profesor.id'), nullable=False)
    colegio=db.Column(db.Text, nullable=False)
    alumnos = db.relationship('Alumno', backref='curso', lazy=True)

class Alumno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    grupo_id = db.Column(db.Integer, db.ForeignKey('grupo.id'), nullable=True)

class Grupo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    colegio = db.Column(db.String(100), nullable=False)  # Cambiado a String simple
    alumnos = db.relationship('Alumno', backref='grupo', lazy=True)
    progreso = db.Column(db.String, nullable=True)

    @classmethod
    def create_with_course(cls, nombre, curso):
        colegio = curso.colegio
        grupo = cls(nombre=nombre, curso_id=curso.id, colegio=colegio)
        db.session.add(grupo)
        db.session.commit()
        return grupo
