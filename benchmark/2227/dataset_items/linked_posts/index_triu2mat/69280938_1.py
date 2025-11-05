#include <iostream>

using namespace std;

int b[2] ={-1,-1};

int Func(int a[4][4],int n)
{
    
    for(int i =0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(a[i][j]==n)
            {
                if(i<j)
                {
                    b[0]=i;
                    b[1]=j;
                    return 0;
                }
            }
        }
    }
}
int main()
{
    int a[4][4] ={{-1, 0, 3, 5}, {-1, -1, 1, 4}, {-1, -1, -1, 2}, {-1, -1, -1, -1}};
    Func(a,5);
    for(int i=0;i<2;i++)
    {
        cout<<b[i]<<" ";
    }
    return 0;
}
