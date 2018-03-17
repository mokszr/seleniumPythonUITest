var submitForm = function(){
    var formDiv = document.getElementById('formDiv');
    var newElement = document.createElement("div");
    newElement.setAttribute('id', "outputDiv");
    newElement.innerHTML = document.getElementsByName('fname')[0].value + " " + document.getElementsByName('lname')[0].value;
    formDiv.appendChild(newElement);
 
};