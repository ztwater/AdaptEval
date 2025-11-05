int main() {
    Digraph<int> g(8);
    g.addEdge(0,1,1);
    g.addEdge(1,2,1);
    g.addEdge(2,4,1);
    g.addEdge(0,3,1);
    g.addEdge(3,4,1);
    g.addEdge(4,7,1);
    g.addEdge(3,5,1);
    g.addEdge(5,6,1);
    g.addEdge(6,7,1);

    cout<<g.maxFlowEdmondsKarp(0,7);

    return 0;
}
