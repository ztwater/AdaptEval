test::SOURCE_FILE:  <root>/test01/test.py
import : <root>/test01/testlib.py as testlib -> []
1 testlib::SOURCE_FILE:  <root>/test01/testlib.py
import : <root>/test01/std1/testlib.std1.py as testlib_std1 -> ['testlib']
import : <root>/test01/std1/../std2/testlib.std2.py as testlib_std2 -> ['testlib', 'testlib_std1']
testlib.std2::SOURCE_FILE:  <root>/test01/std1/../std2/testlib.std2.py
2 testlib::SOURCE_FILE:  <root>/test01/testlib.py
import : <root>/test01/std3/testlib.std3.py as testlib.std3 -> ['testlib']
testlib.std3::SOURCE_FILE:  <root>/test01/std3/testlib.std3.py
3 testlib::SOURCE_FILE:  <root>/test01/testlib.py
dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'os', 'sys', 'inspect', 'copy', 'SOURCE_FILE', 'SOURCE_DIR', 'TackleGlobalImportModuleState', 'tkl_membercopy', 'tkl_merge_module', 'tkl_get_parent_imported_module_state', 'tkl_declare_global', 'tkl_import_module', 'TackleSourceModuleState', 'tkl_source_module', 'TackleLocalImportModuleState', 'testlib'])
base_test
std1_test
std2_test
std3_test
import : <root>/test01/testlib.py as . -> []
1 testlib::SOURCE_FILE:  <root>/test01/testlib.py
import : <root>/test01/std1/testlib.std1.py as testlib_std1 -> ['testlib']
import : <root>/test01/std1/../std2/testlib.std2.py as testlib_std2 -> ['testlib', 'testlib_std1']
testlib.std2::SOURCE_FILE:  <root>/test01/std1/../std2/testlib.std2.py
2 testlib::SOURCE_FILE:  <root>/test01/testlib.py
import : <root>/test01/std3/testlib.std3.py as testlib.std3 -> ['testlib']
testlib.std3::SOURCE_FILE:  <root>/test01/std3/testlib.std3.py
3 testlib::SOURCE_FILE:  <root>/test01/testlib.py
dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'os', 'sys', 'inspect', 'copy', 'SOURCE_FILE', 'SOURCE_DIR', 'TackleGlobalImportModuleState', 'tkl_membercopy', 'tkl_merge_module', 'tkl_get_parent_imported_module_state', 'tkl_declare_global', 'tkl_import_module', 'TackleSourceModuleState', 'tkl_source_module', 'TackleLocalImportModuleState', 'testlib', 'testlib_std1', 'testlib.std3', 'base_test'])
base_test
std1_test
std2_test
std3_test
