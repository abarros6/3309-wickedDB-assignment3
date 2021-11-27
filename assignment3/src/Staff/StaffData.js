let staffJson = {
    staffData: []
};

function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

class staff {
    constructor() {
        this.classId = classId;
        this.classroomNo = classroomNo;
        this.homeInstructor = homeInstructor;
        this.classroomQuantity = classroomQuantity;
    }
}

//-----

function createTuple (id) {
    let tuple = new staff(id);
    return tuple;
}

function generatestaffData () {
    for (let i = 1; i < 67; i++) {
        staffJson.staff.push(createTuple(i));
    }
    let json = JSON.stringify(staffJson);

    let fs = require('fs');
    fs.writeFile('staff.json', json, 'utf8', function(err) {
        if (err) throw err;
        console.log('complete');
        })
}

generatestaffData(); 