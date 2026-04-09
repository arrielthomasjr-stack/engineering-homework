/**

 * Represents a weighted edge.

 */

interface Edge {

  src: number;

  dest: number;

  weight: number;

}



/**

 * A simple Min-Priority Queue (Min-Heap) implementation.

 * Essential for Dijkstra's efficiency.

 */

class MinHeap<T> {

  private heap: { priority: number; value: T }[] = [];



  push(value: T, priority: number) {

    this.heap.push({ priority, value });

    this.bubbleUp();

  }



  pop(): T | undefined {

    if (this.size() === 0) return undefined;

    const top = this.heap[0].value;

    const last = this.heap.pop()!;

    if (this.size() > 0) {

      this.heap[0] = last;

      this.bubbleDown();

    }

    return top;

  }



  size(): number { return this.heap.length; }



  private bubbleUp() {

    let index = this.heap.length - 1;

    while (index > 0) {

      let parentIndex = Math.floor((index - 1) / 2);

      if (this.heap[parentIndex].priority <= this.heap[index].priority) break;

      [this.heap[parentIndex], this.heap[index]] = [this.heap[index], this.heap[parentIndex]];

      index = parentIndex;

    }

  }



  private bubbleDown() {

    let index = 0;

    while (true) {

      let left = 2 * index + 1;

      let right = 2 * index + 2;

      let smallest = index;



      if (left < this.size() && this.heap[left].priority < this.heap[smallest].priority) smallest = left;

      if (right < this.size() && this.heap[right].priority < this.heap[smallest].priority) smallest = right;

      if (smallest === index) break;



      [this.heap[smallest], this.heap[index]] = [this.heap[index], this.heap[smallest]];

      index = smallest;

    }

  }

}



/**

 * Finds and prints the shortest path using Dijkstra's Algorithm.

 */

function printShortestPath(start: number, end: number, adj: Edge[][]): void {

  const n = adj.length;

  const distances = new Array(n).fill(Infinity);

  const parents = new Array(n).fill(-1);

  const pq = new MinHeap<number>();



  distances[start] = 0;

  pq.push(start, 0);



  while (pq.size() > 0) {

    const u = pq.pop()!;



    if (u === end) break; // Optimization



    for (const edge of adj[u]) {

      const newDist = distances[u] + edge.weight;

      if (newDist < distances[edge.dest]) {

        distances[edge.dest] = newDist;

        parents[edge.dest] = u;

        pq.push(edge.dest, newDist);

      }

    }

  }



  // --- Path Reconstruction ---

  if (distances[end] === Infinity) {

    console.log(`No path exists from ${start} to ${end}`);

    return;

  }



  const path: number[] = [];

  for (let v = end; v !== -1; v = parents[v]) {

    path.push(v);

  }

  path.reverse();



  console.log(`Shortest Path (Cost ${distances[end]}): ${path.join(" -> ")}`);

}



// --- Example Usage ---

const n = 4;

const adj: Edge[][] = Array.from({ length: n }, () => []);



// Setup the graph matching your C++ example

adj[0] = [{ src: 0, dest: 1, weight: 4 }, { src: 0, dest: 2, weight: 1 }];

adj[1] = [{ src: 1, dest: 3, weight: 1 }];

adj[2] = [{ src: 2, dest: 1, weight: 2 }, { src: 2, dest: 3, weight: 5 }];

adj[3] = [];



printShortestPath(0, 3, adj);