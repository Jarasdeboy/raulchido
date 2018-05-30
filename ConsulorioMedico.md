# Consultorio Medico

## Especificaciones y Requerimientos
-----------------------------------------------------------------------------------------------------

### Objetivo
-----------------------------------------------------------------------------------------------------

- El problema con los consultorios medicos es que tiene mal organizado sus datos y registros, por lo cual les traemos una aplicación innovadora que tiene como **objetivo** crear una base de datos utilizando *ORM* , para mejorar la comodidad del cliente en esta aplicación creamos una pagina web en *HTML*  en la cual podrán interactuar via internet.

-----------------------------------------------------------------------------------------------------

### About...
-----------------------------------------------------------------------------------------------------

Base de datos:

- Tablas: **Doctores**, **Pacientes**, **Consultas**

- [x] Sqlite

| Doctores   | Pacientes | Concultas |
| ---------- | --------- | --------- |
| Id_doctor  | Id_paciente | Id_consulta |
| Nombre_doctor | | Nombre_paciente | | Doctor |
| Apellido_doctor | | Apellido_paciente | | Paciente |
| Especialidad | | Edad | | Fecha_consulta |
                          | Diagnostico |
                          | Medicamento |



ORM:
- [x] Peewee

- from peewee import *

- db = SqliteDatabase('consultas_db.db')

- class BaseModel(Model):
    - class Meta:
        - database = db

- class Doctores(BaseModel):
    - id_doctor = PrimaryKeyField(null=False)
    - nombre_doctor = TextField()
    - apellidos_doctor = TextField()
    - especialidad = TextField()

    def __str__(self):
        return "ID: {}\nDoctor: {} {}\nEspecialidad: {}".format(self.id_doctor, self.nombre_doctor, self.apellidos_doctor, self.especialidad)


- class Pacientes(BaseModel):
    - id_paciente = PrimaryKeyField(null=False)
    - nombre_paciente = TextField()
    - apellidos_paciente = TextField()
     -edad = IntegerField()

    def __str__(self):
        return "ID:{}\nPaciente:{} {}\nEdad:{}".format(self.id_paciente, self.nombre_paciente, self.apellidos_paciente, self.edad)


- class Consultas(BaseModel):
    - id_consulta = PrimaryKeyField(null=False)
    - doctor = ForeignKeyField(Doctores, related_name="doctor_detalle")
    - paciente = ForeignKeyField(Pacientes, related_name="paciente_detalle")
    - fecha_consulta = DateField()
    - diagnostico = TextField()
    - medicamento = TextField()

    def __str__(self):
        return "No. Cosulta: {}\nDoctor: {} {}\nPaciente: {} {}\nFecha consulta: {}\nDiagnóstico: {}\nMedicamento: {}".format(self
