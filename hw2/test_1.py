import subprocess
import pytest

INTERPRETER = 'python3'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'fact': [
        (5, 120)
    ],
    'fib': [
        (5,[0, 1, 1, 8, 729])
    ],
    'show': [
(("Alice", "50000"), "Alice: 50000 R"),
(("Bob", ""), "Bob: 1000000 R")
],
    'susub': [
        ((5, 4), (9,1))
    ],
    'email': [
(5, ["test@example.com", "invalid-email", "user@domain.com", "another@website.org", "fakeemail.net"],
["another@website.org", "test@example.com", "user@domain.com"]),
(2, ["8642@mailru", "whatsyourdamage11@gmail.com"],
["whatsyourdamage11@gmail.com"]),
(1,['sjhdj'],[])
],
    'format_phone_number': [
('88005553535', '+7 (800) 555-35-35'),
('+79123456789', '+7 (912) 345-67-89'),
('8 800 555 35 35', '+7 (800) 555-35-35')
],
    'scores': [
([(70, 80, 90), (75, 85, 95), (60, 70, 80)], (68.3, 78.3, 88.3)),
([(80, 90, 100), (85, 95, 105)], (82.5, 92.5, 102.5))
],
    'my_sum_argv': [
([1, 2, 3], 6),
([10, 20, 30, 40], 100),
([5.5, 3.3, 1.2], 10)
],
    'sum': [
([1, 2, 3], 6),
([], 0),
([10, 20, 30, 40], 100),
([-1, -2, -3, -4], -10)
]
}

from fact import fact_it

@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected
from  fibonacci import fibonacci

@pytest.mark.parametrize("input_data, expected", test_data['fib'])
def test_fib(input_data, expected):
    assert fibonacci(input_data) == expected
from show_employee import show
@pytest.mark.parametrize("input_data, expected", test_data['show'])
def test_show(input_data, expected):
    assert show(*input_data) == expected

from sum_and_sub import sum_and_sub
@pytest.mark.parametrize("input_data, expected", test_data['susub'])
def test_sub(input_data, expected):
    assert sum_and_sub(*input_data) == expected

from email_validation import is_valid_email, fun

@pytest.mark.parametrize("N, emails, expected", test_data['email'])
def test_email_checker(N, emails, expected):
    result = fun(N, emails)
    assert result == expected
    for email in result:
        assert is_valid_email(email)
from phone_number import format_phone_number

@pytest.mark.parametrize("input_data, expected", test_data['format_phone_number'])
def test_format_phone_number(input_data, expected):
    assert format_phone_number(input_data) == expected


from average_scores import compute_average_scores
@pytest.mark.parametrize("input_data, expected", test_data['scores'])
def test_compute_average_scores(input_data, expected):
    assert compute_average_scores(input_data) == expected


from my_sum_argv import my_sum

@pytest.mark.parametrize("input_data, expected", test_data['my_sum_argv'])
def test_my_sum_argv(input_data, expected):
    assert my_sum(*input_data) == expected
from my_sum import my_sum

@pytest.mark.parametrize("input_data, expected", test_data['sum'])
def test_my_sum(input_data, expected):
    assert my_sum(*input_data) == expected
    
from file_search import search_file
def test_search_file():
    test_data = {
'file_found': {
'filename': 'd.txt',
'directory': 'C:/Users/zarin/OneDrive/Рабочий стол/pythondev/hw2',
'expected_output': True
},
'file_not_found': {
'filename': 'non_existent_file.txt',
'directory': '/path/to/directory',
'expected_output': False
}
}
    for test_case, data in test_data.items():
        assert search_file(data['filename'], data['directory']) == data['expected_output']
import os
from files_sort import sort_files
def test_sort_files(tmp_path):

    test_dir = tmp_path / "test_files"
    test_dir.mkdir()
    test_files = [
        "a.txt",
        "b.txt",
]

    for file in test_files:
        with open(test_dir / file, "w") as f:
            f.write("Test content")

    sorted_files = sort_files(test_dir)

    expected_result = [
        "a.txt",
        "b.txt",
    ]

    assert sorted_files == expected_result