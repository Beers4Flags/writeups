---
layout: post
title: "IceCTF 2016 Blue Monday"
date: 2016-09-20 13:00:00 +0200
comments: true
categories: wu
---

Those who came before me lived through their vocations From the past until completion, 
they'll turn away no more And still I find it so hard to say what I need to say 
But I'm quite sure that you'll tell me just how I should feel today

It seems to be the lyrics from the New Order music Blue Monday 


data analysis with "file" command

=> MIDI FORMAT


I used VLC to play the file. Nothing interessting, just some musicals notes.



Data conversion (musical notes) from midi file to CSV with the tool "Midi 2 csv converter"
http://www.fourmilab.ch/webtools/midicsv/midicsv-1.1.tar.gz


Extraction to CSV :
```
@Rem    Test release versions of Midicsv and Csvmidi with
@Rem    an identity transform.

Release\Midicsv test.mid w.csv
Release\Csvmidi w.csv w.mid
Rem  The following comparison should not find any differences
cmp test.mid w.mid
```

file .csv
```
0, 0, Header, 1, 1, 220
1, 0, Start_track
1, 0, Note_on_c, 0, 73, 100
1, 220, Note_off_c, 0, 73, 0
1, 220, Note_on_c, 0, 99, 100
1, 440, Note_off_c, 0, 99, 0
1, 440, Note_on_c, 0, 101, 100
1, 660, Note_off_c, 0, 101, 0
1, 660, Note_on_c, 0, 67, 100
1, 880, Note_off_c, 0, 67, 0
1, 880, Note_on_c, 0, 84, 100
1, 1100, Note_off_c, 0, 84, 0
1, 1100, Note_on_c, 0, 70, 100
1, 1320, Note_off_c, 0, 70, 0
1, 1320, Note_on_c, 0, 123, 100
1, 1540, Note_off_c, 0, 123, 0
1, 1540, Note_on_c, 0, 72, 100
1, 1760, Note_off_c, 0, 72, 0
1, 1760, Note_on_c, 0, 65, 100
1, 1980, Note_off_c, 0, 65, 0
1, 1980, Note_on_c, 0, 99, 100
1, 2200, Note_off_c, 0, 99, 0
1, 2200, Note_on_c, 0, 107, 100
1, 2420, Note_off_c, 0, 107, 0
1, 2420, Note_on_c, 0, 49, 100
1, 2640, Note_off_c, 0, 49, 0
1, 2640, Note_on_c, 0, 110, 100
1, 2860, Note_off_c, 0, 110, 0
1, 2860, Note_on_c, 0, 57, 100
1, 3080, Note_off_c, 0, 57, 0
1, 3080, Note_on_c, 0, 95, 100
1, 3300, Note_off_c, 0, 95, 0
1, 3300, Note_on_c, 0, 109, 100
1, 3520, Note_off_c, 0, 109, 0
1, 3520, Note_on_c, 0, 85, 100
1, 3740, Note_off_c, 0, 85, 0
1, 3740, Note_on_c, 0, 53, 100
1, 3960, Note_off_c, 0, 53, 0
1, 3960, Note_on_c, 0, 73, 100
1, 4180, Note_off_c, 0, 73, 0
1, 4180, Note_on_c, 0, 99, 100
1, 4400, Note_off_c, 0, 99, 0
1, 4400, Note_on_c, 0, 95, 100
1, 4620, Note_off_c, 0, 95, 0
1, 4620, Note_on_c, 0, 87, 100
1, 4840, Note_off_c, 0, 87, 0
1, 4840, Note_on_c, 0, 49, 100
1, 5060, Note_off_c, 0, 49, 0
1, 5060, Note_on_c, 0, 55, 100
1, 5280, Note_off_c, 0, 55, 0
1, 5280, Note_on_c, 0, 104, 100
1, 5500, Note_off_c, 0, 104, 0
1, 5500, Note_on_c, 0, 95, 100
1, 5720, Note_off_c, 0, 95, 0
1, 5720, Note_on_c, 0, 109, 100
1, 5940, Note_off_c, 0, 109, 0
1, 5940, Note_on_c, 0, 73, 100
1, 6160, Note_off_c, 0, 73, 0
1, 6160, Note_on_c, 0, 68, 100
1, 6380, Note_off_c, 0, 68, 0
1, 6380, Note_on_c, 0, 49, 100
1, 6600, Note_off_c, 0, 49, 0
1, 6600, Note_on_c, 0, 53, 100
1, 6820, Note_off_c, 0, 53, 0
1, 6820, Note_on_c, 0, 95, 100
1, 7040, Note_off_c, 0, 95, 0
1, 7040, Note_on_c, 0, 76, 100
1, 7260, Note_off_c, 0, 76, 0
1, 7260, Note_on_c, 0, 51, 100
1, 7480, Note_off_c, 0, 51, 0
1, 7480, Note_on_c, 0, 116, 100
1, 7700, Note_off_c, 0, 116, 0
1, 7700, Note_on_c, 0, 53, 100
1, 7920, Note_off_c, 0, 53, 0
1, 7920, Note_on_c, 0, 95, 100
1, 8140, Note_off_c, 0, 95, 0
1, 8140, Note_on_c, 0, 72, 100
1, 8360, Note_off_c, 0, 72, 0
1, 8360, Note_on_c, 0, 52, 100
1, 8580, Note_off_c, 0, 52, 0
1, 8580, Note_on_c, 0, 118, 100
1, 8800, Note_off_c, 0, 118, 0
1, 8800, Note_on_c, 0, 69, 100
1, 9020, Note_off_c, 0, 69, 0
1, 9020, Note_on_c, 0, 95, 100
1, 9240, Note_off_c, 0, 95, 0
1, 9240, Note_on_c, 0, 97, 100
1, 9460, Note_off_c, 0, 97, 0
1, 9460, Note_on_c, 0, 95, 100
1, 9680, Note_off_c, 0, 95, 0
1, 9680, Note_on_c, 0, 114, 100
1, 9900, Note_off_c, 0, 114, 0
1, 9900, Note_on_c, 0, 52, 100
1, 10120, Note_off_c, 0, 52, 0
1, 10120, Note_on_c, 0, 118, 100
1, 10340, Note_off_c, 0, 118, 0
1, 10340, Note_on_c, 0, 51, 100
1, 10560, Note_off_c, 0, 51, 0
1, 10560, Note_on_c, 0, 125, 100
1, 10780, Note_off_c, 0, 125, 0
1, 11780, End_track
0, 0, End_of_file
```



conversion from decimal to ascii : 


IceCTF{HAck1n9_mU5Ic_W17h_mID15_L3t5_H4vE_a_r4v3}


flagged

eilco.

