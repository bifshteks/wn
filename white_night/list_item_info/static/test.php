<?php
$text = 'test php tes.php';
if (mail('artem.pif@mail.ru', 'theme php', $text)) {
	echo 'DONE';
} else {
	echo 'NOPE';
}
?>