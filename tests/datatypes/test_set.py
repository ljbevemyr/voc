from unittest import expectedFailure
from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class UnarySetOperationTests(UnaryOperationTestCase, TranspileTestCase):
    x = "{1, 'value', 1.2345}"

UnarySetOperationTests.test_unary_positive = expectedFailure(UnarySetOperationTests.test_unary_positive)
UnarySetOperationTests.test_unary_negative = expectedFailure(UnarySetOperationTests.test_unary_negative)
UnarySetOperationTests.test_unary_not = expectedFailure(UnarySetOperationTests.test_unary_not)
UnarySetOperationTests.test_unary_invert = expectedFailure(UnarySetOperationTests.test_unary_invert)


class BinarySetOperationTests(BinaryOperationTestCase, TranspileTestCase):
    x = "{1, 'value', 1.2345}"

BinarySetOperationTests.test_add_bool_true = expectedFailure(BinarySetOperationTests.test_add_bool_true)
BinarySetOperationTests.test_subtract_bool_true = expectedFailure(BinarySetOperationTests.test_subtract_bool_true)
BinarySetOperationTests.test_multiply_bool_true = expectedFailure(BinarySetOperationTests.test_multiply_bool_true)
BinarySetOperationTests.test_floor_divide_bool_true = expectedFailure(BinarySetOperationTests.test_floor_divide_bool_true)
BinarySetOperationTests.test_true_divide_bool_true = expectedFailure(BinarySetOperationTests.test_true_divide_bool_true)
BinarySetOperationTests.test_modulo_bool_true = expectedFailure(BinarySetOperationTests.test_modulo_bool_true)
BinarySetOperationTests.test_power_bool_true = expectedFailure(BinarySetOperationTests.test_power_bool_true)
BinarySetOperationTests.test_subscr_bool_true = expectedFailure(BinarySetOperationTests.test_subscr_bool_true)
BinarySetOperationTests.test_lshift_bool_true = expectedFailure(BinarySetOperationTests.test_lshift_bool_true)
BinarySetOperationTests.test_rshift_bool_true = expectedFailure(BinarySetOperationTests.test_rshift_bool_true)
BinarySetOperationTests.test_and_bool_true = expectedFailure(BinarySetOperationTests.test_and_bool_true)
BinarySetOperationTests.test_xor_bool_true = expectedFailure(BinarySetOperationTests.test_xor_bool_true)
BinarySetOperationTests.test_or_bool_true = expectedFailure(BinarySetOperationTests.test_or_bool_true)

BinarySetOperationTests.test_add_bool_false = expectedFailure(BinarySetOperationTests.test_add_bool_false)
BinarySetOperationTests.test_subtract_bool_false = expectedFailure(BinarySetOperationTests.test_subtract_bool_false)
BinarySetOperationTests.test_multiply_bool_false = expectedFailure(BinarySetOperationTests.test_multiply_bool_false)
BinarySetOperationTests.test_floor_divide_bool_false = expectedFailure(BinarySetOperationTests.test_floor_divide_bool_false)
BinarySetOperationTests.test_true_divide_bool_false = expectedFailure(BinarySetOperationTests.test_true_divide_bool_false)
BinarySetOperationTests.test_modulo_bool_false = expectedFailure(BinarySetOperationTests.test_modulo_bool_false)
BinarySetOperationTests.test_power_bool_false = expectedFailure(BinarySetOperationTests.test_power_bool_false)
BinarySetOperationTests.test_subscr_bool_false = expectedFailure(BinarySetOperationTests.test_subscr_bool_false)
BinarySetOperationTests.test_lshift_bool_false = expectedFailure(BinarySetOperationTests.test_lshift_bool_false)
BinarySetOperationTests.test_rshift_bool_false = expectedFailure(BinarySetOperationTests.test_rshift_bool_false)
BinarySetOperationTests.test_and_bool_false = expectedFailure(BinarySetOperationTests.test_and_bool_false)
BinarySetOperationTests.test_xor_bool_false = expectedFailure(BinarySetOperationTests.test_xor_bool_false)
BinarySetOperationTests.test_or_bool_false = expectedFailure(BinarySetOperationTests.test_or_bool_false)

# BinarySetOperationTests.test_add_bytearray = expectedFailure(BinarySetOperationTests.test_add_bytearray)
# BinarySetOperationTests.test_subtract_bytearray = expectedFailure(BinarySetOperationTests.test_subtract_bytearray)
# BinarySetOperationTests.test_multiply_bytearray = expectedFailure(BinarySetOperationTests.test_multiply_bytearray)
# BinarySetOperationTests.test_floor_divide_bytearray = expectedFailure(BinarySetOperationTests.test_floor_divide_bytearray)
# BinarySetOperationTests.test_true_divide_bytearray = expectedFailure(BinarySetOperationTests.test_true_divide_bytearray)
# BinarySetOperationTests.test_modulo_bytearray = expectedFailure(BinarySetOperationTests.test_modulo_bytearray)
# BinarySetOperationTests.test_power_bytearray = expectedFailure(BinarySetOperationTests.test_power_bytearray)
# BinarySetOperationTests.test_subscr_bytearray = expectedFailure(BinarySetOperationTests.test_subscr_bytearray)
# BinarySetOperationTests.test_lshift_bytearray = expectedFailure(BinarySetOperationTests.test_lshift_bytearray)
# BinarySetOperationTests.test_rshift_bytearray = expectedFailure(BinarySetOperationTests.test_rshift_bytearray)
# BinarySetOperationTests.test_and_bytearray = expectedFailure(BinarySetOperationTests.test_and_bytearray)
# BinarySetOperationTests.test_xor_bytearray = expectedFailure(BinarySetOperationTests.test_xor_bytearray)
# BinarySetOperationTests.test_or_bytearray = expectedFailure(BinarySetOperationTests.test_or_bytearray)

BinarySetOperationTests.test_add_bytes = expectedFailure(BinarySetOperationTests.test_add_bytes)
BinarySetOperationTests.test_subtract_bytes = expectedFailure(BinarySetOperationTests.test_subtract_bytes)
BinarySetOperationTests.test_multiply_bytes = expectedFailure(BinarySetOperationTests.test_multiply_bytes)
BinarySetOperationTests.test_floor_divide_bytes = expectedFailure(BinarySetOperationTests.test_floor_divide_bytes)
BinarySetOperationTests.test_true_divide_bytes = expectedFailure(BinarySetOperationTests.test_true_divide_bytes)
BinarySetOperationTests.test_modulo_bytes = expectedFailure(BinarySetOperationTests.test_modulo_bytes)
BinarySetOperationTests.test_power_bytes = expectedFailure(BinarySetOperationTests.test_power_bytes)
BinarySetOperationTests.test_subscr_bytes = expectedFailure(BinarySetOperationTests.test_subscr_bytes)
BinarySetOperationTests.test_lshift_bytes = expectedFailure(BinarySetOperationTests.test_lshift_bytes)
BinarySetOperationTests.test_rshift_bytes = expectedFailure(BinarySetOperationTests.test_rshift_bytes)
BinarySetOperationTests.test_and_bytes = expectedFailure(BinarySetOperationTests.test_and_bytes)
BinarySetOperationTests.test_xor_bytes = expectedFailure(BinarySetOperationTests.test_xor_bytes)
BinarySetOperationTests.test_or_bytes = expectedFailure(BinarySetOperationTests.test_or_bytes)

# BinarySetOperationTests.test_add_class = expectedFailure(BinarySetOperationTests.test_add_class)
# BinarySetOperationTests.test_subtract_class = expectedFailure(BinarySetOperationTests.test_subtract_class)
# BinarySetOperationTests.test_multiply_class = expectedFailure(BinarySetOperationTests.test_multiply_class)
# BinarySetOperationTests.test_floor_divide_class = expectedFailure(BinarySetOperationTests.test_floor_divide_class)
# BinarySetOperationTests.test_true_divide_class = expectedFailure(BinarySetOperationTests.test_true_divide_class)
# BinarySetOperationTests.test_modulo_class = expectedFailure(BinarySetOperationTests.test_modulo_class)
# BinarySetOperationTests.test_power_class = expectedFailure(BinarySetOperationTests.test_power_class)
# BinarySetOperationTests.test_subscr_class = expectedFailure(BinarySetOperationTests.test_subscr_class)
# BinarySetOperationTests.test_lshift_class = expectedFailure(BinarySetOperationTests.test_lshift_class)
# BinarySetOperationTests.test_rshift_class = expectedFailure(BinarySetOperationTests.test_rshift_class)
# BinarySetOperationTests.test_and_class = expectedFailure(BinarySetOperationTests.test_and_class)
# BinarySetOperationTests.test_xor_class = expectedFailure(BinarySetOperationTests.test_xor_class)
# BinarySetOperationTests.test_or_class = expectedFailure(BinarySetOperationTests.test_or_class)

# BinarySetOperationTests.test_add_complex = expectedFailure(BinarySetOperationTests.test_add_complex)
# BinarySetOperationTests.test_subtract_complex = expectedFailure(BinarySetOperationTests.test_subtract_complex)
# BinarySetOperationTests.test_multiply_complex = expectedFailure(BinarySetOperationTests.test_multiply_complex)
# BinarySetOperationTests.test_floor_divide_complex = expectedFailure(BinarySetOperationTests.test_floor_divide_complex)
# BinarySetOperationTests.test_true_divide_complex = expectedFailure(BinarySetOperationTests.test_true_divide_complex)
# BinarySetOperationTests.test_modulo_complex = expectedFailure(BinarySetOperationTests.test_modulo_complex)
# BinarySetOperationTests.test_power_complex = expectedFailure(BinarySetOperationTests.test_power_complex)
# BinarySetOperationTests.test_subscr_complex = expectedFailure(BinarySetOperationTests.test_subscr_complex)
# BinarySetOperationTests.test_lshift_complex = expectedFailure(BinarySetOperationTests.test_lshift_complex)
# BinarySetOperationTests.test_rshift_complex = expectedFailure(BinarySetOperationTests.test_rshift_complex)
# BinarySetOperationTests.test_and_complex = expectedFailure(BinarySetOperationTests.test_and_complex)
# BinarySetOperationTests.test_xor_complex = expectedFailure(BinarySetOperationTests.test_xor_complex)
# BinarySetOperationTests.test_or_complex = expectedFailure(BinarySetOperationTests.test_or_complex)

BinarySetOperationTests.test_add_dict = expectedFailure(BinarySetOperationTests.test_add_dict)
BinarySetOperationTests.test_subtract_dict = expectedFailure(BinarySetOperationTests.test_subtract_dict)
BinarySetOperationTests.test_multiply_dict = expectedFailure(BinarySetOperationTests.test_multiply_dict)
BinarySetOperationTests.test_floor_divide_dict = expectedFailure(BinarySetOperationTests.test_floor_divide_dict)
BinarySetOperationTests.test_true_divide_dict = expectedFailure(BinarySetOperationTests.test_true_divide_dict)
BinarySetOperationTests.test_modulo_dict = expectedFailure(BinarySetOperationTests.test_modulo_dict)
BinarySetOperationTests.test_power_dict = expectedFailure(BinarySetOperationTests.test_power_dict)
BinarySetOperationTests.test_subscr_dict = expectedFailure(BinarySetOperationTests.test_subscr_dict)
BinarySetOperationTests.test_lshift_dict = expectedFailure(BinarySetOperationTests.test_lshift_dict)
BinarySetOperationTests.test_rshift_dict = expectedFailure(BinarySetOperationTests.test_rshift_dict)
BinarySetOperationTests.test_and_dict = expectedFailure(BinarySetOperationTests.test_and_dict)
BinarySetOperationTests.test_xor_dict = expectedFailure(BinarySetOperationTests.test_xor_dict)
BinarySetOperationTests.test_or_dict = expectedFailure(BinarySetOperationTests.test_or_dict)

BinarySetOperationTests.test_add_float = expectedFailure(BinarySetOperationTests.test_add_float)
BinarySetOperationTests.test_subtract_float = expectedFailure(BinarySetOperationTests.test_subtract_float)
BinarySetOperationTests.test_multiply_float = expectedFailure(BinarySetOperationTests.test_multiply_float)
BinarySetOperationTests.test_floor_divide_float = expectedFailure(BinarySetOperationTests.test_floor_divide_float)
BinarySetOperationTests.test_true_divide_float = expectedFailure(BinarySetOperationTests.test_true_divide_float)
BinarySetOperationTests.test_modulo_float = expectedFailure(BinarySetOperationTests.test_modulo_float)
BinarySetOperationTests.test_power_float = expectedFailure(BinarySetOperationTests.test_power_float)
BinarySetOperationTests.test_subscr_float = expectedFailure(BinarySetOperationTests.test_subscr_float)
BinarySetOperationTests.test_lshift_float = expectedFailure(BinarySetOperationTests.test_lshift_float)
BinarySetOperationTests.test_rshift_float = expectedFailure(BinarySetOperationTests.test_rshift_float)
BinarySetOperationTests.test_and_float = expectedFailure(BinarySetOperationTests.test_and_float)
BinarySetOperationTests.test_xor_float = expectedFailure(BinarySetOperationTests.test_xor_float)
BinarySetOperationTests.test_or_float = expectedFailure(BinarySetOperationTests.test_or_float)

# BinarySetOperationTests.test_add_frozenset = expectedFailure(BinarySetOperationTests.test_add_frozenset)
# BinarySetOperationTests.test_subtract_frozenset = expectedFailure(BinarySetOperationTests.test_subtract_frozenset)
# BinarySetOperationTests.test_multiply_frozenset = expectedFailure(BinarySetOperationTests.test_multiply_frozenset)
# BinarySetOperationTests.test_floor_divide_frozenset = expectedFailure(BinarySetOperationTests.test_floor_divide_frozenset)
# BinarySetOperationTests.test_true_divide_frozenset = expectedFailure(BinarySetOperationTests.test_true_divide_frozenset)
# BinarySetOperationTests.test_modulo_frozenset = expectedFailure(BinarySetOperationTests.test_modulo_frozenset)
# BinarySetOperationTests.test_power_frozenset = expectedFailure(BinarySetOperationTests.test_power_frozenset)
# BinarySetOperationTests.test_subscr_frozenset = expectedFailure(BinarySetOperationTests.test_subscr_frozenset)
# BinarySetOperationTests.test_lshift_frozenset = expectedFailure(BinarySetOperationTests.test_lshift_frozenset)
# BinarySetOperationTests.test_rshift_frozenset = expectedFailure(BinarySetOperationTests.test_rshift_frozenset)
# BinarySetOperationTests.test_and_frozenset = expectedFailure(BinarySetOperationTests.test_and_frozenset)
# BinarySetOperationTests.test_xor_frozenset = expectedFailure(BinarySetOperationTests.test_xor_frozenset)
# BinarySetOperationTests.test_or_frozenset = expectedFailure(BinarySetOperationTests.test_or_frozenset)

BinarySetOperationTests.test_add_int = expectedFailure(BinarySetOperationTests.test_add_int)
BinarySetOperationTests.test_subtract_int = expectedFailure(BinarySetOperationTests.test_subtract_int)
BinarySetOperationTests.test_multiply_int = expectedFailure(BinarySetOperationTests.test_multiply_int)
BinarySetOperationTests.test_floor_divide_int = expectedFailure(BinarySetOperationTests.test_floor_divide_int)
BinarySetOperationTests.test_true_divide_int = expectedFailure(BinarySetOperationTests.test_true_divide_int)
BinarySetOperationTests.test_modulo_int = expectedFailure(BinarySetOperationTests.test_modulo_int)
BinarySetOperationTests.test_power_int = expectedFailure(BinarySetOperationTests.test_power_int)
BinarySetOperationTests.test_subscr_int = expectedFailure(BinarySetOperationTests.test_subscr_int)
BinarySetOperationTests.test_lshift_int = expectedFailure(BinarySetOperationTests.test_lshift_int)
BinarySetOperationTests.test_rshift_int = expectedFailure(BinarySetOperationTests.test_rshift_int)
BinarySetOperationTests.test_and_int = expectedFailure(BinarySetOperationTests.test_and_int)
BinarySetOperationTests.test_xor_int = expectedFailure(BinarySetOperationTests.test_xor_int)
BinarySetOperationTests.test_or_int = expectedFailure(BinarySetOperationTests.test_or_int)

BinarySetOperationTests.test_add_list = expectedFailure(BinarySetOperationTests.test_add_list)
BinarySetOperationTests.test_subtract_list = expectedFailure(BinarySetOperationTests.test_subtract_list)
BinarySetOperationTests.test_multiply_list = expectedFailure(BinarySetOperationTests.test_multiply_list)
BinarySetOperationTests.test_floor_divide_list = expectedFailure(BinarySetOperationTests.test_floor_divide_list)
BinarySetOperationTests.test_true_divide_list = expectedFailure(BinarySetOperationTests.test_true_divide_list)
BinarySetOperationTests.test_modulo_list = expectedFailure(BinarySetOperationTests.test_modulo_list)
BinarySetOperationTests.test_power_list = expectedFailure(BinarySetOperationTests.test_power_list)
BinarySetOperationTests.test_subscr_list = expectedFailure(BinarySetOperationTests.test_subscr_list)
BinarySetOperationTests.test_lshift_list = expectedFailure(BinarySetOperationTests.test_lshift_list)
BinarySetOperationTests.test_rshift_list = expectedFailure(BinarySetOperationTests.test_rshift_list)
BinarySetOperationTests.test_and_list = expectedFailure(BinarySetOperationTests.test_and_list)
BinarySetOperationTests.test_xor_list = expectedFailure(BinarySetOperationTests.test_xor_list)
BinarySetOperationTests.test_or_list = expectedFailure(BinarySetOperationTests.test_or_list)

BinarySetOperationTests.test_add_set = expectedFailure(BinarySetOperationTests.test_add_set)
BinarySetOperationTests.test_subtract_set = expectedFailure(BinarySetOperationTests.test_subtract_set)
BinarySetOperationTests.test_multiply_set = expectedFailure(BinarySetOperationTests.test_multiply_set)
BinarySetOperationTests.test_floor_divide_set = expectedFailure(BinarySetOperationTests.test_floor_divide_set)
BinarySetOperationTests.test_true_divide_set = expectedFailure(BinarySetOperationTests.test_true_divide_set)
BinarySetOperationTests.test_modulo_set = expectedFailure(BinarySetOperationTests.test_modulo_set)
BinarySetOperationTests.test_power_set = expectedFailure(BinarySetOperationTests.test_power_set)
BinarySetOperationTests.test_subscr_set = expectedFailure(BinarySetOperationTests.test_subscr_set)
BinarySetOperationTests.test_lshift_set = expectedFailure(BinarySetOperationTests.test_lshift_set)
BinarySetOperationTests.test_rshift_set = expectedFailure(BinarySetOperationTests.test_rshift_set)
BinarySetOperationTests.test_and_set = expectedFailure(BinarySetOperationTests.test_and_set)
BinarySetOperationTests.test_xor_set = expectedFailure(BinarySetOperationTests.test_xor_set)
BinarySetOperationTests.test_or_set = expectedFailure(BinarySetOperationTests.test_or_set)

BinarySetOperationTests.test_add_str = expectedFailure(BinarySetOperationTests.test_add_str)
BinarySetOperationTests.test_subtract_str = expectedFailure(BinarySetOperationTests.test_subtract_str)
BinarySetOperationTests.test_multiply_str = expectedFailure(BinarySetOperationTests.test_multiply_str)
BinarySetOperationTests.test_floor_divide_str = expectedFailure(BinarySetOperationTests.test_floor_divide_str)
BinarySetOperationTests.test_true_divide_str = expectedFailure(BinarySetOperationTests.test_true_divide_str)
BinarySetOperationTests.test_modulo_str = expectedFailure(BinarySetOperationTests.test_modulo_str)
BinarySetOperationTests.test_power_str = expectedFailure(BinarySetOperationTests.test_power_str)
BinarySetOperationTests.test_subscr_str = expectedFailure(BinarySetOperationTests.test_subscr_str)
BinarySetOperationTests.test_lshift_str = expectedFailure(BinarySetOperationTests.test_lshift_str)
BinarySetOperationTests.test_rshift_str = expectedFailure(BinarySetOperationTests.test_rshift_str)
BinarySetOperationTests.test_and_str = expectedFailure(BinarySetOperationTests.test_and_str)
BinarySetOperationTests.test_xor_str = expectedFailure(BinarySetOperationTests.test_xor_str)
BinarySetOperationTests.test_or_str = expectedFailure(BinarySetOperationTests.test_or_str)

BinarySetOperationTests.test_add_tuple = expectedFailure(BinarySetOperationTests.test_add_tuple)
BinarySetOperationTests.test_subtract_tuple = expectedFailure(BinarySetOperationTests.test_subtract_tuple)
BinarySetOperationTests.test_multiply_tuple = expectedFailure(BinarySetOperationTests.test_multiply_tuple)
BinarySetOperationTests.test_floor_divide_tuple = expectedFailure(BinarySetOperationTests.test_floor_divide_tuple)
BinarySetOperationTests.test_true_divide_tuple = expectedFailure(BinarySetOperationTests.test_true_divide_tuple)
BinarySetOperationTests.test_modulo_tuple = expectedFailure(BinarySetOperationTests.test_modulo_tuple)
BinarySetOperationTests.test_power_tuple = expectedFailure(BinarySetOperationTests.test_power_tuple)
BinarySetOperationTests.test_subscr_tuple = expectedFailure(BinarySetOperationTests.test_subscr_tuple)
BinarySetOperationTests.test_lshift_tuple = expectedFailure(BinarySetOperationTests.test_lshift_tuple)
BinarySetOperationTests.test_rshift_tuple = expectedFailure(BinarySetOperationTests.test_rshift_tuple)
BinarySetOperationTests.test_and_tuple = expectedFailure(BinarySetOperationTests.test_and_tuple)
BinarySetOperationTests.test_xor_tuple = expectedFailure(BinarySetOperationTests.test_xor_tuple)
BinarySetOperationTests.test_or_tuple = expectedFailure(BinarySetOperationTests.test_or_tuple)


class InplaceSetOperationTests(InplaceOperationTestCase, TranspileTestCase):
    x = "{1, 'value', 1.2345}"


InplaceSetOperationTests.test_add_bool_true = expectedFailure(InplaceSetOperationTests.test_add_bool_true)
InplaceSetOperationTests.test_subtract_bool_true = expectedFailure(InplaceSetOperationTests.test_subtract_bool_true)
InplaceSetOperationTests.test_multiply_bool_true = expectedFailure(InplaceSetOperationTests.test_multiply_bool_true)
InplaceSetOperationTests.test_floor_divide_bool_true = expectedFailure(InplaceSetOperationTests.test_floor_divide_bool_true)
InplaceSetOperationTests.test_true_divide_bool_true = expectedFailure(InplaceSetOperationTests.test_true_divide_bool_true)
InplaceSetOperationTests.test_modulo_bool_true = expectedFailure(InplaceSetOperationTests.test_modulo_bool_true)
InplaceSetOperationTests.test_power_bool_true = expectedFailure(InplaceSetOperationTests.test_power_bool_true)
InplaceSetOperationTests.test_lshift_bool_true = expectedFailure(InplaceSetOperationTests.test_lshift_bool_true)
InplaceSetOperationTests.test_rshift_bool_true = expectedFailure(InplaceSetOperationTests.test_rshift_bool_true)
InplaceSetOperationTests.test_and_bool_true = expectedFailure(InplaceSetOperationTests.test_and_bool_true)
InplaceSetOperationTests.test_xor_bool_true = expectedFailure(InplaceSetOperationTests.test_xor_bool_true)
InplaceSetOperationTests.test_or_bool_true = expectedFailure(InplaceSetOperationTests.test_or_bool_true)

InplaceSetOperationTests.test_add_bool_false = expectedFailure(InplaceSetOperationTests.test_add_bool_false)
InplaceSetOperationTests.test_subtract_bool_false = expectedFailure(InplaceSetOperationTests.test_subtract_bool_false)
InplaceSetOperationTests.test_multiply_bool_false = expectedFailure(InplaceSetOperationTests.test_multiply_bool_false)
InplaceSetOperationTests.test_floor_divide_bool_false = expectedFailure(InplaceSetOperationTests.test_floor_divide_bool_false)
InplaceSetOperationTests.test_true_divide_bool_false = expectedFailure(InplaceSetOperationTests.test_true_divide_bool_false)
InplaceSetOperationTests.test_modulo_bool_false = expectedFailure(InplaceSetOperationTests.test_modulo_bool_false)
InplaceSetOperationTests.test_power_bool_false = expectedFailure(InplaceSetOperationTests.test_power_bool_false)
InplaceSetOperationTests.test_lshift_bool_false = expectedFailure(InplaceSetOperationTests.test_lshift_bool_false)
InplaceSetOperationTests.test_rshift_bool_false = expectedFailure(InplaceSetOperationTests.test_rshift_bool_false)
InplaceSetOperationTests.test_and_bool_false = expectedFailure(InplaceSetOperationTests.test_and_bool_false)
InplaceSetOperationTests.test_xor_bool_false = expectedFailure(InplaceSetOperationTests.test_xor_bool_false)
InplaceSetOperationTests.test_or_bool_false = expectedFailure(InplaceSetOperationTests.test_or_bool_false)

# InplaceSetOperationTests.test_add_bytearray = expectedFailure(InplaceSetOperationTests.test_add_bytearray)
# InplaceSetOperationTests.test_subtract_bytearray = expectedFailure(InplaceSetOperationTests.test_subtract_bytearray)
# InplaceSetOperationTests.test_multiply_bytearray = expectedFailure(InplaceSetOperationTests.test_multiply_bytearray)
# InplaceSetOperationTests.test_floor_divide_bytearray = expectedFailure(InplaceSetOperationTests.test_floor_divide_bytearray)
# InplaceSetOperationTests.test_true_divide_bytearray = expectedFailure(InplaceSetOperationTests.test_true_divide_bytearray)
# InplaceSetOperationTests.test_modulo_bytearray = expectedFailure(InplaceSetOperationTests.test_modulo_bytearray)
# InplaceSetOperationTests.test_power_bytearray = expectedFailure(InplaceSetOperationTests.test_power_bytearray)
# InplaceSetOperationTests.test_lshift_bytearray = expectedFailure(InplaceSetOperationTests.test_lshift_bytearray)
# InplaceSetOperationTests.test_rshift_bytearray = expectedFailure(InplaceSetOperationTests.test_rshift_bytearray)
# InplaceSetOperationTests.test_and_bytearray = expectedFailure(InplaceSetOperationTests.test_and_bytearray)
# InplaceSetOperationTests.test_xor_bytearray = expectedFailure(InplaceSetOperationTests.test_xor_bytearray)
# InplaceSetOperationTests.test_or_bytearray = expectedFailure(InplaceSetOperationTests.test_or_bytearray)

InplaceSetOperationTests.test_add_bytes = expectedFailure(InplaceSetOperationTests.test_add_bytes)
InplaceSetOperationTests.test_subtract_bytes = expectedFailure(InplaceSetOperationTests.test_subtract_bytes)
InplaceSetOperationTests.test_multiply_bytes = expectedFailure(InplaceSetOperationTests.test_multiply_bytes)
InplaceSetOperationTests.test_floor_divide_bytes = expectedFailure(InplaceSetOperationTests.test_floor_divide_bytes)
InplaceSetOperationTests.test_true_divide_bytes = expectedFailure(InplaceSetOperationTests.test_true_divide_bytes)
InplaceSetOperationTests.test_modulo_bytes = expectedFailure(InplaceSetOperationTests.test_modulo_bytes)
InplaceSetOperationTests.test_power_bytes = expectedFailure(InplaceSetOperationTests.test_power_bytes)
InplaceSetOperationTests.test_lshift_bytes = expectedFailure(InplaceSetOperationTests.test_lshift_bytes)
InplaceSetOperationTests.test_rshift_bytes = expectedFailure(InplaceSetOperationTests.test_rshift_bytes)
InplaceSetOperationTests.test_and_bytes = expectedFailure(InplaceSetOperationTests.test_and_bytes)
InplaceSetOperationTests.test_xor_bytes = expectedFailure(InplaceSetOperationTests.test_xor_bytes)
InplaceSetOperationTests.test_or_bytes = expectedFailure(InplaceSetOperationTests.test_or_bytes)

# InplaceSetOperationTests.test_add_class = expectedFailure(InplaceSetOperationTests.test_add_class)
# InplaceSetOperationTests.test_subtract_class = expectedFailure(InplaceSetOperationTests.test_subtract_class)
# InplaceSetOperationTests.test_multiply_class = expectedFailure(InplaceSetOperationTests.test_multiply_class)
# InplaceSetOperationTests.test_floor_divide_class = expectedFailure(InplaceSetOperationTests.test_floor_divide_class)
# InplaceSetOperationTests.test_true_divide_class = expectedFailure(InplaceSetOperationTests.test_true_divide_class)
# InplaceSetOperationTests.test_modulo_class = expectedFailure(InplaceSetOperationTests.test_modulo_class)
# InplaceSetOperationTests.test_power_class = expectedFailure(InplaceSetOperationTests.test_power_class)
# InplaceSetOperationTests.test_lshift_class = expectedFailure(InplaceSetOperationTests.test_lshift_class)
# InplaceSetOperationTests.test_rshift_class = expectedFailure(InplaceSetOperationTests.test_rshift_class)
# InplaceSetOperationTests.test_and_class = expectedFailure(InplaceSetOperationTests.test_and_class)
# InplaceSetOperationTests.test_xor_class = expectedFailure(InplaceSetOperationTests.test_xor_class)
# InplaceSetOperationTests.test_or_class = expectedFailure(InplaceSetOperationTests.test_or_class)

# InplaceSetOperationTests.test_add_complex = expectedFailure(InplaceSetOperationTests.test_add_complex)
# InplaceSetOperationTests.test_subtract_complex = expectedFailure(InplaceSetOperationTests.test_subtract_complex)
# InplaceSetOperationTests.test_multiply_complex = expectedFailure(InplaceSetOperationTests.test_multiply_complex)
# InplaceSetOperationTests.test_floor_divide_complex = expectedFailure(InplaceSetOperationTests.test_floor_divide_complex)
# InplaceSetOperationTests.test_true_divide_complex = expectedFailure(InplaceSetOperationTests.test_true_divide_complex)
# InplaceSetOperationTests.test_modulo_complex = expectedFailure(InplaceSetOperationTests.test_modulo_complex)
# InplaceSetOperationTests.test_power_complex = expectedFailure(InplaceSetOperationTests.test_power_complex)
# InplaceSetOperationTests.test_lshift_complex = expectedFailure(InplaceSetOperationTests.test_lshift_complex)
# InplaceSetOperationTests.test_rshift_complex = expectedFailure(InplaceSetOperationTests.test_rshift_complex)
# InplaceSetOperationTests.test_and_complex = expectedFailure(InplaceSetOperationTests.test_and_complex)
# InplaceSetOperationTests.test_xor_complex = expectedFailure(InplaceSetOperationTests.test_xor_complex)
# InplaceSetOperationTests.test_or_complex = expectedFailure(InplaceSetOperationTests.test_or_complex)

InplaceSetOperationTests.test_add_dict = expectedFailure(InplaceSetOperationTests.test_add_dict)
InplaceSetOperationTests.test_subtract_dict = expectedFailure(InplaceSetOperationTests.test_subtract_dict)
InplaceSetOperationTests.test_multiply_dict = expectedFailure(InplaceSetOperationTests.test_multiply_dict)
InplaceSetOperationTests.test_floor_divide_dict = expectedFailure(InplaceSetOperationTests.test_floor_divide_dict)
InplaceSetOperationTests.test_true_divide_dict = expectedFailure(InplaceSetOperationTests.test_true_divide_dict)
InplaceSetOperationTests.test_modulo_dict = expectedFailure(InplaceSetOperationTests.test_modulo_dict)
InplaceSetOperationTests.test_power_dict = expectedFailure(InplaceSetOperationTests.test_power_dict)
InplaceSetOperationTests.test_lshift_dict = expectedFailure(InplaceSetOperationTests.test_lshift_dict)
InplaceSetOperationTests.test_rshift_dict = expectedFailure(InplaceSetOperationTests.test_rshift_dict)
InplaceSetOperationTests.test_and_dict = expectedFailure(InplaceSetOperationTests.test_and_dict)
InplaceSetOperationTests.test_xor_dict = expectedFailure(InplaceSetOperationTests.test_xor_dict)
InplaceSetOperationTests.test_or_dict = expectedFailure(InplaceSetOperationTests.test_or_dict)

InplaceSetOperationTests.test_add_float = expectedFailure(InplaceSetOperationTests.test_add_float)
InplaceSetOperationTests.test_subtract_float = expectedFailure(InplaceSetOperationTests.test_subtract_float)
InplaceSetOperationTests.test_multiply_float = expectedFailure(InplaceSetOperationTests.test_multiply_float)
InplaceSetOperationTests.test_floor_divide_float = expectedFailure(InplaceSetOperationTests.test_floor_divide_float)
InplaceSetOperationTests.test_true_divide_float = expectedFailure(InplaceSetOperationTests.test_true_divide_float)
InplaceSetOperationTests.test_modulo_float = expectedFailure(InplaceSetOperationTests.test_modulo_float)
InplaceSetOperationTests.test_power_float = expectedFailure(InplaceSetOperationTests.test_power_float)
InplaceSetOperationTests.test_lshift_float = expectedFailure(InplaceSetOperationTests.test_lshift_float)
InplaceSetOperationTests.test_rshift_float = expectedFailure(InplaceSetOperationTests.test_rshift_float)
InplaceSetOperationTests.test_and_float = expectedFailure(InplaceSetOperationTests.test_and_float)
InplaceSetOperationTests.test_xor_float = expectedFailure(InplaceSetOperationTests.test_xor_float)
InplaceSetOperationTests.test_or_float = expectedFailure(InplaceSetOperationTests.test_or_float)

# InplaceSetOperationTests.test_add_frozenset = expectedFailure(InplaceSetOperationTests.test_add_frozenset)
# InplaceSetOperationTests.test_subtract_frozenset = expectedFailure(InplaceSetOperationTests.test_subtract_frozenset)
# InplaceSetOperationTests.test_multiply_frozenset = expectedFailure(InplaceSetOperationTests.test_multiply_frozenset)
# InplaceSetOperationTests.test_floor_divide_frozenset = expectedFailure(InplaceSetOperationTests.test_floor_divide_frozenset)
# InplaceSetOperationTests.test_true_divide_frozenset = expectedFailure(InplaceSetOperationTests.test_true_divide_frozenset)
# InplaceSetOperationTests.test_modulo_frozenset = expectedFailure(InplaceSetOperationTests.test_modulo_frozenset)
# InplaceSetOperationTests.test_power_frozenset = expectedFailure(InplaceSetOperationTests.test_power_frozenset)
# InplaceSetOperationTests.test_lshift_frozenset = expectedFailure(InplaceSetOperationTests.test_lshift_frozenset)
# InplaceSetOperationTests.test_rshift_frozenset = expectedFailure(InplaceSetOperationTests.test_rshift_frozenset)
# InplaceSetOperationTests.test_and_frozenset = expectedFailure(InplaceSetOperationTests.test_and_frozenset)
# InplaceSetOperationTests.test_xor_frozenset = expectedFailure(InplaceSetOperationTests.test_xor_frozenset)
# InplaceSetOperationTests.test_or_frozenset = expectedFailure(InplaceSetOperationTests.test_or_frozenset)

InplaceSetOperationTests.test_add_int = expectedFailure(InplaceSetOperationTests.test_add_int)
InplaceSetOperationTests.test_subtract_int = expectedFailure(InplaceSetOperationTests.test_subtract_int)
InplaceSetOperationTests.test_multiply_int = expectedFailure(InplaceSetOperationTests.test_multiply_int)
InplaceSetOperationTests.test_floor_divide_int = expectedFailure(InplaceSetOperationTests.test_floor_divide_int)
InplaceSetOperationTests.test_true_divide_int = expectedFailure(InplaceSetOperationTests.test_true_divide_int)
InplaceSetOperationTests.test_modulo_int = expectedFailure(InplaceSetOperationTests.test_modulo_int)
InplaceSetOperationTests.test_power_int = expectedFailure(InplaceSetOperationTests.test_power_int)
InplaceSetOperationTests.test_lshift_int = expectedFailure(InplaceSetOperationTests.test_lshift_int)
InplaceSetOperationTests.test_rshift_int = expectedFailure(InplaceSetOperationTests.test_rshift_int)
InplaceSetOperationTests.test_and_int = expectedFailure(InplaceSetOperationTests.test_and_int)
InplaceSetOperationTests.test_xor_int = expectedFailure(InplaceSetOperationTests.test_xor_int)
InplaceSetOperationTests.test_or_int = expectedFailure(InplaceSetOperationTests.test_or_int)

InplaceSetOperationTests.test_add_list = expectedFailure(InplaceSetOperationTests.test_add_list)
InplaceSetOperationTests.test_subtract_list = expectedFailure(InplaceSetOperationTests.test_subtract_list)
InplaceSetOperationTests.test_multiply_list = expectedFailure(InplaceSetOperationTests.test_multiply_list)
InplaceSetOperationTests.test_floor_divide_list = expectedFailure(InplaceSetOperationTests.test_floor_divide_list)
InplaceSetOperationTests.test_true_divide_list = expectedFailure(InplaceSetOperationTests.test_true_divide_list)
InplaceSetOperationTests.test_modulo_list = expectedFailure(InplaceSetOperationTests.test_modulo_list)
InplaceSetOperationTests.test_power_list = expectedFailure(InplaceSetOperationTests.test_power_list)
InplaceSetOperationTests.test_lshift_list = expectedFailure(InplaceSetOperationTests.test_lshift_list)
InplaceSetOperationTests.test_rshift_list = expectedFailure(InplaceSetOperationTests.test_rshift_list)
InplaceSetOperationTests.test_and_list = expectedFailure(InplaceSetOperationTests.test_and_list)
InplaceSetOperationTests.test_xor_list = expectedFailure(InplaceSetOperationTests.test_xor_list)
InplaceSetOperationTests.test_or_list = expectedFailure(InplaceSetOperationTests.test_or_list)

InplaceSetOperationTests.test_add_set = expectedFailure(InplaceSetOperationTests.test_add_set)
InplaceSetOperationTests.test_subtract_set = expectedFailure(InplaceSetOperationTests.test_subtract_set)
InplaceSetOperationTests.test_multiply_set = expectedFailure(InplaceSetOperationTests.test_multiply_set)
InplaceSetOperationTests.test_floor_divide_set = expectedFailure(InplaceSetOperationTests.test_floor_divide_set)
InplaceSetOperationTests.test_true_divide_set = expectedFailure(InplaceSetOperationTests.test_true_divide_set)
InplaceSetOperationTests.test_modulo_set = expectedFailure(InplaceSetOperationTests.test_modulo_set)
InplaceSetOperationTests.test_power_set = expectedFailure(InplaceSetOperationTests.test_power_set)
InplaceSetOperationTests.test_lshift_set = expectedFailure(InplaceSetOperationTests.test_lshift_set)
InplaceSetOperationTests.test_rshift_set = expectedFailure(InplaceSetOperationTests.test_rshift_set)
InplaceSetOperationTests.test_and_set = expectedFailure(InplaceSetOperationTests.test_and_set)
InplaceSetOperationTests.test_xor_set = expectedFailure(InplaceSetOperationTests.test_xor_set)
InplaceSetOperationTests.test_or_set = expectedFailure(InplaceSetOperationTests.test_or_set)

InplaceSetOperationTests.test_add_str = expectedFailure(InplaceSetOperationTests.test_add_str)
InplaceSetOperationTests.test_subtract_str = expectedFailure(InplaceSetOperationTests.test_subtract_str)
InplaceSetOperationTests.test_multiply_str = expectedFailure(InplaceSetOperationTests.test_multiply_str)
InplaceSetOperationTests.test_floor_divide_str = expectedFailure(InplaceSetOperationTests.test_floor_divide_str)
InplaceSetOperationTests.test_true_divide_str = expectedFailure(InplaceSetOperationTests.test_true_divide_str)
InplaceSetOperationTests.test_modulo_str = expectedFailure(InplaceSetOperationTests.test_modulo_str)
InplaceSetOperationTests.test_power_str = expectedFailure(InplaceSetOperationTests.test_power_str)
InplaceSetOperationTests.test_lshift_str = expectedFailure(InplaceSetOperationTests.test_lshift_str)
InplaceSetOperationTests.test_rshift_str = expectedFailure(InplaceSetOperationTests.test_rshift_str)
InplaceSetOperationTests.test_and_str = expectedFailure(InplaceSetOperationTests.test_and_str)
InplaceSetOperationTests.test_xor_str = expectedFailure(InplaceSetOperationTests.test_xor_str)
InplaceSetOperationTests.test_or_str = expectedFailure(InplaceSetOperationTests.test_or_str)

InplaceSetOperationTests.test_add_tuple = expectedFailure(InplaceSetOperationTests.test_add_tuple)
InplaceSetOperationTests.test_subtract_tuple = expectedFailure(InplaceSetOperationTests.test_subtract_tuple)
InplaceSetOperationTests.test_multiply_tuple = expectedFailure(InplaceSetOperationTests.test_multiply_tuple)
InplaceSetOperationTests.test_floor_divide_tuple = expectedFailure(InplaceSetOperationTests.test_floor_divide_tuple)
InplaceSetOperationTests.test_true_divide_tuple = expectedFailure(InplaceSetOperationTests.test_true_divide_tuple)
InplaceSetOperationTests.test_modulo_tuple = expectedFailure(InplaceSetOperationTests.test_modulo_tuple)
InplaceSetOperationTests.test_power_tuple = expectedFailure(InplaceSetOperationTests.test_power_tuple)
InplaceSetOperationTests.test_lshift_tuple = expectedFailure(InplaceSetOperationTests.test_lshift_tuple)
InplaceSetOperationTests.test_rshift_tuple = expectedFailure(InplaceSetOperationTests.test_rshift_tuple)
InplaceSetOperationTests.test_and_tuple = expectedFailure(InplaceSetOperationTests.test_and_tuple)
InplaceSetOperationTests.test_xor_tuple = expectedFailure(InplaceSetOperationTests.test_xor_tuple)
InplaceSetOperationTests.test_or_tuple = expectedFailure(InplaceSetOperationTests.test_or_tuple)
