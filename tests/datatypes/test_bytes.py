from unittest import expectedFailure
from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class UnaryBytesOperationTests(UnaryOperationTestCase, TranspileTestCase):
    x = 'b"This is a string of bytes"'

UnaryBytesOperationTests.test_unary_positive = expectedFailure(UnaryBytesOperationTests.test_unary_positive)
UnaryBytesOperationTests.test_unary_negative = expectedFailure(UnaryBytesOperationTests.test_unary_negative)
UnaryBytesOperationTests.test_unary_not = expectedFailure(UnaryBytesOperationTests.test_unary_not)
UnaryBytesOperationTests.test_unary_invert = expectedFailure(UnaryBytesOperationTests.test_unary_invert)


class BinaryBytesOperationTests(BinaryOperationTestCase, TranspileTestCase):
    x = 'b"This is a string of bytes"'

BinaryBytesOperationTests.test_add_bool_true = expectedFailure(BinaryBytesOperationTests.test_add_bool_true)
BinaryBytesOperationTests.test_subtract_bool_true = expectedFailure(BinaryBytesOperationTests.test_subtract_bool_true)
BinaryBytesOperationTests.test_multiply_bool_true = expectedFailure(BinaryBytesOperationTests.test_multiply_bool_true)
BinaryBytesOperationTests.test_floor_divide_bool_true = expectedFailure(BinaryBytesOperationTests.test_floor_divide_bool_true)
BinaryBytesOperationTests.test_true_divide_bool_true = expectedFailure(BinaryBytesOperationTests.test_true_divide_bool_true)
BinaryBytesOperationTests.test_modulo_bool_true = expectedFailure(BinaryBytesOperationTests.test_modulo_bool_true)
BinaryBytesOperationTests.test_power_bool_true = expectedFailure(BinaryBytesOperationTests.test_power_bool_true)
BinaryBytesOperationTests.test_subscr_bool_true = expectedFailure(BinaryBytesOperationTests.test_subscr_bool_true)
BinaryBytesOperationTests.test_lshift_bool_true = expectedFailure(BinaryBytesOperationTests.test_lshift_bool_true)
BinaryBytesOperationTests.test_rshift_bool_true = expectedFailure(BinaryBytesOperationTests.test_rshift_bool_true)
BinaryBytesOperationTests.test_and_bool_true = expectedFailure(BinaryBytesOperationTests.test_and_bool_true)
BinaryBytesOperationTests.test_xor_bool_true = expectedFailure(BinaryBytesOperationTests.test_xor_bool_true)
BinaryBytesOperationTests.test_or_bool_true = expectedFailure(BinaryBytesOperationTests.test_or_bool_true)

BinaryBytesOperationTests.test_add_bool_false = expectedFailure(BinaryBytesOperationTests.test_add_bool_false)
BinaryBytesOperationTests.test_subtract_bool_false = expectedFailure(BinaryBytesOperationTests.test_subtract_bool_false)
BinaryBytesOperationTests.test_multiply_bool_false = expectedFailure(BinaryBytesOperationTests.test_multiply_bool_false)
BinaryBytesOperationTests.test_floor_divide_bool_false = expectedFailure(BinaryBytesOperationTests.test_floor_divide_bool_false)
BinaryBytesOperationTests.test_true_divide_bool_false = expectedFailure(BinaryBytesOperationTests.test_true_divide_bool_false)
BinaryBytesOperationTests.test_modulo_bool_false = expectedFailure(BinaryBytesOperationTests.test_modulo_bool_false)
BinaryBytesOperationTests.test_power_bool_false = expectedFailure(BinaryBytesOperationTests.test_power_bool_false)
BinaryBytesOperationTests.test_subscr_bool_false = expectedFailure(BinaryBytesOperationTests.test_subscr_bool_false)
BinaryBytesOperationTests.test_lshift_bool_false = expectedFailure(BinaryBytesOperationTests.test_lshift_bool_false)
BinaryBytesOperationTests.test_rshift_bool_false = expectedFailure(BinaryBytesOperationTests.test_rshift_bool_false)
BinaryBytesOperationTests.test_and_bool_false = expectedFailure(BinaryBytesOperationTests.test_and_bool_false)
BinaryBytesOperationTests.test_xor_bool_false = expectedFailure(BinaryBytesOperationTests.test_xor_bool_false)
BinaryBytesOperationTests.test_or_bool_false = expectedFailure(BinaryBytesOperationTests.test_or_bool_false)

# BinaryBytesOperationTests.test_add_bytearray = expectedFailure(BinaryBytesOperationTests.test_add_bytearray)
# BinaryBytesOperationTests.test_subtract_bytearray = expectedFailure(BinaryBytesOperationTests.test_subtract_bytearray)
# BinaryBytesOperationTests.test_multiply_bytearray = expectedFailure(BinaryBytesOperationTests.test_multiply_bytearray)
# BinaryBytesOperationTests.test_floor_divide_bytearray = expectedFailure(BinaryBytesOperationTests.test_floor_divide_bytearray)
# BinaryBytesOperationTests.test_true_divide_bytearray = expectedFailure(BinaryBytesOperationTests.test_true_divide_bytearray)
# BinaryBytesOperationTests.test_modulo_bytearray = expectedFailure(BinaryBytesOperationTests.test_modulo_bytearray)
# BinaryBytesOperationTests.test_power_bytearray = expectedFailure(BinaryBytesOperationTests.test_power_bytearray)
# BinaryBytesOperationTests.test_subscr_bytearray = expectedFailure(BinaryBytesOperationTests.test_subscr_bytearray)
# BinaryBytesOperationTests.test_lshift_bytearray = expectedFailure(BinaryBytesOperationTests.test_lshift_bytearray)
# BinaryBytesOperationTests.test_rshift_bytearray = expectedFailure(BinaryBytesOperationTests.test_rshift_bytearray)
# BinaryBytesOperationTests.test_and_bytearray = expectedFailure(BinaryBytesOperationTests.test_and_bytearray)
# BinaryBytesOperationTests.test_xor_bytearray = expectedFailure(BinaryBytesOperationTests.test_xor_bytearray)
# BinaryBytesOperationTests.test_or_bytearray = expectedFailure(BinaryBytesOperationTests.test_or_bytearray)

BinaryBytesOperationTests.test_add_bytes = expectedFailure(BinaryBytesOperationTests.test_add_bytes)
BinaryBytesOperationTests.test_subtract_bytes = expectedFailure(BinaryBytesOperationTests.test_subtract_bytes)
BinaryBytesOperationTests.test_multiply_bytes = expectedFailure(BinaryBytesOperationTests.test_multiply_bytes)
BinaryBytesOperationTests.test_floor_divide_bytes = expectedFailure(BinaryBytesOperationTests.test_floor_divide_bytes)
BinaryBytesOperationTests.test_true_divide_bytes = expectedFailure(BinaryBytesOperationTests.test_true_divide_bytes)
BinaryBytesOperationTests.test_modulo_bytes = expectedFailure(BinaryBytesOperationTests.test_modulo_bytes)
BinaryBytesOperationTests.test_power_bytes = expectedFailure(BinaryBytesOperationTests.test_power_bytes)
BinaryBytesOperationTests.test_subscr_bytes = expectedFailure(BinaryBytesOperationTests.test_subscr_bytes)
BinaryBytesOperationTests.test_lshift_bytes = expectedFailure(BinaryBytesOperationTests.test_lshift_bytes)
BinaryBytesOperationTests.test_rshift_bytes = expectedFailure(BinaryBytesOperationTests.test_rshift_bytes)
BinaryBytesOperationTests.test_and_bytes = expectedFailure(BinaryBytesOperationTests.test_and_bytes)
BinaryBytesOperationTests.test_xor_bytes = expectedFailure(BinaryBytesOperationTests.test_xor_bytes)
BinaryBytesOperationTests.test_or_bytes = expectedFailure(BinaryBytesOperationTests.test_or_bytes)

# BinaryBytesOperationTests.test_add_class = expectedFailure(BinaryBytesOperationTests.test_add_class)
# BinaryBytesOperationTests.test_subtract_class = expectedFailure(BinaryBytesOperationTests.test_subtract_class)
# BinaryBytesOperationTests.test_multiply_class = expectedFailure(BinaryBytesOperationTests.test_multiply_class)
# BinaryBytesOperationTests.test_floor_divide_class = expectedFailure(BinaryBytesOperationTests.test_floor_divide_class)
# BinaryBytesOperationTests.test_true_divide_class = expectedFailure(BinaryBytesOperationTests.test_true_divide_class)
# BinaryBytesOperationTests.test_modulo_class = expectedFailure(BinaryBytesOperationTests.test_modulo_class)
# BinaryBytesOperationTests.test_power_class = expectedFailure(BinaryBytesOperationTests.test_power_class)
# BinaryBytesOperationTests.test_subscr_class = expectedFailure(BinaryBytesOperationTests.test_subscr_class)
# BinaryBytesOperationTests.test_lshift_class = expectedFailure(BinaryBytesOperationTests.test_lshift_class)
# BinaryBytesOperationTests.test_rshift_class = expectedFailure(BinaryBytesOperationTests.test_rshift_class)
# BinaryBytesOperationTests.test_and_class = expectedFailure(BinaryBytesOperationTests.test_and_class)
# BinaryBytesOperationTests.test_xor_class = expectedFailure(BinaryBytesOperationTests.test_xor_class)
# BinaryBytesOperationTests.test_or_class = expectedFailure(BinaryBytesOperationTests.test_or_class)

# BinaryBytesOperationTests.test_add_complex = expectedFailure(BinaryBytesOperationTests.test_add_complex)
# BinaryBytesOperationTests.test_subtract_complex = expectedFailure(BinaryBytesOperationTests.test_subtract_complex)
# BinaryBytesOperationTests.test_multiply_complex = expectedFailure(BinaryBytesOperationTests.test_multiply_complex)
# BinaryBytesOperationTests.test_floor_divide_complex = expectedFailure(BinaryBytesOperationTests.test_floor_divide_complex)
# BinaryBytesOperationTests.test_true_divide_complex = expectedFailure(BinaryBytesOperationTests.test_true_divide_complex)
# BinaryBytesOperationTests.test_modulo_complex = expectedFailure(BinaryBytesOperationTests.test_modulo_complex)
# BinaryBytesOperationTests.test_power_complex = expectedFailure(BinaryBytesOperationTests.test_power_complex)
# BinaryBytesOperationTests.test_subscr_complex = expectedFailure(BinaryBytesOperationTests.test_subscr_complex)
# BinaryBytesOperationTests.test_lshift_complex = expectedFailure(BinaryBytesOperationTests.test_lshift_complex)
# BinaryBytesOperationTests.test_rshift_complex = expectedFailure(BinaryBytesOperationTests.test_rshift_complex)
# BinaryBytesOperationTests.test_and_complex = expectedFailure(BinaryBytesOperationTests.test_and_complex)
# BinaryBytesOperationTests.test_xor_complex = expectedFailure(BinaryBytesOperationTests.test_xor_complex)
# BinaryBytesOperationTests.test_or_complex = expectedFailure(BinaryBytesOperationTests.test_or_complex)

BinaryBytesOperationTests.test_add_dict = expectedFailure(BinaryBytesOperationTests.test_add_dict)
BinaryBytesOperationTests.test_subtract_dict = expectedFailure(BinaryBytesOperationTests.test_subtract_dict)
BinaryBytesOperationTests.test_multiply_dict = expectedFailure(BinaryBytesOperationTests.test_multiply_dict)
BinaryBytesOperationTests.test_floor_divide_dict = expectedFailure(BinaryBytesOperationTests.test_floor_divide_dict)
BinaryBytesOperationTests.test_true_divide_dict = expectedFailure(BinaryBytesOperationTests.test_true_divide_dict)
BinaryBytesOperationTests.test_modulo_dict = expectedFailure(BinaryBytesOperationTests.test_modulo_dict)
BinaryBytesOperationTests.test_power_dict = expectedFailure(BinaryBytesOperationTests.test_power_dict)
BinaryBytesOperationTests.test_subscr_dict = expectedFailure(BinaryBytesOperationTests.test_subscr_dict)
BinaryBytesOperationTests.test_lshift_dict = expectedFailure(BinaryBytesOperationTests.test_lshift_dict)
BinaryBytesOperationTests.test_rshift_dict = expectedFailure(BinaryBytesOperationTests.test_rshift_dict)
BinaryBytesOperationTests.test_and_dict = expectedFailure(BinaryBytesOperationTests.test_and_dict)
BinaryBytesOperationTests.test_xor_dict = expectedFailure(BinaryBytesOperationTests.test_xor_dict)
BinaryBytesOperationTests.test_or_dict = expectedFailure(BinaryBytesOperationTests.test_or_dict)

BinaryBytesOperationTests.test_add_float = expectedFailure(BinaryBytesOperationTests.test_add_float)
BinaryBytesOperationTests.test_subtract_float = expectedFailure(BinaryBytesOperationTests.test_subtract_float)
BinaryBytesOperationTests.test_multiply_float = expectedFailure(BinaryBytesOperationTests.test_multiply_float)
BinaryBytesOperationTests.test_floor_divide_float = expectedFailure(BinaryBytesOperationTests.test_floor_divide_float)
BinaryBytesOperationTests.test_true_divide_float = expectedFailure(BinaryBytesOperationTests.test_true_divide_float)
BinaryBytesOperationTests.test_modulo_float = expectedFailure(BinaryBytesOperationTests.test_modulo_float)
BinaryBytesOperationTests.test_power_float = expectedFailure(BinaryBytesOperationTests.test_power_float)
BinaryBytesOperationTests.test_subscr_float = expectedFailure(BinaryBytesOperationTests.test_subscr_float)
BinaryBytesOperationTests.test_lshift_float = expectedFailure(BinaryBytesOperationTests.test_lshift_float)
BinaryBytesOperationTests.test_rshift_float = expectedFailure(BinaryBytesOperationTests.test_rshift_float)
BinaryBytesOperationTests.test_and_float = expectedFailure(BinaryBytesOperationTests.test_and_float)
BinaryBytesOperationTests.test_xor_float = expectedFailure(BinaryBytesOperationTests.test_xor_float)
BinaryBytesOperationTests.test_or_float = expectedFailure(BinaryBytesOperationTests.test_or_float)

# BinaryBytesOperationTests.test_add_frozenset = expectedFailure(BinaryBytesOperationTests.test_add_frozenset)
# BinaryBytesOperationTests.test_subtract_frozenset = expectedFailure(BinaryBytesOperationTests.test_subtract_frozenset)
# BinaryBytesOperationTests.test_multiply_frozenset = expectedFailure(BinaryBytesOperationTests.test_multiply_frozenset)
# BinaryBytesOperationTests.test_floor_divide_frozenset = expectedFailure(BinaryBytesOperationTests.test_floor_divide_frozenset)
# BinaryBytesOperationTests.test_true_divide_frozenset = expectedFailure(BinaryBytesOperationTests.test_true_divide_frozenset)
# BinaryBytesOperationTests.test_modulo_frozenset = expectedFailure(BinaryBytesOperationTests.test_modulo_frozenset)
# BinaryBytesOperationTests.test_power_frozenset = expectedFailure(BinaryBytesOperationTests.test_power_frozenset)
# BinaryBytesOperationTests.test_subscr_frozenset = expectedFailure(BinaryBytesOperationTests.test_subscr_frozenset)
# BinaryBytesOperationTests.test_lshift_frozenset = expectedFailure(BinaryBytesOperationTests.test_lshift_frozenset)
# BinaryBytesOperationTests.test_rshift_frozenset = expectedFailure(BinaryBytesOperationTests.test_rshift_frozenset)
# BinaryBytesOperationTests.test_and_frozenset = expectedFailure(BinaryBytesOperationTests.test_and_frozenset)
# BinaryBytesOperationTests.test_xor_frozenset = expectedFailure(BinaryBytesOperationTests.test_xor_frozenset)
# BinaryBytesOperationTests.test_or_frozenset = expectedFailure(BinaryBytesOperationTests.test_or_frozenset)

BinaryBytesOperationTests.test_add_int = expectedFailure(BinaryBytesOperationTests.test_add_int)
BinaryBytesOperationTests.test_subtract_int = expectedFailure(BinaryBytesOperationTests.test_subtract_int)
BinaryBytesOperationTests.test_multiply_int = expectedFailure(BinaryBytesOperationTests.test_multiply_int)
BinaryBytesOperationTests.test_floor_divide_int = expectedFailure(BinaryBytesOperationTests.test_floor_divide_int)
BinaryBytesOperationTests.test_true_divide_int = expectedFailure(BinaryBytesOperationTests.test_true_divide_int)
BinaryBytesOperationTests.test_modulo_int = expectedFailure(BinaryBytesOperationTests.test_modulo_int)
BinaryBytesOperationTests.test_power_int = expectedFailure(BinaryBytesOperationTests.test_power_int)
BinaryBytesOperationTests.test_subscr_int = expectedFailure(BinaryBytesOperationTests.test_subscr_int)
BinaryBytesOperationTests.test_lshift_int = expectedFailure(BinaryBytesOperationTests.test_lshift_int)
BinaryBytesOperationTests.test_rshift_int = expectedFailure(BinaryBytesOperationTests.test_rshift_int)
BinaryBytesOperationTests.test_and_int = expectedFailure(BinaryBytesOperationTests.test_and_int)
BinaryBytesOperationTests.test_xor_int = expectedFailure(BinaryBytesOperationTests.test_xor_int)
BinaryBytesOperationTests.test_or_int = expectedFailure(BinaryBytesOperationTests.test_or_int)

BinaryBytesOperationTests.test_add_list = expectedFailure(BinaryBytesOperationTests.test_add_list)
BinaryBytesOperationTests.test_subtract_list = expectedFailure(BinaryBytesOperationTests.test_subtract_list)
BinaryBytesOperationTests.test_multiply_list = expectedFailure(BinaryBytesOperationTests.test_multiply_list)
BinaryBytesOperationTests.test_floor_divide_list = expectedFailure(BinaryBytesOperationTests.test_floor_divide_list)
BinaryBytesOperationTests.test_true_divide_list = expectedFailure(BinaryBytesOperationTests.test_true_divide_list)
BinaryBytesOperationTests.test_modulo_list = expectedFailure(BinaryBytesOperationTests.test_modulo_list)
BinaryBytesOperationTests.test_power_list = expectedFailure(BinaryBytesOperationTests.test_power_list)
BinaryBytesOperationTests.test_subscr_list = expectedFailure(BinaryBytesOperationTests.test_subscr_list)
BinaryBytesOperationTests.test_lshift_list = expectedFailure(BinaryBytesOperationTests.test_lshift_list)
BinaryBytesOperationTests.test_rshift_list = expectedFailure(BinaryBytesOperationTests.test_rshift_list)
BinaryBytesOperationTests.test_and_list = expectedFailure(BinaryBytesOperationTests.test_and_list)
BinaryBytesOperationTests.test_xor_list = expectedFailure(BinaryBytesOperationTests.test_xor_list)
BinaryBytesOperationTests.test_or_list = expectedFailure(BinaryBytesOperationTests.test_or_list)

BinaryBytesOperationTests.test_add_set = expectedFailure(BinaryBytesOperationTests.test_add_set)
BinaryBytesOperationTests.test_subtract_set = expectedFailure(BinaryBytesOperationTests.test_subtract_set)
BinaryBytesOperationTests.test_multiply_set = expectedFailure(BinaryBytesOperationTests.test_multiply_set)
BinaryBytesOperationTests.test_floor_divide_set = expectedFailure(BinaryBytesOperationTests.test_floor_divide_set)
BinaryBytesOperationTests.test_true_divide_set = expectedFailure(BinaryBytesOperationTests.test_true_divide_set)
BinaryBytesOperationTests.test_modulo_set = expectedFailure(BinaryBytesOperationTests.test_modulo_set)
BinaryBytesOperationTests.test_power_set = expectedFailure(BinaryBytesOperationTests.test_power_set)
BinaryBytesOperationTests.test_subscr_set = expectedFailure(BinaryBytesOperationTests.test_subscr_set)
BinaryBytesOperationTests.test_lshift_set = expectedFailure(BinaryBytesOperationTests.test_lshift_set)
BinaryBytesOperationTests.test_rshift_set = expectedFailure(BinaryBytesOperationTests.test_rshift_set)
BinaryBytesOperationTests.test_and_set = expectedFailure(BinaryBytesOperationTests.test_and_set)
BinaryBytesOperationTests.test_xor_set = expectedFailure(BinaryBytesOperationTests.test_xor_set)
BinaryBytesOperationTests.test_or_set = expectedFailure(BinaryBytesOperationTests.test_or_set)

BinaryBytesOperationTests.test_add_str = expectedFailure(BinaryBytesOperationTests.test_add_str)
BinaryBytesOperationTests.test_subtract_str = expectedFailure(BinaryBytesOperationTests.test_subtract_str)
BinaryBytesOperationTests.test_multiply_str = expectedFailure(BinaryBytesOperationTests.test_multiply_str)
BinaryBytesOperationTests.test_floor_divide_str = expectedFailure(BinaryBytesOperationTests.test_floor_divide_str)
BinaryBytesOperationTests.test_true_divide_str = expectedFailure(BinaryBytesOperationTests.test_true_divide_str)
BinaryBytesOperationTests.test_modulo_str = expectedFailure(BinaryBytesOperationTests.test_modulo_str)
BinaryBytesOperationTests.test_power_str = expectedFailure(BinaryBytesOperationTests.test_power_str)
BinaryBytesOperationTests.test_subscr_str = expectedFailure(BinaryBytesOperationTests.test_subscr_str)
BinaryBytesOperationTests.test_lshift_str = expectedFailure(BinaryBytesOperationTests.test_lshift_str)
BinaryBytesOperationTests.test_rshift_str = expectedFailure(BinaryBytesOperationTests.test_rshift_str)
BinaryBytesOperationTests.test_and_str = expectedFailure(BinaryBytesOperationTests.test_and_str)
BinaryBytesOperationTests.test_xor_str = expectedFailure(BinaryBytesOperationTests.test_xor_str)
BinaryBytesOperationTests.test_or_str = expectedFailure(BinaryBytesOperationTests.test_or_str)

BinaryBytesOperationTests.test_add_tuple = expectedFailure(BinaryBytesOperationTests.test_add_tuple)
BinaryBytesOperationTests.test_subtract_tuple = expectedFailure(BinaryBytesOperationTests.test_subtract_tuple)
BinaryBytesOperationTests.test_multiply_tuple = expectedFailure(BinaryBytesOperationTests.test_multiply_tuple)
BinaryBytesOperationTests.test_floor_divide_tuple = expectedFailure(BinaryBytesOperationTests.test_floor_divide_tuple)
BinaryBytesOperationTests.test_true_divide_tuple = expectedFailure(BinaryBytesOperationTests.test_true_divide_tuple)
BinaryBytesOperationTests.test_modulo_tuple = expectedFailure(BinaryBytesOperationTests.test_modulo_tuple)
BinaryBytesOperationTests.test_power_tuple = expectedFailure(BinaryBytesOperationTests.test_power_tuple)
BinaryBytesOperationTests.test_subscr_tuple = expectedFailure(BinaryBytesOperationTests.test_subscr_tuple)
BinaryBytesOperationTests.test_lshift_tuple = expectedFailure(BinaryBytesOperationTests.test_lshift_tuple)
BinaryBytesOperationTests.test_rshift_tuple = expectedFailure(BinaryBytesOperationTests.test_rshift_tuple)
BinaryBytesOperationTests.test_and_tuple = expectedFailure(BinaryBytesOperationTests.test_and_tuple)
BinaryBytesOperationTests.test_xor_tuple = expectedFailure(BinaryBytesOperationTests.test_xor_tuple)
BinaryBytesOperationTests.test_or_tuple = expectedFailure(BinaryBytesOperationTests.test_or_tuple)


class InplaceBytesOperationTests(InplaceOperationTestCase, TranspileTestCase):
    x = 'b"This is a string of bytes"'


InplaceBytesOperationTests.test_add_bool_true = expectedFailure(InplaceBytesOperationTests.test_add_bool_true)
InplaceBytesOperationTests.test_subtract_bool_true = expectedFailure(InplaceBytesOperationTests.test_subtract_bool_true)
InplaceBytesOperationTests.test_multiply_bool_true = expectedFailure(InplaceBytesOperationTests.test_multiply_bool_true)
InplaceBytesOperationTests.test_floor_divide_bool_true = expectedFailure(InplaceBytesOperationTests.test_floor_divide_bool_true)
InplaceBytesOperationTests.test_true_divide_bool_true = expectedFailure(InplaceBytesOperationTests.test_true_divide_bool_true)
InplaceBytesOperationTests.test_modulo_bool_true = expectedFailure(InplaceBytesOperationTests.test_modulo_bool_true)
InplaceBytesOperationTests.test_power_bool_true = expectedFailure(InplaceBytesOperationTests.test_power_bool_true)
InplaceBytesOperationTests.test_lshift_bool_true = expectedFailure(InplaceBytesOperationTests.test_lshift_bool_true)
InplaceBytesOperationTests.test_rshift_bool_true = expectedFailure(InplaceBytesOperationTests.test_rshift_bool_true)
InplaceBytesOperationTests.test_and_bool_true = expectedFailure(InplaceBytesOperationTests.test_and_bool_true)
InplaceBytesOperationTests.test_xor_bool_true = expectedFailure(InplaceBytesOperationTests.test_xor_bool_true)
InplaceBytesOperationTests.test_or_bool_true = expectedFailure(InplaceBytesOperationTests.test_or_bool_true)

InplaceBytesOperationTests.test_add_bool_false = expectedFailure(InplaceBytesOperationTests.test_add_bool_false)
InplaceBytesOperationTests.test_subtract_bool_false = expectedFailure(InplaceBytesOperationTests.test_subtract_bool_false)
InplaceBytesOperationTests.test_multiply_bool_false = expectedFailure(InplaceBytesOperationTests.test_multiply_bool_false)
InplaceBytesOperationTests.test_floor_divide_bool_false = expectedFailure(InplaceBytesOperationTests.test_floor_divide_bool_false)
InplaceBytesOperationTests.test_true_divide_bool_false = expectedFailure(InplaceBytesOperationTests.test_true_divide_bool_false)
InplaceBytesOperationTests.test_modulo_bool_false = expectedFailure(InplaceBytesOperationTests.test_modulo_bool_false)
InplaceBytesOperationTests.test_power_bool_false = expectedFailure(InplaceBytesOperationTests.test_power_bool_false)
InplaceBytesOperationTests.test_lshift_bool_false = expectedFailure(InplaceBytesOperationTests.test_lshift_bool_false)
InplaceBytesOperationTests.test_rshift_bool_false = expectedFailure(InplaceBytesOperationTests.test_rshift_bool_false)
InplaceBytesOperationTests.test_and_bool_false = expectedFailure(InplaceBytesOperationTests.test_and_bool_false)
InplaceBytesOperationTests.test_xor_bool_false = expectedFailure(InplaceBytesOperationTests.test_xor_bool_false)
InplaceBytesOperationTests.test_or_bool_false = expectedFailure(InplaceBytesOperationTests.test_or_bool_false)

# InplaceBytesOperationTests.test_add_bytearray = expectedFailure(InplaceBytesOperationTests.test_add_bytearray)
# InplaceBytesOperationTests.test_subtract_bytearray = expectedFailure(InplaceBytesOperationTests.test_subtract_bytearray)
# InplaceBytesOperationTests.test_multiply_bytearray = expectedFailure(InplaceBytesOperationTests.test_multiply_bytearray)
# InplaceBytesOperationTests.test_floor_divide_bytearray = expectedFailure(InplaceBytesOperationTests.test_floor_divide_bytearray)
# InplaceBytesOperationTests.test_true_divide_bytearray = expectedFailure(InplaceBytesOperationTests.test_true_divide_bytearray)
# InplaceBytesOperationTests.test_modulo_bytearray = expectedFailure(InplaceBytesOperationTests.test_modulo_bytearray)
# InplaceBytesOperationTests.test_power_bytearray = expectedFailure(InplaceBytesOperationTests.test_power_bytearray)
# InplaceBytesOperationTests.test_lshift_bytearray = expectedFailure(InplaceBytesOperationTests.test_lshift_bytearray)
# InplaceBytesOperationTests.test_rshift_bytearray = expectedFailure(InplaceBytesOperationTests.test_rshift_bytearray)
# InplaceBytesOperationTests.test_and_bytearray = expectedFailure(InplaceBytesOperationTests.test_and_bytearray)
# InplaceBytesOperationTests.test_xor_bytearray = expectedFailure(InplaceBytesOperationTests.test_xor_bytearray)
# InplaceBytesOperationTests.test_or_bytearray = expectedFailure(InplaceBytesOperationTests.test_or_bytearray)

InplaceBytesOperationTests.test_add_bytes = expectedFailure(InplaceBytesOperationTests.test_add_bytes)
InplaceBytesOperationTests.test_subtract_bytes = expectedFailure(InplaceBytesOperationTests.test_subtract_bytes)
InplaceBytesOperationTests.test_multiply_bytes = expectedFailure(InplaceBytesOperationTests.test_multiply_bytes)
InplaceBytesOperationTests.test_floor_divide_bytes = expectedFailure(InplaceBytesOperationTests.test_floor_divide_bytes)
InplaceBytesOperationTests.test_true_divide_bytes = expectedFailure(InplaceBytesOperationTests.test_true_divide_bytes)
InplaceBytesOperationTests.test_modulo_bytes = expectedFailure(InplaceBytesOperationTests.test_modulo_bytes)
InplaceBytesOperationTests.test_power_bytes = expectedFailure(InplaceBytesOperationTests.test_power_bytes)
InplaceBytesOperationTests.test_lshift_bytes = expectedFailure(InplaceBytesOperationTests.test_lshift_bytes)
InplaceBytesOperationTests.test_rshift_bytes = expectedFailure(InplaceBytesOperationTests.test_rshift_bytes)
InplaceBytesOperationTests.test_and_bytes = expectedFailure(InplaceBytesOperationTests.test_and_bytes)
InplaceBytesOperationTests.test_xor_bytes = expectedFailure(InplaceBytesOperationTests.test_xor_bytes)
InplaceBytesOperationTests.test_or_bytes = expectedFailure(InplaceBytesOperationTests.test_or_bytes)

# InplaceBytesOperationTests.test_add_class = expectedFailure(InplaceBytesOperationTests.test_add_class)
# InplaceBytesOperationTests.test_subtract_class = expectedFailure(InplaceBytesOperationTests.test_subtract_class)
# InplaceBytesOperationTests.test_multiply_class = expectedFailure(InplaceBytesOperationTests.test_multiply_class)
# InplaceBytesOperationTests.test_floor_divide_class = expectedFailure(InplaceBytesOperationTests.test_floor_divide_class)
# InplaceBytesOperationTests.test_true_divide_class = expectedFailure(InplaceBytesOperationTests.test_true_divide_class)
# InplaceBytesOperationTests.test_modulo_class = expectedFailure(InplaceBytesOperationTests.test_modulo_class)
# InplaceBytesOperationTests.test_power_class = expectedFailure(InplaceBytesOperationTests.test_power_class)
# InplaceBytesOperationTests.test_lshift_class = expectedFailure(InplaceBytesOperationTests.test_lshift_class)
# InplaceBytesOperationTests.test_rshift_class = expectedFailure(InplaceBytesOperationTests.test_rshift_class)
# InplaceBytesOperationTests.test_and_class = expectedFailure(InplaceBytesOperationTests.test_and_class)
# InplaceBytesOperationTests.test_xor_class = expectedFailure(InplaceBytesOperationTests.test_xor_class)
# InplaceBytesOperationTests.test_or_class = expectedFailure(InplaceBytesOperationTests.test_or_class)

# InplaceBytesOperationTests.test_add_complex = expectedFailure(InplaceBytesOperationTests.test_add_complex)
# InplaceBytesOperationTests.test_subtract_complex = expectedFailure(InplaceBytesOperationTests.test_subtract_complex)
# InplaceBytesOperationTests.test_multiply_complex = expectedFailure(InplaceBytesOperationTests.test_multiply_complex)
# InplaceBytesOperationTests.test_floor_divide_complex = expectedFailure(InplaceBytesOperationTests.test_floor_divide_complex)
# InplaceBytesOperationTests.test_true_divide_complex = expectedFailure(InplaceBytesOperationTests.test_true_divide_complex)
# InplaceBytesOperationTests.test_modulo_complex = expectedFailure(InplaceBytesOperationTests.test_modulo_complex)
# InplaceBytesOperationTests.test_power_complex = expectedFailure(InplaceBytesOperationTests.test_power_complex)
# InplaceBytesOperationTests.test_lshift_complex = expectedFailure(InplaceBytesOperationTests.test_lshift_complex)
# InplaceBytesOperationTests.test_rshift_complex = expectedFailure(InplaceBytesOperationTests.test_rshift_complex)
# InplaceBytesOperationTests.test_and_complex = expectedFailure(InplaceBytesOperationTests.test_and_complex)
# InplaceBytesOperationTests.test_xor_complex = expectedFailure(InplaceBytesOperationTests.test_xor_complex)
# InplaceBytesOperationTests.test_or_complex = expectedFailure(InplaceBytesOperationTests.test_or_complex)

InplaceBytesOperationTests.test_add_dict = expectedFailure(InplaceBytesOperationTests.test_add_dict)
InplaceBytesOperationTests.test_subtract_dict = expectedFailure(InplaceBytesOperationTests.test_subtract_dict)
InplaceBytesOperationTests.test_multiply_dict = expectedFailure(InplaceBytesOperationTests.test_multiply_dict)
InplaceBytesOperationTests.test_floor_divide_dict = expectedFailure(InplaceBytesOperationTests.test_floor_divide_dict)
InplaceBytesOperationTests.test_true_divide_dict = expectedFailure(InplaceBytesOperationTests.test_true_divide_dict)
InplaceBytesOperationTests.test_modulo_dict = expectedFailure(InplaceBytesOperationTests.test_modulo_dict)
InplaceBytesOperationTests.test_power_dict = expectedFailure(InplaceBytesOperationTests.test_power_dict)
InplaceBytesOperationTests.test_lshift_dict = expectedFailure(InplaceBytesOperationTests.test_lshift_dict)
InplaceBytesOperationTests.test_rshift_dict = expectedFailure(InplaceBytesOperationTests.test_rshift_dict)
InplaceBytesOperationTests.test_and_dict = expectedFailure(InplaceBytesOperationTests.test_and_dict)
InplaceBytesOperationTests.test_xor_dict = expectedFailure(InplaceBytesOperationTests.test_xor_dict)
InplaceBytesOperationTests.test_or_dict = expectedFailure(InplaceBytesOperationTests.test_or_dict)

InplaceBytesOperationTests.test_add_float = expectedFailure(InplaceBytesOperationTests.test_add_float)
InplaceBytesOperationTests.test_subtract_float = expectedFailure(InplaceBytesOperationTests.test_subtract_float)
InplaceBytesOperationTests.test_multiply_float = expectedFailure(InplaceBytesOperationTests.test_multiply_float)
InplaceBytesOperationTests.test_floor_divide_float = expectedFailure(InplaceBytesOperationTests.test_floor_divide_float)
InplaceBytesOperationTests.test_true_divide_float = expectedFailure(InplaceBytesOperationTests.test_true_divide_float)
InplaceBytesOperationTests.test_modulo_float = expectedFailure(InplaceBytesOperationTests.test_modulo_float)
InplaceBytesOperationTests.test_power_float = expectedFailure(InplaceBytesOperationTests.test_power_float)
InplaceBytesOperationTests.test_lshift_float = expectedFailure(InplaceBytesOperationTests.test_lshift_float)
InplaceBytesOperationTests.test_rshift_float = expectedFailure(InplaceBytesOperationTests.test_rshift_float)
InplaceBytesOperationTests.test_and_float = expectedFailure(InplaceBytesOperationTests.test_and_float)
InplaceBytesOperationTests.test_xor_float = expectedFailure(InplaceBytesOperationTests.test_xor_float)
InplaceBytesOperationTests.test_or_float = expectedFailure(InplaceBytesOperationTests.test_or_float)

# InplaceBytesOperationTests.test_add_frozenset = expectedFailure(InplaceBytesOperationTests.test_add_frozenset)
# InplaceBytesOperationTests.test_subtract_frozenset = expectedFailure(InplaceBytesOperationTests.test_subtract_frozenset)
# InplaceBytesOperationTests.test_multiply_frozenset = expectedFailure(InplaceBytesOperationTests.test_multiply_frozenset)
# InplaceBytesOperationTests.test_floor_divide_frozenset = expectedFailure(InplaceBytesOperationTests.test_floor_divide_frozenset)
# InplaceBytesOperationTests.test_true_divide_frozenset = expectedFailure(InplaceBytesOperationTests.test_true_divide_frozenset)
# InplaceBytesOperationTests.test_modulo_frozenset = expectedFailure(InplaceBytesOperationTests.test_modulo_frozenset)
# InplaceBytesOperationTests.test_power_frozenset = expectedFailure(InplaceBytesOperationTests.test_power_frozenset)
# InplaceBytesOperationTests.test_lshift_frozenset = expectedFailure(InplaceBytesOperationTests.test_lshift_frozenset)
# InplaceBytesOperationTests.test_rshift_frozenset = expectedFailure(InplaceBytesOperationTests.test_rshift_frozenset)
# InplaceBytesOperationTests.test_and_frozenset = expectedFailure(InplaceBytesOperationTests.test_and_frozenset)
# InplaceBytesOperationTests.test_xor_frozenset = expectedFailure(InplaceBytesOperationTests.test_xor_frozenset)
# InplaceBytesOperationTests.test_or_frozenset = expectedFailure(InplaceBytesOperationTests.test_or_frozenset)

InplaceBytesOperationTests.test_add_int = expectedFailure(InplaceBytesOperationTests.test_add_int)
InplaceBytesOperationTests.test_subtract_int = expectedFailure(InplaceBytesOperationTests.test_subtract_int)
InplaceBytesOperationTests.test_multiply_int = expectedFailure(InplaceBytesOperationTests.test_multiply_int)
InplaceBytesOperationTests.test_floor_divide_int = expectedFailure(InplaceBytesOperationTests.test_floor_divide_int)
InplaceBytesOperationTests.test_true_divide_int = expectedFailure(InplaceBytesOperationTests.test_true_divide_int)
InplaceBytesOperationTests.test_modulo_int = expectedFailure(InplaceBytesOperationTests.test_modulo_int)
InplaceBytesOperationTests.test_power_int = expectedFailure(InplaceBytesOperationTests.test_power_int)
InplaceBytesOperationTests.test_lshift_int = expectedFailure(InplaceBytesOperationTests.test_lshift_int)
InplaceBytesOperationTests.test_rshift_int = expectedFailure(InplaceBytesOperationTests.test_rshift_int)
InplaceBytesOperationTests.test_and_int = expectedFailure(InplaceBytesOperationTests.test_and_int)
InplaceBytesOperationTests.test_xor_int = expectedFailure(InplaceBytesOperationTests.test_xor_int)
InplaceBytesOperationTests.test_or_int = expectedFailure(InplaceBytesOperationTests.test_or_int)

InplaceBytesOperationTests.test_add_list = expectedFailure(InplaceBytesOperationTests.test_add_list)
InplaceBytesOperationTests.test_subtract_list = expectedFailure(InplaceBytesOperationTests.test_subtract_list)
InplaceBytesOperationTests.test_multiply_list = expectedFailure(InplaceBytesOperationTests.test_multiply_list)
InplaceBytesOperationTests.test_floor_divide_list = expectedFailure(InplaceBytesOperationTests.test_floor_divide_list)
InplaceBytesOperationTests.test_true_divide_list = expectedFailure(InplaceBytesOperationTests.test_true_divide_list)
InplaceBytesOperationTests.test_modulo_list = expectedFailure(InplaceBytesOperationTests.test_modulo_list)
InplaceBytesOperationTests.test_power_list = expectedFailure(InplaceBytesOperationTests.test_power_list)
InplaceBytesOperationTests.test_lshift_list = expectedFailure(InplaceBytesOperationTests.test_lshift_list)
InplaceBytesOperationTests.test_rshift_list = expectedFailure(InplaceBytesOperationTests.test_rshift_list)
InplaceBytesOperationTests.test_and_list = expectedFailure(InplaceBytesOperationTests.test_and_list)
InplaceBytesOperationTests.test_xor_list = expectedFailure(InplaceBytesOperationTests.test_xor_list)
InplaceBytesOperationTests.test_or_list = expectedFailure(InplaceBytesOperationTests.test_or_list)

InplaceBytesOperationTests.test_add_set = expectedFailure(InplaceBytesOperationTests.test_add_set)
InplaceBytesOperationTests.test_subtract_set = expectedFailure(InplaceBytesOperationTests.test_subtract_set)
InplaceBytesOperationTests.test_multiply_set = expectedFailure(InplaceBytesOperationTests.test_multiply_set)
InplaceBytesOperationTests.test_floor_divide_set = expectedFailure(InplaceBytesOperationTests.test_floor_divide_set)
InplaceBytesOperationTests.test_true_divide_set = expectedFailure(InplaceBytesOperationTests.test_true_divide_set)
InplaceBytesOperationTests.test_modulo_set = expectedFailure(InplaceBytesOperationTests.test_modulo_set)
InplaceBytesOperationTests.test_power_set = expectedFailure(InplaceBytesOperationTests.test_power_set)
InplaceBytesOperationTests.test_lshift_set = expectedFailure(InplaceBytesOperationTests.test_lshift_set)
InplaceBytesOperationTests.test_rshift_set = expectedFailure(InplaceBytesOperationTests.test_rshift_set)
InplaceBytesOperationTests.test_and_set = expectedFailure(InplaceBytesOperationTests.test_and_set)
InplaceBytesOperationTests.test_xor_set = expectedFailure(InplaceBytesOperationTests.test_xor_set)
InplaceBytesOperationTests.test_or_set = expectedFailure(InplaceBytesOperationTests.test_or_set)

InplaceBytesOperationTests.test_add_str = expectedFailure(InplaceBytesOperationTests.test_add_str)
InplaceBytesOperationTests.test_subtract_str = expectedFailure(InplaceBytesOperationTests.test_subtract_str)
InplaceBytesOperationTests.test_multiply_str = expectedFailure(InplaceBytesOperationTests.test_multiply_str)
InplaceBytesOperationTests.test_floor_divide_str = expectedFailure(InplaceBytesOperationTests.test_floor_divide_str)
InplaceBytesOperationTests.test_true_divide_str = expectedFailure(InplaceBytesOperationTests.test_true_divide_str)
InplaceBytesOperationTests.test_modulo_str = expectedFailure(InplaceBytesOperationTests.test_modulo_str)
InplaceBytesOperationTests.test_power_str = expectedFailure(InplaceBytesOperationTests.test_power_str)
InplaceBytesOperationTests.test_lshift_str = expectedFailure(InplaceBytesOperationTests.test_lshift_str)
InplaceBytesOperationTests.test_rshift_str = expectedFailure(InplaceBytesOperationTests.test_rshift_str)
InplaceBytesOperationTests.test_and_str = expectedFailure(InplaceBytesOperationTests.test_and_str)
InplaceBytesOperationTests.test_xor_str = expectedFailure(InplaceBytesOperationTests.test_xor_str)
InplaceBytesOperationTests.test_or_str = expectedFailure(InplaceBytesOperationTests.test_or_str)

InplaceBytesOperationTests.test_add_tuple = expectedFailure(InplaceBytesOperationTests.test_add_tuple)
InplaceBytesOperationTests.test_subtract_tuple = expectedFailure(InplaceBytesOperationTests.test_subtract_tuple)
InplaceBytesOperationTests.test_multiply_tuple = expectedFailure(InplaceBytesOperationTests.test_multiply_tuple)
InplaceBytesOperationTests.test_floor_divide_tuple = expectedFailure(InplaceBytesOperationTests.test_floor_divide_tuple)
InplaceBytesOperationTests.test_true_divide_tuple = expectedFailure(InplaceBytesOperationTests.test_true_divide_tuple)
InplaceBytesOperationTests.test_modulo_tuple = expectedFailure(InplaceBytesOperationTests.test_modulo_tuple)
InplaceBytesOperationTests.test_power_tuple = expectedFailure(InplaceBytesOperationTests.test_power_tuple)
InplaceBytesOperationTests.test_lshift_tuple = expectedFailure(InplaceBytesOperationTests.test_lshift_tuple)
InplaceBytesOperationTests.test_rshift_tuple = expectedFailure(InplaceBytesOperationTests.test_rshift_tuple)
InplaceBytesOperationTests.test_and_tuple = expectedFailure(InplaceBytesOperationTests.test_and_tuple)
InplaceBytesOperationTests.test_xor_tuple = expectedFailure(InplaceBytesOperationTests.test_xor_tuple)
InplaceBytesOperationTests.test_or_tuple = expectedFailure(InplaceBytesOperationTests.test_or_tuple)
