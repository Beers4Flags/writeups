# Malaysia - The guy who want to obfuscate everything.

We were given a phb (php file compiled with bcompiler) and a .dmp file ; the logs of the compiling phase.

At first we tried to find a decompiler for the .phb file, but after few hours of research we became tired of it.

We found the hint with the .dmp file, and then I tried to decompile it myself from the log file.

While showing my first findings of the php file, my friend ghozt told me that we could "script it".

Yeah, why not.

So we built a log-to-python converter.

To do so, we corrected somehow the file with many replaces (removing the "," unused spaces, and so on).

The goal was to have a decompiled script that we could easily read and update in order to find the flag.
That's what the parser.py file does.

After many (4-5) corrections of the script, we outputed the new3.py file, who was in charge to help us find the flag.

So, I found that there was a relation between the "decalage" (english: offset) and the comparison (IS_EQUAL to a int).

While reading the output of the new4.py script, it took me some time to find every letter (because I was tired of coding, I did it by hand, I know it's stupid) with the help fo the decalage.py script.

./decalage.py int offset ==> Prints one char of the flag. 
