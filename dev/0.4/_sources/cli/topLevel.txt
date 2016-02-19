Top Level Arguments
-------------------

The {{{cli_product}}} command line interface supports the following top-level arguments:

* :ref:`-h <topH>`
* :ref:`-v <topV>`
* :ref:`-q <topQ>`
* :ref:`--registrar-url <topRegistrarUrl>`
* :ref:`--local <topLocal>`
* :ref:`--state <topState>`

These arguments are all optional but must be specified in the order listed above if used.

.. _topH:

-h
~~

-h provides a list of available top level arguments and supported commands with a brief description of each.

Syntax
++++++

``{{{cli_command}}} -h``

Equivalent Options
++++++++++++++++++

The following arguments are equivalent to -h:

* --help

Constraints and Usage Notes
+++++++++++++++++++++++++++

If -h is specified, nothing else in the command is evaluated.

Using -h as a top level argument does not provide any specifics about the requirements or arguments available for commands.

.. _topV:

-v
~~

-v increases the verbosity of the responses from the CLI.

Syntax
++++++

``{{{cli_command}}} -v ...``


Equivalent Options
++++++++++++++++++

The following arguments are equivalent to -v:

* --verbose

Constraints and Usage Notes
+++++++++++++++++++++++++++

The -v flag has no meaning if used with -h.

The CLI supports XXX verbosity levels. By default, most commands that create items (organizations, users, services, tokens, etc.) return a handle to the newly created item.

[[JMK Need more info. As far as I can tell -v currently does nothing.]]

[[JMK what happens if I use both -v and -q at the same time?]]

.. _topQ:

-q
~~

-q suppresses responses from the CLI.

Syntax
++++++

``{{{cli_command}}} -q ...``


Equivalent Options
++++++++++++++++++

The following arguments are equivalent to -q:

* --quiet

Constraints and Usage Notes
+++++++++++++++++++++++++++

-q suppresses responses from the CLI. This may be useful if you are using the interface programmatically or want to maintain privacy and not display information specific to identifiers and tokens.

[[JMK check what this actually does. what about something like invite-user where the output is required to move on to the next step of accept-invitation]]

[[JMK what happens if I use both -v and -q at the same time?]]

.. _topRegistrarUrl:

--registrar-url
~~~~~~~~~~~~~~~

--registrar-url specifies that the request should be handled by a specific {{{identity_server}}} as indicated by a specific fully qualified domain name or IP address.

Syntax
++++++

``{{{cli_command}}} ... --registrar-url <uri> ...``


Equivalent Options
++++++++++++++++++

The following arguments are equivalent to --registrar-url:

* --base-url
* --baseurl

Constraints and Usage Notes
+++++++++++++++++++++++++++

If this argument is omitted, {{{identity_default}}} is used by default.

[[JMK what happens if you specify both --registrar-url and --local?]]

.. _topLocal:

--local
~~~~~~~

--local specifies that the request should be handled by a local {{{identity_server}}}.

Syntax
++++++

``{{{cli_command}}} ... --local ...``


Equivalent Options
++++++++++++++++++

--local is the only way to specify this option.

Constraints and Usage Notes
+++++++++++++++++++++++++++

[[JMK does it listen on a specific port? what happens if no local server is running?]]

[[JMK what happens if you specify both --registrar-url and --local?]]

.. _topState:

--state
~~~~~~~

--state specifies a location for the state file containing information about the current user's organizations, identifiers, and services.

[[JMK currently only one org and just a user ID]]

Syntax
++++++

``{{{cli_command}}} ... --state <path> ...``


Equivalent Options
++++++++++++++++++

The following arguments are equivalent to --state:

* --state-path

Constraints and Usage Notes
+++++++++++++++++++++++++++

If this argument is omitted, {{{state_path}}} is used by default.

