import logging
import os
import pathlib
import shutil
import subprocess
import sys


try:
    import flogging
    flogging.setup(allow_trailing_dot=True)
except ImportError:
    pass

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# Constants for messages
ERROR_MESSAGE = '''
┌───────────────────────────────────────────────────────────────────────┐
│ ERROR:                                                                │
│                                                                       │
│     Your result package is broken. Your bin script named              │
│     "{command_line_interface_bin_name}" will shadow your package.     │
│                                                                       │
│     Python automatically adds the location of scripts to              │
│     `sys.path`. Because of that, the bin script will fail             │
│     to import your package because it has the same name               │
│     (it will try to import itself as a module).                       │
│                                                                       │
│     To avoid this problem you have two options:                       │
│                                                                       │
│     * Remove the ".py" suffix from `command_line_interface_bin_name`. │
│                                                                       │
│     * Use a different `package_name` (not "{bin_name_without_ext}").  │
└───────────────────────────────────────────────────────────────────────┘
'''

GET_STARTED_INSTRUCTIONS = '''
cd {{ cookiecutter.repo_name }}
git init
pre-commit install --install-hooks
pre-commit autoupdate
git add --all
git commit -m "Add initial project skeleton."
git tag v{{ cookiecutter.version }}
git remote add origin git@{{ cookiecutter.repo_hosting_domain }}:{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git
git push -u origin {{ cookiecutter.repo_main_branch }} v{{ cookiecutter.version }}
'''

def main():
    """Adjust project structure based on cookiecutter variables."""
    cwd = pathlib.Path().resolve()
    src = cwd / 'src'

    # Handle Sphinx docs
    {% if cookiecutter.sphinx_docs == "no" %}
    shutil.rmtree(cwd / 'docs', ignore_errors=True)
    cwd.joinpath('.readthedocs.yml').unlink(missing_ok=True)
    {% elif 'readthedocs' not in cookiecutter.sphinx_docs_hosting %}
    cwd.joinpath('.readthedocs.yml').unlink(missing_ok=True)
    {% endif %}

    # Handle command-line interface
    {% if cookiecutter.command_line_interface == 'no' %}
    src.joinpath('{{ cookiecutter.package_name }}', '__main__.py').unlink(missing_ok=True)
    src.joinpath('{{ cookiecutter.package_name }}', 'cli.py').unlink(missing_ok=True)
    src.joinpath('{{ cookiecutter.package_name }}', 'tests', 'test_cli.py').unlink(missing_ok=True)
    cwd.joinpath('tests', 'test_cli.py').unlink(missing_ok=True)
    {% endif %}

    # Handle test location
    shutil.rmtree(src / '{{ cookiecutter.package_name }}' / 'tests', ignore_errors=True)

    # Handle GitHub Actions
    {% if cookiecutter.github_actions == 'no' %}
    github_workflows = cwd.joinpath('.github', 'workflows')
    for workflow_file in ['build.yml', 'documentation.yml', 'draft.yml', 'labeler.yml', 'tests.yml']:
        github_workflows.joinpath(workflow_file).unlink(missing_ok=True)
    {% endif %}

    # Remove CONTRIBUTING file if no repository hosting
    {% if cookiecutter.repo_hosting == 'no' %}
    cwd.joinpath('CONTRIBUTING.md').unlink(missing_ok=True)
    {% endif %}

    # Remove LICENSE if not applicable
    {% if cookiecutter.license == "no" %}
    cwd.joinpath('LICENSE').unlink(missing_ok=True)
    {% endif %}

    # Determine terminal width for formatting
    width = min(140, shutil.get_terminal_size(fallback=(140, 0)).columns)

    # Set up pre-commit
    {% if cookiecutter.pre_commit == "yes" %}
    logger.info(" Setting up pre-commit ".center(width, "#"))
    if cwd.joinpath('.git').exists():
        try:
            subprocess.check_call(['pre-commit', 'install', '--install-hooks'])
            subprocess.check_call(['pre-commit', 'autoupdate'])
        except (subprocess.CalledProcessError, FileNotFoundError)as e:
            logger.error(f"Failed to set up pre-commit: {e}")
    else:
        logger.info('Skipping pre-commit install.')
    {% endif %}
    # Success message
    logger.info(f" Successfully created `{{ cookiecutter.repo_name }}` ".center(width, "#"))
    logger.info('See .cookiecutterrc for instructions on regenerating the project.')
    logger.info('To get started, run these commands:')
    logger.info(GET_STARTED_INSTRUCTIONS)

    # Check for potential package name shadowing
    command_line_interface_bin_name = '{{ cookiecutter.command_line_interface_bin_name }}'
    bin_name_without_ext = os.path.splitext(command_line_interface_bin_name)[0]

    if bin_name_without_ext == '{{ cookiecutter.package_name }}':
        error_msg = ERROR_MESSAGE.format(
            command_line_interface_bin_name=command_line_interface_bin_name,
            bin_name_without_ext=bin_name_without_ext
        )
        logger.error(error_msg)
        sys.exit(1)

if __name__ == "__main__":
    main()
