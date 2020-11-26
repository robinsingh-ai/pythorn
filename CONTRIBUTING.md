# Contributing to Pythorn

We love your input! We want to make contributing to this simple python module as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer


# Contributing

 In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!


## Contributing To Documents

Contributors to documentation should be familiar with `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ (reST) for writing documentation.
Most projects use `Sphinx <http://www.sphinx-doc.org/en/master/>`_ to build documentation from reST source files, and `Read The Docs <https://readthedocs.org/>`_ (RTD) for publishing them on the web.
Experience with Sphinx and RTD may be helpful.


Before submitting a pull request, documentation should be tested locally. Ultimately testing of documentation must be done before merging a pull request

Location
--------

Documentation source files should be contained in a folder named ``docs`` located at the root of the project.
Images and other static assets should be located in ``docs/_static``.

File naming
-----------

reST source files and static assets should have names that consist only of lowercase letters (``a-z``), numbers (``0-9``), periods (``.``), and hyphens (``-``) instead of underscores (``_``).
Files must start a letter.
reST source files should have the extension of ``.rst``.


Source code
-----------

Source code may be displayed in blocks or inline.

Code blocks
^^^^^^^^^^^

Blocks of code should use syntax highlighting and specify the language, and may use line numbering or emphasis.
Avoid the use of two colons (``::``) at the end of a line, followed by a blank line, then code, because this may result in code parsing warnings (or worse, silent failures) and incorrect source code highlighting.
Always indent the source code in a code block.
Code blocks use the directive ``code-block``.
Its syntax is the following, where the Pygments `lexer <http://pygments.org/docs/lexers/>`_ is the name of the language, with options indented on the subsequent lines.

.. code-block:: rst

    .. code-block:: lexer
        :option:

.. seealso:: See also the Sphinx documentation for :ref:`sphinx:code-examples`.


.. _dsg-syntax-highlighting:

Syntax highlighting examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python:

.. code-block:: rst

    .. code-block:: python

        if "foo" == "bar":
            # This is Python code
            pass

Renders as:

.. code-block:: python

    if "foo" == "bar":
        # This is Python code
        pass





[Here](https://gist.github.com/ionelmc/e876b73e2001acd2140f) you can find cheatsheet for .rst files


## Issues


Feel free to submit issues and enhancement requests.

Issues are very valuable to this project.

* Ideas are a valuable source of contributions others can make
* Problems show where this project is lacking
* With a question you show where contributors can improve the user experience

## Pull Requests

Pull requests are, a great way to get your ideas into this repository.

When deciding if I merge in a pull request I look at the following things:

### Does it state intent

You should be clear which problem you're trying to solve with your contribution.

For example:

> Add link to code of conduct in README.md

Doesn't tell me anything about why you're doing that

> Add link to code of conduct in README.md because users don't always look in the CONTRIBUTING.md

Tells me the problem that you have found, and the pull request shows me the action you have taken to solve it.

### Is it of good quality

* There are no spelling mistakes
* It reads well



### Does it move this repository closer to my vision for the repository

The aim of this repository is:

* To provide a simple implementaions of codes with time complexites on the go, anyone can copy and paste, into their project
* The content is usable by someone who hasn't written something like this before
* Foster a culture of respect and gratitude in the open source community.




## Any contributions you make will be under the MIT Software License
In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.



