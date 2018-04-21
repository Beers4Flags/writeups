#include <stdio.h>
#include <stdlib.h>
#include <sys/fcntl.h>
#include <unistd.h>
#include <string.h>
#include <strings.h>



char *gen_rand_string(int len)
{
	int i;
	char buf[4096];
	char tab[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/ ";
	for(i = 0 ; i < len; i ++){
		char c = tab[rand() % (sizeof(tab)-1) ];
		buf[i] = c;
	}
	buf[len] = 0;

	char *s = calloc(len+1, 1);
	memcpy(s, buf, len+1);
	return s;
}

int validate(char *buf, int sz){
	int i;
	for(i = 0 ; i < sz; i++)
	  if ( buf[i] >= 'A' && buf[i] <= 'Z') return(0);
	return(1);
}



int main(int argc,char **argv)
{

  long int seed;
  int i;
  seed=strtol(argv[1],NULL,16);
  srand(seed);
  for(i = 0 ; i < 100; i++){
    char *p = gen_rand_string(100);
    if (validate(p,10))
      printf("%s\n",p);
    else
      printf("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n");
    free(p);
  }
}
