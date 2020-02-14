# QuantumConversor
Efficient reversible quantum design of a sign-magnitude to two's complement converter.

This circuit is prepared to be used in the IBM Quantum Experience platform. It implements the conversion betweens numbers in sign-magnitude representation to two's complement. Its description, details and comparative are explained in the paper Efficient reversible quantum design of a sign-magnitude to two's complement converter, published (I hope so!) in the Quantum Information & Computation journal.

The circuit consists of 2 inputs (and an auxiliar qubit), A and Cin (carry input). By default, these values are 0, and should be changes manually in the code commenting or uncommenting the gates of the step 0. I strongly recommend to contrast the circuit with the Fig. 10(c) of the paper.
