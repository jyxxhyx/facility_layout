# Models for two-dimensional cutting

## Set covering for non-guillotine version

Sets

$\mathcal{N}$: set of cells in a grid

$\mathcal{S}$: set of all possible shapes (same shape with different rotation considered)

$\mathcal{N}_s$: set of cells can be placed by shape $s$

$\mathcal{C}_i=\{(s, j) \mid s \in \mathcal{S}, j \in \mathcal{N}_s, \ \text{s.t. positioning the anchor of shape s at cell j covers cell i}\}$

Decision variables

$$
x_s \in \mathbb{B}, \forall s \in \mathcal{S} \\
y_{si} \in \mathbb{B}, \forall s \in \mathcal{S}, \ i \in \mathcal{N}_s
$$

Formulation

$$
\max \quad \sum_{s \in \mathcal{S}} x_s \\
\text{s.t.} \quad x_s = \sum_{i \in \mathcal{N}_s} y_{si}, \quad \forall s \in \mathcal{S} \\
\sum_{(m,j) \in \mathcal{C}_i} y_{sj} \leq 1, \forall i \in \mathcal{N}.
$$

## Guillotine version
