_UNKNOWN unk_201D60; // weak
void *off_202008 = &off_202008; // weak
char *needle = "I Really LOVE soRting ALgoRithMs!"; // idb
FILE *stdout; // idb
char byte_202020; // weak


//----- (0000000000000B70) ----------------------------------------------------
unsigned __int64 init_B70()
{
  unsigned __int64 v0; // ST08_8

  setbuf(stdout, 0LL);
  alarm(0x3Cu);
}

//----- (0000000000000BBC) ----------------------------------------------------
int __fastcall compar(const void *a1, const void *a2)  // compare a1[1:x+1] a2[1:x+1] avec x = (int *) 
{
  return strncmp(*((const char **)a1 + 1), *((const char **)a2 + 1), *((signed int *)a1 + 4)); // Soit *((int *) &a1[16])
}

//----- (0000000000000C26) ----------------------------------------------------
_DWORD *__fastcall sub_C26(char *chaine, int last)
{
  void *v2; // rsp
  int v4; // [rsp+4h] [rbp-4Ch]
  char *src; // [rsp+8h] [rbp-48h]
  int i; // [rsp+10h] [rbp-40h]
  int j; // [rsp+14h] [rbp-3Ch]
  __int64 v8; // [rsp+18h] [rbp-38h]
  void *base; // [rsp+20h] [rbp-30h]
  char *dest; // [rsp+28h] [rbp-28h]
  _DWORD *v11; // [rsp+30h] [rbp-20h]
  unsigned __int64 v12; // [rsp+38h] [rbp-18h]

  src = chaine;
  v4 = last;
  v8 = last - 1LL;
  v2 = alloca(16 * ((24LL * last + 22) / 0x10uLL));
  base = (void *)(8 * (((unsigned __int64)&v4 + 3) >> 3));
  dest = (char *)calloc(2 * last + 1, 1uLL);
  strcat(dest, src);
  strcat(dest, src);
  for ( i = 0; i < v4; ++i )
  {
    *((_DWORD *)base + 6 * i) = i;  // [src...][src....][
    *((_QWORD *)base + 3 * i + 1) = &dest[i];
    *((_DWORD *)base + 6 * i + 4) = v4;
  }
  qsort(base, v4, 0x18uLL, (__compar_fn_t)compar);
  v11 = malloc(4LL * v4);
  for ( j = 0; j < v4; ++j )
    v11[j] = *((_DWORD *)base + 6 * j);
  return v11;
}

//----- (0000000000000E6A) ----------------------------------------------------
_BYTE *__fastcall sub_E6A(__int64 a1, __int64 a2, int a3)
{
  int v4; // [rsp+Ch] [rbp-34h]
  int i; // [rsp+28h] [rbp-18h]
  int v6; // [rsp+2Ch] [rbp-14h]
  _BYTE *v7; // [rsp+30h] [rbp-10h]

  v4 = a3;
  v7 = calloc(a3 + 1, 1uLL);
  for ( i = 0; i < v4; ++i )
  {
    v6 = *(_DWORD *)(4LL * i + a2) - 1;
    if ( v6 < 0 )
      v6 += v4;
    v7[i] = *(_BYTE *)(v6 + a1);
  }
  v7[i] = 0;
  return v7;
}

//----- (0000000000000F2B) ----------------------------------------------------
unsigned __int64 __fastcall transfo_F2B(char *avant, __int64 nblus, char *apres)
{
  _DWORD *v3; // ST48_8
  char *src; // ST50_8
  char *dest; // [rsp+8h] [rbp-58h]
  int i; // [rsp+2Ch] [rbp-34h]
  int v8; // [rsp+30h] [rbp-30h]
  unsigned __int64 v9; // [rsp+58h] [rbp-8h]

  dest = apres;
  indice = strlen(avant);
  if ( avant[indice - 1] == 10 )
    avant[indice-- - 1] = 0;
  for ( i = 0; i < indice; ++i )
  {
    if ( (unsigned __int8)avant[i] <= 0x1Fu || avant[i] < 0 )
    {
      puts("No swearing in class! Get out!");
      exit(0);
    }
  }
  v3 = sub_C26(avant, indice);
  src = sub_E6A((__int64)avant, (__int64)v3, indice);
  strncpy(dest, src, indice);
}

//----- (0000000000001053) ----------------------------------------------------
__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  unsigned int nbytes; // [rsp+8h] [rbp-888h]
  unsigned int nblus; // [rsp+Ch] [rbp-884h]
  char buf; // [rsp+10h] [rbp-880h]
  char v7; // [rsp+80h] [rbp-810h]
  char s; // [rsp+480h] [rbp-410h]
  unsigned __int64 v9; // [rsp+888h] [rbp-8h]

  init_B70();
  printf(
    "Let's sort out the trash!\n"
    "Can you guess what my function is doing? Give me an input that, upon transformation, outputs %s and you win!\n",
    needle);
  memset(&s, 0, 0x400uLL);
  memset(&blus, 0, 0x400uLL);
  while ( 1 )
  {
    puts("How big is the input?");
    read(0, &buf, 0x64uLL);
    nbytes = atoi(&buf);
    if ( nbytes == -1 )
      nbytes = 5000; // Bof large possible
    nblus = read(0, &blus, nbytes);
    transfo_F2B(&blus, nblus, &s); // Visiblement ça va chercher plus loin
    if ( strstr(&s, needle) == &s )
      break;
    write(1, &s, (signed int) nblus);
    puts("\n-------------------");
  }
  puts("You win!");
  return 0LL;
}

