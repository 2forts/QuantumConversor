OPENQASM 2.0;
include "qelib1.inc";

qreg q[3]; #q[0] is Cin, q[1] is A, q[2] is the ancilla qubit
creg c[3]; #c[0] is P, c[1] is A, c[2] is Cout

# Step 0: Uncomment to change the initial input (Cin = 0 and A = 0 if commented)
# x q[0]; #Cin
# x q[1]; #A

# Step 1
h q[2];
x q[1];

# Step 2
t q[0];
t q[1];
s q[2];

# Step 3
cx q[2],q[0];

# Step 4
tdg q[0];
tdg q[2];

# Step 5
cx q[2],q[0];
cx q[1],q[0];
cx q[2],q[1];

# Step 6
tdg q[0];
tdg q[1];

# Step 7
cx q[2],q[1];
cx q[2],q[0];

# Step 8
t q[0];

# Step 9
cx q[2],q[0];
x q[1];
h q[2];

# Measures
measure q[2] -> c[2]; # Cout
measure q[0] -> c[0]; # P 