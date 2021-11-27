UPDATE AdminStaff
SET position = 'Vice Principal', salary = salary * 1.05
WHERE adminNo = 5;

DELETE FROM Enrollment
WHERE dateEnrolled < DATE(current_date) AND courseID = '47';

UPDATE Classroom
SET classroomQuantity = classroomQuantity * 0.5 
WHERE coursesTaught > 3;