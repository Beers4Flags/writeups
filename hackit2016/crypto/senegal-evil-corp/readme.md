**Evil corp (crypto 115pts)**

EN:  Genegal Thompson welcomes you!  Let me be extremely brief. Our forensic team have already been investigating "The Great Plantation" project for 2 years. During this long period we knew a lot of interesting things like: 1) This is the project of Masons. 2) The main target is to take over the world with planting own people into big companies. 3) Masons do not trust modern encryption algorithms. 4) Masons think their own alphabet will let them to communicate more securely than anything else. Short time ago we have withdrawn the notebook of one of their members. There was one interesting file named "THEPlantation.txt". Surely, it was encrypted. Help us to pull the info out of this! Yours, Gen. Tompson


We have a text that looks like "leet speak" : +θΔӕ¥ ωΣ ∫¦ɲӕλλ¥ Ͻθᛗ∏λΣ+ΣΔ 

So my search first I decided to find some known characters as Σ / λ / β.
This characters strongly resemble ancient Greek and I tried with latin characters traduction, but it doesn't seems to be the right track.

Thankfully a big thank you to our teammate ghozt for his idea :

```
Starting on the first words of the text
+θΔӕ¥ ωΣ ∫¦ɲӕλλ¥ Ͻθᛗ∏λΣ+ΣΔ +ϦΣ 9ʁΣӕ+ ∏λӕɲ+ӕ+¦θɲ ∏ʁθτΣϽ+
ӕɲΔ βΣλθω ¦§ Σɲ+¦+¦Σ§ ωΣ Ϧӕ✔Σ ¦ɲ θµʁ ∏θϽϟΣ+ ∫θʁ ɲθω

We can guess words :
ωΣ  = we 
+ϦΣ = the
¦ɲ  = in 
ӕɲΔ = and
θµʁ = our
∫θʁ = for
ɲθω = now
...
```

We can now determine the corresponding alphabet and I make a little script for decrypt the text. (See script.sh)

```BASH
#!/bin/bash

file="orig.txt"
output="output.txt"

a="s/ӕ/a/g"
b="s/β/b/g"
c="s/Ͻ/c/g"
d="s/Δ/d/g"
e="s/Σ/e/g"
f="s/∫/f/g"
g="s/9/g/g"
h="s/Ϧ/h/g"
i="s/¦/i/g"
k="s/ϟ/k/g"
l="s/λ/l/g"
m="s/ᛗ/m/g"
n="s/ɲ/n/g"
o="s/θ/o/g"
p="s/∏/p/g"
q="s/ⵕ/q/g"
r="s/ʁ/r/g"
s="s/§/s/g"
t="s/+/t/g"
tt="s/τ/t/g"
u="s/µ/u/g"
v="s/✔/v/g"
w="s/ω/w/g"
y="s/¥/y/g"
z="s/ɀ/z/g"

while read -r line ;do
	echo $line | sed -e $a -e $b -e $c -e $d -e $e -e $f -e $g -e $h -e $i -e $k -e $l -e $m -e $n -e $o -e $p -e $q -e $r -e $s -e $t -e $tt -e $u -e $v -e $w -e $y -e $z
done < ${file} > ${output}
```

And the output.txt file done the solution : flagis massonsareeverywherelookbehindyou


The flag is : h4ck1t{massonsareeverywherelookbehindyou}

by team Beers4Flags
