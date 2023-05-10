#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<size_t> used;
vector<vector<size_t >> g;
int counter = 0;

void dfs(size_t v) {
    used[v] = counter;
    for (auto to : g[v]) {
        if (!used[to]) {
            dfs(to);
        }
    }
}

int main() {
    size_t  n, m;
    cin >> n >> m;

    g = vector<vector<size_t >>(n, vector<size_t >());
    used = vector<size_t >(n);

    for (int i = 0; i < m; ++i) {
        int from, to;
        cin >> from >> to;
        g[from - 1].emplace_back(to - 1);
        g[to - 1].emplace_back(from - 1);
    }
    while (find(used.begin(), used.end(), 0) != used.end()) {
        ++counter;
        size_t ind = distance(used.begin(), find(used.begin(), used.end(), 0));
        dfs(ind);
    }

    cout << counter << endl;

    for (size_t use : used) {
        cout << use << " ";
    }

    return 0;
}