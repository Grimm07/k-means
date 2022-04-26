# K-Means > C > Parralelization

## Interface

```c
double *vsub(const double *vector1, const double *vector2, int vector_size)
double *vsum(const double *vector1, const double *vector2, int vector_size)
int rand_num(int size)
double **initialize(double **observations, int k, int observations_size, int vector_size)
int *partition(double **observations, double **cs, int k, int observations_size, int vector_size)
```

## Compiling on Expanse

```
$ module load cpu/0.15.4 gcc/10.2.0 openmpi/4.0.4
$ make
```

## Compiling on MAC (Intel)

```
$ brew install llvm
$ make
```
