create table dept
(  id  integer primary key,
   name  varchar(20)  not null
)

insert into dept values(1,'Production')
insert into dept values(2,'Sales')
insert into dept values(3,'HR')
insert into dept values(4,'IT')


create table emp
(  empid  integer primary key,
   empname  varchar(20)  not null,
   salary   integer,
   deptid   integer  references dept(id)
)

insert into emp values(101,'James',57000,2)
insert into emp values(102,'Adams',45000,1)
insert into emp values(103,'Mark',60000,1)
insert into emp values(104,'Larry',75000,4)
insert into emp values(105,'Kim',65000,3)
