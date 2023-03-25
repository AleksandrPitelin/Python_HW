const myDiv = document.createElement('div');
myDiv.className = 'buttons';
myDiv.style.background = 'purple';
myDiv.style.textAlign = 'center';

let i=Math.floor(Math.random() * 101);


['Додати в друзі','Написати повідомлення ','Запропонувати роботу'].map(buttonName => {
    let button = document.createElement('button');
    button.className = 'btn btn-success';
    button.innerText = `${buttonName} `;
    button.style.margin = '5px'
    myDiv.appendChild(button);
    })
document.getElementsByTagName('body')[0].appendChild(myDiv);



    let button2 = document.createElement('button2');
    button2.className = 'btn btn-success';
    button2.innerText = `Кiлькiсть друзiв ${i}`;
    button2.style.margin = '5px'
    button2.style.color = 'pink'
    myDiv.appendChild(button2);
document.getElementsByTagName('body')[0].appendChild(myDiv);

// events


const btn = document.getElementsByTagName('button')[0];
const btn2 = document.getElementsByTagName('button')[1];
const btn_sum = document.getElementsByTagName('button2')[0];


btn_sum.onclick=(event)=>{
    event.target.innerText = `Кiлькiсть друзiв ${Math.floor(Math.random() * 101)+btn}`

}




btn.onclick = (event) =>{
    event.target.innerText = `Додати в друзі ${1+i}`;
    btn.addEventListener('click', function () {
    this.disabled=true;
    });
}



let colors = ['yellow','green','purple']

btn2.onclick = (event) => {
    let newDiv = document.createElement('div');
    newDiv.style.background = colors[document.getElementsByClassName('dynamic').length % 3];
    newDiv.innerText = 'My dinamic txt'
    newDiv.className = 'dynamic';
    document.getElementsByClassName('dynamic').length
    document.getElementsByTagName('body')[0].appendChild(newDiv);
};