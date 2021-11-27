let departmentJson = {
    department: []
};

function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

class department {
    constructor(deptId, deptName, instructorsAssigned, studentsEnrolled) {
        this.deptId = deptId;
        this.deptName = deptName;
        this.instructorsAssigned = instructorsAssigned;
        this.studentsEnrolled = studentsEnrolled;
    }
}

function getDeptName () {
    let departmentNamesList = ["Math", "Science", "Social_Sciences", "French", "English", "Physical_Activities"];

    for (let i = 0; i < 6; i++)
        return departmentNamesList[i]
        departmentNamesList.remove(i)

}

function getInstructorsAssigned () {

    

}

function getStudentsEnrolled () {
    return getRndInteger(20,40)
}

function createTuple (id) {
    let tuple = new department(id, getDeptName(), getInstructorsAssigned(), getStudentsEnrolled());
    return tuple;
}

function generateDepartmentData () {
    for (let i = 1; i < 7; i++) {
        departmentJson.department.push(createTuple(i));
    }
    let json = JSON.stringify(departmentJson);

    let fs = require('fs');
    fs.writeFile('department.json', json, 'utf8', function(err) {
        if (err) throw err;
        console.log('complete');
        })
}

generateDepartmentData(); 