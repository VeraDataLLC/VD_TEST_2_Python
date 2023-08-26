import hashlib

import pandas as pd
import pytest
import pandas._testing as pd_testing

import files
from tasks import *   # <--- Your functions here


# 1. Say Hi, VeraData!
def test_say_hi():
    assert say_hi() == "Hi, VeraData!"


# 2. Load a CSV file.
# For every column, determine the count of entries that are:
#     Entirely in lowercase (LowerCase).
#     Entirely in uppercase (UpperCase).
#     Neither entirely lowercase nor entirely uppercase (OtherCase).
def test_count_cases():
    expected = pd.DataFrame({
        'first': [1, 999, 0],
        'last': [1, 999, 0],
        'address': [1, 999, 0],
        'city': [1, 999, 0],
        'state': [1, 999, 0],
        'zip5': [0, 0, 1000],
        'zip4': [0, 0, 1000]
    }, index=['LowerCase', 'UpperCase', 'OhterCase'])
    result = count_case_for_each_column(files.sample2)
    pd_testing.assert_frame_equal(result, expected)


# 3. Load a CSV file.
# For the columns ADDRESS, ZIP5, and ZIP4:
#     Shift the first character of each column N positions downward. If characters are pushed out at the bottom, they should reappear at the top.
#     Similarly, shift the third character of each column N positions upward. If characters are pushed out at the top, they should reappear at the bottom.
# Output the result in the 'commaFlat' file format: like a standard flat file, but with columns separated by commas. Expected column widths are: [20,20,30,20,2,5,4].
def test_move_chars():
    expected = files.result3
    result_file = move_chars(files.sample_flat3, 2)

    expected_hash = _calculate_file_hash(expected)
    result_hash = _calculate_file_hash(result_file)
    
    assert expected_hash == result_hash, "Files are different!"



### Help methods

def _calculate_file_hash(file_path, algorithm='md5'):
    hasher = hashlib.new(algorithm)
    with open(file_path, 'rb') as file:
        while chunk := file.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()