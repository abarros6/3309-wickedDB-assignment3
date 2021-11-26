CREATE TABLE Equipment(
    deviceNo int,
    deviceName varchar(255),
    courseAssigned int,
    studentNo int,
    dueDate DATE
);

CREATE TABLE Schedule(
    scheduledToStudent varchar(255),
    courseNames varchar(255),
    coursesEnrolled int,
    studentsEnrolledInClass int,
    totalStudentsEnrolled int
);

CREATE TABLE Course(
    courseID int,
    courseName varchar(255),
    courseClassroom int,
    courseDept varchar(255),
    courseYear int
);

CREATE TABLE Student(
    studentNo int,
    fName varchar(255),
    lName varchar(255),
    studentAge int,
    studentYear int,
    studentAverage int,
    creditsToDate int,
    homeClassroom int,
    numberOfClasses int
);

CREATE TABLE Instructor(
    instructorNo int,
    homeClassroom int
);

CREATE TABLE AdminStaff(
    adminNo int,
    position varchar(255),
    startDate DATE
);

CREATE TABLE Department(
    deptName varchar(255),
    instructorsAssiged int,
    studentsEnrolled int
);

CREATE TABLE Staff(
    staffNo int,
    deptAssigned varchar(255),
    fName varchar(255),
    lName varchar(255)
);

CREATE TABLE Classroom(
    classroomNo int,
    homeInstructor varchar(255),
    classroomQuantity int
);