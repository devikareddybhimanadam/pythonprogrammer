#include<stdio.h>
int main(void)
{
	int i,j,k,l,b1,b2,t,n1,n2;
	scanf("%d%d",&i,&j);
	scanf("%d%d",&k,&l);
	b1=i*60+j;
	b2=k*60+l;
	if(a1>a2)
	{
		t=b1-b2;
		n1=t/60;
		n2=t%60;
		printf("%d %d",n1,n2);
	}
	else
	{
		t=b2-b1;
		n1=t/60;
		n2=t%60;
		printf("%d %d",n1,n2);
	}
}	
