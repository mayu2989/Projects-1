#include <stdio.h>
int main()
{
int i,j;
int n=9;
int array[10] = {1,2,3,4,5,5,5,6,7,8};
i=2;
j=i-1;
while(array[i-1]!=array[i] && i<n)
{
    i = i +1;
    j = i-1;
}
while(i<n)
{
    i = i+1;
    if(array[i-1]!=array[i])
    {
        j = j +1;
        array[j] = array[i];
    }
}
n = j;
for(int a=0;a<n;a++)
{
    printf("%d\t",array[a]);
}
return 0;
}