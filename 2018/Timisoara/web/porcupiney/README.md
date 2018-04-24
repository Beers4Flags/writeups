# CTF - 2018 - Timisoara CTF 2018 Quals / Web / porcupiney

## web - 50 pts - SSL certificate

- We got an html website with nothing interresting.

- When we look at alternative name of the certificate, we find an hidden one
```
true | openssl s_client -connect porcupiney.woodlandhighschool.xyz:443 | openssl x509 -noout -text | grep DNS
depth=2 O = Digital Signature Trust Co., CN = DST Root CA X3
verify return:1
depth=1 C = US, O = Let's Encrypt, CN = Let's Encrypt Authority X3
verify return:1
depth=0 CN = porcupiney.woodlandhighschool.xyz
verify return:1
DONE
                DNS:nonononono.woodlandhighschool.xyz, DNS:porcupiney.woodlandhighschool.xyz
```

- When we navigate to it, the flag is in the page :
```
curl -s https://nonononono.woodlandhighschool.xyz | grep timctf
<p>Look away! Shush! I give you flag, you shush, ok? timctf{w00dl4nd_cr1tt3rs_s3cur3_chr1stm4s}</p>
```

- Demo here : [![asciicast](https://asciinema.org/a/PC9bywxGJb1gYi4JtItgLIXy0.png)](https://asciinema.org/a/PC9bywxGJb1gYi4JtItgLIXy0?speed=2)  

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
