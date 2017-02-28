# kitty (web · 70 pt)

They managed to secure their website this time and moved the hashing to the server :(. 
We managed to leak this hash of the admin's password though! c7e83c01ed3ef54812673569b2d79c4e1f6554ffeb27706e98c067de9ab12d1a. 
Can you get the flag? kitty.vuln.icec.tf

first I check the hash on hashtype checker :)

https://md5hashing.net/hash_type_checker


```
c7e83c01ed3ef54812673569b2d79c4e1f6554ffeb27706e98c067de9ab12d1a

```

it's a sha256 hash


2 solutions : 

We can use Hashcat to brute force it or we can check online if the hash is already known


http://md5decrypt.net/Sha256/


```
c7e83c01ed3ef54812673569b2d79c4e1f6554ffeb27706e98c067de9ab12d1a : Vo83*

```

=> kitty.vuln.icec.tf : admin / Vo83*


Logged in!


Your flag is: IceCTF{i_guess_hashing_isnt_everything_in_this_world}


eilco
