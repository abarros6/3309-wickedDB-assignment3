let courseJson = {
    course: []
};

function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

class course {
    constructor() {
        this.classId = classId;
        this.classroomNo = classroomNo;
        this.homeInstructor = homeInstructor;
        this.classroomQuantity = classroomQuantity;
    }
}

//-----

function createTuple (id) {
    let tuple = new course(id);
    return tuple;
}

function generatecourseData () {
    for (let i = 1; i < 67; i++) {
        courseJson.course.push(createTuple(i));
    }
    let json = JSON.stringify(courseJson);

    let fs = require('fs');
    fs.writeFile('course.json', json, 'utf8', function(err) {
        if (err) throw err;
        console.log('complete');
        })
}

generatecourseData(); 