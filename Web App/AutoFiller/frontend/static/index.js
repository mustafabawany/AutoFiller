
let input = document.getElementById("resume");
let button = document.getElementById("submitButton");

button.disabled = true

input.addEventListener("change" , function (){
	console.log(document.getElementById("resume").value)
	if (document.getElementById("resume").value === ""){
		button.disabled = true;
	} else {
		button.disabled = false;
	}
});

window.addEventListener("load" , function(event){
	this.document.getElementById("preloader").style.display = "none"
})

document.getElementById('submitButton').addEventListener("click" , (e) => {
	this.document.getElementById("preloader").style.display = "flex"
	this.document.getElementById("navbar").style.display = "none"	
	this.document.getElementById("hero").style.display = "none"
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
				const temp = file.name
				let index1 = temp.indexOf('.' , 0)
				const token_id = temp.slice( 0 , index1)
				location.href = 'http://localhost:8000/auto-complete/' + token_id
			})
		}
	)
})