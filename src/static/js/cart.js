updateBtn = document.getElementsByClassName('update-cart')

for (var i=0; i<updateBtn.length; i++ ){
	updateBtn[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action

		console.log('productId', productId, 'action', action)

		console.log('USER', user)
		if (user === 'AnonymousUser') {
			console.log('User not logged in')
		}else{
			UpdateUserOrder(productId, action)
		}
	})
}

function UpdateUserOrder(productId, action){
	console.log('User logged in sending data...')

	var url = '/update_item/'

	fetch(url,{
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken': csrftoken,
		},
		body:JSON.stringify({'productId':productId, 'action':action})
	})

	.then((response)=>{
		return response.json()
	})
	.then((data)=>{
		console.log('Data:',data)
		location.reload()
	})
}


// js code to work on the image slider in the detail page
	let thumbnails = document.getElementsByClassName('thumbnail-detail')
	let activeImages = document.getElementsByClassName('active')
	for (var i=0; i < thumbnails.length; i++){
		thumbnails[i].addEventListener('click', function(){

			if (activeImages.length > 0){
				activeImages[0].classList.remove('active')
			}
		
			this.classList.add('active')
			document.getElementById('featured').src = this.src
		})


	}

	const buttonRight = document.getElementById('slideRight');
	const buttonLeft = document.getElementById('slideLeft');


	buttonRight.addEventListener('click', function(){
		document.getElementById('slider').scrollLeft += 180;
	})



	buttonLeft.addEventListener('click', function(){
	  document.getElementById('slider').scrollLeft -= 180;
	})