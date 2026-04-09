import Graph from "./exercise";

void BFS(Graph G, vertex s):
    Create queue Q
    Mark s as visited
    Enqueue s into Q

    while Q is not empty:
        v ← Dequeue from Q           // take front vertex

        for each neighbor w of v:
            if w is not yet visited:
                Mark w as visited    // mark BEFORE enqueuing!
                edgeTo[w] ← v        // remember we came from v
                distTo[w] ← distTo[v] + 1
                Enqueue w into Q