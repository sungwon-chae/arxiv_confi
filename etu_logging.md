python -c "
import sys
sys.path.append('.')
from etu.utils import *

# 사용 가능한 함수들 확인
print('=== etu.utils에서 사용 가능한 함수들 ===')
functions = [name for name in dir() if not name.startswith('_')]
for func in functions:
    print(f'  {func}')

# get_data 함수의 내부 구조 확인
print('\\n=== get_data 함수 내부 구조 ===')
import inspect
print(inspect.getsource(get_data))
"
