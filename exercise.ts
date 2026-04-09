type Vertex = number;

class Graph {

 // total number of vertices

 private V: number;

 // total number of edges added so far

 private E: number;



 // adj[v] = list of v's neighbors

 private adj: number[][];



 // Constructor: create V vertices, zero edges

 constructor(V: number) {

  this.V = V;

  this.E = 0;

  this.adj = Array.from({ length: V }, () => []);

 }



 // Add undirected edge {u, v}

 addEdge(u: number, v: number): void {

  this.adj[u].push(v); // v appears in u's neighbor list

  this.adj[v].push(u); // u appears in v's neighbor list (undirected)

  this.E++;

 }



 // Return neighbors of v

 neighbors(v: number): number[] {

  return this.adj[v]; // O(degree(v)) iteration

 }



 numVertices(): number {

  return this.V;

 }



 numEdges(): number {

  return this.E;

 } 

}

class DepthFirstSearch {

 private marked: boolean[];

 private edgeTo: number[];



 constructor(G: Graph) {

  const V = G.numVertices();

  this.marked = new Array(V).fill(false);

  this.edgeTo = new Array(V).fill(-1);



  this.dfsAll(G);

 }



 private dfs(G: Graph, v: number): void {

  // ① MARK

  this.marked[v] = true;



  // ② EXPLORE

  for (const w of G.neighbors(v)) {

   // ③ SKIP

   if (!this.marked[w]) {

    // ④ RECORD

    this.edgeTo[w] = v;



    // ⑤ DIVE

    this.dfs(G, w);

   }

  }

  // auto-backtrack when function returns

 }



 // Run DFS on every vertex (handles disconnected graphs)

 private dfsAll(G: Graph): void {

  const V = G.numVertices();

  for (let v = 0; v < V; v++) {

   if (!this.marked[v]) {

    this.dfs(G, v);

   }

  }

 }



 isMarked(v: number): boolean {

  return this.marked[v];

 }



 edgeToVertex(v: number): number {

  return this.edgeTo[v];

 }

}



// function bfs(G: Graph, s: Vertex) {
//   const queue: Vertex[] = [];

//   const visited = new Set<Vertex>();
//   const edgeTo = new Map<Vertex, Vertex>();
//   const distTo = new Map<Vertex, number>();

//   // Initialize
//   visited.add(s);
//   distTo.set(s, 0);
//   queue.push(s);

//   while (queue.length > 0) {
//     const v = queue.shift()!; // dequeue

//     const neighbors = G.neighbors(v);

//     for (const w of neighbors) {
//       if (!visited.has(w)) {
//         visited.add(w);                 // mark BEFORE enqueue
//         edgeTo.set(w, v);               // remember path
//         distTo.set(w, distTo.get(v)! + 1);
//         queue.push(w);
//       }
//     }
//   }

//   return { visited, edgeTo, distTo };



// Example usage

const G = new Graph(4);

G.addEdge(0, 1); // adj[0]={1}   adj[1]={0}

G.addEdge(0, 2); // adj[0]={1,2}  adj[2]={0}

G.addEdge(1, 2); // adj[1]={0,2}  adj[2]={0,1}

G.addEdge(1, 3); // adj[1]={0,2,3} adj[3]={1}

G.addEdge(2, 3); // adj[2]={0,1,3} adj[3]={1,2}

// const result = bfs(G, 0);
// console.log("BFS from vertex 0:");
// console.log("Visited vertices:", Array.from(result.visited));
// console.log("EdgeTo map:", result.edgeTo);
// console.log("DistTo map:", result.distTo);

// for (const w of G.neighbors(1)) {

//  console.log("Neighbor of 1:", w); // visits only 0, 2, 3

// }
const dfs = new DepthFirstSearch(G);



// Example: print edgeTo for each vertex

for (let v = 0; v < 4; v++) {

 console.log(`v=${v}, edgeTo=${dfs.edgeToVertex(v)}`);

}

