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
    tuples = text["Student"]
    r = open('StudentTuples.txt', "w")
    r.write(" ")
    r.close()
    r = open('StudentTuples.txt', "a")

    for x in tuples:
        r.write(',' + str((x['studentNo'], x['fName'], x['lName'], x['studentYear'], x['studentAverage'],
                           x['creditsToDate'], x['numberOfClasses'], x['classroomNo'], x['instructorNo'])))


def convertDepartment(data):
    f = open(data)
    text = json.load(f)
    tuples = text["Department"]
    r = open('DepartmentTuples.txt', "w")
    r.write(" ")
    r.close()
    r = open('DepartmentTuples.txt', "a")

    for x in tuples:
        r.write(',' + str((x['studentNo'], x['fName'], x['lName'], x['studentYear'], x['studentAverage'],
                           x['creditsToDate'], x['numberOfClasses'], x['classroomNo'], x['instructorNo'])))


def convertCourseEquipment(data):
    f = open(data)
    text = json.load(f)
    tuples = text["CourseEquipment"]
    r = open('CourseEquipmentTuples.txt', "w")
    r.write(" ")
    r.close()
    r = open('CourseEquipmentTuples.txt', "a")

    for x in tuples:
        r.write(',' + str((x['studentNo'], x['fName'], x['lName'], x['studentYear'], x['studentAverage'],
                           x['creditsToDate'], x['numberOfClasses'], x['classroomNo'], x['instructorNo'])))


def convertInstructor(data):
    f = open(data)
    text = json.load(f)
    tuples = text["Instructor"]
    r = open('InstructorTuples.txt', "w")
    r.write(" ")
    r.close()
    r = open('InstructorTuples.txt', "a")

    for x in tuples:
        r.write(',' + str((x['studentNo'], x['fName'], x['lName'], x['studentYear'], x['studentAverage'],
                           x['creditsToDate'], x['numberOfClasses'], x['classroomNo'], x['instructorNo'])))


convertStudent('../Student.json')
