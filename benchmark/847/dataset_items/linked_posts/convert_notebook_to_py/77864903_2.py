import json

class NotebookModuleBuilder():
    """ Class helps you extract code cells from ipynb-files by using tags """
    
    @staticmethod
    def _read_json(path: str) -> dict:
        """ Reads a json-file and returns a dictionary
            
        Args:
            path: Path to jupyter notebook (.ipynb)
            
        Returns:
            dictionary representation of notebook
        """
        file = open(path, mode= "r", encoding= "utf-8")
        myfile = file.read()
        myjson = json.loads(myfile)
        file.close()
        return myjson

    @staticmethod
    def _get_code_cells(dictionary: dict) -> list:
        """ Finds cells of ipynb with code
        
        Args:
            dictionary: Dictionary from importing a ipynb notebook
            
        Returns:
            List of code cells
        """
        code_cells = [cell for cell in dictionary['cells'] if cell['cell_type']=='code']
        return code_cells

    @staticmethod
    def _get_labeled_cells(code_cells: dict, label="###EXPORT###") -> dict:
        """ Gets cells with the specified label
        
        Args:
            code_cells: Dictionary with code cells
            
        Returns:
            Dictionary with labeled cells
        """
        label = label + "\n"
        sourced_cells = [cell for cell in code_cells if len(cell['source']) > 0]
        labeled_cells = [cell['source'] for cell in sourced_cells if cell['source'][0]==label]
        return labeled_cells

    @staticmethod
    def _write_to_file(labeled_cells: dict, output_file: str) -> None:
        """ Writes the labeled cells to a file
        
        Args:
            labeled_cells: Dictionary with cells that should be written to a file
        """
        flattened_lists = '\n\n'.join([''.join(labeled_cell[1:]) for labeled_cell in labeled_cells])
        file = open(output_file, 'w')
        file.write(flattened_lists)
        file.close()
    
    def ipynb_to_file(self, ipynb_path: str, py_path: str, label: str = '###EXTRACT###') -> None:
        """ Writes cells labeled with ###EXTRACT### in ipynb into a py-file
        
        Args:
            label: Lable that in first line of a cell to match
            ipynb_path: Input path to ipynb-notebook
            py_path: Output path to py-file
        """
        json_file = self._read_json(ipynb_path)
        code_cells = self._get_code_cells(json_file)
        labeled_cells = self._get_labeled_cells(code_cells,label)
        self._write_to_file(labeled_cells, py_path)
