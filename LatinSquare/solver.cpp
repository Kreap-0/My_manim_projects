/*
Author: @Kreap-0
Date: 2022/7/9

Input Format:
n: Size of the square
m: Number of elements already in the square (m<n!!!)
x y c: An element 'c' in the cell (x,y) 
*/

#define deb 1
// mode options: 1=debug, 0=normal

#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

inline int read(){
    int x=0; char c=getchar(); int flag=1;
    while(c<'0'||c>'9'){if(c=='-') flag=0;c=getchar();}
    while(c>='0'&&c<='9'){x=(x<<1)+(x<<3)+c-48;c=getchar();}
    return flag? x:-x;
}

const int N=203;

void print(int n,int S[][N]){
    if(deb) printf("--------\n");
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++)
            printf("%d ",S[i][j]);
        printf("\n");
    }
    if(deb) printf("--------\n\n");
}

vector<int> e[N];
int f[N],match[N],timer=0,dfn[N];
bool Cmp(int x,int y){return f[x]>f[y];}

bool dfs(int u){
	for(int v:e[u]){
		if(dfn[v]==timer) continue;
		dfn[v]=timer;
		if(!match[v]||dfs(match[v])){
			match[v]=u;
			return 1;
		}
	}
	return 0;
}

void solve(int n,int (*S)[N]){
    if(n<=2){
        printf("end!!!\n");
        if(S[1][1]==1||S[2][2]==1)
            S[1][2]=S[2][1]=2,S[1][1]=S[2][2]=1;
        else S[1][2]=S[2][1]=1,S[1][1]=S[2][2]=2;
        if(deb) print(n,S);
        return ;
    }
    int xx=0,yy=0,v=0,c[N];
    for(int i=1;i<N;i++) c[i]=f[i]=0;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++) c[S[i][j]]++,f[i]+=(S[i][j]>0);
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            if(S[i][j]&&c[S[i][j]]==1) xx=i,yy=j,v=S[i][j];
    if(v){
        if(deb) printf("!!! Case1\n!!! n=%d v=%d\n",n,v);
        if(deb) print(n,S);
        bool tag1=0;
        if(v!=n){
            tag1=1;
            for(int i=1;i<=n;i++)
                for(int j=1;j<=n;j++){
                    if(S[i][j]==n) S[i][j]=v;
                    else if(S[i][j]==v) S[i][j]=n;
                }
            if(deb) print(n,S);
        }
        int sta[N],tp=0,px[N],ppx[N],cnt=0,py[N],ppy[N];
        for(int i=1;i<=n;i++){
            if(f[i]) sta[++tp]=i;
            px[i]=ppx[i]=py[i]=ppy[i]=i;
        }
        bool tag2=0;
        if(sta[1]!=xx){
            swap(S[sta[1]],S[xx]);
            swap(f[sta[1]],f[xx]);
            tag2=1;
            if(deb) print(n,S);
        }
        int x=sta[1],y=ppx[f[sta[1]]];
        if(x!=y){
            swap(S[px[x]],S[px[y]]);
            swap(px[x],px[y]);
            swap(ppx[px[x]],ppx[px[y]]);
            if(deb) print(n,S);
        }
        cnt=f[sta[1]]+1;
        for(int i=2;i<=tp;i++){
            x=sta[i],y=ppx[cnt+=f[sta[i]]];
            if(x==y) continue;
            swap(S[px[x]],S[px[y]]);
            swap(px[x],px[y]);
            swap(ppx[px[x]],ppx[px[y]]);
            if(deb) print(n,S);
        }
        for(int ep=1,now=1;now<=n;now++)
            if(S[px[sta[1]]][now]){
                if(ep==now){ep++;continue;}
                for(int j=1;j<=n;j++)
                    swap(S[j][now],S[j][ep]);
                swap(ppy[ep],ppy[now]);
                swap(py[ppy[ep]],py[ppy[now]]);
                ep++;
                if(deb) print(n,S);
            }
        cnt=px[sta[1]];
        for(int i=1;i<=n;i++)
            if(S[cnt][i]==n) x=i;
        for(int j=1;j<=n;j++)
            swap(S[j][x],S[j][cnt]);
        swap(ppy[x],ppy[cnt]);
        swap(py[ppy[x]],py[ppy[cnt]]);
        cnt++;
        if(deb) print(n,S);
        for(int i=2;i<=tp;i++){
            int tmp=cnt+f[sta[i]];
            for(int ep=cnt,now=cnt;now<=n;now++)
                if(S[tmp][now]){
                    if(ep==now){ep++;continue;}
                    for(int j=1;j<=n;j++)
                        swap(S[j][now],S[j][ep]);
                    swap(ppy[ep],ppy[now]);
                    swap(py[ppy[ep]],py[ppy[now]]);
                    ep++;
                    if(deb) print(n,S);
                }
            cnt=tmp;
        }
        int S_[N][N];
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++) S_[i][j]=0;
        for(int i=1;i<=n-1;i++)
            for(int j=1;j<=i;j++) S_[i][j]=S[i+1][j];
        solve(n-1,S_);
        for(int i=2;i<=n;i++)
            for(int j=1;j<n;j++) S[i][j]=S_[i-1][j];
        if(deb) print(n,S);
        int mt[N]; for(int i=1;i<=n;i++) mt[i]=0;
        for(int i=2;i<=n;i++){
            S[i][n]=n; int x=i;
            swap(S[i][n],S[i][i]);
            while(mt[S[x][n]]){
                swap(mt[S[x][n]],x);
                swap(S[x][n],S[x][i]);
            }
            mt[S[i][n]]=i,mt[S[x][n]]=x;
        //    for(int j=1;j<=n;j++) printf("%d ",mt[j]);
        //    printf("\n");
              if(deb) print(n,S);
        }
        if(deb) print(n,S);
        for(int j=1;j<=n;j++){
            for(int i=1;i<=n;i++) mt[i]=0;
            for(int i=2;i<=n;i++) mt[S[i][j]]=1;
            for(int i=1;i<=n;i++)
                if(!mt[i]){S[1][j]=i;break;}
        }
        if(deb) print(n,S);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++) S_[i][j]=S[px[i]][py[j]];
        if(tag2) swap(S_[sta[1]],S_[xx]);
        if(tag1){
            for(int i=1;i<=n;i++)
                for(int j=1;j<=n;j++){
                    if(S_[i][j]==n) S_[i][j]=v;
                    else if(S_[i][j]==v) S_[i][j]=n;
                }
        }
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++) S[i][j]=S_[i][j];
        if(deb) print(n,S);
    }else{
        if(deb) printf("!!! Case2\n");
        int S_[N][N],p[N],b[N];
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++) S_[i][j]=0;
        if(deb) print(n,S);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                if(S[i][j]) S_[S[i][j]][j]=i;
        if(deb) print(n,S_);
        for(int i=1;i<=n;i++) f[i]=0,p[i]=i;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++) f[i]+=(S_[i][j]>0);
        sort(p+1,p+1+n,Cmp);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++) S[i][j]=S_[p[i]][j];
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                e[j].clear(),match[j]=dfn[j]=0;
                if(S[i][j]) e[j].push_back(S[i][j]);
                else{
                    for(int k=1;k<=n;k++) b[k]=0;
                    for(int k=1;k<=n;k++) b[S[k][j]]=1;
                    for(int k=1;k<=n;k++) if(!b[k]) e[j].push_back(k);
                }
            }
            for(timer=1;timer<=n;timer++) dfs(timer);
            for(int j=1;j<=n;j++) S[i][match[j]]=j;
            if(deb) print(n,S);
        }
        for(int i=1;i<=n;i++) b[p[i]]=i;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++) S_[i][j]=S[b[i]][j];
        if(deb) print(n,S_);
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++) S[S_[i][j]][j]=i;
        if(deb) print(n,S);
    }
}

int S[N][N];
int main(){
    freopen("ex_input.txt","r",stdin);
    freopen("ex_output.txt","w",stdout);
    int n=read(),m=read();
    if(!deb) printf("%d %d\n",n,m);
    for(int i=1;i<=m;i++){
        int x=read(),y=read();
        S[x][y]=read();
        if(!deb) printf("%d %d %d\n",x,y,S[x][y]);
    }
    solve(n,S);
    print(n,S);
}

/*
7 6
2 2 2
2 5 7
3 3 5
3 5 4
5 4 5
7 2 4
*/
