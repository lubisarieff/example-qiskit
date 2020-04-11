## HOW TO USE ? 
Before you run test_full_adder.py, you must install 
* [Python](https://www.python.org/) >= 3.5 (this is required QISKIT)
* [QISKIT] (https://qiskit.org/) >=  0.17.0 (I'm using qiskit 0.17.0 and I recomended using 0.17.0 or higher)

## USAGE
```
python test_full_adder.py
```

## EXAMPLE
![Example](/full-adder/img/example-test-full-adder.png)

If you use IBM Quantum Computing Service, you must add API TOKEN in FullAdder(firstNumber,secondNumber, APITOKEN)\
Get API token from https://quantum-computing.ibm.com/account and copy your token \
Example (Edit test_full_adder.py): 
```
add = FullAdder(firstNumber, secondNumber, YOUR_API_TOKEN)
```

Default provider for IBM Quantum Computing Service is "ibm_qasm_simulator", you can also custom your backend \
Example Change backend (Edit test_full_adder.py):
```
changeBackend = FullAdder(firstNumber, secondNumber, API=YOUR_API_TOKEN, backend=YOUR_BACK_END)
```

## Author
Arief Muhammad
