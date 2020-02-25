from wtgseal import utils


def test_parse_objects(datadir):
    expected = [
        [1],
        [1, 2, 3],
        [4, 5, 6, 7, 8, 9, 10]
    ]
    with (datadir / 'objout.txt').open() as f:
        parsed = utils.parse_objects(f)
    assert parsed is not None
    assert expected == parsed
