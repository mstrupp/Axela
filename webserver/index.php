<!DOCTYPE html> <html> <head> <title>Welcome to Axela!</title> <style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>

<h1>Axela</h1>
<h2>Smart Home System</h2>

<h3>Lampen</h3>

<h4>Grüne LED</h4>
<form method="post" action="">
    <input type="submit" name="Lampe" value="An"/>
    <input type="submit" name="Lampe" value="Aus"/>
</form>

<h4>RGB LED</h4>
<form method="post" action="">
	<input type="color" name="Farbauswahl_RGB" value=""/>
	<input type="submit"/>
</form>

<h3>Sensoren</h3>
<div>
<?php
  echo("Temperatur: ");
  echo(exec('python readTemperature.py'));
  echo(" °C");
?>
</div>
<br><br><br>
<p>Made by Axel and Michael © 2020</p>

</body>
</html>

<?php
// LED
if ($_POST['Lampe'] == 'An') {
	echo exec('sudo python /var/www/html/test1.py');
} elseif ($_POST['Lampe'] == 'Aus') {
  echo exec('sudo python /var/www/html/test0.py');
}

// RGB LED
if ($_POST['Farbauswahl_RGB']) {
	$rgbCode = $_POST['Farbauswahl_RGB'];
	echo exec("sudo python /var/www/html/rgb.py '$rgbCode'");
}
?>
