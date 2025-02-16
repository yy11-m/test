#include <stdio.h>

int arr[5] = {0,0,0,0,0};

void printarr(int * arr)
{
    int len = sizeof(arr)/sizeof(arr[0]);

}

int main()
{
    int a = sizeof(arr)/sizeof(arr[0]);
    print("the length is : %d\n",a);
    return 0;
}