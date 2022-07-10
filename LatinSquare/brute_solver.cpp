#include<stdio.h>

const int N=10;

int n,m;
bool dfs(int x,int y,int S[][N],bool L[][N],bool C[][N]){
    if(S[x][y]) return dfs(x,y+1,S,L,C);
    if(y==n+1) return dfs(x+1,1,S,L,C);
    if(x==n+1) return 1;
    for(int i=1;i<=n;i++)
        if(!L[x][i]&&!C[y][i]){
            L[x][S[x][y]=i]=C[y][i]=1;
            if(dfs(x,y+1,S,L,C)) return 1;
            L[x][i]=C[y][i]=S[x][y]=0;
        }
    return 0;
}

int S[N][N];
bool L[N][N],C[N][N];
int main(){
    freopen("ex_input.txt","r",stdin);
    scanf("%d%d",&n,&m);
    for(int i=1;i<=m;i++){
        int x,y; scanf("%d%d",&x,&y);
        scanf("%d",&S[x][y]);
        L[x][S[x][y]]=C[y][S[x][y]]=1;
    }
    dfs(1,1,S,L,C);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++)
            printf("%d ",S[i][j]);
        printf("\n");
    }
}
