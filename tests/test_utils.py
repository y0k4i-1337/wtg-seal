from collections import Counter

from wtgseal import utils


def test_parse_objects(datadir):
    expected = [
        [1],
        [1, 2, 3],
        [4, 5, 6, 7, 8, 9, 10]
    ]
    with (datadir / 'objout.txt').open() as f:
        it = utils.parse_objects(f)
        for i, obj in enumerate(it):
            assert obj == expected[i]


def test_parse_requests(datadir):
    expected = [1, 5, 3, 1, 1]
    with (datadir / 'name.txt').open() as f:
        it = utils.parse_requests(f)
        assert expected == list(it)


def test_count_requests(datadir):
    expected = Counter({1: 3, 3: 1, 5: 1})
    with (datadir / 'name.txt').open() as f:
        frequencies = utils.count_requests(f)
        assert sorted(expected.most_common()) == sorted(frequencies.most_common())
