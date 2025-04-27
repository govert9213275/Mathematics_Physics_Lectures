# Circuits

## An idea of reducing complexity


### Case 1

#### Initial

This graph represents a simple path from `B+` to `B-` through several nodes (`R1`, `R2`, `R3`, `R4`, and `R5`). The nodes are connected in a linear fashion, with `B+` as the starting point and `B-` as the endpoint.

B+ and B- are the start and end nodes, represents battery endsite. Each



```mermaid
graph LR
    B+((B+))-->R1
    B+-->R2
    R2-->R3
    R3-->R4
    R1-->R4
    R4-->R5
    R5-->B-((B-))
```

#### First step

```mermaid
graph LR
    style R2 fill:#ff0000
    style R3 fill:#ff0000
    B+((B+))-->R1
    B+-->R2
    R2-->R3
    R3-->R4
    R1-->R4
    R4-->R5
    R5-->B-((B-))
```
```mermaid
graph LR
    style R23 fill:#ff0000
    B+((B+))-->R1
    B+-->R23
    R23-->R4
    R1-->R4
    R4-->R5
    R5-->B-((B-))
```

#### Second step

```mermaid
graph LR
    style R4 fill:#00ff00
    style R5 fill:#00ff00
    B+((B+))-->R1
    B+-->R23
    R23-->R4
    R1-->R4
    R4-->R5
    R5-->B-((B-))
```
```mermaid
graph LR
    style R45 fill:#00ff00
    B+((B+))-->R1
    B+-->R23
    R23-->R45
    R1-->R45
    R45-->B-((B-))
```

#### Third step

```mermaid
graph LR
    style R1 fill:#0000ff
    style R23 fill:#0000ff
    B+((B+))-->R1
    B+-->R23
    R23-->R45
    R1-->R45
    R45-->B-((B-))
```

```mermaid
graph LR
    style R123 fill:#0000ff
    B+((B+))-->R123
    R123-->R45
    R45-->B-((B-))
```

#### Fourth step

```mermaid
graph LR
    style R123 fill:#f0f
    style R45 fill:#f0f
    B+((B+))-->R123
    R123-->R45
    R45-->B-((B-))
```

```mermaid
graph LR
    style R12345 fill:#f0f
    B+((B+))-->R12345
    R12345-->B-((B-))
```

### Case 2

#### Initial

```mermaid
graph LR
    B+((B+))-->R1
    R1 --> R2
    R1 --> R3
    R2 --> o1((o))
    R3 --> o1    
    o1 --> R4
    o1 --> R5
    R4 --> B-((B-))
    R5 --> B-((B-))
```

To be more consistent, we should draw

```mermaid
graph LR
    B+((B+))-->o1((o))
    o1 --> R1
    R1 --> o2((o))
    o2 --> R2
    o2 --> R3
    R2 --> o3((o))
    R3 --> o3    
    o3 --> R4
    o3 --> R5
    R4 --> o4((o))
    R5 --> o4((o))
    o4 --> B-((B-))
```

Instead representing the resitors as nodes, we can represent them as edges. This way, we can reduce the complexity of the graph.



```mermaid
graph LR
    B+((B+))-->|R1|o1((o))
    o1-->|R2|o2((o))
    o1-->|R3|o2
    o2-->|R4|o3((o))
    o2-->|R5|o3
    o3-->B-((B-))
```


## Building blocks

### Series configuration

```mermaid
graph LR
    style o2 fill:#ff0000
    style o1 fill:#00ff00
    style o3 fill:#00ff00
    I1(I1)-->o1
    ... -->o1
    In(In)-->o1
    o1((o1))-->R1
    R1-->o2((o2))
    o2-->R2
    R2-->o3((o3))
    o3-->D1(D1)
    o3-->.,.
    o3-->D4(D4)
```

Can be replaced by

```mermaid
graph LR
    style o1 fill:#00ff00
    style o3 fill:#00ff00
    I1(I1)-->o1
    ... -->o1
    In(In)-->o1
    o1((o1))-->R12
    R12-->o3((o3))
    o3-->D1(D1)
    o3-->.,.
    o3-->Dm(Dm)
```

How find this situation?
1. Find the first node with degree 2 (`o2`)
2. Find the nodes to which it is connected: `o1` and `o3`
3. Remove edge `o1-o2` and `o2-o3`
4. Add edge `o1-o3` with the new resistance `R12 = R1 + R2`

### Parallel configuration

```mermaid
graph LR
    style o1 fill:#00ff00
    style o3 fill:#00ff00
    I1(I1)-->o1
    ... -->o1
    In(In)-->o1
    o1((o1))-->R1
    R1-->o3
    o1-->R2
    R2-->o3((o3))
    o3-->D1(D1)
    o3-->.,.
    o3-->D4(D4)
```

Can be replaced by

```mermaid
graph LR
    style o1 fill:#00ff00
    style o3 fill:#00ff00
    I1(I1)-->o1
    ... -->o1
    In(In)-->o1
    o1((o1))-->R12
    R12-->o3((o3))
    o3-->D1(D1)
    o3-->.,.
    o3-->Dm(Dm)
```
How find this situation?
1. Find two edges with the same start and end nodes (`o1` and `o3`)
2. Remove the edges `o1-o3` with label `R1` and `R2`
3. Add edge `o1-o3` with the new resistance `R12 = R1*R2/(R1 + R2)`