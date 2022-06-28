##################
### Parameters ###
##################

param T;

param N;

param W {i in 0..N-1} >= 0;

var X {i in 0..N-1} binary;

##################
### Objective ####
##################

maximize objective: sum {i in 0..N-1} X[i] * Y[i];

##################
### Constraints ##
##################

subject to C1: sum {i in 0..N-1} X[i] * Y[i] <= T;