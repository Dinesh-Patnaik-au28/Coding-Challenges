var numOne = document.getElementById("num1");
var numTwo = document.getElementById("num2");
var btnEle = document.getElementById("btn");
var resultEle = document.getElementById("result");

btnEle.addEventListener("click", add);
btnEle.removeEventListener("click");

function add() {
    var x = numOne.value;
    var y = numTwo.value;
    resultEle.innerHTML = parseInt(x)+parseInt(y);
}

