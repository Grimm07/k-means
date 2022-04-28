# K-Means - C Implementation

###### The following algorithm was forked from github: `dcasella/k-means`

## Interface

```c
double ***km(double **observations, int k, int observations_size, int vector_size);

double *centroid(double **observations, int observations_size, int vector_size);

double *vsum(double *vector1, double *vector2, int vector_size);

double *vsub(double *vector1, double *vector2, int vector_size);

double innerprod(double *vector1, double *vector2, int vector_size);

double norm(double *vector, int vector_size);

void print_vector(double *vector, int vector_size);

void print_observations(double **observations, int observations_size, int vector_size);

void print_clusters(double ***clusters, int k, int observations_size, int vector_size);
```

- KM - consutructor for the K-Means Algorithm
- Centroid - method defines the behaviors of the centroid used in the K-Means algorithm
- Vsum - Vector Sum
- VSub - Vector Subtraction
- Innerprod - Inner product of vectors
- Norm - matrix norm 

## Parallelization
- Pragma statements were added to the following methods
  - vsum
  - vsub
  - rand_num
  - initialize
  - partition

## Example

```c
int observationssize = 9;
int vector_size = 2;
int k = 3;
/* observations = {(3.0, 7.0), (0.5, 1.0), (0.8, 0.5),
 *                 (1.0, 8.0), (0.9, 1.2), (6.0, 4.0),
 *                 (7.0, 5.5), (4.0, 9.0), (9.0, 4.0)};
 */

print_observations(observations, observations_size, vector_size);

double ***clusters = km(observations, k, observations_size, vector_size);
print_clusters(clusters, k, observations_size, vector_size);
```

Output:

```c
[(3.00, 7.00), (0.50, 1.00), (0.80, 0.50),
 (1.00, 8.00), (0.90, 1.20), (6.00, 4.00),
 (7.00, 5.50), (4.00, 9.00), (9.00, 4.00)]

{[(0.50, 1.00), (0.80, 0.50), (0.90, 1.20)],
 [(6.00, 4.00), (7.00, 5.50), (9.00, 4.00)],
 [(3.00, 7.00), (1.00, 8.00), (4.00, 9.00)]}
```

## Run Steps
- Change directory to the project, specifically the `C` directory
- Run `make` command
- To run the iris dataset, use the command: `./main IrisStripped.txt 150 4 3`