**Web - Compromised - 200pts**


Enoncé :
```
The administrator of this website has been hacked multiple times. As a result, they gave the sources of their site and ask users to look for vulns.

https://compromised.thcon.party

WARNING: The flag is given without the surrounding "THC{...}"
```

On commence avec les sources de l'application web [Sources](sources/sources.zip)

**Résolution :**

La page d'accueil nous demande de nous authentifier.


Le fichier login.php contient l'authentification suivante :

```PHP
if (!empty($_POST['username']) && !empty($_POST['password'])) {
	$account = json_decode(file_get_contents('configs/account.json'));

	if ($_POST['username'] == $account->username && hsha1($_POST['password']) == $account->password) {
		$_SESSION['logged'] = $account->username;
		header('Location: admin.php');
		echo 'bon';
		exit();
	}
	else {
		$error = "Invalid username of password";
	}
}

```

On essaye d'accèder au fichier qui contient les comptes utilisateurs sur le serveur :

[configs/account.json](https://compromised.thcon.party/configs/account.json)

```PHP
{
	"username": "admin",
	"password": "f17c99cf95443a9a8768547fb91377a6da9f2a6e"
}
```

Sans succès après avoir essayer de chercher une correspondance du sha1 , nous sommes aller voir plus en détail la fonction "hsha1".

Contenu du fichier : "base/sha1.php"

```PHP
<?php
[...]

function sha1x($order, $b, $c, $d)
{
	switch ($order) {
		case 0:
			return (~$b & $d) ^ ($b & $c);
		case 1:
		case 3:
			return $b ^ $d ^ $c;
		case 2:
			return ($b & $c) ^ ($c & $d) ^ ($b & $d);
		case 4:
			return ($b ^ 0x2a);
	}
}

function hsha1($input) {
	$p0 = 1732584193;
	$p1 = 4023233417;
	$p2 = 2562383102;
	$p3 = 271733878;
	$p4 = 3285377520;
	
	$c0 = 1226721361;
	$c1 = 16862785;
	$c2 = 725571416;

	$K = [1518500249, 1859775393, 2400959708, 3395469782];
	$B = str_split(str_pad(substr($input, 10), 40), 8);

	$msg = get_msg($input);
	$parts = str_split($msg, 64);
	
	$i = 0;
	$z = 0;
	foreach ($parts as $part) {
		$parcels = str_split($part, 4);
		foreach ($parcels as $i => $chrs) {
			$chrs = str_split($chrs);
			var_dump($chrs);
			$parcel = '';
			foreach ($chrs as $chr) {
				$parcel .= sprintf('%08b', ord($chr));
			}
			$parcels[$i] = bindec($parcel);
		}

		for ($i = 16; $i < 80; $i++) {
			$parcels[$i] = rotl($parcels[$i - 3] ^ $parcels[$i - 8] ^ $parcels[$i - 14] ^ $parcels[$i - 16], 1) & 0xffffffff;
		}

		$a = $p0; $b = $p1; $c = $p2; $d = $p3; $e = $p4;

		foreach ($parcels as $i => $parcel) {
			$j = floor($i / 20);
			if ($i < 10) {
				if (@sha1x(4, ord($input[$i]), $c, $d) == (movr($i / 4, $c0, $c1, $c2) & 0xff)) {
					$z++;
				}
				$i++;
			}
			$f = sha1x($j, $b, $c, $d);
			$temp = rotl($a, 5) + $f + $e + $K[$j] + ($parcel) & 0xffffffff;
			$e = $d;
			$d = $c;
			$c = rotl($b, 30);
			$b = $a;
			$a = $temp;
			$x = $z == 0xa ? chr(115) : chr(120);
		}

		$p0 = $z == 10 ? $B[0] : (($p0 + $a) & 0xffffffff);
		$p1 = $z == 10 ? $B[1] : (($p1 + $b) & 0xffffffff);
		$p2 = $z == 10 ? $B[2] : (($p2 + $c) & 0xffffffff);
		$p3 = $z == 10 ? $B[3] : (($p3 + $d) & 0xffffffff);
		$p4 = $z == 10 ? $B[4] : (($p4 + $e) & 0xffffffff);
	}

	return sprintf("%08$x%08$x%08$x%08$x%08$x", $p0, $p1, $p2, $p3, $p4);
}

```

On constate que :

```PHP
$p0 = $z == 10 ? $B[0] : (($p0 + $a) & 0xffffffff);
```
Si $z est égal à 10 alors $p0 vaut "$B[0]" (valeur) transmis par l'utilisateur) 

On cherche donc un moyen de mettre $z à 10 :

```PHP
@sha1x(4, ord($input[$i]), $c, $d) == (movr($i / 4, $c0, $c1, $c2) & 0xff)
```

Si on execute la page de login avec un mot de passe de test et que l'on affiche **(movr($i / 4, $c0, $c1, $c2) & 0xff)** , on obtient : 

```PHP
	if ($i < 10) {
				echo "\n--------------\n";
				echo (movr($i / 4, $c0, $c1, $c2) & 0xff);
				echo "\n---------------\n";
				/*if (@sha1x(4, ord($input[$i]), $c, $d) == (movr($i / 4, $c0, $c1, $c2) & 0xff)) {
					
					$z++;
					var_dump($z);
				}*/
				$i++;
			}

```

Résultat :
```
81, 72, 30, 73, 65, 78, 1, 1, 88, 87
```

Il faut xorer chaque résultat avec 0x2a.


```PHP

case 4:
			return ($b ^ 0x2a);

```


```PYTHON
>>> import sys
>>> values = [81, 72, 30, 73, 65, 78, 1, 1, 88, 87]
>>> for elem in values:
...     sys.stdout.write(chr(elem ^ 0x2a))
... 
{b4ckd++r}
```

Pour se connecter sur la page admin il fallait alors utiliser les identifians :

```
admin / {b4ckd++r}f17c99cf95443a9a8768547fb91377a6da9f2a6e
```

```
Le flag est : THC{tata}
```




By team Beers4Flags


```
 ________
|        |
|  #BFF  |
|________|
   _.._,_|,_
  (      |   )
   ]~,"-.-~~[
 .=] Beers ([
 | ])  4   ([
 '=]) Flags [
   |:: '    |
    ~~----~~
```
