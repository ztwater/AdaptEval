# Importing Custom Module
from ipynb_exporter import NotebookModuleBuilder as nmb

# Exporting labeled cells
nmb().ipynb_to_file(ipynb_path="mynotebook.ipynb",
                    label="###EXTRACT###",
                    py_path="mynotebookcells.py")
