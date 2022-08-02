import os
from pathlib import Path


DELIMITER = '////////////////////////////'


def parse_sample_file(filepath):
    buffer = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if DELIMITER in line:
                yield ''.join(buffer)
                buffer = []
                continue
            buffer.append(line)
        yield ''.join(buffer)


def pytest_generate_tests(metafunc):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    samples = Path(dir_path).parent / 'samples'

    if "input_str" in metafunc.fixturenames:
        metafunc.parametrize(
            ("test_name", "input_str", "output_str"),
            [(filepath.name, *parse_sample_file(filepath)) for filepath in samples.glob("*.txt")]
        )
