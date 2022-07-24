document.getElementById('submitButton').addEventListener("click" , (e) => {
	let file = document.getElementById('resume').files[0]
	console.log(file)
	const storageRef = firebase.storage().ref("Resume/" + file.name)
	const task = storageRef.put(file)

	task.on(
		"state change" ,
		function progress(progress){
			console.log(progress.bytesTransferred / progress.totalBytes *100)
		},  
		function error(err){
			console.log('There was An Err ' + err)
		},
		function completed(){
			storageRef.getDownloadURL()
			.then(url => {
				const newURL = new URL(url)
				// let tempToken = newURL.search				
				// let index1 = tempToken.indexOf('&' , 0);
				// let index2 = tempToken.length
				// const token_id = tempToken.slice(index1 + 1, index2)
				const temp = file.name
				let index1 = temp.indexOf('.' , 0)
				const token_id = temp.slice( 0 , index1)
				location.href = 'http://localhost:8000/auto-complete/' + token_id
			})
		}
	)
})