# test runner
import sys
import unittest

suite = unittest.TestLoader().discover('test')
unittest.TextTestRunner(verbosity=2).run(suite)