Top Level Arguments
-------------------

The {{{cli_product}}} command line interface supports the following top-level arguments:

* :ref:`-h <topH>`
* :ref:`-v <topV>`
* :ref:`-q <topQ>`
* :ref:`{{{dash_dash}}}registrar-url <topRegistrarUrl>`
* :ref:`{{{dash_dash}}}local <topLocal>`
* :ref:`{{{dash_dash}}}state <topState>`

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

* {{{dash_dash}}}help

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

or 

``{{{cli_command}}} -vv ...``

Equivalent Options
++++++++++++++++++

The following arguments are equivalent to -v:

* {{{dash_dash}}}verbose

The following arguments are equivalent to -vv:

* {{{dash_dash}}}verbose {{{dash_dash}}}verbose

Constraints and Usage Notes
+++++++++++++++++++++++++++

The -v flag has no meaning if used with -h.

The -v flag takes precedence over the -q flag if both are specified.

.. ifconfig:: 'draft' in publish_state
      
   [[JMK: -v or -vv currently takes precedence over -q but we expected it to be the other way around. See cloud-tools issue #41.]]


The CLI supports three verbosity levels including the default level (no flag specified). By default, most commands that create items (organizations, users, services, tokens, etc.) return a handle to the newly created item. In general, the default level should supply sufficient information for normal usage.

With one additional level of verbosity specified, users are notified that tokens are not being verified and given the FQDN of the {{{identity_server}}} used to service the CLI requests ({{{identity_default}}} by default). Note that token verification is not currently supported by the {{{cli_product}}} CLI so this message will always display in verbose mode.

With a second level of additional verbosity specified, the location of the key that would be used to verify tokens (if such keys were currently supported) is added to the information supplied in the first level of verbosity.

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

* {{{dash_dash}}}quiet

Constraints and Usage Notes
+++++++++++++++++++++++++++

-q suppresses responses from the CLI. This may be useful if you are using the interface programmatically or want to maintain privacy and not display information specific to identifiers and tokens.

The -v flag takes precedence over the -q flag if both are specified.

.. ifconfig:: 'draft' in publish_state
      
   [[JMK: -v or -vv currently takes precedence over -q but we expected it to be the other way around. See cloud-tools issue #41.]]
   
   [[JMK: -q is currently a no op. See cloud-tools issue #41.]]

.. _topRegistrarUrl:

{{{dash_dash}}}registrar-url
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This option is internal and should not be used without explicit direction from {{{company}}}.

.. _topLocal:

{{{dash_dash}}}local
~~~~~~~~~~~~~~~~~~~~

This option is internal and should not be used without explicit direction from {{{company}}}.

.. _topState:

{{{dash_dash}}}state
~~~~~~~~~~~~~~~~~~~~

{{{dash_dash}}}state specifies a location for the state file containing information about the current user's organizations, identifiers, and services.

.. ifconfig:: 'draft' in publish_state
    
   [[JMK: currently only one org and just a user ID]]

Syntax
++++++

``{{{cli_command}}} ... {{{dash_dash}}}state <path> ...``


Equivalent Options
++++++++++++++++++

The following arguments are equivalent to {{{dash_dash}}}state:

* {{{dash_dash}}}state-path

Constraints and Usage Notes
+++++++++++++++++++++++++++

If this argument is omitted, {{{state_path}}} is used by default.

