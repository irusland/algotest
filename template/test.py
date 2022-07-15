import sys
import time
from io import StringIO

from .main import main


class TestAlgo:
    def test_algo(self, input_str, output_str):
        old_stdin = sys.stdin
        sys.stdin = StringIO(str(input_str))
        backup = sys.stdout
        sys.stdout = StringIO()

        a = time.perf_counter()
        main()
        runtime = time.perf_counter() - a

        actual_output_str = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = backup
        sys.stdin.close()
        sys.stdin = old_stdin

        print()
        print(f'OUTPUT    >>> \n{actual_output_str}')
        print(f'EXPECTED  >>> \n{output_str}')
        print(f'TIME >>> {runtime:.5f}s')

        assert actual_output_str == output_str
