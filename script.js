const transaction =[
    /*{
        id:1,
        name: 'salary',
        amount:5000,
        date: new Date(),
        type:'income'
    },
    {
        id:2,
        name: 'Rent',
        amount:5000,
        date: new Date(),
        type:'expenses'
    },
    {
        id:3,
        name: 'Grocery',
        amount:5000,
        date: new Date(),
        type:'expenses'
    },*/

];
const list = document.getElementById("transactionList");
const status =document.getElementById('status')
function renderList(){
    list.innerHTML = "";
    if (transaction.length===0) {
        status.textContent='No transaction.';
        return;
    }
    transaction.forEach((name,amount,date)=>{
        const li= document.createElement("li")
        li.innerHTML=
        <div class ="name">
            <h4>${name}</h4>
            <p>${new Date(date).toLocaleDateString()}</p>

        </div>;
        <div class ="amount">
            <span>${amount}</span>

        </div>

        list.appendChild(li);
    });
}
renderList();
