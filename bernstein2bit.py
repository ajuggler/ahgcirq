"""Bernstein-Vazirani algorithm for two qubits in Cirq."""

# Import the Cirq library
import cirq

# Get three qubits -- two data and one target qubit
q0, q1, q2 = cirq.LineQubit.range(3)

# Dictionary for oracles
oracles = {'00' : [], '01' : [cirq.CNOT(q1, q2)], '10' : [cirq.CNOT(q0, q2)], 
           '11' : [cirq.CNOT(q0, q2), cirq.CNOT(q1, q2)]}

# Línea del duende
a = '00'

def thecircuit(oracle):
    yield cirq.X(q2)
    yield cirq.H(q0), cirq.H(q1), cirq.H(q2)
    yield oracle
    yield cirq.H(q0), cirq.H(q1)
    yield cirq.measure(q0, q1)

# Imprimir el circuito
print('Circuito para cuando el duende elije {}...'.format(a))
print(cirq.Circuit(thecircuit(oracles[a])), end="\n\n")

# Inicializar el simulador
simulator = cirq.Simulator()

# Ejecutar la simulación
result = simulator.run(cirq.Circuit(thecircuit(oracles[a])), repetitions=10)
print(result)