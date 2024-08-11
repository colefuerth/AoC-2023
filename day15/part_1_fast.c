#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>

#define BUFSIZE 128

// I'm basically just planning to turing machine it, one pass, as it comes in, unbuffered
// im on a plane and am bored ok

int main(int argc, char **argv)
{

    if (argc != 2)
    {
        fprintf(stderr, "Wrong number of args!\nUsage: %s <filename>\n\n", argv[0]);
        exit(1);
    }

    FILE *fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        fprintf(stderr, "There was an error opening \"%s\"!\n", argv[1]);
        exit(2);
    }

    char c;
    char buf[BUFSIZE];
    int sum = 0;
    int hash = 0;
    int bitesize, x;

    while (bitesize = fread(buf, sizeof(char), BUFSIZE, fp))
    {
        for (x = 0; x < bitesize; ++x) {
            c = buf[x];
            switch (c)
            {
            case ',':
                sum += hash;
                hash = 0;
            case '\n':
                break;
            default:
                hash = ((hash + (int)c) * 17) % 256;
            }
        }
    }
    sum += hash;

    printf("Part 1: %d\n", sum);
}