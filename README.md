# cookiecutter-pylibrary

Cookiecutter template for a Python library.

*Notes*:

- There's a bare library using this template (if you're curious about the final result): <https://github.com/FragileTech/mloq_template>.


## Features

This is an "all inclusive" sort of template.

- Choice of various licenses.
- [Pytest](http://pytest.org/) for testing Python 3.9+, PyPy etc.
- *Optional* support for creating a tests matrix out of dependencies and python versions.
- [Codecov](http://codecov.io/) for coverage tracking (using Tox).
- Documentation with [Sphinx](http://sphinx-doc.org/), ready for [ReadTheDocs](https://readthedocs.org/).
- Configurations for:
  - [isort](https://pypi.org/project/isort)
  - [bumpversion](https://pypi.org/project/bump2version) ([bump2version](https://github.com/c4urself/bump2version) required)
  - [ruff](https://docs.astral.sh/ruff/) For linting and formatting your code.
- Packaging and code quality checks. This template comes with a tox environment (`check`) that will:
  - Check if your `README.md` is valid.
  - Check if the `MANIFEST.in` has any issues.

## Requirements

Projects using this template have these minimal dependencies:

- [Cookiecutter](https://github.com/audreyr/cookiecutter) - just for creating the project.
- [Setuptools](https://pypi.org/project/setuptools) - for building the package, wheels etc. Nowadays Setuptools is widely available, it shouldn't pose a problem :)

To get quickly started on a new system, just [install setuptools](https://pypi.org/project/setuptools#installation-instructions) and then [install pip](https://pip.pypa.io/en/latest/installing.html). That's the bare minimum required to install Tox and Cookiecutter. To install them, just run this in your shell or command prompt:

```bash
pip install cookiecutter
```

## Usage and options

This template is more involved than the regular [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

First generate your project:

```bash
cookiecutter gh:FragileTech/mloq-cookiecutter
```

You will be asked for these fields:

> **Note**: Fields that work together usually use the same prefix. If you answer "no" on the first one then the rest won't have any effect so just ignore them. Maybe in the future cookiecutter will allow option hiding or something like a wizard.

### `full_name`

**Default**:

```python
"Guillem Duran Ballester"
```

Main author of this library or application (used in `AUTHORS.md` and `pyproject.toml`).

Can be set in your `~/.cookiecutterrc` config file.

### `email`

**Default**:

```python
"guillem@fragile.tech"
```

Contact email of the author (used in `AUTHORS.md` and `pyproject.toml`).

Can be set in your `~/.cookiecutterrc` config file.

### `website`

**Default**:

```python
"https://fragile.tech"
```

Website of the author (used in `AUTHORS.md`).

Can be set in your `~/.cookiecutterrc` config file.

### `repo_username`

**Default**:

```python
"FragileTech"
```

GitHub username of this project (used for GitHub link).

Can be set in your `~/.cookiecutterrc` config file.

### `project_name`

**Default**:

```python
"MLOQ Template"
```

Verbose project name, used in headings (docs, readme, etc).

### `repo_hosting_domain`

**Default**:

```python
"github.com"
```

Use `"no"` for no hosting (various links will disappear). You can also use `"gitlab.com"` and such but various things will be broken.

### `repo_name`

**Default**:

```python
"mloq-template"
```

Repository name on GitHub (and project's root directory name).

### `package_name`

**Default**:

```python
"mloq_template"
```

Python package name (whatever you would import).

### `distribution_name`

**Default**:

```python
"mloq_template"
```

PyPI distribution name (what you would `pip install`).

### `module_name`

**Default**:

```python
"core"
```

This template assumes there's going to be an "implementation" module inside your package.

### `project_short_description`

**Default**:

```python
"An example package [...]"
```

One line description of the project (used in `README.md` and `pyproject.toml`).

### `release_date`

**Default**:

```python
"today"
```

Release date of the project (ISO 8601 format) default to today (used in `CHANGELOG.md`).

### `year`

**Default**:

```python
"now"
```

Copyright year (used in Sphinx `conf.py`).

### `version`

**Default**:

```python
"0.1.0"
```

Release version (see `.bumpversion.cfg` and in Sphinx `conf.py`).



Enables the use of [setuptools-scm](https://pypi.org/project/setuptools-scm/). You can continue using bumpversion with this enabled.

### `command_line_interface`

**Default**:

```python
"plain"
```

Option to enable a CLI (a bin/executable file). Available options:

- `plain` - a very simple command.
- `argparse` - a command implemented with `argparse`.
- `click` - a command implemented with [click](http://click.pocoo.org/) - which you can use to build more complex commands.
- `no` - no CLI at all.

### `command_line_interface_bin_name`

**Default**:

```python
"nameless"
```

Name of the CLI bin/executable file (set the console script name in `setup.py`).

### `license`

**Default**:

```python
"BSD license"
```

License to use. Available options:

- MIT license
- BSD license
- ISC license
- Apache Software License 2.0

What license to pick? https://choosealicense.com/


### `codecov`

**Default**:

```python
"yes"
```

Enable pushing coverage data to Codecov and add badge in `README.md`.

### `sphinx_docs`

**Default**:

```python
"yes"
```

Have Sphinx documentation.

### `sphinx_docs_hosting`

**Default**:

```python
"repo_name.readthedocs.io"
```

Leave as default if your documentation will be hosted on readthedocs. If your documentation will be hosted elsewhere (such as GitHub Pages or GitLab Pages), enter the top-level URL.

### `pypi_badge`

**Default**:

```python
"yes"
```

By default, this will insert links to your project's page on PyPI.org. If you choose `"no"`, then these links will not be created.

### `pypi_disable_upload`

**Default**:

```python
"no"
```

If you specifically want to be sure your package will never be accidentally uploaded to PyPI, you can pick `"yes"`.

## Developing the project

To format and lint the code:

```bash
  rye run style
````

To run all the tests, just run:

```bash
rye run test
```

To see all the hatch environments:

```bash
TODO
```

To only build the docs:

```bash
rye run build-docs
```

To build and verify that the built package is proper and other code QA checks:

```bash
rye run check
```

## Releasing the project

Before releasing your package on PyPI you should have all the tests in the different environments passing.

### Version management

This template provides a basic bumpversion configuration. It's as simple as running:

- `bumpversion patch` to increase version from `1.0.0` to `1.0.1`.
- `bumpversion minor` to increase version from `1.0.0` to `1.1.0`.
- `bumpversion major` to increase version from `1.0.0` to `2.0.0`.

You should read [Semantic Versioning 2.0.0](http://semver.org/) before bumping versions.

### Building and uploading

TODO

## Changelog

See [CHANGELOG.md](https://github.com/FragileTech/mloq-cookiecutter/blob/master/CHANGELOG.md).

## Questions & answers

**There's no Makefile?**

Sorry, no `Makefile` yet. The Hatch environments stand for whatever you'd have in a `Makefile`.

**Why is the version stored in several files (`pkg/__init__.py`, `setup.py`, `docs/conf.py`)?**

We cannot use a metadata/version file[^1] because this template is to be used with both distributions of packages (dirs with `__init__.py`) and modules (simple `.py` files that go straight in `site-packages`). There's no good place for that extra file if you're distributing modules.

But this isn't so bad - bumpversion manages the version string quite neatly.

[^1]: Example, an `__about__.py` file.

## Not Exactly What You Want?

No way, this is the best. 😜

If you have criticism or suggestions please open up an Issue or Pull Request.