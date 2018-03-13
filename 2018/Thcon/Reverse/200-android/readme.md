# [CTF THCON18] Write-Up - Reverse: android (200 points)

## Description

Le challenge contenait un apk nommé « THC.apk ». Le texte qui l'accompagnait disait qu'il fallait trouver le serial pour activer l'application. N'ayant pas sous la main un émulateur android, je me suis lancé directement dans sa décompilation.

## Décompilation de l'apllication

Un APK est une simple archive zip que l'on peut extraire:

```
> unzip -d THC THC.apk
...
> ls THC
AndroidManifest.xml  classes.dex  META-INF  res  resources.ars
```

Il contient les fichiers classiques d'une application Android. Le bytecode java est dans le *classes.dex*. L'outil **dex2jar** permet de le convertir au format *jar*. En quelques mots, le *jar* est le format historique pour stocker le bytecode java, mais Android préfère le format *dex* qui est optimisé pour les mobiles.

L'application **jd-gui** est très pratique pour décompiler les **.jar*.

```
> dex2jar classes.dex
dex2jar classes.dex -> ./classes-dex2jar.jar
> jd-gui classes-dex2jar.jar
```

## Analyse du code

Dans l'interface, on voit immédiatement un package nommé *com.thc.bestpig.serial* qui contient un fichier *MainActivity.class*. Les activités sont au coeur des interfaces utilisateurs sous Android. Ouvrons-le:


```java
package com.thc.bestpig.serial;

import android.annotation.TargetApi;
import android.content.DialogInterface;
import android.content.DialogInterface.OnClickListener;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AlertDialog.Builder;
import android.support.v7.app.AppCompatActivity;
import android.text.InputFilter;
import android.text.InputFilter.AllCaps;
import android.text.InputFilter.LengthFilter;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity
  extends AppCompatActivity
{
  protected boolean checkPassword(String paramString)
  {
    if (validateSerial(paramString))
    {
      new AlertDialog.Builder(this).setTitle("Well done ;)").setMessage("You can now validate this challenge.\n\nThe flag is the serial").setCancelable(false).setNeutralButton("Ok", new DialogInterface.OnClickListener()
      {
        public void onClick(DialogInterface paramAnonymousDialogInterface, int paramAnonymousInt)
        {
          paramAnonymousDialogInterface = new Intent(MainActivity.this.getApplicationContext(), PremiumActivity.class);
          MainActivity.this.startActivity(paramAnonymousDialogInterface);
        }
      }).show();
      return true;
    }
    new AlertDialog.Builder(this).setTitle("Premium activation failed").setMessage("Please don't try random serial, buy a legit premium license to support developers.").setCancelable(false).setNeutralButton("Ok", new DialogInterface.OnClickListener()
    {
      public void onClick(DialogInterface paramAnonymousDialogInterface, int paramAnonymousInt) {}
    }).show();
    return false;
  }

  @TargetApi(21)
  protected void onCreate(final Bundle paramBundle)
  {
    super.onCreate(paramBundle);
    setContentView(2131296283);
    getSupportActionBar().setDisplayShowHomeEnabled(true);
    getSupportActionBar().setLogo(2131361792);
    getSupportActionBar().setDisplayUseLogoEnabled(true);
    paramBundle = (EditText)findViewById(2131165286);
    paramBundle.setFilters(new InputFilter[] { new InputFilter.AllCaps(), new InputFilter.LengthFilter(19) });
    ((Button)findViewById(2131165219)).setOnClickListener(new View.OnClickListener()
    {
      public void onClick(View paramAnonymousView)
      {
        MainActivity.this.checkPassword(paramBundle.getText().toString());
      }
    });
  }

  protected boolean validateSerial(String paramString)
  {
    if (paramString.length() != 19) {}
    while ((paramString.charAt(4) != '-') || (paramString.charAt(9) != '-') || (paramString.charAt(14) != '-') || (paramString.charAt(5) != paramString.charAt(6) + '\001') || (paramString.charAt(5) != paramString.charAt(18)) || (paramString.charAt(1) != paramString.charAt(18) % '\004' * 22) || (paramString.charAt(3) * paramString.charAt(15) / paramString.charAt(17) - 1 != paramString.charAt(10)) || (paramString.charAt(10) != paramString.charAt(1)) || (paramString.charAt(13) != paramString.charAt(10) + '\005') || (paramString.charAt(10) != paramString.charAt(5) - '\t') || (paramString.charAt(0) % paramString.charAt(7) * paramString.charAt(11) != 1440) || (paramString.charAt(2) - paramString.charAt(8) + paramString.charAt(12) != paramString.charAt(10) - '\t') || ((paramString.charAt(3) + paramString.charAt(12)) / 2 != paramString.charAt(16)) || (paramString.charAt(0) - paramString.charAt(2) + paramString.charAt(3) != paramString.charAt(12) + '\017') || (paramString.charAt(3) != paramString.charAt(13)) || (paramString.charAt(16) != paramString.charAt(0)) || (paramString.charAt(7) + '\001' != paramString.charAt(2)) || (paramString.charAt(15) + '\001' != paramString.charAt(11)) || (paramString.charAt(11) + '\003' != paramString.charAt(17)) || (paramString.charAt(7) + '\024' != paramString.charAt(6))) {
      return false;
    }
    return true;
  }
}
```

Il y a deux fonctions qui sautent aux yeux: **checkPassword()** et **validateSerial()**. Le **checkPassword()** appelle la fonction de validation du serial et affiche success en disant que le flag est le serial lui-même.

La fonction **validateSerial()** est très simple. Elle teste une série de conditions entre les 20 caractères du serial. On est sur un cas typique où il suffit de satisfaire toutes les contraintes entre les caractères pour trouver la valeur de chacun d'eux. Ce type de problème se résout à l'aide d'un solveur SAT.

## Trouver le serial avec z3

La librarie z3 a un solveur SAT très pratique. La définition des variables et des contraintes se fait naturellement en Python:

```python
#!/usr/bin/env python

from z3 import *
import os

solver = Solver()

# Define the serial characters
c0 = Int('c0')
c1 = Int('c1')
c2 = Int('c2')
c3 = Int('c3')
c4 = Int('c4')
c5 = Int('c5')
c6 = Int('c6')
c7 = Int('c7')
c8 = Int('c8')
c9 = Int('c9')
c10 = Int('c10')
c11 = Int('c11')
c12 = Int('c12')
c13 = Int('c13')
c14 = Int('c14')
c15 = Int('c15')
c16 = Int('c16')
c17 = Int('c17')
c18 = Int('c18')
c19 = Int('c19')

# Define the possible values for each characters,
# from ' ' and '~' (printable chars).
solver.add((c0 >= 0x20, c0 <=0x7e))
solver.add((c1 >= 0x20, c1 <=0x7e))
solver.add((c2 >= 0x20, c2 <=0x7e))
solver.add((c3 >= 0x20, c3 <=0x7e))
solver.add((c4 >= 0x20, c4 <=0x7e))
solver.add((c5 >= 0x20, c5 <=0x7e))
solver.add((c6 >= 0x20, c6 <=0x7e))
solver.add((c7 >= 0x20, c7 <=0x7e))
solver.add((c8 >= 0x20, c8 <=0x7e))
solver.add((c9 >= 0x20, c9 <=0x7e))
solver.add((c10 >= 0x20, c10 <=0x7e))
solver.add((c11 >= 0x20, c11 <=0x7e))
solver.add((c12 >= 0x20, c12 <=0x7e))
solver.add((c13 >= 0x20, c13 <=0x7e))
solver.add((c14 >= 0x20, c14 <=0x7e))
solver.add((c15 >= 0x20, c15 <=0x7e))
solver.add((c16 >= 0x20, c16 <=0x7e))
solver.add((c17 >= 0x20, c17 <=0x7e))
solver.add((c18 >= 0x20, c18 <=0x7e))
solver.add((c19 >= 0x20, c19 <=0x7e))

# Define the constraints that have been
# founded in MainActivity.class.
solver.add(c4 == 45)
solver.add(c9 == 45)
solver.add(c14 == 45)
solver.add(c5 == (c6 + 1))
solver.add(c5 == c18)
solver.add(c1 == c18 % 4 * 22)
solver.add(c10 == c3 * c15 / c17 - 1)
solver.add(c10 == c1)
solver.add(c13 == c10 + 5)
solver.add(c10 == c5 - 9)
solver.add(c0 % c7 * c11 == 1440)
solver.add(c2 - c8 + c12 == c10 - 9)
solver.add((c3 + c12) / 2 == c16)
solver.add(c0 - c2 + c3 == c12 + 15)
solver.add(c3 == c13)
solver.add(c16 == c0)
solver.add(c7 + 1 == c2)
solver.add(c15 + 1 == c11)
solver.add(c11 + 3 == c17)
solver.add(c7 + 20 == c6)

# Check() returns true if there is a solution
# and model() the values founded.
if solver.check():
	print(solver.model())
else:
	print('Not found.')
```

On lance le script...

```
> python2 solver.py
[k!3 = 18,
 c17 = 83,
 c19 = 33,
 k!7 = 1,
 c8 = 71,
 c12 = 73,
 c2 = 55,
 c15 = 79,
 c11 = 80,
 c1 = 66,
 c18 = 75,
 c5 = 75,
 c6 = 74,
 c7 = 54,
 c16 = 72,
 c0 = 72,
 c3 = 71,
 c13 = 71,
 c10 = 66,
 c14 = 45,
 c9 = 45,
 c4 = 45]
```

Une fois les caractères dans l'ordre et le decimal converti en ascii, on obtient le serial:

```
HB7G-KJ6G-BPIG-OHSK!
```
Merci aux organisateurs :)
