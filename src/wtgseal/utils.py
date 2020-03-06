"""Utilities for wtg-seal.

This module offers utilities function for wtg-seal, mainly focused on
file parsing.

"""

from typing import Counter, Generator, List, TextIO  # noqa


def parse_objects(file: TextIO,
                  /) -> Generator[List[str], None, None]:  # noqa: E225
    """Parse a text file containing objects definitions into lists.

    Read a file containing web objects representations and generates
    lists of URIs related to each object.

    Parameters
    ----------
    file : {TextIO}
        A file handler to the file to be parsed. The file should contain
        one or more lines, which being a space-separated list of
        integers. Each line represents an object to be retrieved from a
        web server. An object is composed by one or more files, given by
        the integers.

    Yields
    ------
    List[str]
        The representation of the next object, *i.e.* the URIs of the
        files that compose the object.

    Notes
    -----
    Ideally, `file` is the file `objout.txt` generated by the program
    `objects`, part of SURGE [1]_.

    References
    ----------
    .. [1] Barford, P., & Crovella, M. (1998, June). Generating
       representative web workloads for network and server performance
       evaluation. In *Proceedings of the 1998 ACM SIGMETRICS joint
       international conference on Measurement and modeling of computer
       systems* (pp. 151-160).

    """
    for line in file:
        yield [f'/{x}.txt' for x in line.split()]


def parse_requests(file: TextIO,
                   /) -> Generator[int, None, None]:  # noqa: E225
    """Parse a text file containing a sequence of objects requests.

    Read a file containing a sequence of object identifiers which was
    to be requested to a web server.

    Parameters
    ----------
    file : {TextIO}
        A file handler to the file to be parsed. The file should contain
        one or more lines with an integer in each of them.

    Yields
    ------
    int
        The index of the next object to be requested.

    Notes
    -----
    Ideally, `file` is the file `name.txt` generated by the program
    `lru`, part of SURGE [1]_.

    References
    ----------
    .. [1] Barford, P., & Crovella, M. (1998, June). Generating
       representative web workloads for network and server performance
       evaluation. In *Proceedings of the 1998 ACM SIGMETRICS joint
       international conference on Measurement and modeling of computer
       systems* (pp. 151-160).

    """
    for x in file:
        yield int(x)


def count_requests(file: TextIO, /) -> Counter:  # noqa: E225
    """Count the number of requests for each object.

    Count the number of requests made for each object based on a
    given sequence of object requests.

    Parameters
    ----------
    file : {TextIO}
        A file containing a sequence of integers representing indexes of
        objects in a web server.

    Returns
    -------
    Frequency

        A `collection.Counter` with the frequencies for each object.

    See Also
    --------
        parse_requests

    """
    parser = parse_requests(file)
    frequencies = Counter(parser)
    return frequencies


def calc_weights(freqs: Counter) -> Counter:
    weights = Counter(freqs)
    _, least = freqs.most_common()[-1]
    for key in weights:
        weights[key] = round(weights[key] / least)
    return weights
