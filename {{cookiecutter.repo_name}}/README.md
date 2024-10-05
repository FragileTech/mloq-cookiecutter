# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if cookiecutter.license != "no" %}
* Free software: {{ cookiecutter.license }}
{% endif %}

## Features

This is an "all inclusive" sort of template.

- Choice of various licenses.
- [Pytest](http://pytest.org/) for testing Python {{ cookiecutter.target_python_version }}.
- *Optional* support for creating a tests matrix out of dependencies and Python versions.
{% if cookiecutter.codecov == "yes" %}
- [Codecov](http://codecov.io/) for coverage tracking.
{% endif %}
{% if cookiecutter.sphinx_docs == "yes" %}
- Documentation with [Sphinx](http://sphinx-doc.org/), ready for [ReadTheDocs](https://readthedocs.org/).
{% endif %}
- Configurations for:
  - [isort](https://pypi.org/project/isort)
  - [bumpversion](https://pypi.org/project/bump2version) ([bump2version](https://github.com/c4urself/bump2version) required)
  - [ruff](https://docs.astral.sh/ruff/) for linting and formatting your code.
- Packaging and code quality checks. This template comes with a Hatch environment (`check`) that will:
  - Check if your `README.md` is valid.
  - Check if the `MANIFEST.in` has any issues.

## Requirements

Projects using this template have these minimal dependencies:

- [Cookiecutter](https://github.com/audreyr/cookiecutter) - just for creating the project.
- [Setuptools](https://pypi.org/project/setuptools) - for building the package, wheels, etc. Nowadays Setuptools is widely available, it shouldn't pose a problem :)

To get quickly started on a new system, just [install setuptools](https://pypi.org/project/setuptools#installation-instructions) and then [install pip](https://pip.pypa.io/en/latest/installing.html). That's the bare minimum required to install Hatch and Cookiecutter. To install them, just run this in your shell or command prompt:

```bash
pip install cookiecutter
```

## Usage and options

This template is more involved than the regular [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

First generate your project:

```bash
cookiecutter gh:{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
```

You will be asked for these fields:

> **Note**: Fields that work together usually use the same prefix. If you answer "no" on the first one, then the rest won't have any effect so just ignore them. Maybe in the future Cookiecutter will allow option hiding or something like a wizard.

### `full_name`

**Default**:

```python
"{{ cookiecutter.full_name }}"
```

Main author of this library or application (used in `AUTHORS.md` and `pyproject.toml`).

Can be set in your `~/.cookiecutterrc` config file.

### `email`

**Default**:

```python
"{{ cookiecutter.email }}"
```

Contact email of the author (used in `AUTHORS.md` and `pyproject.toml`).

Can be set in your `~/.cookiecutterrc` config file.

### `website`

**Default**:

```python
"{{ cookiecutter.website }}"
```

Website of the author (used in `AUTHORS.md`).

Can be set in your `~/.cookiecutterrc` config file.

### `repo_username`

**Default**:

```python
"{{ cookiecutter.repo_username }}"
```

Repository username of this project (used for repository link).

Can be set in your `~/.cookiecutterrc` config file.

### `project_name`

**Default**:

```python
"{{ cookiecutter.project_name }}"
```

Verbose project name, used in headings (docs, README, etc).

### `repo_hosting_domain`

**Default**:

```python
"{{ cookiecutter.repo_hosting_domain }}"
```

Use `"no"` for no hosting (various links will disappear). You can also use `"gitlab.com"` and such, but various things will be broken.

### `repo_name`

**Default**:

```python
"{{ cookiecutter.repo_name }}"
```

Repository name on hosting service (and project's root directory name).

### `package_name`

**Default**:

```python
"{{ cookiecutter.package_name }}"
```

Python package name (whatever you would import).

### `distribution_name`

**Default**:

```python
"{{ cookiecutter.distribution_name }}"
```

PyPI distribution name (what you would `pip install`).

### `module_name`

**Default**:

```python
"{{ cookiecutter.module_name }}"
```

This template assumes there's going to be an "implementation" module inside your package.

### `project_short_description`

**Default**:

```python
"{{ cookiecutter.project_short_description }}"
```

One-line description of the project (used in `README.md` and `pyproject.toml`).

### `release_date`

**Default**:

```python
"{{ cookiecutter.release_date }}"
```

Release date of the project (ISO 8601 format), defaults to today (used in `CHANGELOG.md`).

### `year_from`

**Default**:

```python
"{{ cookiecutter.year_from }}"
```

Copyright start year.

### `year_to`

**Default**:

```python
"{{ cookiecutter.year_to }}"
```

Copyright end year.

### `version`

**Default**:

```python
"{{ cookiecutter.version }}"
```

Release version (see `.bumpversion.cfg` and in Sphinx `conf.py`).

### `command_line_interface`

**Default**:

```python
"{{ cookiecutter.command_line_interface }}"
```

Option to enable a CLI (a bin/executable file). Available options:

- `plain` - a very simple command.
- `argparse` - a command implemented with `argparse`.
- `click` - a command implemented with [click](http://click.pocoo.org/) - which you can use to build more complex commands.
- `no` - no CLI at all.

### `command_line_interface_bin_name`

**Default**:

```python
"{{ cookiecutter.command_line_interface_bin_name }}"
```

Name of the CLI bin/executable file (set the console script name in `pyproject.toml`).

### `license`

**Default**:

```python
"{{ cookiecutter.license }}"
```

License to use. Available options:

- BSD 2-Clause License
- BSD 3-Clause License
- MIT license
- ISC license
- Apache Software License 2.0
- GNU Lesser General Public License v3 or later (LGPLv3+)
- GNU Lesser General Public License v3 (LGPLv3)
- GNU Lesser General Public License v2.1 or later (LGPLv2+)
- GNU Lesser General Public License v2.1 (LGPLv2)
- no

What license to pick? https://choosealicense.com/

### `codecov`

**Default**:

```python
"{{ cookiecutter.codecov }}"
```

Enable pushing coverage data to Codecov and add badge in `README.md`.

### `sphinx_docs`

**Default**:

```python
"{{ cookiecutter.sphinx_docs }}"
```

Have Sphinx documentation.

### `sphinx_docs_hosting`

**Default**:

```python
"{{ cookiecutter.sphinx_docs_hosting }}"
```

Leave as default if your documentation will be hosted on ReadTheDocs. If your documentation will be hosted elsewhere (such as GitHub Pages or GitLab Pages), enter the top-level URL.

### `pypi_badge`

**Default**:

```python
"{{ cookiecutter.pypi_badge }}"
```

By default, this will insert links to your project's page on PyPI.org. If you choose `"no"`, then these links will not be created.

### `pypi_disable_upload`

**Default**:

```python
"{{ cookiecutter.pypi_disable_upload }}"
```

If you specifically want to be sure your package will never be accidentally uploaded to PyPI, you can pick `"yes"`.

## Developing the project

To format and lint the code:

```bash
rye run style
```

To run all the tests, just run:

```bash
rye run test
```

To see all the Hatch environments:

```bash
rye run hatch env show
```

To only build the docs:

```bash
rye run build-docs
```

To build and verify that the built package is proper and perform other code QA checks:

```bash
rye run check
```

## Releasing the project

Before releasing your package on PyPI, you should have all the tests in the different environments passing.

### Version management

This template provides a basic bumpversion configuration. It's as simple as running:

- `bumpversion patch` to increase version from `1.0.0` to `1.0.1`.
- `bumpversion minor` to increase version from `1.0.0` to `1.1.0`.
- `bumpversion major` to increase version from `1.0.0` to `2.0.0`.

You should read [Semantic Versioning 2.0.0](http://semver.org/) before bumping versions.

### Building and uploading

TODO

## Changelog

See [CHANGELOG.md](https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/blob/{{ cookiecutter.repo_main_branch }}/CHANGELOG.md).

## Questions & answers

**There's no Makefile?**

Sorry, no `Makefile` yet. The Hatch environments stand for whatever you'd have in a `Makefile`.

**Why is the version stored in several files (`pkg/__init__.py`, `pyproject.toml`, `docs/conf.py`)?**

We cannot use a metadata/version file[^1] because this template is to be used with both distributions of packages (dirs with `__init__.py`) and modules (simple `.py` files that go straight into `site-packages`). There's no good place for that extra file if you're distributing modules.

But this isn't so bad—bumpversion manages the version string quite neatly.

[^1]: Example, an `__about__.py` file.

## Not Exactly What You Want?

No way, this is the best. 😜

If you have criticism or suggestions, please open up an Issue or Pull Request.
