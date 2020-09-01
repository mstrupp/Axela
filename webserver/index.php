<!--
  index.php
  HTML/ PHP Code zur Visualisierung der Bus-Steuerung.

  LAMPEN
  Jede Lampensteuerung besteht aus einem HTML Formular.
  Beim Absenden des Formulars wird jeweils eine PHP Funktion aufgerufen. 
  Diese ruft wiederum ein entsprechendes Python Skript auf dem Server auf, das die 
  Bus-Kommunikation startet.
  Die LED kann entweder an- oder ausgeschaltet werden. Zum Ausschalten wird test0.py 
  aufgerufen, zum Einschalten = test1.py.
  Für die RGB LED wird ein HTML Farbwähler verwendet. Das Skript rgb.py wird dann 
  mit der gewählten Farbe als Parameter aufgerufen.

  Temperatursensor
  Für die Anzeige der Temperatur wird auf dem Server das Skript readTemperature.py 
  aufgerufen. Es gibt die aktuelle Temperatur formatiert aus.

  Author: Alexander Ehre, Michael Strupp
  Date: 17.07.2020
 -->

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

</body>
</html>
