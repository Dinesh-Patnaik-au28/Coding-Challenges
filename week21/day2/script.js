var stack = [];

const pushBtnEle = document.getElementById('push');
const popBtnEle = document.getElementById('pop');

pushBtnEle.addEventListener('click', pushHandler);
popBtnEle.addEventListener('click', popHandler);

const resultEle = document.getElementById('result');

function pushHandler() {
    if(document.getElementById('num').value == ''){
        alert('Enter Something in Input Field');
    }else{
        const num = document.getElementById('num').value;
        stack.push(num);
        console.log(stack);
        document.getElementById('num').value = '';
        displayStack();
    }
    
}

function popHandler() {

    if(stack.length > 0){
        const num = stack.pop();
        console.log(stack);
        document.getElementById('num').value = '';
        displayStack();
    } else {
        alert('Stack is Empty');
    }
    
}

function displayStack() {
    const result = document.getElementById('result');
    result.innerHTML = '';
    var flagFirstELement = true;
    stack.forEach(element => {
        if(flagFirstELement){
            result.innerHTML += element;
            flagFirstELement = false;
        } else {
            result.innerHTML += ',' + element;
        }
    })
}
