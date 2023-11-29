<?php
	$im=new imagick("image.png");
	$pixel= $im->getimagepixelcolor(240, 30);
	$color= $pixel->getcolor();
	echo "<img src='image.png' /><br>";
	print_r($color);
?>
