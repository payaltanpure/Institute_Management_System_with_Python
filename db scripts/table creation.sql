use ims;

create table students (
   student_id int primary key auto_increment ,
   student_name varchar(100) not null,
   mobile varchar(15) unique not null,
   email varchar(100) unique,
   address text,
   admission_date date
);