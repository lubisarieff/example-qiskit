"""
Author : Arief Muhammad Lubis
Created on 11 Apr 2020
Code for adder two number using quantum computing
"""
#import libarary qiskit
from qiskit import(
    QuantumRegister,
    ClassicalRegister,
    QuantumCircuit,
    execute,
    Aer,
    IBMQ
)
from qiskit.tools.monitor import job_monitor

class FullAdder:
    def __init__(self, firstNumber, secondNumber, API=None):
        self._firstNumber = self._int_to_binary(int(firstNumber))
        self._secondNumber = self._int_to_binary(int(secondNumber))
        self._quantum_circuit(API)

    #Convert int number to binary
    def _int_to_binary(self, value, type=int):
        try:
            return format(type(value), 'b')
        except ValueError:
            print(value + " Not valid integer, Please try again")

    #Create quantum circuit
    def _quantum_circuit(self, API):
        number1 = len(self._firstNumber)
        number2 = len(self._secondNumber)
        if (number1 >= number2):
            n = number1
        else:
            n = number2

        self._q1 = QuantumRegister(n, 'q1') # first number
        self._q2 = QuantumRegister(n+1, 'q2') #second number
        self._carry = QuantumRegister(n, 'carry') #carry bits
        self._c = ClassicalRegister(n+1, 'classical')
        self._qc = QuantumCircuit(self._q1, self._q2, self._carry, self._c)
        
        #Setting up the registers using the values inputted
        self._setting_up_register(number1, number2) 
        #Implementing a carry gate that is applied on all (c[i], a[i], b[i]) #with output fed to c[i+1]
        self._carry_gate(n)
        #This is done to ensure the sum gates are fed with the correct input bit states
        self._sum_gates(n)
        #execute quantum circuit
        self._execute(API)

    #Setting up the registers using the values inputted
    def _setting_up_register(self, number1, number2):
        for i in range(number1):
            if self._firstNumber[i] == "1":
                self._qc.x(self._q1[number1 - (i+1)])

        for i in range(number2):
            if self._secondNumber[i] == "1":
                self._qc.x(self._q2[number2 - (i+1)]) #Flip the qubit from 0 to 1

    #Implementing a carry gate that is applied on all (c[i], a[i], b[i]) #with output fed to c[i+1]
    def _carry_gate(self, n) :
        for i in range(n-1):
            self._qc.ccx(self._q1[i], self._q2[i], self._carry[i+1])
            self._qc.cx(self._q1[i], self._q2[i])
            self._qc.ccx(self._carry[i], self._q2[i], self._carry[i+1])

        #For the last iteration of the carry gate, instead of feeding the #result to c[n], we use b[n], which is why c has only n bits, with #c[n-1] being the last carry bit
        self._qc.ccx(self._q1[n-1], self._q2[n-1], self._q2[n])
        self._qc.cx(self._q1[n-1], self._q2[n-1])
        self._qc.ccx(self._carry[n-1], self._q2[n-1], self._q2[n])
        #Reversing the gate operation performed on b[n-1]
        self._qc.cx(self._carry[n-1], self._q2[n-1])
    
    #Reversing the gate operations performed during the carry gate implementations
    #This is done to ensure the sum gates are fed with the correct input bit states
    def _sum_gates(self, n):
        for i in range(n-1):
                self._qc.ccx(self._carry[(n-2)-i], self._q2[(n-2)-i], self._carry[(n-1)-i])
                self._qc.cx(self._q1[(n-2)-i], self._q2[(n-2)-i]) 
                self._qc.ccx(self._q1[(n-2)-i], self._q2[(n-2)-i], self._carry[(n-1)-i])
                 #These two operations act as a sum gate; if a control bit is at                
                 #the 1> state then the target bit b[(n-2)-i] is flipped
                self._qc.cx(self._carry[(n-2)-i], self._q2[(n-2)-i]) 
                self._qc.cx(self._q1[(n-2)-i], self._q2[(n-2)-i]) 
        
        for i in range(n+1):
            self._qc.measure(self._q2[i], self._c[i])
                
    def _execute(self, API):
        if API == None:
            backend = Aer.get_backend('qasm_simulator')
            count = execute(self._qc, backend, shots=1).result().get_counts(self._qc)
            print("Measured : ", count)
            nilai = list(count.keys())[list(count.values()).index(1)]
            measured_int = int(nilai,2)
            print("Result = %i" % measured_int)
        else:
            provider = IBMQ.enable_account(API)
            backend = provider.get_backend('ibmq_qasm_simulator')
            job_exp = execute(self._qc, backend = backend, shots=1)
            job_monitor(job_exp)
            result = job_exp.result()
            count = result.get_counts(self._qc)
            print("Measured : ", count)
            nilai = list(count.keys())[list(count.values()).index(1)]
            measured_int = int(nilai,2)
            print("Result = %i" % measured_int)
        

    @property
    def first_number(self):
        return self._firstNumber

    @property
    def second_number(self):
        return self._secondNumber

    @property
    def first_quantum_register(self):
        return self._q1
    
    @property
    def second_quantum_register(self):
        return self._q2
    
    @property
    def carry_quantum_register(self):
        return self._carry

    @property
    def classical_register(self):
        return self._c

    @property
    def quantum_circuit(self):
        return self._qc

    def __str__(self):
        return str(self._qc)