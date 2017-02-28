void *lecture_nom()
{
  void *v0; // ST10_8@3
  void *struct_long_nom; // ST18_8@3
  void *result; // rax@3
  __int64 v3; // rbx@3
  int longueur; // [sp+Ch] [bp-124h]@1
  char *v5; // [sp+10h] [bp-120h]@1
  char nom; // [sp+20h] [bp-110h]@1
  __int64 v7; // [sp+118h] [bp-18h]@1

  v7 = *MK_FP(__FS__, 40LL); // canari
  write(1, "What's your name?\n", 0x12uLL);
  memset(&nom, 0, 0xF8uLL);
  longueur = read(0, &nom, 0xF7uLL);
  v5 = strchr(&nom, 10);	// recherche du linefeed
  if ( v5 )
    *v5 = 0;
  v0 = malloc(longueur); // mis en rbp -120 soit v5 !!
  struct_long_nom = malloc(0x80uLL); // rbp - 118
  memset(struct_long_nom, 0, 0x80uLL);
  *((_QWORD *)struct_long_nom + 1) = v0; // + 8
  *((_DWORD *)struct_long_nom + 1) = longueur; // + 4 ... donc 0/longueur/point vers buf_nom sur 8 octets/
  memcpy(*((void **)struct_long_nom + 1), &nom, longueur);
  result = struct_long_nom;
  v3 = *MK_FP(__FS__, 40LL) ^ v7; //canari
  return result;
}

// nom + 8 = *(vrai nom), nom + 4 est la longueur
void __fastcall partie(__int64 nom, int fdrandom)
{
  char v2; // [sp+1Ah] [bp-46h]@5
  char v3; // [sp+1Bh] [bp-45h]@29
  int v4; // [sp+1Ch] [bp-44h]@5
  int v5; // [sp+20h] [bp-40h]@5
  int v6; // [sp+24h] [bp-3Ch]@1
  int v7; // [sp+28h] [bp-38h]@17
  int v8; // [sp+2Ch] [bp-34h]@30
  unsigned __int64 i; // [sp+30h] [bp-30h]@2
  unsigned __int64 j; // [sp+38h] [bp-28h]@6
  unsigned __int64 k; // [sp+40h] [bp-20h]@17
  void *buf; // [sp+48h] [bp-18h]@1
  void *s; // [sp+50h] [bp-10h]@30
  char *v14; // [sp+58h] [bp-8h]@30

  longueur_nom = *(_DWORD *)(nom + 4);
  buf = malloc(longueur_nom);
  if ( buf )
  {
    read(fdrandom, buf, longueur_nom);
    for ( i = 0LL; longueur_nom - 1 > i; ++i )
    {
      buf[i] ^= nom->nom[i];
      buf[i] = buf[i] % 0x1Au + 97;
    }
    v4 = 3;
    v5 = 0;
    v2 = 95;
    while ( v4 > 0 )
    {
      for ( j = 0LL; longueur_nom - 1 > j; ++j )
      {
        if ( *(_BYTE *)(nom + *((_BYTE *)buf + j) - 97 + 16) )
          write(1, (char *)buf + j, 1uLL);
        else
          write(1, "_", 1uLL);
      }
      write(1, "\n", 1uLL);
      __isoc99_scanf(" %c", &v2);
      if ( v2 > 96 && v2 <= 122 )
      {
        if ( *(_BYTE *)(nom + v2 - 97 + 16) )
        {
          puts("nope");
          --v4;
        }
        else
        {
          v7 = v5;
          for ( k = 0LL; longueur_nom - 1 > k; ++k )
          {
            if ( *((_BYTE *)buf + k) == v2 )
            {
              *(_BYTE *)(nom + v2 - 97 + 16) = 1;
              ++v5;
            }
          }
          if ( v7 == v5 )
            --v4;
          if ( longueur_nom - 1 <= v5 )
          {
            *(_DWORD *)nom = (signed int)floor((double)(longueur_nom - 1) * 0.25 * 32.0 + (double)*(signed int *)nom);
            goto LABEL_28;
          }
        }
      }
      else
      {
        puts("nope");
        --v4;
      }
    }
    *(_DWORD *)nom = (signed int)floor((double)(longueur_nom - 1) * 0.25 * (double)v5 + (double)*(signed int *)nom);
LABEL_28:
    if ( *(_DWORD *)nom > Global_score )
    {
      puts("High score! change name?");
      __isoc99_scanf(" %c", &v3);
      if ( v3 == 121 )
      {
        s = malloc(0xF8uLL);
        memset(s, 0, 0xF8uLL);
        v8 = read(0, s, 0xF8uLL);
        *(_DWORD *)(nom + 4) = v8;
        v14 = strchr((const char *)s, 10);
        if ( v14 )
          *v14 = 0;
        memcpy(*(void **)(nom + 8), s, v8); // ecrasement de nom: nom+0 = score, nom + 4 
        free(s);
      }
      snprintf(byte_602100, 0x200uLL, "Highest player: %s", *(_QWORD *)(nom + 8)); // segfault si écrasement de nom
      Global_score = *(_DWORD *)nom;
    }
    memset((void *)(nom + 16), 0, 0x1AuLL);
    free(buf);
  }
}
// strchr=602038, memcpy=602078
// buf_highscore = 602100
// Global_score = 602300
//  Global_nom = 6020E0

int __fastcall main(__int64 argc, char **argv, char **envp)
{
  __int64 v3; // rax@3 
  char v5; // [sp+Bh] [bp-5h]@4
  int fd; // [sp+Ch] [bp-4h]@1

  setvbuf(stdout, 0LL, 2, 0LL);
  memset(buf_highscore, 0, 0x200uLL);
  memcpy(buf_highscore, "Default Highscore ", 0x14uLL);
  Global_score = 64;
  fd = open("/dev/urandom", 0);
  if ( fd == -1 )
    exit(1);
  LODWORD(v3) = lecture_nom();
  Global_nom = v3;
  printf("Welcome %s\n", *(_QWORD *)(v3 + 8));
  do
  {
    partie(Global_nom, (unsigned int)fd);
    printf("%s ", buf_highscore);
    printf("score: %d\n", (unsigned int)Global_score);
    printf("Continue? ");
    __isoc99_scanf(" %c", &v5);
  }
  while ( v5 != 110 );
  return close(fd);
}

