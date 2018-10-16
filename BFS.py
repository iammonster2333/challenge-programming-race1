const int INF=100000000;
int MAX_N=10000,MAX_M=10000;
typedef pair<int,int> P;

char maze[MAX_N][MAX_M+1];

int N,M;
int sx,sy;
int gx,gy;

int d[MAX_N][MAX_M];

int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};

int bfs(){
    queue<p> que;
    for(int i=0;i<N;i++){
    for(int j=0;j<M;j++){
    d[i][j]=INF;
    }
    }

    que.push(P(sx,sy));
    d[sx][sy]=0;

    while(que.size()){
    p=que.front();
    que.pop();

    if(p.first==gx&&p.second=gy){
    break;
    }

    for(int i=0;i<4;i++){
    int nx=p.first+dx[i],ny=p.second+dy[i];
    if(nx>=0&&nx<N&&ny>=0&&ny<M&&maze[nx][ny]!='#'&&d[nx][ny]==INF){
    que.push(P(nx,ny));
    d[nx][ny]=d[p.first][p.second]+1;
    }
    }

    }
        return d[gx][gy];
}

void solve(){
    int res=bfs();
    printf("%d",res);
}
