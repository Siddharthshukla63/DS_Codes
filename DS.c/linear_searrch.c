#include<stdio.h>
int main()
{
    int a[10],i,key,flag,pos;
    for (i=0;i<10;i++)
    {
        printf("Enter element %d: ",i+1);
        scanf("%d",&a[i]);
    }
    printf("Enter the key to be searched: ");
    scanf("%d",&key);
    flag=0;
    for (i=0;i<10;i++)
    {
        if (a[i]==key)
        {
            flag=1;
            pos=i+1;
            break;

        }
    }
    if (flag==1)
        printf("Element found at position %d\n",pos);
    else
        printf("Element not found\n");
}