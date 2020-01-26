
const headerDiv = document.getElementById("header");
const mainDiv = document.getElementById("main");
const stateCon = () => {
    let innerState = undefined;
    return {
        trigger: (id, mainRepaint) =>{
            if(innerState != id){
                innerState = id;
                removeButtonsClass();
                addActiveToButton(id);
                mainRepaint();
            }        
        }
    }
}

const removeButtonsClass = () =>{
    Array.from(document.getElementsByClassName("button")).forEach((element)=>element.classList= 'button');
}

const addActiveToButton= (id) =>{
    document.getElementById(id).classList = 'button active';
}

const initHeader = (headerDivElement, mainDivElement) => {
    const state = stateCon();

    createButton("admin", headerDivElement, mainDivElement, state, (divElement) => {
        return () => {
            divElement.innerHTML = '';
            const loadingDiv = document.createElement("div");
            loadingDiv.innerHTML = "Loading please wait";
            divElement.appendChild(loadingDiv);
            const table = document.createElement("table");
            divElement.appendChild(table);
            const row = table.insertRow(0)
            const idCell = row.insertCell(0);
            const secondCell = row.insertCell(1);
            const thirdCell = row.insertCell(2);
            idCell.innerHTML = 'id';
            secondCell.innerHTML = 'name';
            thirdCell.innerHTML = 'createdDate';
            // call preload (async call)
            fetch('http://localhost:5000/availabledata').then(response => response.json()).then(json => {
                // it will run after the response
                divElement.removeChild(loadingDiv);
                json.forEach(element => {
                    // it fills the table
                    const row = table.insertRow(Number(element.id))
                    const idCell = row.insertCell(0);
                    const secondCell = row.insertCell(1);
                    const thirdCell = row.insertCell(2);
                    idCell.innerHTML = element.id;
                    secondCell.innerHTML = element.name;
                    thirdCell.innerHTML = Intl.DateTimeFormat('en-US').format(new Date(element.createdDate));
                });    
            })
        }
    }
    );
}

const createClickCallback = (state, mainDiv, id, mainInitCallback) => {
    return () =>{
        state.trigger(id, mainInitCallback(mainDiv));
    }
}

const createButton = (id,parent, maindiv, state, clickCallback) => {
    const button = document.createElement("div");
    button.addEventListener("click", createClickCallback(state, maindiv, id, clickCallback));
    button.id = id;
    button.classList = "button";
    button.innerHTML= id
    parent.appendChild(button);
    return button;
}

// const idBox = document.getElementById("idBox");
// const doSearchButton = document.getElementById("doSearchButton");
// const resultBox = document.getElementById("resultBox");



// firstHeader.innerHTML = "<b>Id</b>";
// secondHeader.innerHTML = "<b>Number Data</b>";
// orderNumHeader.innerHTML = "<b>OrderNum</b>";



// // init button
// // it runs after the trigger of call preload. (sync call)
// doSearchButton.addEventListener("click", (event)=>{
//     resultBox.innerHTML="Loading...."
//     resultBox.style="background-color: orange";
//     // fetch data from server
//     fetch('http://localhost:5000/getdatabyid?id='+idBox.value).then(response => response.json()).then((jsonvalue)=>{
//         if(jsonvalue.error){
//             resultBox.style="background-color: red; color: black;";
//             resultBox.innerHTML=jsonvalue.error;
//         }else{
//             resultBox.style="background-color: green; color: white;";
//             resultBox.innerHTML=`id: ${jsonvalue.id}, numData:${jsonvalue.numData}, orderNum: ${jsonvalue.orderNum} `;
//         }
        
//     })
// });


initHeader(headerDiv, mainDiv)