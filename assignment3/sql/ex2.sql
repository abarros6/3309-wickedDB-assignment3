CREATE TABLE CourseEquipment(
    deviceNo int,
    deviceName varchar(255),
    courseAssigned int,
    studentNo int,
    dueDate DATE
);

CREATE TABLE Schedule(
    scheduledToStudent varchar(255),
    coursesEnrolled int,
    totalStudentsEnrolled int,
    studentNo int
);

CREATE TABLE Course(
    courseID int,
    courseName varchar(255),
    courseClassroom int,
    deptName varchar(255),
    courseYear int,
    instructorNo int
);

CREATE TABLE Student(
    studentNo int,
    fName varchar(255),
    lName varchar(255),
    studentAge int,
    studentYear int,
    studentAverage int,
    creditsToDate int,
    numberOfClasses int,
    classroomNo int,
    instructorNo int
);

CREATE TABLE Instructor(
    instructorNo int,
    classroomNo int,
    deptName varchar(255),
    coursesTaught int
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
    deptName varchar(255),
    fName varchar(255),
    lName varchar(255)
);

CREATE TABLE Classroom(
    classroomNo int,
    homeInstructor varchar(255),
    classroomQuantity int,
    coursesTaught int
);

CREATE TABLE Enrollment(
    studentNo int,
    courseID int,
    dateEnrolled DATE
);

CREATE TABLE Timing(
    scheduledToStudent int,
    courseID int,
    startDate DATE,
    endDate DATE,
    startTime TIME,
    endTime TIME
);

CREATE TABLE Allotment(
    instructorNo int,
    classroomNo int,
    dateAssigned DATE,
    timeAssigned TIME
);