#include<bits/stdc++.h>
using namespace std;

// visited aur adjList global me bna liya
vector<int> adjList[10005];
int vis[10005];

void storeGraphInAdjMatrix() {
  int n, m;
  cin >> n >> m;
  int adjMat[n+1][n+1];

  // take the edges as input
  for(int i = 0; i < m; ++i) {
    int u, v;
    cin >> u >> v;
    adjMat[u][v] = 1;
    adjMat[v][u] = 1;
  }
}

void storeGraphInAdjList() {
  int n, m;
  cin >> n >> m;
  vector<int> adjList[n+1];

  for(int i = 0; i < m; ++i) {
    int u, v;
    cin >> u >> v;
    adjList[u].push_back(v);
    adjList[v].push_back(u);
  }
}


void dfs(int node) {
  cout << node << " ";
  vis[node] = 1;

  // traverse for all adj nodes

  // ye normal for loop se hai
  // for(int i = 0; i < adjList[node].size(); ++i) {
  //   if (vis[adjList[node][i]] == 0) {
  //     dfs(i);
  //   }
  // }


  // ye iterator waale loop se
  for(auto it: adjList[node]) {
    if (vis[it] == 0) {
      dfs(it);
    }
  }
}

void dfsSolve() {
  // First Store the graph in adj List
  // n -> no of nodes/vertex
  // m -> no of edges
  int n, m;
  cin >> n >> m;

  for(int i = 1; i <= m; ++i) {
    int u, v;
    cin >> u >> v;
    adjList[u].push_back(v);
    adjList[v].push_back(u);
  }

  // ab saare components ke liye dfs call karenge
  for(int i = 1; i <= n; ++i) {
    if(vis[i] == 0) {
      dfs(i);
    }
  }
}


void bfs(int node){
  vis[node] = 1;
  queue<int> q;
  q.push(node);

  while (!q.empty()) {
    int temp = q.front();
    q.pop();
    cout << temp << " ";

    for(auto it: adjList[temp]) {
      if (!vis[it]) {
        vis[it] = 1;
        q.push(it);
      }
    }

  }
}

void bfsSolve() {
  // First Store the graph in adj List, sab input leke
  int n, m;
  cin >> n >> m;

  for(int i = 1; i <= m; ++i) {
    int u, v;
    cin >> u >> v;
    adjList[u].push_back(v);
    adjList[v].push_back(u);
  }

  // ab saare components ke liye bfs call karenge
  for(int i = 1; i <= n; ++i) {
    if(vis[i] == 0) {
      bfs(i);
    }
  }
}


// Minimum no of steps to reach from start to end by doing multiplication
int findMinimumMoves(int start, int end, int arr[], int n) {
  int vis[end+1] {};
  vis[start] = 1;

  queue<pair<int, int>> q;
  q.push({start, 0});

  while (!q.empty()) {
    int node = q.front().first;
    int steps = q.front().second;

    if (node == end)  return steps;
    q.pop();

    for(int i = 0; i < n; ++i) {
      int dest = node*arr[i];
      if (dest <= end && !vis[dest]) {
        vis[dest] = 1;
        q.push({dest, steps+1});
      }
    }
  }

  return -1;
}

void shortestPathBFS() {
  // Take the input of graph in adjList
  // m edges and n nodes 
  int n, m;
  cin >> n >> m;

  for (int i = 0; i < m; ++i) {
    int u, v;
    cin >> u >> v;
    adjList[u].push_back(v);
    adjList[v].push_back(u);
  }

  // Ab shortest path nikalo iss graph ka
  int dist[n];
  for(int i = 0; i < n; ++i) {
    dist[i] = INT_MAX;
  }

  // For printing the adjList
  // for(int i = 0; i < m; ++i) {
  //   for(auto it: adjList[i]) {
  //     cout << it << " ";
  //   }cout << endl;
  // }cout << endl;

  queue<int> q;
  int src = 0;
  dist[src] = 0;
  q.push(src);

  while(!q.empty()) {
    int node = q.front();
    q.pop();

    for(auto it: adjList[node]) {
      if (dist[node]+1 < dist[it]) {
        dist[it] = dist[node]+1;
        q.push(it);
      }
    }
  }

  for(int i = 0; i < n; ++i)  cout << dist[i] << " ";
  cout << endl;

}


int main() {

  // int n, start, end;
  // cin >> n >> start >> end;
  // int arr[n];
  // for(int i = 0; i < n; ++i) {
  //   cin >> arr[i];
  // }

  // cout << findMinimumMoves(start, end, arr, n) << endl;
  shortestPathBFS();

  return 0;
}