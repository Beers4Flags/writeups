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
