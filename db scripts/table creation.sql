use ims;

create table students (
   student_id int primary key auto_increment ,
   student_name varchar(100) not null,
   mobile varchar(15) unique not null,
   email varchar(100) unique,
   address text,
   admission_date date
);

create table courses(
       course_id int primary key auto_increment,
       course_name varchar(100) unique not null,
       duration varchar(50),
       fees decimal(10,2)
);

create table batches(
    batch_id int primary key auto_increment,
    batch_name varchar(100) not null,
    timing varchar(50),
    start_date date,
    course_id int,
    
    foreign key(course_id)
    references courses(course_id)
    );