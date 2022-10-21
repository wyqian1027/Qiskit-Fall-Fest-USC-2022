import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_multivector, array_to_latex

##### DO NOT CHANGE THIS CODE #######
# This is used to help you check if your exercises are correct and allow you to keep track
# of your progress. Modifying this can make the system fail.

ex_correct_dict = {'ex1': False, 'ex2': False, 'ex3': False, 'ex4': False, 'ex5': False, 
                  'ex6': False, 'ex7': False}

def language(x):
    global ESP
    ESP = x
    
    
def correction_announcer(x):
    if ESP:
        if x:
            print('¡La respuesta es correcta! :) \n¡Te llevas un MAPI!')
        else:
            print('La respuesta es incorrecta :(')
    else:
        if x:
            print('Your answer is correct! :)')
        else:
            print('Your answer is incorrect :(')
        
        
def ex1_grader(qc):
    from qiskit.quantum_info import Statevector
    
    state_vector_solution = Statevector(qc)
    state_vector_real = Statevector((1./np.sqrt(2))*np.array([1., 0., 0., -1.]))
    
    if state_vector_solution==state_vector_real or state_vector_solution==-state_vector_real:
        ex_correct_dict['ex1'] = True
        correction_announcer(True)
        
    else:
        correction_announcer(False)
        
def ex2_grader(qc):
    from qiskit.quantum_info import Statevector
    
    state_vector_solution = Statevector(qc)
    state_vector_real = Statevector((1./np.sqrt(2))*np.array([0., 1., 1., 0.]))
    
    if state_vector_solution==state_vector_real or state_vector_solution==-state_vector_real:
        ex_correct_dict['ex2'] = True
        correction_announcer(True)
        
    else:
        correction_announcer(False)
        
def ex3_grader(qc):
    from qiskit.quantum_info import Statevector
    
    state_vector_solution = Statevector(qc)
    state_vector_real = Statevector((1./np.sqrt(2))*np.array([0., 1., -1., 0.]))
    if state_vector_solution==state_vector_real or state_vector_solution==-state_vector_real:
        ex_correct_dict['ex3'] = True
        correction_announcer(True)
        
    else:
        correction_announcer(False)
        
def ex4_grader(qc):
    from qiskit.quantum_info import Statevector
    
    state_vector_solution = Statevector(qc)
    state_vector_real = Statevector((1./np.sqrt(2))*np.array([1., 0., 0., 0., 0., 0., 0., 1.]))
    if state_vector_solution==state_vector_real or state_vector_solution==-state_vector_real:
        ex_correct_dict['ex4'] = True
        correction_announcer(True)
        
    else:
        correction_announcer(False)
        
def ex5_grader(qc):
    from qiskit.quantum_info import Statevector
    
    state_vector_solution = Statevector(qc)
    state_vector_real = Statevector((1./2.)*np.array([1., 0., 0., 1., 0., 1., 1., 0.]))
    if state_vector_solution==state_vector_real or state_vector_solution==-state_vector_real:
        ex_correct_dict['ex5'] = True
        correction_announcer(True)
        
    else:
        correction_announcer(False)
        
def ex6_grader(qc):
    from qiskit.quantum_info import Statevector
    
    state_vector_solution = Statevector(qc)
    state_vector_real = Statevector((1./2.)*np.array([0., 1., 1., 0., 1., 0., 0., 1.]))
    if state_vector_solution==state_vector_real or state_vector_solution==-state_vector_real:
        ex_correct_dict['ex6'] = True
        correction_announcer(True)
        
    else:
        correction_announcer(False)
        
def ex7_grader(fun):
    from qiskit.quantum_info import Statevector
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    fun(qc, 0, 0)
    backend_shots = Aer.get_backend('qasm_simulator', shots = 1024)
    result = execute(qc, backend_shots).result().get_counts()
    if result['0'] == 1024:
        qc = QuantumCircuit(1, 1)
        qc.x(0)
        qc.h(0)
        fun(qc, 0, 0)
        result = execute(qc, backend_shots).result().get_counts()
        
        if result['1'] == 1024:
            ex_correct_dict['ex7'] = True
            correction_announcer(True)

        else:
            correction_announcer(False)