document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').onclick = count
})
let counter = 0
function count(){
    counter++
    document.querySelector('h1').innerHTML = counter

    if (counter % 10 === 0){
        alert(`hob, now counter is ${counter}`)
    }
}
