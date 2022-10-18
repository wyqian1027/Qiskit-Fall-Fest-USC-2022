# Quantum Challenges

## Qiskit Installation

- It is advised to install Qiskit library properly on your computer before starting the quantum challenge
- Here is the recommended installation procedure using Conda package manager. Alternatively you can also install Qiskit directly on your operating system via Pip.
1. [Install Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) (if you are familiar with Conda)
2. [Install Qiskit](https://qiskit.org/documentation/getting_started.html) (in the Conda environment if you installed Conda)
3. [Install Jupyter Lab](https://jupyter.org/install) via Pip.   
4. Activate your environment with Conda and run Jupyter Lab if you installed Conda
```bash
conda activate (your-env-name)
jupyter lab
```
4. Run Jupyter Lab directly if you did not install Conda
```bash
jupyter lab
```
5. Additional packages such as Numpy will also need to be installed with either Conda or Pip.

## During Quantum Challenge

- The quantum challenge questions will be available to download at the start of the quantum challenge.
- You will work through the provided Jupyter notebook by providing your solutions to each problem.
- You are allowed to ask installation related questions during the quantum challenge. Local mentors will be around to help you with the installation.
- You are asked to work on the problem on your own. 

## Submission
- Please include a Qiskit version summary at the end of your submitted Jupyter notebook.
```python
import qiskit.tools.jupyter
%qiskit_version_table
%qiskit_copyright
```
- Please submit your solution notebook by sending it to meijian.li@usc.es with the title "Qiskit-Fall-Fest-USC-2022 Challenge". We recommend that you use the same email as for the registration.

## After the Quantum Challenge

- We will discuss the quantum problems during the Discussion period, and the solution will appear on Github shortly after the event.
- The submitted notebook will be graded by (1) Correctness (2) Submission time.
- The top scores will be contacted by us and the IBM Quantum team will send you an online Winner's Form to enter your mailing address for the swag pack.
