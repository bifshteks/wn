$(document).ready(function() {
	$(".popup").magnificPopup();

	$(".send").click(function() {
	alert('from commot1');
		$.ajax ({
			type: "POST",
			url: "mail.php",
			data: $(this).serialize()
		}).done(function() {
			alert("Спасибо за заявку! Скоро мы вам перезвоним!");
		})

		alert("до ретурна фолс ");
		return false;
	})
})