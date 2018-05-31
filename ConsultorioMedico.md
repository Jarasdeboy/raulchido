# Consultorio Medico :pill: :syringe: :hospital:

## Especificaciones y Requerimientos
-----------------------------------------------------------------------------------------------------

### Objetivo :page_facing_up:
-----------------------------------------------------------------------------------------------------

- El problema con los consultorios medicos es que tiene mal organizado sus datos y registros, por lo cual les traemos una aplicación innovadora que tiene como **objetivo** crear una base de datos utilizando *ORM* , para mejorar la comodidad del cliente en esta aplicación creamos una pagina web en *HTML*  en la cual podrán interactuar via internet.

-----------------------------------------------------------------------------------------------------

## Aplicativo :briefcase:
-----------------------------------------------------------------------------------------------------

### Base de datos :triangular_flag_on_post: 

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



### ORM :moyai:

- Utilizamos el *ORM* **peewee**,  porque es simple y pequeño, que podemos aprender a utilizar rápidamente ya que su manejo es muy intuitivo.

- [x] Peewee :penguin:

### Creacion de tablas con el Mapeo obejto-relacional :squirrel:

- Doctores :mask:

![doctorespewwe](https://user-images.githubusercontent.com/35546433/40743098-38f1022e-6416-11e8-9d74-00d85f5605e6.PNG)


- Pacientes :boy:

![pacientespeewee](https://user-images.githubusercontent.com/35546433/40743197-7c3201e6-6416-11e8-93c2-da668be1f34a.PNG)

- Consultas  :blue_book:

![consultapewwe1](https://user-images.githubusercontent.com/35546433/40743228-892073ba-6416-11e8-9d90-52fb2b2f1a03.PNG)


### Pagina web :bomb:

- [x] HTML :trollface:


### Modelo de Clases :school_satchel:

![modeloclase](https://user-images.githubusercontent.com/35546433/40706787-6d000fd6-63b4-11e8-855e-a2f674f140c9.PNG)


Modelo Entidad Relacion:


![poweropsq](https://user-images.githubusercontent.com/35546433/40754913-5db28ab2-6441-11e8-95a8-5fc4d0391192.PNG)


Modelo de componentes:

![compoojddafds](https://user-images.githubusercontent.com/35546433/40754793-9ce6bb64-6440-11e8-83bd-a1baed28cada.PNG)



## Referencias :computer: :floppy_disk:

### WebService

- [WEBSERVICE JSON](https://www.youtube.com/watch?v=akIMTwskeOY&index=1&list=PLAg6Lv5Bbjjeh7m51aXdKcdWf6kMKylzN)
- [WEBSERVICE Wamp Service](https://www.youtube.com/watch?v=IkR_fewaWVc)

### JSON Data Format

- [JSON Beginners](https://www.youtube.com/watch?v=0yn7_YuIBdo&list=PLw02n0FEB3E2RDlD2cBULQjvXJ1K_jS1O&index=32)

### Peewee Docs

- [Peewee Info](http://docs.peewee-orm.com/en/latest/)
  

### Sqlite3

- [Sqlite3 Python](https://docs.python.org/3/library/sqlite3.html)






