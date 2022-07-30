var idInstance = "";
var businessKey = "";
var idTask = "";

function createInstance(){
    var ulrC = 'http://camunda.encisosystems.com/engine-rest/process-definition/key/RS_Client/start';
    var data = { variables: { assigne: { value: 'demo', type: 'String' } }, businessKey: 'test2' };

    fetch(ulrC, {
        method: 'POST',
        credentials: 'omit',
        body: JSON.stringify(data),
        headers:{
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        })
        .then(res => res.json())
        .then((response) => {
            console.log('Success:', response);
            idInstance = response['id'];
            businessKey = response['businessKey'];
        })
        .catch(error => console.error('Error:', error));
}

function getTask(){
    var ulrC = 'http://camunda.encisosystems.com/engine-rest/task?processInstanceId='+idInstance+'&processInstanceBusinessKey='+businessKey;
    var data = { };
    alert("url"+ulrC);
    fetch(ulrC, {
        method: 'POST',
        credentials: 'omit',
        body: JSON.stringify(data),
        headers:{
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then((response) => {
            console.log('Success:', response);
            idTask = response['id'];
            alert("idtask= "+idTask);
        });
}

function completeTask(){

    var ulrC = 'http://camunda.encisosystems.com/engine-rest/task/<id>/complete';
    var data = { variables: { requester: { value: 'aStringValue' }, area: { value: "" }, title: { value: "" }, location: { value: "" }, vacancies: { value: "" } } };

    fetch(ulrC, {
        method: 'POST',
        credentials: 'omit',
        body: JSON.stringify(data),
        headers:{
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then(response => console.log('Success:', response));
}

$( document ).ready(function() {
    
    createInstance();
    setTimeout(() => {
        getTask()
      }, 1000);

});