# Exposed

In this example, we realized there was a flaw with the apache configuration, since we were able to clone the source files from the git repository.

To get any repository from the website
```bash
  mkdir exposed
  git init
  git add remote origin http://exposed.vuln.icec.tf/.git
  git pull origin _hash_
```

The hash list was in log file:

```bash
  wget http://exposed.vuln.icec.tf/.git/logs/heads/master
```

We only needed to pull every hash listed.

(note: the file is not the same as the cloned one).
flag was located in index.php file.
