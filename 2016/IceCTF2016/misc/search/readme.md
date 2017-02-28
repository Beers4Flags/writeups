# Search (Misc · 40 pt)

We have as a information "...maybe its all about the conTEXT." The challenge insists well  on 'TEXT'

```
dig -t txt search.icec.tf

; <<>> DiG 9.9.5-9+deb8u6-Debian <<>> -t txt search.icec.tf
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 15523
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 2, ADDITIONAL: 3

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;search.icec.tf.			IN	TXT

;; ANSWER SECTION:
search.icec.tf.		300	IN	TXT	"IceCTF{flag5_all_0v3r_the_Plac3}"
...
```

The flag is : IceCTF{flag5_all_0v3r_the_Plac3}
