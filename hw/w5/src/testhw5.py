from ROW import *
from COLS import *
from utils import *
from NUM import NUM
from statistics import mode

def test_cols_add():
    row_data = {'A': 10, 'b': 5, 'c': 6, 'D': 1, 'E!': 5}
    row = ROW(cells=list(row_data.keys()))
    cols = COLS(row)
    row_vals = ROW(list(row_data.values()))
    cols.add(row_vals)
    row_data = {'A': 20, 'b': 3, 'c': 2, 'D': 11, 'E!': 2}
    row_vals = ROW(list(row_data.values()))
    cols.add(row_vals)

    assert (
        cols.x[0].n == 2 and
        cols.y[4].mu == 3.5 and
        cols.klass.txt == 'E!'
    )

def test_num_mid():
    num = NUM()
    vals = [1, 2, 3, 4]
    for val in vals:
        num.add(val)
    expected_mean = 0
    for val in vals:
        expected_mean += val
    expected_mean /= len(vals)
    assert num.mid() == expected_mean
    
def test_num_lo():
    num = NUM()
    vals = [19,89,112,12]
    for val in vals:
        num.add(val)
    assert num.lo == min(vals)
    
def test_sym_mid():
    sym = SYM()
    vals = [1, 2, 3, 4, 3]
    for val in vals:
        sym.add(val)
    mid = mode(vals)
    assert sym.mid() == mid




def test_div_with_empty_values():
        sym_instance = SYM()
        result = sym_instance.div()
        assert result == 0  # Entropy of an empty set should be 0.

def test_div_with_multiple_values():
        sym_instance = SYM()
        sym_instance.add('value1')
        sym_instance.add('value2')
        sym_instance.add('value3')
        result = sym_instance.div()
        # Entropy for a set with different values should be greater than 0.
        assert result > 0

test_cols_add()
test_num_mid()
test_num_lo()

