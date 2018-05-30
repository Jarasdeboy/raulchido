# Consultorio Medico

## Especificaciones y Requerimientos
-----------------------------------------------------------------------------------------------------

### Objetivo
-----------------------------------------------------------------------------------------------------

- El problema con los consultorios medicos es que tiene mal organizado sus datos y registros, por lo cual les traemos una aplicación innovadora que tiene como **objetivo** crear una base de datos utilizando *ORM* , para mejorar la comodidad del cliente en esta aplicación creamos una pagina web en *HTML*  en la cual podrán interactuar via internet.

-----------------------------------------------------------------------------------------------------

### Aplicativo...
-----------------------------------------------------------------------------------------------------

Base de datos:

- Tablas: **Doctores**, **Pacientes**, **Consultas**

- [x] Sqlite

| Doctores   | Pacientes | Concultas |
| ---------- | --------- | --------- |
| Id_doctor  | Id_paciente | Id_consulta |
| Nombre_doctor | Nombre_paciente | Doctor |
| Apellidos_doctor | Apellidos_paciente | Paciente |
| Especialidad | Edad | Fecha_consulta |
|                     |                | Diagnostico |
|                     |                | Medicamento |



ORM:
- Utilizamos el *ORM* **peewee**,  porque es simple y pequeño, que podemos aprender a utilizar rápidamente ya que su manejo es muy intuitivo.

- [x] Peewee  

###Creacion de tablas con el Mapeo obejto-relacional 


- from peewee import *

- db = SqliteDatabase('consultas_db.db')

- class Doctores(Model):
	 id_doctor = PrimaryKeyField(null=False)
	 nombre_doctor = TextField()
	 apellidos_doctor = TextField()
	 especialidad = TextField()

	- class Meta:
		 database = db

	def __str__(self):
		return "ID: {}\nDoctor: {} {}\nEspecialidad: {}\n".format(self.id_doctor, self.nombre_doctor, self.apellidos_doctor,             self.especialidad)

- class Pacientes(Model):
	 id_paciente = PrimaryKeyField(null=False)
	 nombre_paciente = TextField()
	 apellidos_paciente = TextField()
	 edad = IntegerField()

	- class Meta:
		 database = db
 
	def __str__(self):
		return "ID: {}\nPaciente: {} {}\nEdad: {}\n".format(self.id_paciente, self.nombre_paciente, self.apellidos_paciente, self.edad)

- class Consultas(Model):
	 id_consulta = PrimaryKeyField(null=False)
	 doctor = ForeignKeyField(Doctores, related_name="doctor_detalle")
	 paciente = ForeignKeyField(Pacientes, related_name="paciente_detalle")
	 fecha_consulta = DateField()
	 diagnostico = TextField()
	 medicamento = TextField()

	- class Meta:
		 database = db

	def __str__(self):
		return "No. consulta: {}\nDoctor: {} {}\nPaciente: {} {}\nFecha: {}\nDiagnóstico: {}\nMedicamento: {}\n".format(self.id_consulta, self.doctor.nombre_doctor, self.doctor.apellidos_doctor, self.paciente.nombre_paciente, self.paciente.apellidos_paciente, self.fecha_consulta, self.diagnostico, self.medicamento)
		#return "No. consulta: {}\nDoctor: {}\nPaciente: {}\nFecha: {}\nDiagnóstico: {}\nMedicamento: {}\n".format(self.id_consulta, self.doctor, self.self.paciente, self.fecha_consulta, self.diagnostico, self.medicamento)




Pagina web:

- [x] HTML
- [x] jinja


Modelo de Clases:

![modeloclase](https://user-images.githubusercontent.com/35546433/40706787-6d000fd6-63b4-11e8-855e-a2f674f140c9.PNG)

Modelo Entidad Relacion:

![entidad relacion consultorio](https://user-images.githubusercontent.com/35546433/40707984-d66b24bc-63b7-11e8-9c47-754364aeffbf.PNG)




