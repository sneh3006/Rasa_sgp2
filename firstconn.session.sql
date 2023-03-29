-- @block
CREATE TABLE STUDENT(
    ID INT PRIMARY KEY,
    EMAIL VARCHAR(50) NOT NULL,
    NAME VARCHAR(50) NOT NULL
);
-- @block
CREATE TABLE class(
    ID INT PRIMARY KEY,
    batch VARCHAR(4) NOT NULL,
    Attendence INT NOT NULL,
    FOREIGN KEY(ID) REFERENCES STUDENT(ID)
);
create TABLE Result(
    ID INT PRIMARY KEY,
    Semester int NOT NULL,
    MARKS INT NOT NULL,
    FOREIGN KEY(ID) REFERENCES STUDENT(ID)
);
--@block
insert into student values
('001', '21ce001@charusat.edu.in', 'Harshit Ajakiya'),
('002', '21ce002@charusat.edu.in', 'Andrew Augustine'),
('003', '21ce003@charusat.edu.in', 'Haril Ankleshwariya'),
('004', '21ce031@charusat.edu.in', 'Dulari Gajjar'),
('005', '21ce042@charusat.edu.in', 'Sneh Jani');

-- @block
insert into class values
('001', 'A1', 80),
('002', 'A1', 90),
('003', 'A1', 85),
('004', 'B1', 75),
('005', 'B1', 95);

-- @block
insert into result values
('001', 4, 9.6),
('002', 4, 9.2),
('003', 4, 8.5),
('004', 4, 9.5),
('005', 4, 7.5);