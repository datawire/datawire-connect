Command Line Syntax
===================

The {{{cli_product}}} command line interface has the following general syntax:

``{{{cli_command}}} <top level arguments> <command> <command arguments>``

In general, the arguments are order dependent and must appear in a specific order if specified at all (for optional arguments). In particular, all top level arguments must appear before the command and all arguments modifying a command (whether specific to that command or a general argument available for all commands) must appear after the actual command. Failure to specify an argument in the expected order may result in an  unrecognized argument error.

Specifics about the available commands and arguments can be found below:

.. toctree::
   :maxdepth: 2

   Top Level Arguments <topLevel>
   General Command Arguments <general>
   Commands <commands>
