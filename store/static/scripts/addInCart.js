let btnSub = document.getElementById('addInCart');
let formElem = document.getElementById('addInCart')
let csrfToken = getCookie('csrftoken');
// const data = new URLSearchParams(new FromData(formElem));
// Отправка запроса по кнопке
// btnSub.onclick = function(e) {

//     e.preventDefault();

//     if(document.getElementsByName('product')){
//         let prodId = document.getElementById('productId').value;
//         alert(prodId);

//         sendRequest(prodId)
//     }
// }

// function sendRequest(prodId) {
//     fetch("cart", {
//         method: 'POST',
//         headers: {
//             'Accept': 'application/json',
//             'X-Requested-With': 'XMLHttpRequest',
//             "X-CSRFToken": csrfToken,
//         },
//         body: JSON.stringify({
//             'product': prodId
//         })
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data)
//     })
//     .catch(er => console.log("Error: ", er))
// }


// Отправка запроса через форму

formElem.onsubmit = async (e) => {

    e.preventDefault();

    await fetch('cart', {
        method: 'POST',
        body: new FormData(formElem)
    })
    .then(response => {
        console.log(response);
        response.json();
    })
    .then(data => console.log(data))
    .catch(er => console.log("Error: ", er))



    // let response = await fetch('/cart', {
    //     method: 'POST',
    //     body: new FormData(formElem),
    // });

    // console.log(response.json())
    // let res = await response.json()

    // onsole.log(response)
}



function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}