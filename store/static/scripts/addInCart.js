let btnSub = document.querySelectorAll('#addInCart');
let csrfToken = getCookie('csrftoken')
let cartNE = document.getElementById('cart_quantity_label')
let prodQuant;


if(document.getElementById('prodQuant')){
    prodQuant = document.getElementById('prodQuant').value;
    console.log(prodQuant)
} else { prodQuant = 1 }


btnSub.forEach((btn) => {
    btn.addEventListener('click', function(event){
        event.preventDefault();

        let prodId = event.target.closest('.btn-block').querySelector('#productId').value
        console.log(typeof(+prodId))

        sendRequest(+prodId)
    })

    function sendRequest(prodId) {
        fetch("cart", {
            method: 'POST',
            headers: {
                "Accept": 'application/json',
                "Content-Type": 'application/json',
                "X-CSRFToken": csrfToken,
            },
            body: JSON.stringify({
                'product': prodId,
                'prodQuant': +prodQuant,
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            
    
        })
        .catch(er => console.log("Error: ", er))
}})


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
