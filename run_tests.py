import unittest

test_cases = ('TestItemModel')

def load_tests(pattern):
  suite = unittest.TestSuite()
  loader = unittest.TestLoader()
  this_dir = 'tests'
  package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
  suite.addTests(package_tests)
  
  return suite

unittest.TextTestRunner(verbosity=2).run(load_tests('test*.py'))
