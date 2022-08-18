let S = document.getElementById("str");
let btnEle = document.getElementById("btn");
let outputEle = document.getElementById("result");

btnEle.addEventListener("click",main)

function stringParser(S){
    let q = [];
    for(let i=0;i<S.length;++i)
    {
        if(S[i]!='//')
            q.push(S[i]);
        else if (q.lemgth!=0)
            q.pop();
    }

    let ans = "";
    while (q.length!=0){
        ans+=q.pop();
    }

    let answer="";
    for(let j=ans.length-1;j>=0;j--){
        answer += ans[j];

    }
    return answer;
}

function main(){
    const str = S.value;

    const result = stringParser(str);
    
    outputEle.innerHTML = result;

}

   