from flask import Blueprint, render_template, current_app, send_from_directory, request, redirect, url_for , flash ,jsonify
from app.modelo.sql import db, Profesor , Curso , Alumno ,Grupo
from bleak import BleakClient
from werkzeug.security import generate_password_hash
import random  # Importar el módulo random


main_bp = Blueprint('main', __name__)


@main_bp.route('/crear_grupos/<int:curso_id>/<int:tamano_grupo>', methods=['POST'])
def crear_grupos(curso_id, tamano_grupo):
    # Obtener los alumnos del curso especificado
    alumnos = Alumno.query.filter_by(curso_id=curso_id).all()
    
    # Convertir a lista de alumnos
    alumnos_list = [alumno for alumno in alumnos]

    # Barajar la lista de alumnos
    random.shuffle(alumnos_list)

    # Crear grupos
    grupos = []
    for i in range(0, len(alumnos_list), tamano_grupo):
        grupo = alumnos_list[i:i + tamano_grupo]
        grupos.append(grupo)

    # Crear y guardar los grupos en la base de datos
    for index, grupo in enumerate(grupos):
        nuevo_grupo = Grupo(nombre=f'Grupo {index + 1}', curso_id=curso_id)
        db.session.add(nuevo_grupo)
        db.session.commit()  # Guardar el grupo en la base de datos

        # Asignar el grupo a los alumnos
        for alumno in grupo:
            alumno.grupo_id = nuevo_grupo.id  # Asignar el grupo al alumno
            db.session.commit()  # Guardar los cambios

    flash('Grupos creados exitosamente.', 'success')
    return redirect(url_for('main.registro'))


@main_bp.route('/grupos', methods=['GET'])
def get_grupos():
    # Obtener todos los grupos de la base de datos
    grupos = Grupo.query.all()
    
    # Convertir los grupos a un formato que jsonify pueda manejar
    grupos_list = []
    for grupo in grupos:
        grupos_list.append({
            'id': grupo.id,
            'nombre': grupo.nombre,
            'curso_id': grupo.curso_id,
            'alumnos': [{'id': alumno.id, 'nombre': alumno.nombre} for alumno in grupo.alumnos]
        })
    
    # Devolver la lista de grupos como respuesta JSON
    return jsonify(grupos_list)

@main_bp.route('/cursos', methods=['GET'])
def get_cursos():
    # Obtener todos los cursos de la base de datos
    cursos = Curso.query.all()
    
    # Convertir los cursos a un formato que jsonify pueda manejar
    cursos_list = []
    for curso in cursos:
        cursos_list.append({
            'id': curso.id,
            'nombre': curso.nombre,
            'descripcion': curso.descripcion,
            'profesor_id': curso.profesor_id,
            'colegio': curso.colegio,
            'profesor_nombre': curso.profesor.nombre  # Para incluir el nombre del profesor
        })
    
    # Devolver la lista de cursos como respuesta JSON
    return jsonify(cursos_list)

@main_bp.route('/alumnos', methods=['GET'])
def get_alumnos():
    # Obtener todos los alumnos de la base de datos
    alumnos = Alumno.query.all()
    
    # Convertir los alumnos a un formato que jsonify pueda manejar
    alumnos_list = []
    for alumno in alumnos:
        alumnos_list.append({
            'id': alumno.id,
            'nombre': alumno.nombre,
            'curso_id': alumno.curso_id,
            'grupo_id': alumno.grupo_id,
            'curso_nombre': alumno.curso.nombre,  # Para incluir el nombre del curso
            'grupo_nombre': alumno.grupo.nombre if alumno.grupo else None  # Incluir el nombre del grupo si existe
        })
    
    # Devolver la lista de alumnos como respuesta JSON
    return jsonify(alumnos_list)



@main_bp.route('/eliminar_grupo/<int:grupo_id>', methods=['POST'])
def eliminar_grupo(grupo_id):
    # Buscar el grupo por su ID
    grupo = Grupo.query.get(grupo_id)

    if not grupo:
        flash('El grupo no existe.', 'error')
        return redirect(url_for('main.registro'))

    # Opción 1: Eliminar la relación entre los alumnos y el grupo
    for alumno in grupo.alumnos:  # Asegúrate de que la relación esté definida en el modelo
        alumno.grupo_id = None  # Eliminar la asignación del grupo
        db.session.add(alumno)  # Añadir el alumno actualizado a la sesión

    # Opción 2: Eliminar el grupo
    db.session.delete(grupo)  # Eliminar el grupo de la base de datos
    db.session.commit()  # Guardar los cambios

    flash('Grupo eliminado exitosamente.', 'success')
    return redirect(url_for('main.registro'))



@main_bp.route('/registro', methods=['GET'])
def registro():
    profesores = Profesor.query.all()
    cursos = Curso.query.all()  # Obtener la lista de cursos
    alumnos = Alumno.query.all()  # Obtener la lista de alumnos
    grupos = Grupo.query.all()  # Obtener la lista de grupos
    
    return render_template('registro.html', profesores=profesores, cursos=cursos, alumnos=alumnos, grupos=grupos)

@main_bp.route('/crear_alumno', methods=['POST'])
def crear_alumno():
    nombre = request.form.get('nombre')
    
    curso_id = request.form.get('curso_id')
    grupo_id = request.form.get('grupo_id')

    if not nombre   or not curso_id:
        flash('Todos los campos son requeridos', 'error')
        return redirect(url_for('main.registro'))

    nuevo_alumno = Alumno(nombre=nombre, curso_id=curso_id, grupo_id=grupo_id)
    db.session.add(nuevo_alumno)
    db.session.commit()
    flash('Alumno creado exitosamente', 'success')
    return redirect(url_for('main.registro'))

@main_bp.route('/eliminar_alumno/<int:id>', methods=['POST'])
def eliminar_alumno(id):
    alumno = Alumno.query.get(id)
    if alumno:
        db.session.delete(alumno)
        db.session.commit()
        flash('Alumno eliminado exitosamente', 'success')
    else:
        flash('Alumno no encontrado', 'error')
    return redirect(url_for('main.registro'))

@main_bp.route('/crear_curso', methods=['POST'])
def crear_curso():
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    profesor_id = request.form.get('profesor_id')
    colegio = request.form.get('colegio')

    # Validar que todos los campos estén completos
    if not nombre or not descripcion or not profesor_id:
        flash('Todos los campos son obligatorios.', 'error')
        return redirect(url_for('main.registro'))

    # Crear un nuevo curso
    nuevo_curso = Curso(
        nombre=nombre,
        descripcion=descripcion,
        profesor_id=int(profesor_id),
        colegio=colegio# Convertir a entero
    )

    # Guardar en la base de datos
    db.session.add(nuevo_curso)
    db.session.commit()

    flash('Curso creado exitosamente.', 'success')
    return redirect(url_for('main.registro'))

@main_bp.route('/eliminar_curso/<int:id>', methods=['POST'])
def eliminar_curso(id):
    # Buscar el curso por ID
    curso = Curso.query.get(id)
    
    if not curso:
        flash('Curso no encontrado.', 'error')
        return redirect(url_for('main.registro'))
    
    # Eliminar el curso de la base de datos
    db.session.delete(curso)
    db.session.commit()
    
    flash('Curso eliminado con éxito.', 'success')
    return redirect(url_for('main.registro'))


@main_bp.route('/registro_profesor', methods=['POST'])
def profesor_registro():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    contraseña = request.form.get('contraseña')

    # Validar que todos los campos estén completos
    if not nombre or not email or not contraseña:
        flash('Todos los campos son obligatorios.', 'error')
        return redirect(url_for('main.registro'))

    # Validar si el correo ya existe en la base de datos
    profesor_existente = Profesor.query.filter_by(email=email).first()
    if profesor_existente:
        flash('El correo ya está registrado.', 'error')
        return redirect(url_for('main.registro'))

    # Crear un nuevo profesor
    nuevo_profesor = Profesor(
        nombre=nombre,
        email=email,
        contraseña=generate_password_hash(contraseña)  # Encriptar la contraseña
    )

    # Guardar en la base de datos
    db.session.add(nuevo_profesor)
    db.session.commit()

    flash('Registro exitoso del profesor.', 'success')
    return redirect(url_for('main.registro'))

@main_bp.route('/eliminar_profesor/<int:id>', methods=['POST'])
def eliminar_profesor(id):
    # Buscar el profesor por ID
    profesor = Profesor.query.get(id)
    
    if not profesor:
        flash('Profesor no encontrado.', 'error')
        return redirect(url_for('main.registro'))
    
    # Eliminar el profesor de la base de datos
    db.session.delete(profesor)
    db.session.commit()
    
    flash('Profesor eliminado con éxito.', 'success')
    return redirect(url_for('main.registro'))
    




