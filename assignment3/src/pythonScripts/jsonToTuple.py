import json


def convertStudent(data):
    f = open(data)
    text = json.load(f)
    tuples = text["Student"]
    r = open('StudentTuples.txt', "w")
    r.write(" ")
    r.close()
    r = open('StudentTuples.txt', "a")

    for x in tuples:
        r.write(',' + str((x['studentNo'], x['fName'], x['lName'], x['studentYear'], x['studentAverage'],
                           x['creditsToDate'], x['numberOfClasses'], x['classroomNo'], x['instructorNo'])))


def convertClassroom(data):
    f = open(data)
    text = json.load(f)
    tuples = text["classroom"]
    r = open('ClassroomTuples.txt', "w")
    r.write(" ")
    r.close()
    r = open('ClassroomTuples.txt', "a")

    for x in tuples:
        r.write(',' + str((x['classId'], x['classroomNo'],
                x['homeInstructor'], x['classroomQuantity'])))


def convertDepartment(data):
    f = open(data)
    text = json.load(f)
    tuples = text["Department"]
    r = open('DepartmentTuples.txt', "w")
    r.write(" ")
    r.close()
    r = open('DepartmentTuples.txt', "a")

    for x in tuples:
        r.write(',' + str((x['studentNo'], x['fName'], x['lName'], x['studentAge'], x['studentYear'], x['studentAverage'],
                           x['creditsToDate'], x['numberOfClasses'], x['classroomNo'], x['instructorNo'])))


def convertCourseEquipment(data):
    f = open(data)
    text = json.load(f)
    tuples = text["CoruseEquipment"]
    r = open('CourseEquipmentTuples.txt', "w")
    r.write(" ")
    r.close()
    r = open('CourseEquipmentTuples.txt', "a")

    for x in tuples:
        r.write(
            ',' + str((x['deviceNo'], x['deviceName'], x['classAssigned'])))


def convertInstructor(data):
    f = open(data)
    text = json.load(f)
    tuples = text["instructor"]
    r = open('InstructorTuples.txt', "w")
    r.write(" ")
    r.close()
    r = open('InstructorTuples.txt', "a")

    for x in tuples:
        r.write(',' + str((x['InstructorId'], x['homeClassroom'])))


convertStudent('../Students/Student.json')

convertInstructor('../Instructor/instructor.json')

convertCourseEquipment('../CourseEquipment/CoruseEquipment.json')

convertClassroom('../Classroom/classroom.json')
