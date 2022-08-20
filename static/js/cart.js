var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)
        console.log('user:',myuser)
        if (myuser == 'AnonymousUser' ) {
          console.log("this is not user")
        } else {
          updateuserOrder(productId,action)
          
        }
        
    })
}



function updateuserOrder(productId,action) {
  console.log('product:',productId ,'action:', action)
  fetch (url = '/updateitem', {
    method :'POST',
    Headers : {
      csrfmiddlewaretoken: '{{ csrf_token }}',
      'Content-Type':'application/json',
    },
    body : JSON.stringify({'productId': productId ,'action': action})
  })
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log('data:', data);
    location.reload()
  })
}



function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');






