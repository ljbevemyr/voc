import unittest

from unittest import expectedFailure
from ..utils import TranspileTestCase


class MathModuleTests(TranspileTestCase):

    @expectedFailure
    def test_sqrt_no_number(self):
        self.assertCodeExecution("""
            import math
            print(math.sqrt("no number"))
            """)

    @expectedFailure
    def test_sqrt_negatives(self):
        self.assertCodeExecution("""
            import math
            print(math.sqrt(-1.0))
            """)
    
    def test_sqrt_int(self):
        self.assertCodeExecution("""
            import math
            print(math.sqrt(4))
            """)

    def test_sqrt_floats(self):
        self.assertCodeExecution("""
            import math
            print(math.sqrt(4.2))
            """)
    
    def test_sqrt_bool_true(self):
        self.assertCodeExecution("""
            import math
            print(math.sqrt(True))
            """)
    
    def test_sqrt_bool_false(self):
        self.assertCodeExecution("""
            import math
            print(math.sqrt(False))
            """)
    
    def test_sqrt_zero(self):
        self.assertCodeExecution("""
            import math
            print(math.sqrt(0))
            """)