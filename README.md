[![Total alerts](https://img.shields.io/lgtm/alerts/g/mchoji/wtg-seal.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/mchoji/wtg-seal/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/mchoji/wtg-seal.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/mchoji/wtg-seal/context:python)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/09009dc4036a4b5c8b1e5d77fd5f31bf)](https://www.codacy.com/manual/mchoji/wtg-seal?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mchoji/wtg-seal&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/mchoji/wtg-seal/badge.svg?branch=master)](https://coveralls.io/github/mchoji/wtg-seal?branch=master)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# WTG-SEAL
A **W**eb **T**raffic **G**enerator based on **S**URG**E**, St**a**tistics and
**L**ocust

## Overview
WTG-SEAL is a web traffic generator based on a statistical approach inspired
by SURGE <span id="a1">[[1]](#f1)</span> and implemented using
[Locust](https://github.com/locustio/locust).

## Contributing

### Pre-commit hooks
In order to make sure the hooks will run, please don't forget to install the
`pre-commit` package:

```shell
cd wtg-seal
pipenv install --dev
pipenv run pre-commit install
# update the hooks to the latest version
pipenv run pre-commit autoupdate
```

## License
WTG-SEAL is licensed under the GNU General Public License v3.0.
See [LICENSE](LICENSE.txt) for more information.

## References
<b id="f1">[1]</b> Barford, P., & Crovella, M. (1998, June). Generating
representative web workloads for network and server performance evaluation.
In *Proceedings of the 1998 ACM SIGMETRICS joint international conference on
Measurement and modeling of computer systems* (pp. 151-160). [↩](#a1)
