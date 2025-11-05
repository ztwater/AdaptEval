#!/usr/bin/python


# A short routine to convert a Jupyter Notebook to a Python file

import json

def ipynb_to_py(input_ipynb_file,output_py_file=None):
    """
    Generate a Python script (.py) that includes all source code from the input Jupyter notebook (.ipynb).
    
    The user can input a Jupyter Notebook file from the current working directory or from a path.
    
    If the name for output Python file is not specified, 
    the output file name will copy the file name of the input Jupyter Notebook, 
    but the file exention will be changed from ".ipynb" chanegd to ".py".
    And the output Python file will be saved at the same directory of the input Jupyter Notebook.
    For example:
    ipynb_to_py("test-jupyternotebook.ipynb")
    ipynb_to_py("./test-input-dir/test-jupyternotebook.ipynb")
    
    The user can also specify an output file name that ends with ".py".
    If the output file name is provided, but no path to output file is added, 
    the file will be saved at the current working directory.
    For example:
    ipynb_to_py("test-jupyternotebook.ipynb","test1.py")
    ipynb_to_py("./test-input-dir/test-jupyternotebook.ipynb","test2.py")
        
    The user can save out the file at a target directory by adding a path to the output file.
    For example: 
    ipynb_to_py("test-jupyternotebook.ipynb","./test-outputdir/test3.py")
    ipynb_to_py("./test-input-dir/test-jupyternotebook.ipynb","./test-output-dir/test4.py")
    
    This function does not edit or delete the original input Jupyter Notebook file.
    
    Args:
    -----
        input_ipynb_file: The file name string for the Jupyter Notebook (ends with ".ipynb")
        output_py_file (optional): The file name for Python file to be created (ends with ".py"). 
    
    Returns:
    --------
        A Python file containing all source code in the Jupyter Notebook.
        
    Example usages:
    ---------------
        ipynb_to_py("test-jupyternotebook.ipynb")
        ipynb_to_py("./test-input-dir/test-jupyternotebook.ipynb")
        ipynb_to_py("test-jupyternotebook.ipynb","test1.py")
        ipynb_to_py("test-jupyternotebook.ipynb","./test-outputdir/test2.py")
        ipynb_to_py("test-jupyternotebook.ipynb","./test-outputdir/test3.py")
        ipynb_to_py("./test-input-dir/test-jupyternotebook.ipynb","./test-output-dir/test4.py")
             
    """
    # Check if the input file is a Jupyter Notebook
    if input_ipynb_file.endswith(".ipynb"):
        
        # Open the input Jupyter Notebook file
        notebook = open(input_ipynb_file)
        
        # Read its content in the json format
        notebook_content = json.load(notebook)

        # Only extract the source code snippet from each cell in the input Jupyter Notebook
        source_code_snippets = [cell['source'] for cell in notebook_content['cells']]
        
        # If the name for output Python file is not specified,
        # The name of input Jupyter Notebook will be used after changing ".ipynb" to ".py".
        if output_py_file == None:
            output_py_file = input_ipynb_file.split('.ipynb')[0]+".py"
        else:
            pass

        # Create a Python script to save out all the extracted source code snippets
        output_file = open(output_py_file,'w')

        # Print out each line in each source code snippet to the output file
        for snippet in source_code_snippets:
            for line in snippet:
                # Use end='' to avoid creating unwanted gaps between lines
                print(line,end = '',file = output_file)
            # At end of each snippet, move to the next line before printing the next one
            print('',sep = '\n',file=output_file)

        # Close the output file
        output_file.close()
        print("The path to output file:",output_py_file)
        
    else:
        print("The input file must be a Jupyter Notebook (in .ipynb format)!")
        
def main():
    pass

if __name__ == "__main__":
    main()
