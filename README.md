# Diamond dataflow written in series-parallel manner (Proof of Concept)

This repository shows how to represent Two-terminal [Diamond graph](https://en.wikipedia.org/wiki/Forbidden_graph_characterization) in *series-parallel* manner.

Two-terminal diamond graph is:
```
U
| \
|  \
L -- R
  \  |
   \ |
     D
```
with arrows top to down, left to right. Note that it is the smallest two-terminal multidag that is not a two-terminal series-parallel graph (least number of vertices and edges).

---

Diamond graph's importance is supported by the following statement (He and Yesha 1987; Lemma 3):

> A two-terminal multidag is a two-terminal series parallel graph iff G contains two-terminal diamond graph as a subgraph

("contains" in the sense of graph homeomorphism)

It implies that if we can represent two-terminal diamond graphs into series-parallel graphs, we can represent arbitrary loop-free functions as series-parallel graphs.
