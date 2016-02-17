accept-invitation
~~~~~~~~~~~~~~~~~

The accept-invitation command allows an invited user to join an organization.

Syntax
++++++

The basic syntax of the accept-invitation command is:

``dwc accept-invitation <orgId> <invitationCode> <emailAddress>``

The full syntax including all optional arguments is:

``dwc accept-invitation -h --name <name> --password <password> --verify <orgId> <invitationCode> <emailAddress>``

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

* -h
* --name
* --password
* --verify
* <orgId>
* <invitationCode>
* <emailAddress>

-h
&&

-h is described under :ref:`general command arguments <generalH>`.

.. _acceptInvitationName:

--name
&&&&&&

Optional. Indicates a handle for the user creating the new organization. This handle is an external identifier; the user will be given a userID to identify him within {{{company}}}.

Equivalent Options
%%%%%%%%%%%%%%%%%%

The following arguments are equivalent to --name:

* --fullname

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

If used, this option sets the user name in the system.

If omitted, the user is prompted to enter a name interactively after submitting the command.

Any UTF-8 string may be used for the name. Quotes must be used around the value if it includes spaces. The name may be up to XXX characters long.

[[JMK test this]]

.. _acceptInvitationPassword:

--password
&&&&&&&&&&

Optional. Allows the user to specify his password directly in the command.

Equivalent Options
%%%%%%%%%%%%%%%%%%

The following arguments are equivalent to --password:

* --pw

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

If used, this option does not require two identical passwords to create the account.

If omitted, the user is prompted to enter a password interactively after submitting the command. In this case, the password must be entered twice and if the values do not agree the user is offered a second chance to supply a valid password.

There are no restrictions on password value imposed by {{{cli_product}}}. If your organization requires specific rules for passwords in third party systems they should be managed on your end.

--verify
&&&&&&&&

--verify is described under :ref:`general command arguments <generalVerify>`.

.. _acceptInvitationOrgId:

<orgId>
&&&&&&&

Required. Indicates the {{{company}}} organization ID for the organization the user was invited to join.

Equivalent Options
%%%%%%%%%%%%%%%%%%

This argument does not have a corresponding flag. It is determined by position within the command.

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

The organization ID must be the third to last argument supplied with the command.

.. _acceptInvitationCode:

<invitationCode>
&&&&&&&&&&&&&&&&

Required. Indicates the identifier returned by the invite-user command that generated this invitation.

Equivalent Options
%%%%%%%%%%%%%%%%%%

This argument does not have a corresponding flag. It is determined by position within the command.

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

The invitation code must be the second to last argument supplied with the command.

.. _acceptInvitationEmail:

<emailAddress>
&&&&&&&&&&&&&&

**Required** Indicates the email address for the invited user.

Equivalent Options
%%%%%%%%%%%%%%%%%%

This argument does not have a corresponding flag. It is determined by position within the command.

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

The email address must be the last argument supplied with the command.

Any valid email address may be used. The string must have the format a@b.c or it will be rejected.

[[JMK test this]]

Each email address may only be used once in the system. A user may not have multiple accounts or belong to multiple organizations.

At the current time {{{company}}} does not send emails to the specified address. The output of this command should be sent to the new user so they can run the command and add themselves to your organization.
