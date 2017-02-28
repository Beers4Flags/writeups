The team told me that the QRcode was a reverse of base64 of the text.

Tie21 found out that there was a SQLI when the site was reading the QRCode

Using the python script, we could easily retrieve the content of the database.
Here is what we retrieved:

```
db:
information_schema
hackques_db

tables:
messages

fields:
id,name,message,secret_field
```

by group_concating the secret_field I got the flag ! o/


By Birdy42
