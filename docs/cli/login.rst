login
~~~~~

The login command allows an existing user to log in to the {{{identity_server}}}.

Syntax
++++++

The basic syntax of the login command is:

``{{{cli_command}}} login userEmail``

The full syntax (excepting :doc:`top level arguments<topLevel>`) is:

``{{{cli_command}}} ... login -h``

or

``{{{cli_command}}} ... login {{{dash_dash}}}password <password> {{{dash_dash}}}org-id <orgId> {{{dash_dash}}}verify <userEmail>``

More information about each command argument can be found under :ref:`arguments <statusArguments>`.

Expected Response
+++++++++++++++++

Successful calls will result in the following response:

.. code-block:: none
   
   Now logged in as [<orgId>]<email>

where <orgId> is the {{{company}}} ID for the new organization and <email> is the email address of its creator.

Common Error States
+++++++++++++++++++

The most common error encountered with this call is that the user supplies the wrong password. If this occurs, please try again to ensure that you did not make a typo. 

If you specify an organization ID in the call and it does not match the one stored for your user (correlated by email address) an error will also be thrown. In this case, you may use the :doc:`status command <status>` to retrieve the proper organization ID and try again.

.. _loginArguments:

Arguments
+++++++++

The following arguments are supported for the login command:

* :ref:`-h <generalH>`
* :ref:`{{{dash_dash}}}password <loginPassword>`
* :ref:`{{{dash_dash}}}org-id <loginOrgId>`
* :ref:`{{{dash_dash}}}verify <generalVerify>`
* :ref:`\<userEmail\> <loginUserEmail>`

-h
&&

-h is described under :ref:`general command arguments <generalH>`.

.. _loginPassword:

{{{dash_dash}}}password
&&&&&&&&&&&&&&&&&&&&&&&

Optional. Allows the user to specify his password directly in the command.

Equivalent Options
%%%%%%%%%%%%%%%%%%

The following arguments are equivalent to {{{dash_dash}}}password:

* {{{dash_dash}}}pw

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

If omitted, the user is prompted to enter a password interactively after submitting the command. 

.. _loginOrgId:

{{{dash_dash}}}org-id
&&&&&&&&&&&&&&&&&&&&&

Optional. Allows the user to specify his organization ID directly in the command.

Equivalent Options
%%%%%%%%%%%%%%%%%%

The following arguments are equivalent to {{{dash_dash}}}org-id:

* {{{dash_dash}}}organization-id
* {{{dash_dash}}}orgid

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

If omitted, the organization ID is taken from the user's stored state information.

{{{dash_dash}}}verify
&&&&&&&&&&&&&&&&&&&&&

{{{dash_dash}}}verify is described under :ref:`general command arguments <generalVerify>`.

.. _loginUserEmail:

<userEmail>
&&&&&&&&&&&

Required. Indicates an email address for the user trying to log in.

Equivalent Options
%%%%%%%%%%%%%%%%%%

This argument does not have a corresponding flag. It is determined by position within the command.

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

The email address must be the last argument supplied with the command.
