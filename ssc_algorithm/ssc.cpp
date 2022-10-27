#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include<queue>

using namespace std;

vector<int> g[10001];
vector<int> gr[10001];
int pre[10001], post[10001];
vector<pair<int, int>> sorted;
queue<int> scc;
int clock = 0;

void initVisit() {

    clock = 0;
    for (int i = 0; i < 10001; i++) {
        pre[i] = post[i] = -1;
    }
}

void dfs(int v) {
    
    printf("%d visiting\n", v);
    pre[v] = clock++;

    for (int i = 0; i < gr[v].size(); i++) {
        if (pre[gr[v][i]] < 0)
            dfs(gr[v][i]);
    }
    post[v] = clock++;
    //<post[v],v>를 저장
    sorted.push_back(make_pair(post[v], v));
}

void dfs2(int v) {

    pre[v] = clock++;
    scc.push(v);

    for (int i = 0; i < g[v].size(); i++) {
        if (pre[g[v][i]] < 0)
            dfs2(g[v][i]);
    }
}
int main(){

    int i, j;
    int n, m; // n: V의 수, m: E의 수
    int u, v; //<u,v>는 edge
// 1. load G(G 읽어들이기)
    FILE* fp = fopen("graph1.txt", "r+t");

    fscanf(fp, "%d %d", &n, &m);

    for (i = 0; i < m; i++)
    {
        fscanf(fp, "%d %d", &u, &v);
        g[u].push_back(v);
    }
    fclose(fp);

    for (i = 1; i <= n; i++)
    {
        sort(g[i].begin(), g[i].end());
    }
//그래프 출력해보기
    for (i = 1; i <= n; i++)
    {
        printf("[%d] %d", i, g[i].size());
        for (j = 0; j < g[i].size(); j++)
        {
            printf(" <%d, %d>", i, g[i][j]);
        }
        printf("\n");
    }


// 2. G.reverse (gr) 만들기
    for (i = 1; i <= n; i++) {
        for (j = 0; j < g[i].size(); j++) {
            gr[g[i][j]].push_back(i);
        }
    }
    for (i = 1; i <= n; i++) {
        sort(gr[i].begin(),gr[i].end());
    }
// 3. G reverse에서 dfs 하면서 pre, post 계산
    initVisit();
    for (i = 1; i <= n; i++) {
        if (pre[i] < 0)
            dfs(i);
    }
   

    reverse(sorted.begin(), sorted.end());
   /* for (i = 0; i < n; i++)
        printf("[%d] %d, %d\n", i, sorted[i].first, sorted[i].second);*/
// 4. G에서 postnum의 역순으로 dfs를 이용해서 scc를 만든다.
    initVisit();
    for (i = 1; i <= n; i++) {
        if (pre[sorted[i].second] < 0) {
            dfs2(sorted[i].second);
            if (!scc.empty()) {
                printf("scc:");
                while (!scc.empty()) {
                    printf("%d", scc.front());
                    scc.pop();
                }
                printf("\n");
            }
        }
    }
    return 0;
}