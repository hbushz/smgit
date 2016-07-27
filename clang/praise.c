#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <float.h>
#define PRAISE "You are an extraodinary being"

int main(void)
{
	char name[40];

	printf("What's your name?\n");
	scanf("%s", name);
	printf("Hello, %s. %s\n",name,PRAISE);
	printf("Your name of %zd letters occupies %zd memory cells.\n",strlen(name),sizeof(name));
	printf("The phrase of PRAISE has %zd letters", strlen(PRAISE));
	printf("and occupies %zd memory cells.\n", sizeof(PRAISE));
	printf("Int max number  %d.\n", INT_MAX);
	printf("float Max   %a.\n", FLT_MAX);
	printf("float min number  %a.\n",FLT_EPSILON );

}
