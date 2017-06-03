<?php

$recepient = "artem.pif@mail.ru";
$sitename = "Белая Ночь";

$name = trim($_POST["name"]);
$phone = trim($_POST["phone"])
$details = trim($_POST["details"])
$message = "Имя: $name \nТелефон: $phone \nПодробности: $details"

$pagetitle = "Новая заявка с сайта \"$sitename\""
mail($recepient, $pagetitle, $message, "Content-type: text/plain; charset=\"utf-8\"\n From: $recepient");
?>