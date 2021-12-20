var update_butns = document.getElementsByClassName('update-cart')
var checkout_btn = document.getElementsByClassName('checkout-btn')
var form = document.getElementById('form')

for(let count = 0; count < update_butns.length; count++){
    update_butns[count].addEventListener('click', function() {
        let product_id = this.dataset.product
        let action = this.dataset.action
        console.log('product_name:', product_id, 'action:', action)
        console.log(user)
        if(user === "AnonymousUser"){
            console.log("user is not logged in")
        }else{
            update_user_order(product_id, action)
        }
    })
}

function update_user_order(product_id, action){
    console.log("User is logged in, senting data..")

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'product_id': product_id, 'action': action})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}

form.addEventListener('submit', function(e) {
    e.preventDefault()
    console.log('Form submitted....')
    console.log(total)
    document.getElementById('form-button').classList.add('hidden')
    document.getElementById('payment-info').classList.remove('hidden')
})

document.getElementById('payment-button').addEventListener('click', function(e) {
    submit_form_data()
})

function submit_form_data() {
    console.log('Payment button clicked')

    var user_form_data = {
        'name' : null,
        'email' : null,
        'total' : total
    }

    var shipping_info = {
        'address' : null,
        'city' : null,
        'zipcode' : null,
        'state' : null
    }

    shipping_info.address = form.address.value
    shipping_info.city = form.city.value
    shipping_info.state = form.state.value
    shipping_info.zipcode = form.zipcode.value


    var url = '/process_order/'
    fetch(url, {
        method:'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'form':user_form_data, 'shipping':shipping_info})
    })
    .then((response) =>{ response.json()
    })
    .then((data) =>{
        console.log('success', data);
        alert('Transaction completed');
        window.location.href = "http://127.0.0.1:8000/"
    })
}
