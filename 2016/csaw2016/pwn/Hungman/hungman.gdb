Le script a débuté sur dim. 18 sept. 2016 11:57:13 CEST
]0;francois@athos: ~/tmp/csawfrancois@athos:~/tmp/csaw$ ./hungman [1@g[1@d[1@b[1@ 
GNU gdb (Debian 7.7.1+dfsg-5) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
ansicolor = 'off'
Reading symbols from ./hungman...(no debugging symbols found)...done.
(gdb) r
Starting program: /home/francois/tmp/csaw/hungman 
What's your name?
AAABBBCC        ^C
Program received signal SIGINT, Interrupt.
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0xFFFFFFFFFFFFFE00  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDCA8  o d I t s Z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFFFFFDCD0  RDX: 0x00000000000000F7  RCX: 0xFFFFFFFFFFFFFFFF  RIP: 0x00007FFFF7B0CDF0
  R8 : 0x0000000000000000  R9 : 0x00007FFFF7DEADE0  R10: 0x00007FFFFFFFDA70  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDCA8]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDCA8 : 0x00400f8e   0x00000000 - 0xffffffff   0x00000000 ..@.............
0x00007FFFFFFFDCB8 : 0x004003c8   0x00000000 - 0xf7a3ea90   0x00007fff ..@.............
0x00007FFFFFFFDCC8 : 0xf7ff74c0   0x00007fff - 0x00000000   0x00000000 .t..............
0x00007FFFFFFFDCD8 : 0x00000000   0x00000000 - 0x00000000   0x00000000 ................
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x7ffff7b0cdf0 <__read_nocancel+7>:	cmp    $0xfffffffffffff001,%rax
   0x7ffff7b0cdf6 <__read_nocancel+13>:	jae    0x7ffff7b0ce29 <read+73>
   0x7ffff7b0cdf8 <__read_nocancel+15>:	retq   
   0x7ffff7b0cdf9 <read+25>:	sub    $0x8,%rsp
   0x7ffff7b0cdfd <read+29>:	callq  0x7ffff7b25e30 <__libc_enable_asynccancel>
   0x7ffff7b0ce02 <read+34>:	mov    %rax,(%rsp)
   0x7ffff7b0ce06 <read+38>:	mov    $0x0,%eax
   0x7ffff7b0ce0b <read+43>:	syscall 
-----------------------------------------------------------------------------------------------------------------------------
0x00007ffff7b0cdf0 in __read_nocancel () at ../sysdeps/unix/syscall-template.S:81
81	../sysdeps/unix/syscall-template.S: Aucun fichier ou dossier de ce type.
(gdb) quit
]0;francois@athos: ~/tmp/csawfrancois@athos:~/tmp/csaw$ gdb ./hungman 
GNU gdb (Debian 7.7.1+dfsg-5) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
ansicolor = 'off'
Reading symbols from ./hungman...(no debugging symbols found)...done.
(gdb) r
Starting program: /home/francois/tmp/csaw/hungman 
What's your name?
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
Welcome AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
________________________________
azert
___________a________a___________
______zz___a________a___________
______zz___a_e______a___________
______zz___a_e______ar_____r____
______zz___a_e______ar_____r____
yuiop
______zz___a_e______ar_____r____
______zz___a_e__u___ar_____r____
______zz_i_a_e__u___ar_i___r____
______zz_i_aoeo_u___ar_i___r____
p_____zz_i_aoeo_u___ar_i___r____
q
p_____zz_i_aoeoqu___ar_i___r____
s
High score! change name?
y
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHAAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH

Program received signal SIGSEGV, Segmentation fault.
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000000000  RBX: 0x00007FFFFFFFDB40  RBP: 0x00007FFFFFFFDB30  RSP: 0x00007FFFFFFFD560  o d I t S z a P c 
  RDI: 0x4848484847474747  RSI: 0x0000000000401175  RDX: 0x0000000000000020  RCX: 0xFFFFFFFFFFFFFFFF  RIP: 0x00007FFFF7A7BDCC
  R8 : 0x4848484847474747  R9 : 0x00007FFFF7A7C99A  R10: 0x00007FFFFFFFDB40  R11: 0x00007FFFF7A81DA0  R12: 0x0000000000401175
  R13: 0x0000000000000000  R14: 0x0000000000000000  R15: 0x00007FFFFFFFDCA8
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFD560]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFD560 : 0x004004a1   0x00000000 - 0xf7ffe180   0x00007fff ..@.............
0x00007FFFFFFFD570 : 0xffffd6c0   0x00007fff - 0x003aaa20   0x00000000 ........ .:.....
0x00007FFFFFFFD580 : 0x00000006   0x00000000 - 0xffffd338   0x00007fff ........8.......
0x00007FFFFFFFD590 : 0x00000802   0x00000000 - 0x00120107   0x00000000 ................
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x7ffff7a7bdcc <_IO_vfprintf_internal+19468>:	repnz scas %es:(%rdi),%al
   0x7ffff7a7bdce <_IO_vfprintf_internal+19470>:	movl   $0x0,-0x4c8(%rbp)
   0x7ffff7a7bdd8 <_IO_vfprintf_internal+19480>:	mov    %rcx,%rsi
   0x7ffff7a7bddb <_IO_vfprintf_internal+19483>:	not    %rsi
   0x7ffff7a7bdde <_IO_vfprintf_internal+19486>:	lea    -0x1(%rsi),%r10
   0x7ffff7a7bde2 <_IO_vfprintf_internal+19490>:	jmpq   0x7ffff7a7bb34 <_IO_vfprintf_internal+18804>
   0x7ffff7a7bde7 <_IO_vfprintf_internal+19495>:	lea    -0x480(%rbp),%rax
   0x7ffff7a7bdee <_IO_vfprintf_internal+19502>:	mov    %r8,-0x470(%rbp)
-----------------------------------------------------------------------------------------------------------------------------
0x00007ffff7a7bdcc in _IO_vfprintf_internal (s=s@entry=0x7fffffffdb40, format=<optimized out>, format@entry=0x401175 "Highest player: %s", ap=ap@entry=0x7fffffffdca8) at vfprintf.c:1642
1642	vfprintf.c: Aucun fichier ou dossier de ce type.
(gdb) 
(gdb) backtrace
#0  0x00007ffff7a7bdcc in _IO_vfprintf_internal (s=s@entry=0x7fffffffdb40, format=<optimized out>, format@entry=0x401175 "Highest player: %s", ap=ap@entry=0x7fffffffdca8) at vfprintf.c:1642
#1  0x00007ffff7aa3409 in _IO_vsnprintf (string=0x602100 "Highest player: e ", maxlen=<optimized out>, format=0x401175 "Highest player: %s", args=args@entry=0x7fffffffdca8) at vsnprintf.c:119
#2  0x00007ffff7a81e22 in __snprintf (s=<optimized out>, maxlen=<optimized out>, format=<optimized out>) at snprintf.c:33
#3  0x0000000000400ef9 in ?? ()
#4  0x0000000000400ace in ?? ()
#5  0x00007ffff7a52b45 in __libc_start_main (main=0x400a0d, argc=0x1, argv=0x7fffffffdee8, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffded8) at libc-start.c:287
#6  0x0000000000400949 in ?? ()
(gdb) x/s 0x602100
0x602100:	"Highest player: e "
(gdb) x/s 0x7fffffffdca8
0x7fffffffdca8:	" "
(gdb) x/16[K[K4wx 0x7fffffffdca8~[K
0x7fffffffdca8:	0x00000020	0x00000030	0xffffdd80	0x00007fff
(gdb) x/[K[Kbreak *0x0400ef4
Breakpoint 1 at 0x400ef4
(gdb) r
Starting program: /home/francois/tmp/csaw/hungman 
What's your name?
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
Welcome AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
________________________________
azerty
________________________________
________________________________
_________________e______________
_________________e___________r__
_____t______t____e________t__r__
_____t______t____e_____y__t__r__
u
Default Highscore  score: 64
Continue? 
azertyu
________________________________
______z_________________________
__e___z___________________e_____
__e___z________r__________e_____
__e___z________r__t_______e_____
__e___z________r__t_______eyy___
_ue___z________r__t_______eyy___
i
_ue_i_z____i_i_r__t_____i_eyy___
o
_ue_i_z____i_i_r__t_____i_eyy___
q
_ue_i_z____i_i_r__t_____i_eyy___
s
_ue_i_z____i_i_r__ts____i_eyy___
d
_ue_i_z____i_i_r__ts____i_eyy__d
g
High score! change name?
y
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHAAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000000000  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000602100  RSI: 0x0000000000000200  RDX: 0x0000000000401175  RCX: 0x4848484847474747  RIP: 0x0000000000400EF4
  R8 : 0x00007FFFF7DD6678  R9 : 0x00007FFFF7DD6670  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796702e5   0x00000000  .@.......gy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000041 ....!.......A...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
   0x400f05:	mov    -0x58(%rbp),%rax
   0x400f09:	add    $0x10,%rax
   0x400f0d:	mov    $0x1a,%edx
   0x400f12:	mov    $0x0,%esi
-----------------------------------------------------------------------------------------------------------------------------

Breakpoint 1, 0x0000000000400ef4 in ?? ()
(gdb) x/s 0x0000000000401175
0x401175:	"Highest player: %s"
(gdb) x/s 0x0000000000602100
0x602100:	"Default Highscore "
(gdb) x/30gx $rsp
0x7fffffffdd80:	0x0000000300000000	0x0000000000603040
0x7fffffffdd90:	0x0000000000400920	0x00000000796702e5
0x7fffffffdda0:	0x000000210000000e	0x000000410000000e
0x7fffffffddb0:	0x0000000000000020	0x0000000000000020
0x7fffffffddc0:	0x0000000000000020	0x00000000006030d0
0x7fffffffddd0:	0x0000000000603100	0x0000000000603140
0x7fffffffdde0:	0x00007fffffffde00	0x0000000000400ace
0x7fffffffddf0:	0x00007fffffffdee0	0x0000000361000000
0x7fffffffde00:	0x0000000000000000	0x00007ffff7a52b45
0x7fffffffde10:	0x0000000000000000	0x00007fffffffdee8
0x7fffffffde20:	0x0000000100000000	0x0000000000400a0d
0x7fffffffde30:	0x0000000000000000	0x510329d0a59910e9
0x7fffffffde40:	0x0000000000400920	0x00007fffffffdee0
0x7fffffffde50:	0x0000000000000000	0x0000000000000000
0x7fffffffde60:	0xaefcd62f19b910e9	0xaefcc69af06310e9
(gdb) 
0x7fffffffde70:	0x0000000000000000	0x0000000000000000
0x7fffffffde80:	0x0000000000000000	0x0000000000401080
0x7fffffffde90:	0x00007fffffffdee8	0x0000000000000001
0x7fffffffdea0:	0x0000000000000000	0x0000000000000000
0x7fffffffdeb0:	0x0000000000400920	0x00007fffffffdee0
0x7fffffffdec0:	0x0000000000000000	0x0000000000400949
0x7fffffffded0:	0x00007fffffffded8	0x000000000000001c
0x7fffffffdee0:	0x0000000000000001	0x00007fffffffe1aa
0x7fffffffdef0:	0x0000000000000000	0x00007fffffffe1ca
0x7fffffffdf00:	0x00007fffffffe1d5	0x00007fffffffe1e8
0x7fffffffdf10:	0x00007fffffffe1f9	0x00007fffffffe225
0x7fffffffdf20:	0x00007fffffffe270	0x00007fffffffe2a4
0x7fffffffdf30:	0x00007fffffffe2d6	0x00007fffffffe2ea
0x7fffffffdf40:	0x00007fffffffe2f5	0x00007fffffffe305
0x7fffffffdf50:	0x00007fffffffe31b	0x00007fffffffe32d
(gdb) r
Starting program: /home/francois/tmp/csaw/hungman 
What's your name?
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
Welcome AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
________________________________
abcdefgh
________________________________
______________________________b_
_________________________c_c__b_
_______d_________________c_c__b_
___e___d_____________e___cec__b_
___e___d_f___________e___cec__b_
___e_g_d_f___________e___cec__b_
___ehg_d_f_______h___e___cec__b_
i
___ehg_d_f_______h___e___cec__bi
j
___ehg_d_f_______h___e___cec__bi
k
__kehg_d_f_k_____h___e___cec__bi
l
llkehg_d_f_k____lh___e___cec__bi
m
llkehg_d_f_k____lhm__e_m_cec__bi
n
llkehg_d_f_k____lhmn_e_m_cec__bi
w
High score! change name?
y
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHAAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH        321
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000000000  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000602100  RSI: 0x0000000000000200  RDX: 0x0000000000401175  RCX: 0x0000000000313233  RIP: 0x0000000000400EF4
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x00007FFFFFFFDB40  R11: 0x00007FFFF7AAD600  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797702e5   0x00000000  .@.......wy....
0x00007FFFFFFFDDA0 : 0x00000014   0x00000021 - 0x00000014   0x0000003c ....!.......<...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
   0x400f05:	mov    -0x58(%rbp),%rax
   0x400f09:	add    $0x10,%rax
   0x400f0d:	mov    $0x1a,%edx
   0x400f12:	mov    $0x0,%esi
-----------------------------------------------------------------------------------------------------------------------------

Breakpoint 1, 0x0000000000400ef4 in ?? ()
(gdb) ni

Program received signal SIGSEGV, Segmentation fault.
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000000000  RBX: 0x00007FFFFFFFDB40  RBP: 0x00007FFFFFFFDB30  RSP: 0x00007FFFFFFFD560  o d I t S z a P c 
  RDI: 0x0000000000313233  RSI: 0x0000000000401175  RDX: 0x0000000000000020  RCX: 0xFFFFFFFFFFFFFFFF  RIP: 0x00007FFFF7A7BDCC
  R8 : 0x0000000000313233  R9 : 0x00007FFFF7A7C99A  R10: 0x00007FFFFFFFDB40  R11: 0x00007FFFF7A81DA0  R12: 0x0000000000401175
  R13: 0x0000000000000000  R14: 0x0000000000000000  R15: 0x00007FFFFFFFDCA8
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFD560]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFD560 : 0x004004a1   0x00000000 - 0xf7ffe180   0x00007fff ..@.............
0x00007FFFFFFFD570 : 0xffffd6c0   0x00007fff - 0x003aaa20   0x00000000 ........ .:.....
0x00007FFFFFFFD580 : 0x00000006   0x00000000 - 0xffffd338   0x00007fff ........8.......
0x00007FFFFFFFD590 : 0x00000802   0x00000000 - 0x00120107   0x00000000 ................
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x7ffff7a7bdcc <_IO_vfprintf_internal+19468>:	repnz scas %es:(%rdi),%al
   0x7ffff7a7bdce <_IO_vfprintf_internal+19470>:	movl   $0x0,-0x4c8(%rbp)
   0x7ffff7a7bdd8 <_IO_vfprintf_internal+19480>:	mov    %rcx,%rsi
   0x7ffff7a7bddb <_IO_vfprintf_internal+19483>:	not    %rsi
   0x7ffff7a7bdde <_IO_vfprintf_internal+19486>:	lea    -0x1(%rsi),%r10
   0x7ffff7a7bde2 <_IO_vfprintf_internal+19490>:	jmpq   0x7ffff7a7bb34 <_IO_vfprintf_internal+18804>
   0x7ffff7a7bde7 <_IO_vfprintf_internal+19495>:	lea    -0x480(%rbp),%rax
   0x7ffff7a7bdee <_IO_vfprintf_internal+19502>:	mov    %r8,-0x470(%rbp)
-----------------------------------------------------------------------------------------------------------------------------
0x00007ffff7a7bdcc in _IO_vfprintf_internal (s=s@entry=0x7fffffffdb40, format=<optimized out>, format@entry=0x401175 "Highest player: %s", ap=ap@entry=0x7fffffffdca8) at vfprintf.c:1642
1642	vfprintf.c: Aucun fichier ou dossier de ce type.
(gdb) break[3Pni[1Prx/30gx $rsps 0x0000000000602100401175[C[C[C[C[C[Cr[Kbreak *0x0400ef4[C[C[C[C[C[Cx/4wx 0x7fffffffdca8[C[C[C[C[C[C[4Pbreak *0x0400ef4[K[Kc9
Breakpoint 2 at 0x400ec9
(gdb) r
Starting program: /home/francois/tmp/csaw/hungman 
What's your name?
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
Welcome AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
________________________________
azertyuiop
________________________________
________________________________
___________________________e____
Default Highscore  score: 64
Continue? ________________________________
___y____________________________
___y______________________u_____
___y______________________u_____
___y______________________uo____
___y_________________p____uo____
qsdfgh
___y_____________q___p____uo____
___y___s_________q___p____uo____
___y___s_d___d___q___p____uo____
___y___s_d___d___q___p____uo____
___y___s_d__gd___q___p____uo___g
___y___shd__gd___q___p____uo___g
j
_j_y___shd__gd___qj__p____uo___g
k
_j_y__kshd__gd___qj__p____uo___g
l
_j_y__kshd__gdl__qj__p_l__uo___g
w
High score! change name?
y
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHAAAABBBBCCCCDDDDEEEEFFFF321           aaaabbbbcccc-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603010  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t S z a P C 
  RDI: 0x0000000000603010  RSI: 0x0000000000603100  RDX: 0x000000000000003C  RCX: 0x0000000000000078  RIP: 0x0000000000400EC9
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797702e5   0x00000000  .@.......wy....
0x00007FFFFFFFDDA0 : 0x00000010   0x00000021 - 0x00000010   0x0000003c ....!.......<...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ec9:	mov    -0x10(%rbp),%rax
   0x400ecd:	mov    %rax,%rdi
   0x400ed0:	callq  0x400800 <free@plt>
   0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
-----------------------------------------------------------------------------------------------------------------------------

Breakpoint 2, 0x0000000000400ec9 in ?? ()
(gdb) n[Kr
Starting program: /home/francois/tmp/csaw/hungman 
What's your name?
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
Welcome AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
________________________________
azertyui
________a_______________________
________a_____________z_________
________a_________e___z_________
________a_________e___z_________
________at________e___z_________
________at_____y__e___z_________
___u__u_at___u_y__e___z__u___u__
___u__u_at___u_y__e___zi_u___u__
o
___u_ou_at___u_y__e___zi_u__ou__
p
___u_ou_at___u_y__e_p_zi_u__ou__
q
___u_ou_at___u_yq_e_p_zi_u__ou__
s
_s_u_ousat___u_yq_e_p_zi_u__ou__
d
_s_u_ousat___u_yq_e_p_zidu__ou__
f
_s_u_ousat___u_yq_e_p_zidu__ou__
g
_s_u_ousat___u_yq_e_p_zidug_oug_
h
_s_uhousat___u_yq_e_p_zidug_ough
j
_s_uhousat___ujyq_e_p_zidug_ough
k
High score! change name?
l y
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHaaaabbbbccccdddd
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603010  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t S z a p C 
  RDI: 0x0000000000603010  RSI: 0x0000000000603100  RDX: 0x0000000000000031  RCX: 0x0000000000000062  RIP: 0x0000000000400EC9
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796b02e5   0x00000000  .@.......ky....
0x00007FFFFFFFDDA0 : 0x00000017   0x00000021 - 0x00000017   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ec9:	mov    -0x10(%rbp),%rax
   0x400ecd:	mov    %rax,%rdi
   0x400ed0:	callq  0x400800 <free@plt>
   0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
-----------------------------------------------------------------------------------------------------------------------------

Breakpoint 2, 0x0000000000400ec9 in ?? ()
(gdb) x/s 0x0000000000603010
0x603010:	"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHaaaabbbbccccdddd"
(gdb) x/gx $rpb-0x58
Argument to arithmetic operation not a number or boolean.
(gdb) x/gx $rpb-0x58[1P-0x58[1P-0x58b-0x58p-0x58
0x7fffffffdd88:	0x0000000000603040
(gdb) x/s 0x0000000000603040*[K
0x603040:	""
(gdb) ni
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603100  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t S z a p C 
  RDI: 0x0000000000603010  RSI: 0x0000000000603100  RDX: 0x0000000000000031  RCX: 0x0000000000000062  RIP: 0x0000000000400ECD
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796b02e5   0x00000000  .@.......ky....
0x00007FFFFFFFDDA0 : 0x00000017   0x00000021 - 0x00000017   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ecd:	mov    %rax,%rdi
   0x400ed0:	callq  0x400800 <free@plt>
   0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ecd in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603100  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t S z a p C 
  RDI: 0x0000000000603100  RSI: 0x0000000000603100  RDX: 0x0000000000000031  RCX: 0x0000000000000062  RIP: 0x0000000000400ED0
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796b02e5   0x00000000  .@.......ky....
0x00007FFFFFFFDDA0 : 0x00000017   0x00000021 - 0x00000017   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ed0:	callq  0x400800 <free@plt>
   0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ed0 in ?? ()
(gdb) info breakpoints
Num     Type           Disp Enb Address            What
1       breakpoint     keep y   0x0000000000400ef4 
2       breakpoint     keep y   0x0000000000400ec9 
	breakpoint already hit 1 time
(gdb) delete 2
(gdb) e[Kbreak *0x0000000000400ec9[K4
Breakpoint 3 at 0x400ec4
(gdb) r
Starting program: /home/francois/tmp/csaw/hungman 
What's your name?
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
Welcome AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
________________________________
azerty
___________a____________________
___________a____________________
___________a____________________
___________a__r_________________
___________a__r__t______________
_______y___a__r__t___y__________
u
__u____y_u_a__r__t___y_____u__u_
i
__u____y_u_a__r__t___y_i___u__u_
o
__u____y_u_a__r__t___y_i__ou__u_
p
__u__p_y_u_a__r__t___y_i__ou__u_
qs
q_u__p_y_u_a__r__t___y_i_qou__u_
High score! change name?
y
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHaaaabbbbccccdddd
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603010  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000603010  RSI: 0x0000000000603100  RDX: 0x0000000000000031  RCX: 0x0000000000603100  RIP: 0x0000000000400EC4
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797302e5   0x00000000  .@.......sy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ec4:	callq  0x4008c0 <memcpy@plt>
   0x400ec9:	mov    -0x10(%rbp),%rax
   0x400ecd:	mov    %rax,%rdi
   0x400ed0:	callq  0x400800 <free@plt>
   0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
-----------------------------------------------------------------------------------------------------------------------------

Breakpoint 3, 0x0000000000400ec4 in ?? ()
(gdb) x/s 0x0000000000603100
0x603100:	"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHaaaabbbbccccdddd"
(gdb) x/s 0x0000000000603010
0x603010:	"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH"
(gdb) x/8[K10gx 0x0000000000603010
0x603010:	0x4242424241414141	0x4444444443434343
0x603020:	0x4646464645454545	0x4848484847474747
0x603030:	0x0000000000000000	0x0000000000000091
0x603040:	0x0000003100000070	0x0000000000603010
0x603050:	0x0000000000000001	0x0101000000000001
(gdb) x/s 0x0000000000603010
0x603010:	"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH"
(gdb) x/s 0x0000000000603010[C[C[C[C[C[C[C[C[3@10gx[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[C[1P[1@8
0x603010:	0x4242424241414141	0x4444444443434343
0x603020:	0x4646464645454545	0x4848484847474747
0x603030:	0x0000000000000000	0x0000000000000091
0x603040:	0x0000003100000070	0x0000000000603010
0x603050:	0x0000000000000001	0x0101000000000001
0x603060:	0x0000000101000101	0x0000000000000001
0x603070:	0x0000000000000000	0x0000000000000000
0x603080:	0x0000000000000000	0x0000000000000000
0x603090:	0x0000000000000000	0x0000000000000000
(gdb) x/18gx 0x0000000000603010[1P[1P[1@3[1@4
0x603010:	0x4242424241414141	0x4444444443434343
0x603020:	0x4646464645454545	0x4848484847474747
0x603030:	0x0000000000000000	0x0000000000000091
0x603040:	0x0000003100000070	0x0000000000603010
0x603050:	0x0000000000000001	0x0101000000000001
0x603060:	0x0000000101000101	0x0000000000000001
0x603070:	0x0000000000000000	0x0000000000000000
0x603080:	0x0000000000000000	0x0000000000000000
0x603090:	0x0000000000000000	0x0000000000000000
0x6030a0:	0x0000000000000000	0x0000000000000000
0x6030b0:	0x0000000000000000	0x0000000000000000
0x6030c0:	0x0000000000000000	0x0000000000000031
0x6030d0:	0x796370666a756e71	0x6672676c61667562
0x6030e0:	0x69777967626a7477	0x6275686e756f7164
0x6030f0:	0x00000000000000fc	0x0000000000000101
0x603100:	0x4242424241414141	0x4444444443434343
0x603110:	0x4646464645454545	0x4848484847474747
(gdb) x/s 0x6030d0:[K
0x6030d0:	"qnujfpcybufalgrfwtjbgywidqounhu", <incomplete sequence \374>
(gdb) ni
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603010  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t S z a p C 
  RDI: 0x0000000000603010  RSI: 0x0000000000603100  RDX: 0x0000000000000031  RCX: 0x0000000000000062  RIP: 0x0000000000400EC9
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797302e5   0x00000000  .@.......sy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ec9:	mov    -0x10(%rbp),%rax
   0x400ecd:	mov    %rax,%rdi
   0x400ed0:	callq  0x400800 <free@plt>
   0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ec9 in ?? ()
(gdb) nix/s 0x6030d0[C[C[C[C[C[C[C[C34gx 0x0000000000603010
0x603010:	0x4242424241414141	0x4444444443434343
0x603020:	0x4646464645454545	0x4848484847474747
0x603030:	0x6262626261616161	0x6464646463636363
0x603040:	0x0000003100000000	0x0000000000603010
0x603050:	0x0000000000000001	0x0101000000000001
0x603060:	0x0000000101000101	0x0000000000000001
0x603070:	0x0000000000000000	0x0000000000000000
0x603080:	0x0000000000000000	0x0000000000000000
0x603090:	0x0000000000000000	0x0000000000000000
0x6030a0:	0x0000000000000000	0x0000000000000000
0x6030b0:	0x0000000000000000	0x0000000000000000
0x6030c0:	0x0000000000000000	0x0000000000000031
0x6030d0:	0x796370666a756e71	0x6672676c61667562
0x6030e0:	0x69777967626a7477	0x6275686e756f7164
0x6030f0:	0x00000000000000fc	0x0000000000000101
0x603100:	0x4242424241414141	0x4444444443434343
0x603110:	0x4646464645454545	0x4848484847474747
(gdb) x[Kx/40gx 0x0000000000603010
0x603010:	0x4242424241414141	0x4444444443434343
0x603020:	0x4646464645454545	0x4848484847474747
0x603030:	0x6262626261616161	0x6464646463636363
0x603040:	0x0000003100000000	0x0000000000603010
0x603050:	0x0000000000000001	0x0101000000000001
0x603060:	0x0000000101000101	0x0000000000000001
0x603070:	0x0000000000000000	0x0000000000000000
0x603080:	0x0000000000000000	0x0000000000000000
0x603090:	0x0000000000000000	0x0000000000000000
0x6030a0:	0x0000000000000000	0x0000000000000000
0x6030b0:	0x0000000000000000	0x0000000000000000
0x6030c0:	0x0000000000000000	0x0000000000000031
0x6030d0:	0x796370666a756e71	0x6672676c61667562
0x6030e0:	0x69777967626a7477	0x6275686e756f7164
0x6030f0:	0x00000000000000fc	0x0000000000000101
0x603100:	0x4242424241414141	0x4444444443434343
0x603110:	0x4646464645454545	0x4848484847474747
0x603120:	0x6262626261616161	0x6464646463636363
0x603130:	0x0000000000000000	0x0000000000000000
0x603140:	0x0000000000000000	0x0000000000000000
(gdb) x/40gx 0x0000000000603010[1P10[C[C0
0x603100:	0x4242424241414141	0x4444444443434343
0x603110:	0x4646464645454545	0x4848484847474747
0x603120:	0x6262626261616161	0x6464646463636363
0x603130:	0x0000000000000000	0x0000000000000000
0x603140:	0x0000000000000000	0x0000000000000000
0x603150:	0x0000000000000000	0x0000000000000000
0x603160:	0x0000000000000000	0x0000000000000000
0x603170:	0x0000000000000000	0x0000000000000000
0x603180:	0x0000000000000000	0x0000000000000000
0x603190:	0x0000000000000000	0x0000000000000000
0x6031a0:	0x0000000000000000	0x0000000000000000
0x6031b0:	0x0000000000000000	0x0000000000000000
0x6031c0:	0x0000000000000000	0x0000000000000000
0x6031d0:	0x0000000000000000	0x0000000000000000
0x6031e0:	0x0000000000000000	0x0000000000000000
0x6031f0:	0x0000000000000000	0x0000000000020e11
0x603200:	0x0000000000000000	0x0000000000000000
0x603210:	0x0000000000000000	0x0000000000000000
0x603220:	0x0000000000000000	0x0000000000000000
0x603230:	0x0000000000000000	0x0000000000000000
(gdb) ni
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603100  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t S z a p C 
  RDI: 0x0000000000603010  RSI: 0x0000000000603100  RDX: 0x0000000000000031  RCX: 0x0000000000000062  RIP: 0x0000000000400ECD
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797302e5   0x00000000  .@.......sy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ecd:	mov    %rax,%rdi
   0x400ed0:	callq  0x400800 <free@plt>
   0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ecd in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603100  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t S z a p C 
  RDI: 0x0000000000603100  RSI: 0x0000000000603100  RDX: 0x0000000000000031  RCX: 0x0000000000000062  RIP: 0x0000000000400ED0
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797302e5   0x00000000  .@.......sy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ed0:	callq  0x400800 <free@plt>
   0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ed0 in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000000001  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFF7DD6678  RDX: 0x0000000000000000  RCX: 0x0000000000000000  RIP: 0x0000000000400ED5
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x00007FFFFFFFDB40  R11: 0x00007FFFF7AAD600  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797302e5   0x00000000  .@.......sy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ed5 in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603040  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFF7DD6678  RDX: 0x0000000000000000  RCX: 0x0000000000000000  RIP: 0x0000000000400ED9
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x00007FFFFFFFDB40  R11: 0x00007FFFF7AAD600  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797302e5   0x00000000  .@.......sy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ed9 in ?? ()
(gdb) x:g[Kwx [K[K[K[K/wx 0x0000000000603040
0x603040:	0x00000000
(gdb) x/wx 0x0000000000603040[1P[1@g
0x603040:	0x0000003100000000
(gdb) ni
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603010  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFF7DD6678  RDX: 0x0000000000000000  RCX: 0x0000000000000000  RIP: 0x0000000000400EDD
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x00007FFFFFFFDB40  R11: 0x00007FFFF7AAD600  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797302e5   0x00000000  .@.......sy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400edd in ?? ()
(gdb) x/s 0x0000000000603010[K0
0x603010:	"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHaaaabbbbccccdddd"
(gdb) ni
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603010  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFF7DD6678  RDX: 0x0000000000000000  RCX: 0x0000000000603010  RIP: 0x0000000000400EE0
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x00007FFFFFFFDB40  R11: 0x00007FFFF7AAD600  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797302e5   0x00000000  .@.......sy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ee0 in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603010  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFF7DD6678  RDX: 0x0000000000401175  RCX: 0x0000000000603010  RIP: 0x0000000000400EE5
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x00007FFFFFFFDB40  R11: 0x00007FFFF7AAD600  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797302e5   0x00000000  .@.......sy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
   0x400f05:	mov    -0x58(%rbp),%rax
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ee5 in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603010  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000000000  RSI: 0x0000000000000200  RDX: 0x0000000000401175  RCX: 0x0000000000603010  RIP: 0x0000000000400EEA
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x00007FFFFFFFDB40  R11: 0x00007FFFF7AAD600  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797302e5   0x00000000  .@.......sy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
   0x400f05:	mov    -0x58(%rbp),%rax
   0x400f09:	add    $0x10,%rax
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400eea in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603010  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000602100  RSI: 0x0000000000000200  RDX: 0x0000000000401175  RCX: 0x0000000000603010  RIP: 0x0000000000400EEF
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x00007FFFFFFFDB40  R11: 0x00007FFFF7AAD600  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797302e5   0x00000000  .@.......sy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
   0x400f05:	mov    -0x58(%rbp),%rax
   0x400f09:	add    $0x10,%rax
   0x400f0d:	mov    $0x1a,%edx
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400eef in ?? ()
(gdb) x/s 0x0000000000602100
0x602100:	"Default Highscore "
(gdb) ni
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000000000  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000602100  RSI: 0x0000000000000200  RDX: 0x0000000000401175  RCX: 0x0000000000603010  RIP: 0x0000000000400EF4
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x00007FFFFFFFDB40  R11: 0x00007FFFF7AAD600  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797302e5   0x00000000  .@.......sy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
   0x400f05:	mov    -0x58(%rbp),%rax
   0x400f09:	add    $0x10,%rax
   0x400f0d:	mov    $0x1a,%edx
   0x400f12:	mov    $0x0,%esi
-----------------------------------------------------------------------------------------------------------------------------

Breakpoint 1, 0x0000000000400ef4 in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000000040  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x00007FFFFFFFDB40  RSI: 0x000000007FFFFFBF  RDX: 0x0000000000602140  RCX: 0x0000000000000040  RIP: 0x0000000000400EF9
  R8 : 0x6464646463636363  R9 : 0x00007FFFF7A7C99A  R10: 0x00007FFFF7DD5460  R11: 0x00000000FFFFFFD0  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x797302e5   0x00000000  .@.......sy....
0x00007FFFFFFFDDA0 : 0x0000000e   0x00000021 - 0x0000000e   0x00000031 ....!.......1...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
   0x400f05:	mov    -0x58(%rbp),%rax
   0x400f09:	add    $0x10,%rax
   0x400f0d:	mov    $0x1a,%edx
   0x400f12:	mov    $0x0,%esi
   0x400f17:	mov    %rax,%rdi
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ef9 in ?? ()
(gdb) c
Continuing.
Highest player: AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHaaaabbbbccccdddd score: 0
Continue? y
________________________________________________
azertyui
aa____________________a________________a________
aa____________________a___z____________a________
aa____________________a___z____________a________
aa____________________a___z____________a__r_____
aa__t___________t_____a___z____________a__r_____
aa__t___________t____ya___z_________y__a__r_____
aa__t___________t____ya___z_________y__a__r_____
aa__t________i__t__i_ya__iz_________y__a__r_____
qsd
aa__t__q_____i__t__i_ya__iz_________y__a__r_____
aa__t_sq_____i__t__i_ya__iz__s______ys_a__rss_s_
aa__t_sq_____i__t_di_ya__iz__s______ys_a__rss_s_
f
High score! change name?
y
eee   AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHaaaabbbbccccddddeeeeffff
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603010  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000603010  RSI: 0x0000000000603140  RDX: 0x0000000000000039  RCX: 0x0000000000603140  RIP: 0x0000000000400EC4
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796602e5   0x00000000  .@.......fy....
0x00007FFFFFFFDDA0 : 0x00000015   0x00000031 - 0x00000015   0x00000039 ....1.......9...
0x00007FFFFFFFDDB0 : 0x00000030   0x00000000 - 0x00000030   0x00000000 0.......0.......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ec4:	callq  0x4008c0 <memcpy@plt>
   0x400ec9:	mov    -0x10(%rbp),%rax
   0x400ecd:	mov    %rax,%rdi
   0x400ed0:	callq  0x400800 <free@plt>
   0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
-----------------------------------------------------------------------------------------------------------------------------

Breakpoint 3, 0x0000000000400ec4 in ?? ()
(gdb) x/40[K[K32gx 0x0000000000603010
0x603010:	0x4242424241414141	0x4444444443434343
0x603020:	0x4646464645454545	0x4848484847474747
0x603030:	0x6262626261616161	0x6464646463636363
0x603040:	0x00000039000000fc	0x0000000000603010
0x603050:	0x0000000001000001	0x0000000000000001
0x603060:	0x0000000001010101	0x0000000000000101
0x603070:	0x0000000000000000	0x0000000000000000
0x603080:	0x0000000000000000	0x0000000000000000
0x603090:	0x0000000000000000	0x0000000000000000
0x6030a0:	0x0000000000000000	0x0000000000000000
0x6030b0:	0x0000000000000000	0x0000000000000000
0x6030c0:	0x0000000000000000	0x0000000000000031
0x6030d0:	0x0000000000000000	0x6672676c61667562
0x6030e0:	0x69777967626a7477	0x6275686e756f7164
0x6030f0:	0x00000000000000fc	0x0000000000000041
0x603100:	0x717368746a6e6161	0x767069706a6c6b76
(gdb) ni
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603010  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t S z a P C 
  RDI: 0x0000000000603010  RSI: 0x0000000000603140  RDX: 0x0000000000000039  RCX: 0x0000000000000072  RIP: 0x0000000000400EC9
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796602e5   0x00000000  .@.......fy....
0x00007FFFFFFFDDA0 : 0x00000015   0x00000031 - 0x00000015   0x00000039 ....1.......9...
0x00007FFFFFFFDDB0 : 0x00000030   0x00000000 - 0x00000030   0x00000000 0.......0.......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ec9:	mov    -0x10(%rbp),%rax
   0x400ecd:	mov    %rax,%rdi
   0x400ed0:	callq  0x400800 <free@plt>
   0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ec9 in ?? ()
(gdb) nix/32gx 0x0000000000603010
0x603010:	0x4242424241414141	0x4444444443434343
0x603020:	0x4646464645454545	0x4848484847474747
0x603030:	0x6262626261616161	0x6464646463636363
0x603040:	0x6666666665656565	0x0000000000603000
0x603050:	0x0000000001000001	0x0000000000000001
0x603060:	0x0000000001010101	0x0000000000000101
0x603070:	0x0000000000000000	0x0000000000000000
0x603080:	0x0000000000000000	0x0000000000000000
0x603090:	0x0000000000000000	0x0000000000000000
0x6030a0:	0x0000000000000000	0x0000000000000000
0x6030b0:	0x0000000000000000	0x0000000000000000
0x6030c0:	0x0000000000000000	0x0000000000000031
0x6030d0:	0x0000000000000000	0x6672676c61667562
0x6030e0:	0x69777967626a7477	0x6275686e756f7164
0x6030f0:	0x00000000000000fc	0x0000000000000041
0x603100:	0x717368746a6e6161	0x767069706a6c6b76
(gdb) ni
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603140  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t S z a P C 
  RDI: 0x0000000000603010  RSI: 0x0000000000603140  RDX: 0x0000000000000039  RCX: 0x0000000000000072  RIP: 0x0000000000400ECD
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796602e5   0x00000000  .@.......fy....
0x00007FFFFFFFDDA0 : 0x00000015   0x00000031 - 0x00000015   0x00000039 ....1.......9...
0x00007FFFFFFFDDB0 : 0x00000030   0x00000000 - 0x00000030   0x00000000 0.......0.......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ecd:	mov    %rax,%rdi
   0x400ed0:	callq  0x400800 <free@plt>
   0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ecd in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603140  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t S z a P C 
  RDI: 0x0000000000603140  RSI: 0x0000000000603140  RDX: 0x0000000000000039  RCX: 0x0000000000000072  RIP: 0x0000000000400ED0
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796602e5   0x00000000  .@.......fy....
0x00007FFFFFFFDDA0 : 0x00000015   0x00000031 - 0x00000015   0x00000039 ....1.......9...
0x00007FFFFFFFDDB0 : 0x00000030   0x00000000 - 0x00000030   0x00000000 0.......0.......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ed0:	callq  0x400800 <free@plt>
   0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ed0 in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000000001  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFF7DD6678  RDX: 0x0000000000000000  RCX: 0x0000000000000000  RIP: 0x0000000000400ED5
  R8 : 0x00007FFFF7DD6678  R9 : 0x00007FFFF7DD6670  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796602e5   0x00000000  .@.......fy....
0x00007FFFFFFFDDA0 : 0x00000015   0x00000031 - 0x00000015   0x00000039 ....1.......9...
0x00007FFFFFFFDDB0 : 0x00000030   0x00000000 - 0x00000030   0x00000000 0.......0.......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ed5 in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603040  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFF7DD6678  RDX: 0x0000000000000000  RCX: 0x0000000000000000  RIP: 0x0000000000400ED9
  R8 : 0x00007FFFF7DD6678  R9 : 0x00007FFFF7DD6670  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796602e5   0x00000000  .@.......fy....
0x00007FFFFFFFDDA0 : 0x00000015   0x00000031 - 0x00000015   0x00000039 ....1.......9...
0x00007FFFFFFFDDB0 : 0x00000030   0x00000000 - 0x00000030   0x00000000 0.......0.......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ed9 in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603000  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFF7DD6678  RDX: 0x0000000000000000  RCX: 0x0000000000000000  RIP: 0x0000000000400EDD
  R8 : 0x00007FFFF7DD6678  R9 : 0x00007FFFF7DD6670  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796602e5   0x00000000  .@.......fy....
0x00007FFFFFFFDDA0 : 0x00000015   0x00000031 - 0x00000015   0x00000039 ....1.......9...
0x00007FFFFFFFDDB0 : 0x00000030   0x00000000 - 0x00000030   0x00000000 0.......0.......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400edd in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603000  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFF7DD6678  RDX: 0x0000000000000000  RCX: 0x0000000000603000  RIP: 0x0000000000400EE0
  R8 : 0x00007FFFF7DD6678  R9 : 0x00007FFFF7DD6670  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796602e5   0x00000000  .@.......fy....
0x00007FFFFFFFDDA0 : 0x00000015   0x00000031 - 0x00000015   0x00000039 ....1.......9...
0x00007FFFFFFFDDB0 : 0x00000030   0x00000000 - 0x00000030   0x00000000 0.......0.......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ee0:	mov    $0x401175,%edx
   0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ee0 in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603000  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFF7DD6678  RDX: 0x0000000000401175  RCX: 0x0000000000603000  RIP: 0x0000000000400EE5
  R8 : 0x00007FFFF7DD6678  R9 : 0x00007FFFF7DD6670  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796602e5   0x00000000  .@.......fy....
0x00007FFFFFFFDDA0 : 0x00000015   0x00000031 - 0x00000015   0x00000039 ....1.......9...
0x00007FFFFFFFDDB0 : 0x00000030   0x00000000 - 0x00000030   0x00000000 0.......0.......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ee5:	mov    $0x200,%esi
   0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
   0x400f05:	mov    -0x58(%rbp),%rax
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ee5 in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603000  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000000000  RSI: 0x0000000000000200  RDX: 0x0000000000401175  RCX: 0x0000000000603000  RIP: 0x0000000000400EEA
  R8 : 0x00007FFFF7DD6678  R9 : 0x00007FFFF7DD6670  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796602e5   0x00000000  .@.......fy....
0x00007FFFFFFFDDA0 : 0x00000015   0x00000031 - 0x00000015   0x00000039 ....1.......9...
0x00007FFFFFFFDDB0 : 0x00000030   0x00000000 - 0x00000030   0x00000000 0.......0.......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400eea:	mov    $0x602100,%edi
   0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
   0x400f05:	mov    -0x58(%rbp),%rax
   0x400f09:	add    $0x10,%rax
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400eea in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603000  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000602100  RSI: 0x0000000000000200  RDX: 0x0000000000401175  RCX: 0x0000000000603000  RIP: 0x0000000000400EEF
  R8 : 0x00007FFFF7DD6678  R9 : 0x00007FFFF7DD6670  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796602e5   0x00000000  .@.......fy....
0x00007FFFFFFFDDA0 : 0x00000015   0x00000031 - 0x00000015   0x00000039 ....1.......9...
0x00007FFFFFFFDDB0 : 0x00000030   0x00000000 - 0x00000030   0x00000000 0.......0.......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400eef:	mov    $0x0,%eax
   0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
   0x400f05:	mov    -0x58(%rbp),%rax
   0x400f09:	add    $0x10,%rax
   0x400f0d:	mov    $0x1a,%edx
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400eef in ?? ()
(gdb) 
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000000000  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000602100  RSI: 0x0000000000000200  RDX: 0x0000000000401175  RCX: 0x0000000000603000  RIP: 0x0000000000400EF4
  R8 : 0x00007FFFF7DD6678  R9 : 0x00007FFFF7DD6670  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796602e5   0x00000000  .@.......fy....
0x00007FFFFFFFDDA0 : 0x00000015   0x00000031 - 0x00000015   0x00000039 ....1.......9...
0x00007FFFFFFFDDB0 : 0x00000030   0x00000000 - 0x00000030   0x00000000 0.......0.......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
   0x400f05:	mov    -0x58(%rbp),%rax
   0x400f09:	add    $0x10,%rax
   0x400f0d:	mov    $0x1a,%edx
   0x400f12:	mov    $0x0,%esi
-----------------------------------------------------------------------------------------------------------------------------

Breakpoint 1, 0x0000000000400ef4 in ?? ()
(gdb) x/s 0x0000000000602100
0x602100:	"Highest player: AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHaaaabbbbccccdddd"
(gdb) ni[K[Kx/s 0x0000000000603000
0x603000:	""
(gdb) ni
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000000010  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x00007FFFFFFFDB40  RSI: 0x000000007FFFFFEF  RDX: 0x0000000000602110  RCX: 0x0000000000000010  RIP: 0x0000000000400EF9
  R8 : 0x0000000000603000  R9 : 0x00007FFFF7A7C99A  R10: 0x00007FFFF7DD5460  R11: 0x0000000000000000  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796602e5   0x00000000  .@.......fy....
0x00007FFFFFFFDDA0 : 0x00000015   0x00000031 - 0x00000015   0x00000039 ....1.......9...
0x00007FFFFFFFDDB0 : 0x00000030   0x00000000 - 0x00000030   0x00000000 0.......0.......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
   0x400f05:	mov    -0x58(%rbp),%rax
   0x400f09:	add    $0x10,%rax
   0x400f0d:	mov    $0x1a,%edx
   0x400f12:	mov    $0x0,%esi
   0x400f17:	mov    %rax,%rdi
-----------------------------------------------------------------------------------------------------------------------------
0x0000000000400ef9 in ?? ()
(gdb) nix/s 0x00000000006030002100
0x602100:	"Highest player: "
(gdb) c
Continuing.
Highest player:  score: 1701143909
Continue? ^C
Program received signal SIGINT, Interrupt.
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0xFFFFFFFFFFFFFE00  RBX: 0x00007FFFF7DD74E0  RBP: 0x00007FFFF7DD72A0  RSP: 0x00007FFFFFFFD9E8  o d I t s Z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFF7FF5000  RDX: 0x0000000000000400  RCX: 0xFFFFFFFFFFFFFFFF  RIP: 0x00007FFFF7B0CDF0
  R8 : 0x00007FFFF7FCC700  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000401151
  R13: 0x0000000000000001  R14: 0x0000000000000000  R15: 0x00007FFFF7DD74E0
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFD9E8]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFD9E8 : 0xf7aa63a0   0x00007fff - 0xf7dd3d40   0x00007fff .c......@=......
0x00007FFFFFFFD9F8 : 0xf7dd74e0   0x00007fff - 0xffffdcf0   0x00007fff .t..............
0x00007FFFFFFFDA08 : 0xf7aa71ce   0x00007fff - 0x00000063   0x00000000 .q......c.......
0x00007FFFFFFFDA18 : 0xf7a8b542   0x00007fff - 0xffffff90   0xffffffff B...............
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x7ffff7b0cdf0 <__read_nocancel+7>:	cmp    $0xfffffffffffff001,%rax
   0x7ffff7b0cdf6 <__read_nocancel+13>:	jae    0x7ffff7b0ce29 <read+73>
   0x7ffff7b0cdf8 <__read_nocancel+15>:	retq   
   0x7ffff7b0cdf9 <read+25>:	sub    $0x8,%rsp
   0x7ffff7b0cdfd <read+29>:	callq  0x7ffff7b25e30 <__libc_enable_asynccancel>
   0x7ffff7b0ce02 <read+34>:	mov    %rax,(%rsp)
   0x7ffff7b0ce06 <read+38>:	mov    $0x0,%eax
   0x7ffff7b0ce0b <read+43>:	syscall 
-----------------------------------------------------------------------------------------------------------------------------
0x00007ffff7b0cdf0 in __read_nocancel () at ../sysdeps/unix/syscall-template.S:81
81	../sysdeps/unix/syscall-template.S: Aucun fichier ou dossier de ce type.
(gdb) cx/s 0x0000000000602100[C[C[C[C[C[Cni[Kx/s 0x00000000006030002100[C[C[C[C[C[Cni[Kx/32gx 0x0000000000603010
0x603010:	0x4242424241414141	0x4444444443434343
0x603020:	0x4646464645454545	0x4848484847474747
0x603030:	0x6262626261616161	0x6464646463636363
0x603040:	0x6666666665656565	0x0000000000603000
0x603050:	0x0000000000000000	0x0000000000000000
0x603060:	0x0000000000000000	0x0000000000000000
0x603070:	0x0000000000000000	0x0000000000000000
0x603080:	0x0000000000000000	0x0000000000000000
0x603090:	0x0000000000000000	0x0000000000000000
0x6030a0:	0x0000000000000000	0x0000000000000000
0x6030b0:	0x0000000000000000	0x0000000000000000
0x6030c0:	0x0000000000000000	0x0000000000000031
0x6030d0:	0x00007ffff7dd6678	0x00007ffff7dd6678
0x6030e0:	0x69777967626a7477	0x6275686e756f7164
0x6030f0:	0x0000000000000030	0x0000000000000040
0x603100:	0x0000000000000000	0x767069706a6c6b76
(gdb) r
Starting program: /home/francois/tmp/csaw/hungman 
What's your name?
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
Welcome AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHH
________________________________
azertyuiop
______a________________a________
______a______z________za________
______a______z________za___e____
______a______z_r______za___e____
______a______z_r_____tza___e____
_____ya______z_r__y__tza___e____
_____ya__u___z_r__y__tza___eu___
_____ya__u___z_ri_y__tza___euii_
_____ya__u___z_ri_y__tza___euii_
_____ya__u_p_z_ri_y__tza___euii_
qs 
_____ya__u_p_z_ri_y__tza___euii_
d
High score! change name?
y
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHaaaabbbbccccddddxxxxxxx
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000603010  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a p c 
  RDI: 0x0000000000603010  RSI: 0x0000000000603100  RDX: 0x0000000000000038  RCX: 0x0000000000603100  RIP: 0x0000000000400EC4
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796402e5   0x00000000  .@.......dy....
0x00007FFFFFFFDDA0 : 0x0000000f   0x00000021 - 0x0000000f   0x00000038 ....!.......8...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ec4:	callq  0x4008c0 <memcpy@plt>
   0x400ec9:	mov    -0x10(%rbp),%rax
   0x400ecd:	mov    %rax,%rdi
   0x400ed0:	callq  0x400800 <free@plt>
   0x400ed5:	mov    -0x58(%rbp),%rax
   0x400ed9:	mov    0x8(%rax),%rax
   0x400edd:	mov    %rax,%rcx
   0x400ee0:	mov    $0x401175,%edx
-----------------------------------------------------------------------------------------------------------------------------

Breakpoint 3, 0x0000000000400ec4 in ?? ()
(gdb) c
Continuing.
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x0000000000000000  RBX: 0x0000000000000000  RBP: 0x00007FFFFFFFDDE0  RSP: 0x00007FFFFFFFDD80  o d I t s z a P c 
  RDI: 0x0000000000602100  RSI: 0x0000000000000200  RDX: 0x0000000000401175  RCX: 0x0000000000603010  RIP: 0x0000000000400EF4
  R8 : 0x0000000000000003  R9 : 0x00007FFFF7B7FF80  R10: 0x00007FFFFFFFDB40  R11: 0x00007FFFF7AAD600  R12: 0x0000000000400920
  R13: 0x00007FFFFFFFDEE0  R14: 0x0000000000000000  R15: 0x0000000000000000
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFDD80]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFDD80 : 0x00000000   0x00000003 - 0x00603040   0x00000000 ........@0`.....
0x00007FFFFFFFDD90 : 0x00400920   0x00000000 - 0x796402e5   0x00000000  .@.......dy....
0x00007FFFFFFFDDA0 : 0x0000000f   0x00000021 - 0x0000000f   0x00000038 ....!.......8...
0x00007FFFFFFFDDB0 : 0x00000020   0x00000000 - 0x00000020   0x00000000  ....... .......
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x400ef4:	callq  0x400860 <snprintf@plt>
   0x400ef9:	mov    -0x58(%rbp),%rax
   0x400efd:	mov    (%rax),%eax
   0x400eff:	mov    %eax,0x2013fb(%rip)        # 0x602300
   0x400f05:	mov    -0x58(%rbp),%rax
   0x400f09:	add    $0x10,%rax
   0x400f0d:	mov    $0x1a,%edx
   0x400f12:	mov    $0x0,%esi
-----------------------------------------------------------------------------------------------------------------------------

Breakpoint 1, 0x0000000000400ef4 in ?? ()
(gdb) c
Continuing.
Highest player: AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHaaaabbbbccccddddxxxxxxx score: 2021161080
Continue? ^[[A^C
Program received signal SIGINT, Interrupt.
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0xFFFFFFFFFFFFFE00  RBX: 0x00007FFFF7DD74E0  RBP: 0x00007FFFF7DD72A0  RSP: 0x00007FFFFFFFD9E8  o d I t s Z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFF7FF5000  RDX: 0x0000000000000400  RCX: 0xFFFFFFFFFFFFFFFF  RIP: 0x00007FFFF7B0CDF0
  R8 : 0x00007FFFF7FCC700  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000401151
  R13: 0x0000000000000001  R14: 0x0000000000000000  R15: 0x00007FFFF7DD74E0
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFD9E8]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFD9E8 : 0xf7aa63a0   0x00007fff - 0xf7dd3d40   0x00007fff .c......@=......
0x00007FFFFFFFD9F8 : 0xf7dd74e0   0x00007fff - 0xffffdcf0   0x00007fff .t..............
0x00007FFFFFFFDA08 : 0xf7aa71ce   0x00007fff - 0x00000063   0x00000000 .q......c.......
0x00007FFFFFFFDA18 : 0xf7a8b542   0x00007fff - 0xffffff90   0xffffffff B...............
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x7ffff7b0cdf0 <__read_nocancel+7>:	cmp    $0xfffffffffffff001,%rax
   0x7ffff7b0cdf6 <__read_nocancel+13>:	jae    0x7ffff7b0ce29 <read+73>
   0x7ffff7b0cdf8 <__read_nocancel+15>:	retq   
   0x7ffff7b0cdf9 <read+25>:	sub    $0x8,%rsp
   0x7ffff7b0cdfd <read+29>:	callq  0x7ffff7b25e30 <__libc_enable_asynccancel>
   0x7ffff7b0ce02 <read+34>:	mov    %rax,(%rsp)
   0x7ffff7b0ce06 <read+38>:	mov    $0x0,%eax
   0x7ffff7b0ce0b <read+43>:	syscall 
-----------------------------------------------------------------------------------------------------------------------------
0x00007ffff7b0cdf0 in __read_nocancel () at ../sysdeps/unix/syscall-template.S:81
81	../sysdeps/unix/syscall-template.S: Aucun fichier ou dossier de ce type.
(gdb) c
Continuing.
^C
Program received signal SIGINT, Interrupt.
-----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0xFFFFFFFFFFFFFE00  RBX: 0x00007FFFF7DD74E0  RBP: 0x00007FFFF7DD72A0  RSP: 0x00007FFFFFFFD9E8  o d I t s Z a P c 
  RDI: 0x0000000000000000  RSI: 0x00007FFFF7FF5000  RDX: 0x0000000000000400  RCX: 0xFFFFFFFFFFFFFFFF  RIP: 0x00007FFFF7B0CDF0
  R8 : 0x00007FFFF7FCC700  R9 : 0x00007FFFF7B7FF80  R10: 0x000000000040114F  R11: 0x0000000000000246  R12: 0x0000000000401151
  R13: 0x0000000000000001  R14: 0x0000000000000000  R15: 0x00007FFFF7DD74E0
  CS: 0033  DS: 0000  ES: 0000  FS: 0000  GS: 0000  SS: 002b				
[0x002b:0x00007FFFFFFFD9E8]-------------------------------------------------------------------------------------------[stack]
0x00007FFFFFFFD9E8 : 0xf7aa63a0   0x00007fff - 0xf7dd3d40   0x00007fff .c......@=......
0x00007FFFFFFFD9F8 : 0xf7dd74e0   0x00007fff - 0xffffdcf0   0x00007fff .t..............
0x00007FFFFFFFDA08 : 0xf7aa71ce   0x00007fff - 0x00000063   0x00000000 .q......c.......
0x00007FFFFFFFDA18 : 0xf7a8b542   0x00007fff - 0xffffff90   0xffffffff B...............
-----------------------------------------------------------------------------------------------------------------------[code]
=> 0x7ffff7b0cdf0 <__read_nocancel+7>:	cmp    $0xfffffffffffff001,%rax
   0x7ffff7b0cdf6 <__read_nocancel+13>:	jae    0x7ffff7b0ce29 <read+73>
   0x7ffff7b0cdf8 <__read_nocancel+15>:	retq   
   0x7ffff7b0cdf9 <read+25>:	sub    $0x8,%rsp
   0x7ffff7b0cdfd <read+29>:	callq  0x7ffff7b25e30 <__libc_enable_asynccancel>
   0x7ffff7b0ce02 <read+34>:	mov    %rax,(%rsp)
   0x7ffff7b0ce06 <read+38>:	mov    $0x0,%eax
   0x7ffff7b0ce0b <read+43>:	syscall 
-----------------------------------------------------------------------------------------------------------------------------
0x00007ffff7b0cdf0 in __read_nocancel () at ../sysdeps/unix/syscall-template.S:81
81	in ../sysdeps/unix/syscall-template.S
(gdb) quit
]0;francois@athos: ~/tmp/csawfrancois@athos:~/tmp/csaw$ exit

Script terminé sur dim. 18 sept. 2016 15:02:43 CEST
