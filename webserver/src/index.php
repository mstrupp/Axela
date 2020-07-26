<?php
// LED
if ($_POST['Lampe'] == 'An') {
	echo exec('sudo python test1.py');
} elseif ($_POST['Lampe'] == 'Aus') {
  echo exec('sudo python test0.py');
}

// RGB LED
if ($_POST['Farbauswahl_RGB']) {
	$rgbCode = $_POST['Farbauswahl_RGB'];
	echo exec("sudo python rgb.py '$rgbCode'");
}
?>

<!DOCTYPE html> 
<html> 

<head> 
  <title>Welcome to Axela!</title> 
  <link rel="stylesheet" href="tailwind.css">
</head>

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
	<input type="color" name="Farbauswahl_RGB" value="<?php echo exec('python readRGB.py') ?>"/>
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
  </div>
</body>
</html>
