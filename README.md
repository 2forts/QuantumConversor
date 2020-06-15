# QuantumConversor
Efficient reversible quantum design of a sign-magnitude to two's complement converters.

These circuits implement the conversion betweens numbers in sign-magnitude representation to two's complement. Their description, details and comparative are explained in the paper Efficient reversible quantum design of a sign-magnitude to two's complement converter, published (I hope so!) in the Quantum Information & Computation journal.

Version 1: 
This circuit is prepared to be used in Quirk, an open-source drag-and-drop quantum circuit simulator for exploring and understanding small quantum circuits. 

The circuit consists of 2 inputs (and an auxiliar qubit), A and Cin (carry input). By default, these values are 0, and should be changes manually in the circuit adding or removing Pauli-X gates at the beginning. I strongly recommend to contrast the circuit with the Figs. 4 and 5 of the paper.

Version 2:
This circuit is prepared to be used in the IBM Quantum Experience platform. 

The circuit consists of 2 inputs (and an auxiliar qubit), A and Cin (carry input). By default, these values are 0, and should be changes manually in the code commenting or uncommenting the gates of the step 0. I strongly recommend to contrast the circuit with the Fig. 7(c) of the paper.
