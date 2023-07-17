import crypto_lib
import pytest

test_cases_md5 = [
    ('qwerty', 'd8578edf8458ce06fbc5bb76a58c5ca4'),
    ('6666666777', '6eec3f3f0c7758333adca3af93213758')
]


@pytest.mark.parametrize('value, expected', test_cases_md5)
def test_encode_md5(value, expected):
    assert crypto_lib.encode_md5(value) == expected
