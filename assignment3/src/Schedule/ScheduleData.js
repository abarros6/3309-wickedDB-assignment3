let scheduleJson = {
    schedule: []
};

function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

class schedule {
    constructor(scheduledToStudent, courseNames, coursesEnrolled, studentsEnrolledinClass) {
        this.scheduledToStudent = scheduledToStudent;
        this.courseNames = courseNames;
        this.coursesEnrolled = coursesEnrolled;
        this.studentsEnrolledinClass = studentsEnrolledinClass;
    }
}

function getscheduledToStudent() {
    return getRndInteger(354216,499422);
}

function getcourseNames() {
    let depts = ["Math", "Science", "Social_Science", "English", "French", "Physical_Activities"];
    return depts[getRndInteger(0,5)];
}

function getstudentsEnrolledinClass() {
    return getRndInteger(20,40);
}

function createTuple () {
    let tuple = new schedule(getscheduledToStudent(), getcourseNames(), getcourseNames(), getstudentsEnrolledinClass());
    return tuple;
}

function generatescheduleData () {
    for (let i = 1; i < 2001; i++) {
        scheduleJson.schedule.push(createTuple(i));
    }
    let json = JSON.stringify(scheduleJson);

    let fs = require('fs');
    fs.writeFile('schedule.json', json, 'utf8', function(err) {
        if (err) throw err;
        console.log('complete');
        })
}

generatescheduleData(); 