# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

```{contents}
```

## Bug reports

When [reporting a bug](https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/issues) please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

## Documentation improvements

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog posts, articles, and such.

## Feature requests and feedback

The best way to send feedback is to file an issue at [https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/issues](https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/issues).

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that code contributions are welcome :)

## Development

To set up `{{ cookiecutter.repo_name }}` for local development:

1. Fork [{{ cookiecutter.repo_name }}](https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}) (look for the "Fork" button).
2. Clone your fork locally:

    ```bash
    git clone git@{{ cookiecutter.repo_hosting_domain }}:YOURGITHUBNAME/{{ cookiecutter.repo_name }}.git
    ```

3. Create a branch for local development:

    ```bash
    git checkout -b name-of-your-bugfix-or-feature
    ```

   Now you can make your changes locally.

4. When you're done making changes run all the checks and docs builder with one command:

    ```bash
    rye run all
    ```

5. Commit your changes and push your branch to GitHub:

    ```bash
    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature
    ```

6. Submit a pull request through the GitHub website.

## Pull Request Guidelines

If you need some code review or feedback while you're developing the code just make the pull request.

For merging, you should:

1. Include passing tests (run `hatch test`).
2. Update documentation when there's new API, functionality etc.
3. Add a note to `CHANGELOG.md` about the changes.
4. Add yourself to `AUTHORS.md`.

