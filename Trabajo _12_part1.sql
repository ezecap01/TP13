create database trabajo_12
use trabajo_12

create table Registro
(id_registro int identity(1,1),
nombre_usuario varchar (250),
contraseña varchar(250),
constraint pk_Registro primary key (id_registro),
)

insert into Registro (nombre_usuario, contraseña)
values ('Mateo','2345'),
		('Valen','3456'),
		('Polo','4567'),
		('Maxi','5678'),
		('test','test'),
		('joan','1234');
		

select * from Registro