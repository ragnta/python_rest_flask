const table = document.getElementById("resultTable");
const idBox = document.getElementById("idBox");
const doSearchButton = document.getElementById("doSearchButton");
const resultBox = document.getElementById("resultBox");

doSearchButton.addEventListener("click", (event)=>{
    resultBox.innerHTML="Loading...."
    resultBox.style="background-color: orange";
    fetch('http://localhost:5000/getdatabyid?id='+idBox.value).then(response => response.json()).then((jsonvalue)=>{
        if(jsonvalue.error){
            resultBox.style="background-color: red; color: black;";
            resultBox.innerHTML=jsonvalue.error;
        }else{
            resultBox.style="background-color: green; color: white;";
            resultBox.innerHTML=`id: ${jsonvalue.id}, numData:${jsonvalue.numData}, orderNum: ${jsonvalue.orderNum} `;
        }
        
    })
});

const header = table.createTHead();
const row = header.insertRow(0);    
const firstHeader = row.insertCell(0);
const secondHeader = row.insertCell(1);
const orderNumHeader = row.insertCell(2);

firstHeader.innerHTML = "<b>Id</b>";
secondHeader.innerHTML = "<b>Number Data</b>";
orderNumHeader.innerHTML = "<b>OrderNum</b>";

fetch('http://localhost:5000/availabledata').then(response => response.json()).then(json => {
    json.forEach(element => {
        const row = table.insertRow(Number(element.id))
        const idCell = row.insertCell(0);
        const secondCell = row.insertCell(1);
        const thirdCell = row.insertCell(2);
        idCell.innerHTML = element.id;
        secondCell.innerHTML = element.numData;
        thirdCell.innerHTML = element.orderNum;
    });    
})