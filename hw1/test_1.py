import subprocess
import pytest

INTERPRETER = 'python'

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
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6', 'Weird'),
        ('22', 'Not Weird')
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50']),
        (['20', '15'], ['35', '5', '300'])
    ],
    'loops': [
        ('3',['0','1','4']),
        ('5',['0','1','4','9','16']),
        ('8',['0','1','4','9','16','25','36','49'])
    ],
    'print': [
        ('3',['123']),
        ('8',['12345678']),
        ('1',['1']),
        ('9',['123456789'])
        
    ],
    'second': [
        (['3','3 1 32'],['3']),
        (['8','8 6 32 423 653 6343 3 32'],['653']),
        (['4','8 6 4 2'],['6']),
        (['6','0 10 9 123'],['10'])
        
    ]
    ,
    'division': [
        (['3','5'],['0','0.6']),
        (['5','2'],['2','2.5']),
        (['9','3'],['3','3.0']),
        (['9','0'],['0'])
    ],
    'swap': [
        (['DELTARUNE'],['deltarune']),
        (['The Boys'],['tHE bOYS']),
        (['fKDdj'],['FkdDJ'])
    ],
    'splitjoin': [
        (['this is string'],['this-is-string']),
        (['The Boys'],['The-Boys']),
        (['fKdssd dsdds ds'],['fKdssd-dsdds-ds']),
        (['4 2 5 52'],['4-2-5-52'])
    ],
   'year': [
       (['2000'],['True']),
       (['2024'],['True']),
       (['2023'],['False']),
       (['1996'],['True']),
       (['2014'],['False'])
    
   ],
      'happy': [
       (['3 2','1 5 3','3 1','5 7'],['1']),
       (['4 2','8 6 4 2','4 2','8 6'],['0']),
       (['6 3','8 4 2 5 1 0','5 1 0','7 12 10'],['3'])
       
   ],
      'lists': [    
       (['4','append 1','append 2','insert 1 3','print'],['[1, 3, 2]']),
       (['1','print'],['[]']),
       (['6','append 1','insert 0 2','insert 1 9','pop','reverse','print'],['[9, 2]'])
   ]
    ,
   'nested': [
       (['2','Harry','202','SJ','20'],['SJ']),
       (['3','VERONICA','89','JD','90','KURT','43'],['VERONICA']),
       (['5','Кирилл','0','Федя','1','Валера','92','Юра','1','Tолик','1'],['Tолик','Федя','Юра']),
       (['5','bon','30','anna','31','ally','30','berny','30','alice','31','bendy','14'],['ally','berny','bon'])
   ],
   'anagram': [
       (['UNDERTALE','DELTARUNE'],['YES']),
       (['IAMLORDVOLDEMORT','TOMMARVOLORIDDLE'],['YES']),
       (['ASRIELDREEMURR','SERIALMURDERER'],['YES']),
       (['KRIS','CHARA'],['NO']),
   
   ],
   'matrix': [
       (['3','1 2 3','4 5 6','7 8 9','9 8 7','6 5 4','3 2 1'],['30 24 18','84 69 54','138 114 90']),
       (['4','8 6 4 2','4 5 6 7','7 8 8 9','9 2 8 7','6 5 2 4','3 2 5 1','3 4 2 1','9 4 8 1'],['96 76 70 44','120 82 101 34','171 119 142 53','147 109 100 53'])
       
       
   ],
   'minions': [
       (['BANANA'],['Stuart 12']),
       (['SUS'],['Stuart 4']),
       (['NANI'],['Stuart 6']),
       (['ALENKA'],['Kevin 11'])
   ],
   'ship': [
       (['40 3','1 27 1500','2 17 1000','3 20 100'],['2 17.00 1000.00','1 23.00 1277.78']),
        (['100 2','золото 95 1000','серебро 20 150'],['золото 95.00 1000.00','серебро 5.00 37.50']),
        (['100 4','1 10 15000','2 87 10000','3 500 500','4 250 500'],['1 10.00 15000.00','2 87.00 10000.00','4 3.00 6.00'])
   ],
   'metro': [
     (['3','10 20','20 34','15 20','20'],['3']),
      (['1','17 20','17'],['1'])
 ]
}

def test_hello_world():
    assert run_script('hello_world.py') == 'Hello, world!'
    
def test_max():
    assert run_script('max_word.py') == 'сосредоточенности'
def test_price_sum():
    assert run_script('price_sum.py') == '6842.84 5891.06 6810.90'
@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['print'])  
def test_print(input_data, expected):
    assert run_script('print_function.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['second'])  
def test_second(input_data, expected):
    assert run_script('second_score.py', input_data).split('\n') == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['division'])  
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['swap'])  
def test_swap(input_data, expected):
    assert run_script('swap_case.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['splitjoin'])  
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data).split('\n') == expected
    

@pytest.mark.parametrize("input_data, expected", test_data['year'])  
def test_year(input_data, expected):
    assert run_script('is_leap.py', input_data).split('\n') == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['happy'])  
def test_happy(input_data, expected):
    assert run_script('happiness.py', input_data).split('\n') == expected
    

    
@pytest.mark.parametrize("input_data, expected", test_data['nested'])  
def test_nested(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['lists'])  
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['anagram'])  
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['matrix'])  
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['minions'])  
def test_minions(input_data, expected):
    assert run_script('minion_game.py', input_data).split('\n') == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['ship'])  
def test_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data).split('\n') == expected
    
@pytest.mark.parametrize("input_data, expected", test_data['metro'])  
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data).split('\n') == expected