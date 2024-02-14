#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
/**
  * main - entry point.
  * Return - 1 for success.
  */
int main()
{
	FILE *fp = fopen("write.txt", "w");
	fputs("This is python-C extension\n", fp);
	fclose(fp);
	return (1);
}
