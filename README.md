# django-dynamic-shields

[![sphinx](https://github.com/Uno-Takashi/django-dynamic-shields/actions/workflows/sphinx.yml/badge.svg?branch=main&event=push)](https://github.com/Uno-Takashi/django-dynamic-shields/actions/workflows/sphinx.yml)
[![Code Quality](https://github.com/Uno-Takashi/django-dynamic-shields/actions/workflows/code-quality.yml/badge.svg?branch=main&event=push)](https://github.com/Uno-Takashi/django-dynamic-shields/actions/workflows/code-quality.yml)
[![security](https://github.com/Uno-Takashi/django-dynamic-shields/actions/workflows/security.yml/badge.svg?branch=main)](https://github.com/Uno-Takashi/django-dynamic-shields/actions/workflows/security.yml)

[![codecov](https://codecov.io/gh/Uno-Takashi/django-dynamic-shields/branch/main/graph/badge.svg?token=3CWnrX8w7n)](https://codecov.io/gh/Uno-Takashi/django-dynamic-shields)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/django-dynamic-shields?label=PyPI%20download&logo=python)](https://pypi.org/project/django-dynamic-shields/)
[![PyPI](https://img.shields.io/pypi/v/django-dynamic-shields?label=PyPI&logo=python)](https://pypi.org/project/django-dynamic-shields/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Uno-Takashi/django-dynamic-shields/blob/main/LICENSE)

## 📚 Overview

[Shields.io](https://shields.io/) is one of the great inventions in human history. Everyone has collected badges and stickers as a child. In other words, it is one of the fundamental human needs to stick a badge.

With django-dynamic-badge, the display can be changed dynamically using information from a server built with [Django](https://www.djangoproject.com/).

For example, create a badge with the number of active users today, the number of times the function has been used, and the results of the server health check.

## 💾 Install

Published on [PyPI](https://pypi.org/project/django-dynamic-shields/). It can be installed with the following command.

```shell
pip install django-dynamic-shields
```

Alternatively, you can download and install the .whl file from the [release](https://github.com/Uno-Takashi/django-dynamic-shields/releases).

## 📔 Document

Uploaded to the following github pages

- [django-dynamic-shields documentation](https://uno-takashi.github.io/django-dynamic-shields/)

## 🎮 Usage

## ⚒️ Develop

### Preparation

Development requires installation of [Poetry](https://python-poetry.org/).

- [Introduction | Documentation | Poetry - Python dependency management and packaging made easy](https://python-poetry.org/docs/)

[Watchman](https://facebook.github.io/watchman/) is required to run code checks with pyre. Although not required for development, code that fails pyre-check cannot be merged.

- [Installation | Watchman](https://facebook.github.io/watchman/docs/install.html)

After installing the required software, execute the following commands to set up the development environment.

```shell
poetry install
```

### Code Check

This repository uses Github actions for code checking. These actions are automatically executed when you push, but you can also execute them in your local environment before pushing.

#### pytest

[![codecov](https://codecov.io/gh/Uno-Takashi/django-dynamic-shields/branch/main/graph/badge.svg?token=3CWnrX8w7n)](https://codecov.io/gh/Uno-Takashi/django-dynamic-shields)

Must pass CI by pytest.

```shell
poetry run pytest --cov=django_dynamic_shields --cov-report=xml --workers auto
```

#### lizard


lizard is a tool for measuring CCN. lizard allows us to block merging of overly complex code.

```shell
poetry run lizard ./django_dynamic_shields/
```

#### pyre


Pyre is a performant type checker for Python compliant with PEP 484.

```shell
poetry run pyre
```

#### bndit

bandit is a static analysis tool for python. It blocks vulnerable code.

```shell
poetry run bandit django_dynamic_shields -r 
```

#### python-taint

python-taint(pyt) is a static analysis tool for python. It blocks vulnerable code.

```shell
poetry run pyt -a D  ./django_dynamic_shields
```

### Other

Develop according to [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow)

If you have any questions, feel free to ask in the [Q&A](https://github.com/Uno-Takashi/django-dynamic-shields/discussions/categories/q-a)

## 📝 License

- [MIT License](https://github.com/Uno-Takashi/django-dynamic-shields/blob/main/LICENSE)

![GitHub watchers](https://img.shields.io/github/watchers/Uno-Takashi/django-dynamic-shields?style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/Uno-Takashi/django-dynamic-shields?style=social)
![GitHub forks](https://img.shields.io/github/forks/Uno-Takashi/django-dynamic-shields?style=social)
[![Python](https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=flat)](https://www.djangoproject.com/)
