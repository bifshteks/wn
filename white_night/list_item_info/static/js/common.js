$(document).ready(function() {
	$(".popup").magnificPopup();

	$(".send").click(function() {
		$.ajax ({
			type: "POST",
			url: "js/mail.php",
			data: $(this).serialize()
		}).done(function() {
			alert("Спасибо за заявку! Скоро мы вам перезвоним!");
		})

		return false;
	})
})