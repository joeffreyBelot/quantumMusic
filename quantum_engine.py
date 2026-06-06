from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

import random


def generate_quantum_measurements(
    qubits=4,
    depth=6,
    shots=32
):

    qc = QuantumCircuit(qubits, qubits)

    for _ in range(depth):

        gate = random.choice(
            ["h", "x", "ry", "cx"]
        )

        if gate == "h":

            q = random.randint(0, qubits - 1)
            qc.h(q)

        elif gate == "x":

            q = random.randint(0, qubits - 1)
            qc.x(q)

        elif gate == "ry":

            q = random.randint(0, qubits - 1)
            angle = random.uniform(0, 3.14)
            qc.ry(angle, q)

        elif gate == "cx" and qubits > 1:

            c = random.randint(0, qubits - 1)

            t = random.randint(0, qubits - 1)

            while t == c:
                t = random.randint(0, qubits - 1)

            qc.cx(c, t)

    qc.measure(range(qubits), range(qubits))

    simulator = AerSimulator()

    result = simulator.run(
        qc,
        shots=shots
    ).result()

    counts = result.get_counts()

    sequence = []

    for state, count in counts.items():
        sequence.extend([state] * count)

    random.shuffle(sequence)

    return sequence
