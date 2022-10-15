

DROP TABLE STUDENT;
CREATE TABLE STUDENT(

ID INT NOT NULL,
STUDENT_NAME VARCHAR(30),
COURSE VARCHAR(30)

);

SHOW COLUMNS FROM STUDENT;
ALTER TABLE STUDENT CHANGE ID STUDENT_ID INT;

CREATE TABLE person (
person_id INT NOT NULL AUTO_INCREMENT,
first_name VARCHAR(100) NOT NULL COMMENT "First name of the person",
last_name VARCHAR(100) NOT NULL,
age INT,
PRIMARY KEY(person_id)
);

DROP TABLE person;
ALTER TABLE person
ADD email varchar(255);

SHOW FULL COLUMNS FROM PERSON;

INSERT INTO person (first_name, last_name, age)
VALUES ('Jane', 'Bloggs', 32);
INSERT INTO person (first_name, last_name, age)
VALUES ('Joe', 'Bloggs', 28);
INSERT INTO person (first_name, last_name, age)
VALUES ('Cody', 'Bloggs', 20);

DROP TABLE person;
SELECT * FROM person;
UPDATE person
SET age = 28
WHERE person_id = 3;

DELETE FROM person
WHERE
person_id=3;

SELECT * FROM person;

SELECT * FROM person
WHERE
first_name = 'Cody';

SELECT * FROM person
WHERE first_name like 'J%'
and email is not null;

