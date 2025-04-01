from flask import Blueprint, render_template, current_app, send_from_directory, request, redirect, url_for , flash ,jsonify
from app.modelo.sql import db, Profesor , Curso , Alumno ,Grupo
from bleak import BleakClient
from werkzeug.security import generate_password_hash
import random  # Importar el módulo random
from app.modelo.supabase_client import supabase


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def registro():
    # Consultas a Supabase
    profesores = supabase.table('profesor').select('*').execute().data
    print("profesores :", profesores)
    
    cursos = supabase.table('curso').select('*').execute().data
    print("cursos:", cursos)
    
    # Obtener los alumnos y agruparlos por grupo_id
    alumnos = supabase.table('alumno').select('*').execute().data
    print("alumnos :", alumnos)
    
    # Agrupar los alumnos por grupo_id
    grupos_alumnos = {}
    for alumno in alumnos:
        grupo_id = alumno.get('grupo_id')
        if grupo_id not in grupos_alumnos:
            grupos_alumnos[grupo_id] = []
        grupos_alumnos[grupo_id].append(alumno)
    
    # Consultar los grupos
    grupos = supabase.table('grupo').select('*').execute().data
    print("grupos :", grupos)
    
    # Asociar los alumnos a cada grupo
    for grupo in grupos:
        grupo['alumnos'] = grupos_alumnos.get(grupo['id'], [])

    return render_template(
        'registro.html', 
        profesores=profesores, 
        cursos=cursos, 
        alumnos=alumnos, 
        grupos=grupos
    )



@main_bp.route('/grupos', methods=['GET'])
def get_grupos():
    try:
        # Obtener todos los grupos de la base de datos y la información del curso asociado
        response = supabase.from_('grupo').select('id, nombre, curso_id, progreso, curso(nombre as curso_nombre), alumnos(id, nombre)').execute()
        data, error = response.data, response.error

        if error:
            print(f"Error al obtener los grupos: {error}")
            return jsonify({"error": "Error al obtener los grupos"}), 500

        grupos_list = []
        for grupo in data:
            grupo_formateado = {
                'id': grupo['id'],
                'nombre': grupo['nombre'],
                'curso_id': grupo['curso_id'],
                'progreso': grupo.get('progreso') if grupo.get('progreso') is not None else 'Sin progreso',
                'alumnos': [{'id': alumno['id'], 'nombre': alumno['nombre']} for alumno in grupo.get('alumnos', [])]
            }
            grupos_list.append(grupo_formateado)

        return jsonify(grupos_list)

    except Exception as e:
        print(f"Error inesperado al obtener los grupos: {e}")
        return jsonify({"error": "Error inesperado al obtener los grupos"}), 500

@main_bp.route('/crear_grupos/<int:curso_id>/<int:tamano_grupo>', methods=['POST'])
def crear_grupos(curso_id, tamano_grupo):
    # 1️⃣ Obtener los alumnos del curso desde Supabase
    response = supabase.table('alumno').select('*').eq('curso_id', curso_id).execute()
    alumnos = response.data if response.data else []
    
    if not alumnos:
        flash('No hay alumnos en este curso.', 'warning')
        return redirect(url_for('main.registro'))

    # 2️⃣ Obtener el colegio del curso
    curso_response = supabase.table('curso').select('colegio').eq('id', curso_id).execute()
    curso_data = curso_response.data

    if not curso_data:
        flash('El curso no existe.', 'error')
        return redirect(url_for('main.registro'))

    colegio = curso_data[0]['colegio']  # Obtener el colegio del curso

    # 3️⃣ Barajar la lista de alumnos
    random.shuffle(alumnos)

    # 4️⃣ Crear grupos en Supabase
    grupos = []
    for i in range(0, len(alumnos), tamano_grupo):
        grupo_alumnos = alumnos[i:i + tamano_grupo]

        # Crear un nuevo grupo con el colegio
        grupo_nombre = f"Grupo {len(grupos) + 1}"
        grupo_response = supabase.table('grupo').insert({
            'nombre': grupo_nombre,
            'curso_id': curso_id,
            'colegio': colegio  # ✅ Se agrega el campo colegio
        }).execute()
        
        if grupo_response.data:
            grupo_id = grupo_response.data[0]['id']
            grupos.append({'id': grupo_id, 'nombre': grupo_nombre})

            # 5️⃣ Asignar `grupo_id` a los alumnos del grupo
            for alumno in grupo_alumnos:
                supabase.table('alumno').update({'grupo_id': grupo_id}).eq('id', alumno['id']).execute()

    flash('Grupos creados exitosamente.', 'success')
    return redirect(url_for('main.registro'))

    
@main_bp.route('/crear_curso', methods=['POST'])
def crear_curso():
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    profesor_id = request.form.get('profesor_id')
    colegio = request.form.get('colegio')  # Nuevo campo

    # Validar que los campos no estén vacíos
    if not nombre or not descripcion or not profesor_id or not colegio:
        flash('Todos los campos son requeridos', 'error')
        return redirect(url_for('main.registro'))

    # Insertar el curso en Supabase
    data = supabase.table('curso').insert({
        "nombre": nombre,
        "descripcion": descripcion,
        "profesor_id": int(profesor_id),  # Asegurar que es un entero
        "colegio": colegio
    }).execute()

    print("Curso creado:", data)

    flash('Curso creado exitosamente', 'success')
    return redirect(url_for('main.registro'))

    
@main_bp.route('/eliminar_curso/<int:id>', methods=['POST'])
def eliminar_curso(id):
    try:
        response = supabase.from_('curso').delete().eq('id', id).execute()
        if response.data:
            flash('Curso eliminado exitosamente', 'success')
        else:
            flash('Curso no encontrado', 'error')
    except Exception as e:
        flash(f"Error al eliminar curso: {str(e)}", "error")

    return redirect(url_for('main.registro'))

    
@main_bp.route('/eliminar_alumno/<int:id>', methods=['POST'])
def eliminar_alumno(id):
    try:
        # Eliminar el alumno por ID en Supabase
        response = supabase.table("alumno").delete().eq("id", id).execute()
        
        if response.data:
            flash('Alumno eliminado exitosamente', 'success')
        else:
            flash('Alumno no encontrado', 'error')
    
    except Exception as e:
        flash(f"Error al eliminar alumno: {str(e)}", "error")

    return redirect(url_for('main.registro'))    
    
    
    
@main_bp.route('/registro_profesor', methods=['POST'])
def profesor_registro():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    contraseña = request.form.get('contraseña')
    print(nombre , email ,contraseña)
    # Validar que todos los campos estén completos
    if not nombre or not email or not contraseña:
        flash('Todos los campos son obligatorios.', 'error')
        return redirect(url_for('main.registro'))

    try:
        # Validar si el correo ya existe en la base de datos de Supabase
        response = supabase.from_('profesor').select('email').eq('email', email).execute()
        data = response.data
        print(data)
        

        

        # Crear un nuevo profesor en Supabase
        hashed_password = generate_password_hash(contraseña)
        response = supabase.from_('profesor').insert([{'nombre': nombre, 'email': email, 'contraseña': hashed_password}]).execute()
        data = response.data

        

        flash('Registro exitoso del profesor.', 'success')
        return redirect(url_for('main.registro'))

    except Exception as e:
        flash(f'Ocurrió un error inesperado: {e}', 'error')
        return redirect(url_for('main.registro'))
    
    
@main_bp.route('/eliminar_profesor/<int:id>', methods=['POST'])
def eliminar_profesor(id):
    try:
        # Eliminar el profesor de la base de datos de Supabase por ID
        response = supabase.from_('profesor').delete().eq('id', id).execute()
        data = response.data
        print(data)
        
          # Redirige a la página apropiada

        if response.count == 0:
            flash('Profesor no encontrado.', 'error')
            return redirect(url_for('main.registro'))  # Redirige a la página apropiada

        flash('Profesor eliminado con éxito.', 'success')
        return redirect(url_for('main.registro'))  # Redirige a la página apropiada

    except Exception as e:
        flash(f'Ocurrió un error inesperado: {e}', 'error')
        return redirect(url_for('main.registro'))


@main_bp.route('/crear_alumno', methods=['POST'])
def crear_alumno():
    nombre = request.form.get('nombre')
    curso_id = request.form.get('curso_id')
    grupo_id = request.form.get('grupo_id')

    if not nombre or not curso_id:
        flash('Todos los campos son requeridos', 'error')
        return redirect(url_for('main.registro'))

    # Insertar en Supabase
    data = {
        "nombre": nombre,
        "curso_id": int(curso_id),  # Asegurar tipo correcto
        "grupo_id": int(grupo_id) if grupo_id else None
    }
    
    response = supabase.table("alumno").insert(data).execute()

    if response.data:
        flash('Alumno creado exitosamente', 'success')
    else:
        flash('Error al crear el alumno', 'error')

    return redirect(url_for('main.registro')) 

@main_bp.route('/eliminar_grupo/<int:grupo_id>', methods=['POST'])
def eliminar_grupo(grupo_id):
    # 1️⃣ Verificar si el grupo existe en Supabase
    grupo_response = supabase.table('grupo').select('*').eq('id', grupo_id).execute()

    if not grupo_response.data:
        flash('El grupo no existe.', 'error')
        return redirect(url_for('main.registro'))

    # 2️⃣ Eliminar la relación entre alumnos y el grupo (poner grupo_id en NULL)
    supabase.table('alumno').update({'grupo_id': None}).eq('grupo_id', grupo_id).execute()

    # 3️⃣ Eliminar el grupo de la base de datos
    supabase.table('grupo').delete().eq('id', grupo_id).execute()

    flash('Grupo eliminado exitosamente.', 'success')
    return redirect(url_for('main.registro'))


