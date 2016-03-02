logout
~~~~~~

The logout command logs the current user out of the {{{identity_server}}}.

Syntax
++++++

The basic syntax of the logout command is:

``{{{cli_command}}} logout``

The full syntax (excepting :doc:`top level arguments<topLevel>`) is:

``{{{cli_command}}} ... logout -h``

or

``{{{cli_command}}} ... logout --force --verify``

More information about each command argument can be found under :ref:`arguments <logoutArguments>`.

Expected Response
+++++++++++++++++

With the default options, you will be asked to verify that you want to log out:

.. code-block:: none

   THIS WILL COMPLETELY LOG YOU OUT AND REMOVE ALL YOUR DATAWIRE STATE.
   Continue?

If you turn off the confirmation option or confirm that you do want to log out, you will be silently logged out and returned to your normal command prompt.

If you get the confirmation request and reply with anything other than y or yes, you will get the following response:

.. code-block:: none
   
   OK, carry on.

and remain logged in.

Common Error States
+++++++++++++++++++

None

.. _logoutArguments:

Arguments
+++++++++

The following arguments are supported for the login command:

* :ref:`-h <generalH>`
* :ref:`--force <logoutForce>`
* :ref:`--verify <generalVerify>`

-h
&&

-h is described under :ref:`general command arguments <generalH>`.

.. _logoutForce:

--force
&&&&&&&

Optional. Forces a logout without prompting for verification.

Equivalent Options
%%%%%%%%%%%%%%%%%%

The following arguments are equivalent to --force:

* --yes

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

If omitted, the user is prompted to confirm that they really do want to log out after submitting the command. 

--verify
&&&&&&&&

--verify is described under :ref:`general command arguments <generalVerify>`.

