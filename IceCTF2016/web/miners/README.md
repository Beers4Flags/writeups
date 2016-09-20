# Miners

This one was really easy, it said you must login but there is not users in the database. The source code showed an obvious SQLI flaw on the username field.

username :
```
asdf' union select 1,2,3 #
```

I was logged in and had the flag.
