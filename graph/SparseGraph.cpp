#include <iostream>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

class SparseGraph
{
private:
    int n_v;
    vector<vector<int>> edges;
    vector<vector<int>> vertices;
    vector<bool> visited;
    bool directed;

public:
    SparseGraph(vector<vector<int>> edges, int n_vertices, bool directed)
    {
        this->n_v = n_vertices;
        this->vertices = {};
        this->edges = {};
        this->directed = directed;
        for (int i = 0; i < n_vertices; i++)
        {
            this->vertices.push_back({});
            this->visited.push_back(false);
        }
        for (int i = 0; i < edges.size(); i++)
        {
            this->vertices[edges[i][0]].push_back(i);
            if (!directed)
                this->vertices[edges[i][1]].push_back(i);

            vector<int> v = {};
            for (int j = 0; j < edges[i].size(); j++)
                v.push_back(edges[i][j]);
            this->edges.push_back(v);
        }
    }

    void printEdges()
    {
        for (int i = 0; i < edges.size(); i++)
        {
            for (int j = 0; j < edges[i].size(); j++)
                cout << edges[i][j] << " ";
            cout << endl;
        }
    }

    void printVertices()
    {
        for (int i = 0; i < vertices.size(); i++)
        {
            for (int j = 0; j < vertices[i].size(); j++)
                cout << vertices[i][j] << " ";
            cout << endl;
        }
    }

    void clear_visited()
    {
        for (int i = 0; i < visited.size(); i++)
            visited[i] = false;
    }

    void dfs(int node, int destination)
    {
        stack<int> s;
        s.push(node);
        while (!s.empty())
        {
            int node = s.top();
            visited[node] = true;
            if (node == destination)
            {
                clear_visited();
                return;
            }
            cout << "node : " << node << endl;
            s.pop();
            for (int i = 0; i < vertices[node].size(); i++)
            {
                int next_node = edges[vertices[node][i]][0] + edges[vertices[node][i]][1] - node;
                if (!visited[next_node])
                {
                    visited[next_node] = true;
                    s.push(next_node);
                }
            }
        }
        clear_visited();
    }

    void bfs(int node, int destination)
    {
        queue<int> q;
        q.push(node);
        while (!q.empty())
        {
            int node = q.front();
            visited[node] = true;
            if (node == destination)
            {
                clear_visited();
                return;
            }
            cout << "node : " << node << endl;
            q.pop();
            for (int i = 0; i < vertices[node].size(); i++)
            {
                int next_node = edges[vertices[node][i]][0] + edges[vertices[node][i]][1] - node;
                if (!visited[next_node])
                {
                    visited[next_node] = true;
                    q.push(next_node);
                }
            }
        }
        clear_visited();
    }
};

int main(int argc, char const *argv[])
{
    vector<vector<int>>
        edges = {{1, 0, 10}, {0, 4, 20}, {1, 3, 5}, {2, 3, 6}, {3, 4, 20}, {4, 1, 10}};
    int n_vertices = 5;
    SparseGraph G = SparseGraph(edges, n_vertices, false);
    cout << "edges" << endl;
    G.printEdges();
    cout << endl
         << "nodes" << endl;
    G.printVertices();
    cout << endl
         << "DFS" << endl;
    G.dfs(0, -1);
    cout << endl
         << "BFS" << endl;
    G.bfs(0, -1);
    // print(* G.layer_vertices);
    // print(G.topo_sort());
    // print(G.strongly_connected());
    // G.get_vertices();
    // print(G.connectivity());
    return 0;
}
