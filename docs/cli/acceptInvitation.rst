accept-invitation
~~~~~~~~~~~~~~~~~

The accept-invitation command allows an invited user to join an organization.

Syntax
++++++

The basic syntax of the accept-invitation command is:

``{{{cli_command}}} accept-invitation <invitationCode>``

The full syntax (excepting :doc:`top level arguments<topLevel>`) is:

``{{{cli_command}}} ... accept-invitation -h``

or

``{{{cli_command}}} ... accept-invitation {{{dash_dash}}}name <name> {{{dash_dash}}}password <password> {{{dash_dash}}}verify <invitationCode>``

More information about each argument can be found under :ref:`arguments <acceptInvitationArguments>`.

Expected Response
+++++++++++++++++

Successful calls will result in the following response:

.. code-block:: none

   Accepting invitation to <orgId>
   Now logged in as [<orgId>]<emailAddress>

where <orgId> is the organization ID of your organization and <emailAddress> is the email address supplied in the request.

Common Error States
+++++++++++++++++++

The most common error encountered with this call is that the user fails to provide matching passwords. They will be given two chances to supply matching passwords before the command fails.

.. _acceptInvitationArguments:

Arguments
+++++++++

The following arguments are supported for the invite-user command:

* :ref:`-h <generalH>`
* :ref:`{{{dash_dash}}}name <acceptInvitationName>`
* :ref:`{{{dash_dash}}}password <acceptInvitationPassword>`
* :ref:`{{{dash_dash}}}verify <generalVerify>`
* :ref:`\<invitationCode\> <acceptInvitationCode>`

-h
&&

-h is described under :ref:`general command arguments <generalH>`.

.. _acceptInvitationName:

{{{dash_dash}}}name
&&&&&&&&&&&&&&&&&&&

Optional. Indicates a handle for the user creating the new organization. This handle is an external identifier; the user will be given a userID to identify him within {{{company}}}.

Equivalent Options
%%%%%%%%%%%%%%%%%%

The following arguments are equivalent to {{{dash_dash}}}name:

* {{{dash_dash}}}fullname

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

If used, this option sets the user name in the system.

If omitted, the user is prompted to enter a name interactively after submitting the command.

Any UTF-8 string may be used for the name. Quotes must be used around the value if it includes spaces or apostrophes.

.. ifconfig:: 'draft' in conditions
       
   [[JMK: determine any length limits]]

.. _acceptInvitationPassword:

{{{dash_dash}}}password
&&&&&&&&&&&&&&&&&&&&&&&

Optional. Allows the user to specify his password directly in the command.

Equivalent Options
%%%%%%%%%%%%%%%%%%

The following arguments are equivalent to {{{dash_dash}}}password:

* {{{dash_dash}}}pw

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

If used, this option does not require two identical passwords to create the account.

If omitted, the user is prompted to enter a password interactively after submitting the command. In this case, the password must be entered twice and if the values do not agree the user is offered a second chance to supply a valid password.

There are no restrictions on password value imposed by {{{cli_product}}}. If your organization requires specific rules for passwords in third party systems they should be managed on your end.

{{{dash_dash}}}verify
&&&&&&&&&&&&&&&&&&&&&

{{{dash_dash}}}verify is described under :ref:`general command arguments <generalVerify>`.

.. _acceptInvitationCode:

<invitationCode>
&&&&&&&&&&&&&&&&

Required. Indicates the identifier returned by the invite-user command that generated this invitation.

Equivalent Options
%%%%%%%%%%%%%%%%%%

This argument does not have a corresponding flag. It is determined by position within the command.

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

The invitation code must be the last argument supplied with the command.
