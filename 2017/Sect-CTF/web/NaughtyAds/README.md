# Naughty Ads

On remarque rapidement une possibilité d'injection sql dans le champ "id"

De plus, le fichier robots.txt nous permet de retrouver la source de la page index 

### http://naughtyads.alieni.se/index.phps
```
<?php
require_once 'lib.php';
header('X-XSS-Protection: 0');
$cols = array(
    "e8c4-437b-9476",
    "849e-416e-acf7",
    "7f9d-470f-8698",
    "c8bb-4695-93f7",
    "5fbc-4729-8821",
    "3ad3-46c3-b975",
    "f44f-4cc9-a5e0",
    "0c3f-42c8-a0ae"
    );

if(isset($_REQUEST['id'])){
    if(preg_match("/'(?:\w*)\W*?[a-z].*(R|ELECT|OIN|NTO|HERE|NION)/i", $_REQUEST['id'])){
        die("Attack detected!!!");
    }
    $ad = get_ad($_GET['id']);
    ?>
    <HTML>
    <HEAD>
        <TITLE>NAUGHTY ADS c1994</TITLE>
    </HEAD>
    <BODY BGCOLOR="WHITE">
        <CENTER>
        <?php echo $ad['description'] ?><br />
        <a href="/">Home</a>
        </CENTER>
    </BODY>
    </HTML>
    <?php
    die;
}

?>
<HTML>
    <HEAD>
        <TITLE>NAUGHTY ADS c1994</TITLE>
    </HEAD>
    <BODY BGCOLOR="WHITE">
        <CENTER>
            <img class="ads" src="middle.png" width="800" height="600" usemap="#planetmap">
            <map name="planetmap">
              <area shape="rect" coords="287,93,523,261" href="?id=<?php echo array_pop($cols); ?>" alt="BDSM hookup">
              <area shape="rect" coords="542,93,774,261" href="?id=<?php echo array_pop($cols); ?>" alt="Fat fetish">

              <area shape="rect" coords="34,282,269,449" href="?id=<?php echo array_pop($cols); ?>" alt="Dirty mistress">
              <area shape="rect" coords="292,282,521,449" href="?id=<?php echo array_pop($cols); ?>" alt="Femdom one night stand">
              <area shape="rect" coords="545,282,777,449" href="?id=<?php echo array_pop($cols); ?>" alt="Waterboarding extasy">

              <area shape="rect" coords="33,468,266,595" href="?id=<?php echo array_pop($cols); ?>" alt="Kinky nightmare">
              <area shape="rect" coords="277,456,534,598" href="?id=<?php echo array_pop($cols); ?>" alt="Food fetish">
              <area shape="rect" coords="547,466,780,599" href="?id=<?php echo array_pop($cols); ?>" alt="Whip experience">

              <area shape="rect" coords="595,23,619,57" href="/admin" alt="Admin">
            </map>
        </CENTER>
    </BODY>
</HTML>
```

Pour bypasser l'expression régulière, on va utiliser le linefeed %0a puis ensuite travailler en mode blind.

On retrouve la table login avec ses champs name et password, puis on dump les champs (cf sploit.py)

username --> webmasterofdoom3755
password -- 5ebe2294ecd0e0f08eab7690d2a6ee69 --> secret

On se connecte à l'interface Admin, puis on rempli le formulaire avec le numéro de téléphone indiqué dans l'énnoncé, le flag est affiché.

SECT{~tr4nsv3stiT3s_w3lc0me_t00~}
