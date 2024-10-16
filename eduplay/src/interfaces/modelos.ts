// models.ts

// Interface para el modelo Profesor
export interface Profesor {
  id: number;
  nombre: string;
  email: string;
  contraseña: string;
  cursos?: Curso[]; // Opcional, ya que puede no tener cursos al inicio
}

// Interface para el modelo Curso
export interface Curso {
  id: number;
  nombre: string;
  descripcion: string;
  profesor_id: number;
  colegio: string;
  alumnos?: Alumno[]; // Opcional, ya que puede no tener alumnos al inicio
}

// Interface para el modelo Alumno
export interface Alumno {
  id: number;
  nombre: string;
  curso_id: number;
  grupo_id?: number | null; // Puede ser opcional o null
}

// Interface para el modelo Grupo
export interface Grupo {
  id: number;
  nombre: string;
  curso_id: number;
  alumnos?: Alumno[];
  progreso?: string[]; // Opcional, ya que puede no tener alumnos al inicio
}

export interface GrupoSeleccionado {
  id: number;
  nombre: string;
  curso_id: number;
  alumnos?: Alumno[];
  colegio: string;
  progreso?: string[];
}

export interface Nivel {
  id: string;
  name: string;
  puntajes: Puntaje[];
}

export interface Puntaje {
  id: string;
  name: string;
  completeAt?: Date;
}
