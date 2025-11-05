from qiskit.visualization import array_to_latex
import numpy as np

x = np.zeros(100).reshape(10,10)


# Max rows and cols = 24
array_to_latex(array=x, prefix='Output = ', max_size=(10,10)) # If max_size not set then matrix will have ellipses
# print latex source only: Source=True
latex_source = array_to_latex(array=x, source=True, max_size=(10,10))

# If you are using Jupyter Notebook: 
from IPython.display import display, Markdown
display(Markdown(latex_source))
