# Quantum Challenges

## Qiskit Installation

- It is advised to install Qiskit library properly on your computer before starting the quantum challenge
- Here is the recommended installation procedure using Conda package manager, following the [official installation](https://qiskit.org/documentation/stable/0.39/getting_started.html). In summary, you need to do the following:
1. [Install Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
2. [Install Qiskit](https://qiskit.org/documentation/stable/0.39/getting_started.html) in the created virtual environment.
3. [Install Jupyter Lab](https://jupyter.org/install) via Pip.   
4. Run Jupyter Lab inside the created conda environment.
```bash
conda activate (your-env-name)
jupyter lab
```
5. Additional packages such as [Numpy](https://numpy.org/install/) may also need to be installed with either Conda or Pip.   
6. Open a Jupyter Notebook and run "import qiskit". If it is successful, then you successfully installed Qiskit.  

- It is also possible to run the repository without installing it locally using [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wyqian1027/Qiskit-Fall-Fest-USC-2022/HEAD?urlpath=%2Ftree%2F), but it is extremelly not recommended as the changes that you make will not be saved automatically

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
```
- Please submit your solution notebook by sending it to meijian.li@usc.es with the title **"Qiskit-Fall-Fest-USC-2022 Challenge Submission (First name, Last name)"**. We recommend that you use the same email as for the registration.

## After the Quantum Challenge

- We will discuss the quantum problems during the Discussion period, and the solution will appear on Github shortly after the event.
- The submitted notebook will be graded by (1) Correctness (2) Submission time.
- The top scores will be contacted by us and the IBM Quantum team will send you an online Winner's Form to enter your mailing address for the swag pack.
