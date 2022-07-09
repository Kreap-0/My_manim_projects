#include<stdio.h>

const int N=203;
int n,m,S[N][N],c[N],a[N][N];
int main(){
    freopen("ex_output.txt","r",stdin);
    scanf("%d %d",&n,&m);
    for(int i=1;i<=m;i++){
        int x,y,z; scanf("%d%d",&x,&y);
        scanf("%d",&z); a[x][y]=z;
    }
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            scanf("%d",&S[i][j]);
    for(int i=1;i<=n;i++) c[i]=0;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            if((++c[S[i][j]])!=i||S[i][j]<1||S[i][j]>n)
                return printf("invalid1! %d %d %d %d",i,j,S[i][j],c[S[i][j]]),(0-0);
    for(int i=1;i<=n;i++) c[i]=0;
    for(int j=1;j<=n;j++)
        for(int i=1;i<=n;i++)
            if((++c[S[i][j]])!=j)
                return printf("invalid2! %d %d %d %d",i,j,S[i][j],c[S[i][j]]),(0-0);
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            if(a[i][j]&&a[i][j]!=S[i][j])
                return printf("invalid3! (%d,%d)",i,j),(0-0);
    return printf("valid!"),(0-0);
}