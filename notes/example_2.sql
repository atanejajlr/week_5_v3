CREATE TABLE student (
    student_id INT PRIMARY KEY,
    name  VARCHAR(20),
    major VARCHAR(20)
);

DROP TABLE student;

SELECT * FROM student;
INSERT INTO student(student_id, name, major)VALUES(1, 'Jack', 'Biology');
INSERT INTO student(student_id, name, major)VALUES(2, 'Kate', 'Sociology');
INSERT INTO student(student_id, name)VALUES(3, 'Claire');

/* Adding with same primary id will raise an error*/

INSERT INTO student(student_id, name, major)VALUES(2, 'Kate', 'Sociology');

/*Adding with different ame and major but with different primary id is acceptable*/

INSERT INTO student(student_id, name, major)VALUES(4, 'Jack', 'Biology');



#Conditional Statements - IF and CASE WHEN  
CREATE TABLE STUDENT (
    STUDENT_ID INT NOT NULL AUTO_INCREMENT
    , STUDENT_NAME VARCHAR(100) NOT NULL
    , SCHOOL_NAME VARCHAR(100) NOT NULL
    , DISTANCETOSCHOOL DECIMAL(5,2)
    ,PRIMARY KEY(STUDENT_ID)
);
INSERT INTO STUDENT (STUDENT_NAME, SCHOOL_NAME, DISTANCETOSCHOOL)
VALUES ('John', 'London Higher sec school', 5.2)
        , ('Mary', 'London Higher sec school', 10.2)
        , ('Tilda', 'Leamington Higher sec school', 1.2)
        , ('Amy', 'Leamington Higher sec school', 5.2)
        , ('Cathy', 'Birmingham Higher sec school', 10.2)
        , ('Bob', 'Birmingham Higher sec school', 1.2);
SELECT * FROM STUDENT;
SELECT *, IF(DISTANCETOSCHOOL BETWEEN 0 AND 3,'Living NEAR',
            (IF(DISTANCETOSCHOOL BETWEEN 3 AND 7,'Average Distance', 'Long Distance'))) AS DISTANCE_METRICS
FROM STUDENT;
CREATE TABLE RESULT 
AS
SELECT *,
    CASE WHEN DISTANCETOSCHOOL BETWEEN 0 AND 3 THEN 'Living NEAR'
        WHEN DISTANCETOSCHOOL BETWEEN 3 AND 7 THEN (DISTANCETOSCHOOL * 1000)
        ELSE 'Long Distance' END AS DISTANCE_METRICS
FROM STUDENT;
SELECT * FROM RESULT;
# VIEWS

# VIEWS
CREATE OR REPLACE VIEW RESULT_VIEW 
AS
    SELECT *,
    CASE WHEN DISTANCETOSCHOOL BETWEEN 0 AND 4 THEN 'Living NEAR'
        WHEN DISTANCETOSCHOOL BETWEEN 4 AND 8 THEN (DISTANCETOSCHOOL * 1000)
        ELSE 'Long Distance' END AS DISTANCE_METRICS
    FROM STUDENT;
SELECT * FROM RESULT_VIEW;




