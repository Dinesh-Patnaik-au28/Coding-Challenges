var queue = [];

const addBtnEle = document.getElementById('add');
const removeBtnEle = document.getElementById('remove');

addBtnEle.addEventListener('click', addHandler);
removeBtnEle.addEventListener('click', removeHandler);

const resultEle = document.getElementById('result');

function addHandler() {
    if(document.getElementById('num').value == ''){
        alert('Enter Something in Input Field');
    }else{
        const num = document.getElementById('num').value;
        queue.push(num);
        console.log(queue);
        document.getElementById('num').value = '';
        displayQueue();
    }
    
}

function removeHandler() {

    if(queue.length > 0){
        const num = queue.shift();
        console.log(queue);
        document.getElementById('num').value = '';
        displayQueue();
    } else {
        alert('Queue is Empty');
    }
    
}

function displayQueue() {
    const result = document.getElementById('result');
    result.innerHTML = '';
    var flagFirstELement = true;
    queue.forEach(element => {
        if(flagFirstELement){
            result.innerHTML += element;
            flagFirstELement = false;
        } else {
            result.innerHTML += ',' + element;
        }
    })
}
