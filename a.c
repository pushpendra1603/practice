#include <stdio.h>
void main()
{
	int a=0;
	printf("enter ur numbers\n");
	scanf("%d",&a);
	for(;;)
	{
		if(a==42)
			break;
		else
			scanf("%d",&a);
	}
}
