$(document).ready(function() {
	$(".popup").magnificPopup();

	$("#buy-item").submit(function() {
		$.ajax ({
			type: "POST",
			url: "mail.php",
			data: $(this).serialize()
		}).done(function() {
			alert("Спасибо за заявку! Скоро мы вам перезвоним!")
		})
		return false;
	})
})