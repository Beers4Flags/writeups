#include <stdio.h>
#include <stdlib.h>
#include <sys/fcntl.h>
#include <unistd.h>
#include <string.h>
#include <strings.h>

void setup(){
	int fd = open("/dev/urandom", O_RDONLY);
	long int seed;
	read(fd, &seed, sizeof(seed) );
	srand(seed);
	printf("Today's magic number is %lx\n", seed);
	alarm(60);
	close(fd);

        setbuf(stdout, NULL);
        setbuf(stdin, NULL);

}

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

void validate(char *buf, int sz){
	int i;
	for(i = 0 ; i < sz; i++)
		if ( buf[i] >= 'A' && buf[i] <= 'Z') {
			puts("Come on.... seriously?");
			exit(-1);
		}
}

void chance(char *p){
	char buf[4096];
	int readcount = read(0, buf, 4095);
	if (readcount < 10) {
		puts("Come on.... seriously?");
		exit(-1);
	}
	validate(buf, readcount);

	if (memcmp(buf, p, 100) == 0 ){
		puts("You win!");
		system("cat /home/`whoami`/flag");
		exit(0);
	} else {
		puts("Guess again!");
	}
}


int main()
{
	setup();
	puts("Let's play a game!");
	puts("We recently heard that China wants to ban the letter N. Why not all uppercase?");
	puts("Let's not make it super hard, though: you have 100 tries. Do you know your maths and probabilities?");
	puts("Use the magic number above and give me the password. But no uppercase please!");

	int i;
	for(i = 0 ; i < 100; i++){
		char *p = gen_rand_string(100);
		chance(p);
		free(p);
	}
}
