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
        (5, 120),
        (1, 1),
        (10,3628800)
    ],
    'fib': [
        (5,[0, 1, 1, 2, 3]),
         (10,[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    
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
],

'greeting_format': [
('John', 'Hello, John!')
],
'process_list': [
([1, 2, 3, 4, 5], [1, 4, 27, 16, 125]),
([-3, 0, 7, 8], [(-3)**3, 0**2, 7**3, 8**2])
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
        "b.py",
        "c.py",
        "b.txt",
        "a.py"
]

    for file in test_files:
        with open(test_dir / file, "w") as f:
            f.write("Test content")

    sorted_files = sort_files(test_dir)

    expected_result = [
        "a.py",
        "b.py",
        "c.py",
        "a.txt",
        "b.txt"
        
    ]

    assert sorted_files == expected_result
from log_decorator import greeting_format

@pytest.mark.parametrize("input_data, expected", test_data['greeting_format'])
def test_greeting_format(input_data, expected):
    assert greeting_format(input_data) == expected
def test_log_file_contents():
    with open('the.log', 'r') as file:
        lines = file.readlines()
    assert len(lines) > 0
    
from plane_angle import Point
from plane_angle import plane_angle
def test_subtraction():
    p1 = Point(1, 2, 3)
    p2 = Point(4, 5, 6)
    result = p1 - p2
    assert result.x == -3
    assert result.y == -3
    assert result.z == -3

def test_dot():
    p1 = Point(1, 2, 3)
    p2 = Point(4, 5, 6)
    result = p1.dot(p2)
    assert result == 32

def test_cross():
    p1 = Point(1, 2, 3)
    p2 = Point(4, 5, 6)
    result = p1.cross(p2)
    assert result.x == -3
    assert result.y == 6
    assert result.z == -3

def test_absolute():
    p = Point(3, 4, 0)
    result = p.absolute()
    assert result == 5

def test_plane_angle():
    a = Point(0, 0, 0)
    b = Point(1, 0, 0)
    c = Point(0, 1, 0)
    d = Point(0, 0, 1)
    result = plane_angle(a, b, c, d)
    assert result == 55
from circle_square_mk import circle_square_mk
from pytest import approx  
@pytest.mark.parametrize("r, n, expected", [
    (1, 1000, 3.14)
])
def test_circle_square_mk(r, n, expected):
    estimated_square = circle_square_mk(r, n)
    assert estimated_square == approx(expected, rel=0.1)
from process_list import process_list
@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list(input_data, expected):
    assert process_list(input_data) == expected
