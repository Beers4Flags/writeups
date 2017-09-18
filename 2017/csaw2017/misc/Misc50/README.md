---
layout: post
title: "CSAW CTF"
date: 18 Septembre 2017
comments: true
categories: wu
---
Il s'agit de retrouver à partir d'un envoi de plusieurs bits un suite
d'octets composant le flag. Les bits envoyés sont
0 <8 bits de données> parité 1

On reconstitue le message en demandant la reatransmission plusieurs fois et
en prenant pour chaque bit le bit majoritaire. Ça marche bien.

francois@aramis:~/BFF/beers4flags/writeups/2017/csaw2017/misc/Misc50$ python payload.py
```
[+] Opening connection to misc.chal.csaw.io on port 4239: Done
0 0 1 1 0 0 1 1 0 0 1 102 f
0 0 1 1 0 1 1 0 0 0 1 108 fl
0 0 1 1 0 0 0 0 1 1 1 97 fla
0 0 1 1 0 0 1 1 1 1 1 103 flag
0 0 1 1 1 1 0 1 1 0 1 123 flag{
0 0 1 0 0 0 0 0 0 1 1 64 flag{@
0 0 1 1 0 1 1 1 0 1 1 110 flag{@n
0 0 1 0 1 1 1 1 1 0 1 95 flag{@n_
0 0 1 1 0 1 0 0 1 0 1 105 flag{@n_i
0 0 1 1 0 1 1 1 0 1 1 110 flag{@n_in
0 0 1 1 1 0 1 0 0 0 1 116 flag{@n_int
0 0 0 1 1 0 0 1 1 0 1 51 flag{@n_int3
0 0 1 1 1 0 0 1 0 0 1 114 flag{@n_int3r
0 0 1 1 0 0 1 1 0 0 1 102 flag{@n_int3rf
0 0 1 1 0 0 0 0 1 1 1 97 flag{@n_int3rfa
0 0 1 1 0 0 0 1 1 0 1 99 flag{@n_int3rfac
0 0 1 1 0 0 1 0 1 0 1 101 flag{@n_int3rface
0 0 1 0 1 1 1 1 1 0 1 95 flag{@n_int3rface_
0 0 1 1 0 0 0 1 0 1 1 98 flag{@n_int3rface_b
0 0 1 1 0 0 1 0 1 0 1 101 flag{@n_int3rface_be
0 0 1 1 1 0 1 0 0 0 1 116 flag{@n_int3rface_bet
0 0 1 1 1 0 1 1 1 0 1 119 flag{@n_int3rface_betw
0 0 0 1 1 0 0 1 1 0 1 51 flag{@n_int3rface_betw3
0 0 0 1 1 0 0 1 1 0 1 51 flag{@n_int3rface_betw33
0 0 1 1 0 1 1 1 0 1 1 110 flag{@n_int3rface_betw33n
0 0 1 0 1 1 1 1 1 0 1 95 flag{@n_int3rface_betw33n_
0 0 1 1 0 0 1 0 0 1 1 100 flag{@n_int3rface_betw33n_d
0 0 1 1 0 0 0 0 1 1 1 97 flag{@n_int3rface_betw33n_da
0 0 1 1 1 0 1 0 0 0 1 116 flag{@n_int3rface_betw33n_dat
0 0 1 1 0 0 0 0 1 1 1 97 flag{@n_int3rface_betw33n_data
0 0 1 0 1 1 1 1 1 0 1 95 flag{@n_int3rface_betw33n_data_
0 0 1 1 1 0 1 0 0 0 1 116 flag{@n_int3rface_betw33n_data_t
0 0 1 1 0 0 1 0 1 0 1 101 flag{@n_int3rface_betw33n_data_te
0 0 1 1 1 0 0 1 0 0 1 114 flag{@n_int3rface_betw33n_data_ter
0 0 1 1 0 1 1 0 1 1 1 109 flag{@n_int3rface_betw33n_data_term
0 0 0 1 1 0 0 0 1 1 1 49 flag{@n_int3rface_betw33n_data_term1
0 0 1 1 0 1 1 1 0 1 1 110 flag{@n_int3rface_betw33n_data_term1n
0 0 1 1 0 1 0 0 1 1 1 105 flag{@n_int3rface_betw33n_data_term1ni
0 0 1 1 0 1 1 0 0 0 1 108 flag{@n_int3rface_betw33n_data_term1nil
0 0 1 0 1 1 1 1 1 0 1 95 flag{@n_int3rface_betw33n_data_term1nil_
0 0 0 1 1 0 0 1 1 0 1 51 flag{@n_int3rface_betw33n_data_term1nil_3
0 0 1 1 1 0 0 0 1 0 1 113 flag{@n_int3rface_betw33n_data_term1nil_3q
0 0 1 1 1 0 1 0 1 1 1 117 flag{@n_int3rface_betw33n_data_term1nil_3qu
0 0 1 1 0 1 0 0 1 0 1 105 flag{@n_int3rface_betw33n_data_term1nil_3qui
0 0 1 1 1 0 0 0 0 1 1 112 flag{@n_int3rface_betw33n_data_term1nil_3quip
0 0 1 1 0 1 1 0 1 1 1 109 flag{@n_int3rface_betw33n_data_term1nil_3quipm
0 0 1 1 0 0 1 0 1 0 1 101 flag{@n_int3rface_betw33n_data_term1nil_3quipme
0 0 1 1 0 1 1 1 0 1 1 110 flag{@n_int3rface_betw33n_data_term1nil_3quipmen
0 0 1 1 1 0 1 0 0 0 1 116 flag{@n_int3rface_betw33n_data_term1nil_3quipment
0 0 1 0 1 1 1 1 1 0 1 95 flag{@n_int3rface_betw33n_data_term1nil_3quipment_
0 0 1 1 0 0 0 0 1 1 1 97 flag{@n_int3rface_betw33n_data_term1nil_3quipment_a
0 0 1 1 0 1 1 1 0 1 1 110 flag{@n_int3rface_betw33n_data_term1nil_3quipment_an
0 0 1 1 0 0 1 0 0 1 1 100 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and
0 0 1 0 1 1 1 1 1 0 1 95 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_
0 0 1 1 0 0 1 0 0 1 1 100 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d
0 0 1 0 0 0 0 0 0 1 1 64 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@
0 0 1 1 1 0 1 0 0 0 1 116 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t
0 0 1 0 0 0 0 0 0 1 1 64 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@
0 0 1 0 1 1 1 1 1 0 1 95 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_
0 0 1 1 0 0 0 1 1 0 1 99 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_c
0 0 1 1 0 1 0 0 1 0 1 105 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_ci
0 0 1 1 1 0 0 1 0 0 1 114 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_cir
0 0 1 1 0 0 0 1 1 0 1 99 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circ
0 0 1 1 1 0 1 0 1 1 1 117 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circu
0 0 1 1 0 1 0 0 1 0 1 105 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circui
0 0 1 1 1 0 1 0 0 0 1 116 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit
0 0 0 1 0 1 1 0 1 0 1 45 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-
0 0 1 1 1 0 1 0 0 0 1 116 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-t
0 0 1 1 0 0 1 0 1 0 1 101 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-te
0 0 1 1 1 0 0 1 0 0 1 114 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-ter
0 0 1 1 0 1 1 0 1 1 1 109 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term
0 0 0 1 1 0 0 0 1 1 1 49 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1
0 0 1 1 0 1 1 1 0 1 1 110 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1n
0 0 1 1 0 0 0 0 1 1 1 97 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1na
0 0 1 1 1 0 1 0 0 0 1 116 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nat
0 0 1 1 0 1 0 0 1 0 1 105 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nati
0 0 1 1 0 1 1 1 0 1 1 110 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1natin
0 0 1 1 0 0 1 1 1 1 1 103 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nating
0 0 1 0 1 1 1 1 1 0 1 95 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nating_
0 0 0 1 1 0 0 1 1 0 1 51 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nating_3
0 0 1 1 1 0 0 0 1 0 1 113 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nating_3q
0 0 1 1 1 0 1 0 1 1 1 117 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nating_3qu
0 0 1 1 0 1 0 0 1 0 1 105 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nating_3qui
0 0 1 1 1 0 0 0 0 1 1 112 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nating_3quip
0 0 1 1 0 1 1 0 1 1 1 109 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nating_3quipm
0 0 1 1 0 0 1 0 1 0 1 101 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nating_3quipme
0 0 1 1 0 1 1 1 0 1 1 110 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nating_3quipmen
0 0 1 1 1 0 1 0 0 0 1 116 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nating_3quipment
0 0 1 1 1 1 1 0 1 0 1 125 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nating_3quipment}
0 0 0 0 0 1 0 1 0 0 1 10 flag{@n_int3rface_betw33n_data_term1nil_3quipment_and_d@t@_circuit-term1nating_3quipment}
```