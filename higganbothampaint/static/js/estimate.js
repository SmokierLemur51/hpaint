document.addEventListener('DOMContentLoaded', function () {
	const estimateForm = document.getElementById('schedule_estimate');

	estimateForm.addEventListener('submit', function (event) {
		event.preventDefault();

		const formData = new formData(estimateForm);

		fetch('/process-estimate', {
			method: 'POST',
			body: formData,
		})
		.then(response => response.json())
		.then(data => {
			console.log(data.message);
		})
		.catch(error => {
			console.error('Error', error);
		});
	});
});