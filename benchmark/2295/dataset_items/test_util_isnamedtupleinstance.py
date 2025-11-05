import unittest
from collections import namedtuple
import re
import inspect
import builtins
import util

def getattr_side_effect(obj, attr, defaults=None):
    if attr == '_fields':
        return (1, 2)
    else:
        return getattr(obj, attr)

 
class TestIsnamedtupleinstance(unittest.TestCase):

    def test_is_named_tuple_instance(self):
        # Create a named tuple type
        Point = namedtuple('Point', ['x', 'y'])

        # Create an instance of the named tuple
        p = Point(1, 2)

        # Test if the instance is recognized as a named tuple
        self.assertTrue(util.isnamedtupleinstance(p))

    def test_is_not_named_tuple_instance(self):
        # Test with a regular tuple
        t = (1, 2)
        self.assertFalse(util.isnamedtupleinstance(t))

        # Test with a dictionary
        d = {'x': 1, 'y': 2}
        self.assertFalse(util.isnamedtupleinstance(d))

        # Test with a list
        l = [1, 2]
        self.assertFalse(util.isnamedtupleinstance(l))

        # Test with an integer
        i = 1
        self.assertFalse(util.isnamedtupleinstance(i))


    def test_named_tuple_with_non_string_fields(self):
        # Test if the instance with non-string fields is recognized as not a named tuple
        
        # Create a named tuple type with non-string field names
        NonStringFields = namedtuple('NonStringFields', ['x', 'y'] )
        nsf = NonStringFields(1, 2)
        
        # Directly modifying the _fields attribute to contain non-string fields (for testing purposes)
        
        # AttributeError: 'NonStringFields' object attribute '_fields' is read-only
        # nsf._fields = (1, 2)
        
        # so better way is that:
        get_attr = getattr
        try:
            builtins.getattr = getattr_side_effect
            self.assertFalse(util.isnamedtupleinstance(nsf))
        finally:
            builtins.getattr = get_attr

    
    def test_instance_estimation_logic_change(self):
        NonStringFields = namedtuple('NonStringFields', ['x', 'y'])
        nsf = NonStringFields(1, 2)
        self.assertTrue(nsf.x == 1)
        is_instance = builtins.isinstance
        get_attr = getattr
        get_type = builtins.type
        
        def isinstance_side_effect(obj, cls):
            if cls == str:
                return True
            else:
                return is_instance(obj, cls)

        try:
            builtins.isinstance = isinstance_side_effect
            builtins.getattr = getattr_side_effect
            self.assertTrue(util.isnamedtupleinstance(nsf))
            builtins.isinstance = is_instance
            builtins.type = lambda x: x in (1, 2) and str or get_type(x)
            self.assertFalse(util.isnamedtupleinstance(nsf))
        finally:
            builtins.getattr = get_attr
            builtins.isinstance = is_instance
            builtins.type = get_type
        

if __name__ == '__main__':
    unittest.main()
