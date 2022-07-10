#include<stdio.h>
#include<stdlib.h>
#include<time.h>

const int N=203;
bool b[N][N],L[N][N],C[N][N];

int main(){
    freopen("ex_input.txt","w",stdout);
 //   int n,m; scanf("%d %d",&n,&m);
    int n=200,m=199;
    printf("%d %d\n",n,m);
    srand(time(NULL));
    for(int i=1;i<=m;i++){
        int x,y,c;
        do{
            x=rand()%n+1;
            y=rand()%n+1;
            c=rand()%n+1;
        }while(b[x][y]||L[x][c]||C[y][c]);
        b[x][y]=L[x][c]=C[y][c]=1;
        printf("%d %d %d\n",x,y,c);
    }
}