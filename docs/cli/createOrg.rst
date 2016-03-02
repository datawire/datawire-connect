create-org
~~~~~~~~~~

The create-org command creates a new organization in the {{{cli_product}}} with a single member. That member can then invite additional people into the organization as needed.

Syntax
++++++

The basic syntax of the create-org command is:

``{{{cli_command}}} create-org <organizationName> <userName> <userEmail>``

The full syntax (excepting :doc:`top level arguments<topLevel>`) is:

``{{{cli_command}}} ... create-org -h``

or

``{{{cli_command}}} ... create-org {{{dash_dash}}}adminpass <password> {{{dash_dash}}}verify <organizationName> <userName> <userEmail>``

More information about each argument can be found under :ref:`arguments <createOrgArguments>`.

Expected Response
+++++++++++++++++

Successful calls will result in the following response:

.. code-block:: none
   
   Now logged in as [<orgId>]<email>

where <orgId> is the {{{company}}} ID for the new organization and <email> is the email address of its creator.

Common Error States
+++++++++++++++++++

The most common error encountered with this call is that the user trying to create a new organization is already registered with {{{company}}} under a different organization. In this case, the user must use their existing organization instead of creating a new one.

.. _createOrgArguments:

Arguments
+++++++++

The following arguments are supported for the create-org command:

* :ref:`-h <generalH>`
* :ref:`{{{dash_dash}}}adminpass <createOrgAdminPass>`
* :ref:`{{{dash_dash}}}verify <generalVerify>`
* :ref:`\<organizationName\> <createOrgOrganizationName>`
* :ref:`\<userName\> <createOrgUserName>`
* :ref:`\<userEmail\> <createOrgUserEmail>`

-h
&&

-h is described under :ref:`general command arguments <generalH>`.

.. _createOrgAdminPass:

{{{dash_dash}}}adminpass
&&&&&&&&&&&&&&&&&&&&&&&&

Optional. Allows the user creating a new organization to specify his password directly in the command.

Equivalent Options
%%%%%%%%%%%%%%%%%%

The following arguments are equivalent to {{{dash_dash}}}adminpass:

* {{{dash_dash}}}password
* {{{dash_dash}}}pw

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

If used, this option does not require two identical passwords to create the account.

If omitted, the user is prompted to enter a password interactively after submitting the command. In this case, the password must be entered twice and if the values do not agree the user is offered a second chance to supply a valid password.

There are no restrictions on password value imposed by {{{cli_product}}}. If your organization requires specific rules for passwords in third party systems they should be managed on your end.

{{{dash_dash}}}verify
&&&&&&&&&&&&&&&&&&&&&

{{{dash_dash}}}verify is described under :ref:`general command arguments <generalVerify>`.

.. _createOrgOrganizationName:

<organizationName>
&&&&&&&&&&&&&&&&&&

Required. Indicates a handle for the new organization. This handle is an external identifier; the organization will be given an orgID to identify it within {{{company}}}.

Equivalent Options
%%%%%%%%%%%%%%%%%%

This argument does not have a corresponding flag. It is determined by position within the command.

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

The organization name must be the third to last argument supplied with the command.

Any UTF-8 string may be used as the organization name. Quotes must be used around the value if it includes spaces or apostrophes. 

.. ifconfig:: 'draft' in conditions
       
   [[JMK: Add any length restrictions. I've successfully used several hundred characters.]]

.. _createOrgUserName:

<userName>
&&&&&&&&&&

Required. Indicates a handle for the user creating the new organization. This handle is an external identifier; the user will be given a userID to identify him within {{{company}}}.

Equivalent Options
%%%%%%%%%%%%%%%%%%

This argument does not have a corresponding flag. It is determined by position within the command.

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

The user's name must be the second to last argument supplied with the command.

Any UTF-8 string may be used for the name. Quotes must be used around the value if it includes spaces or apostrophes.

.. ifconfig:: 'draft' in conditions
    
   [[JMK: Add any length restrictions. I've successfully used several hundred characters.]]

.. _createOrgUserEmail:

<userEmail>
&&&&&&&&&&&

Required. Indicates an email address for the user creating the new organization.

Equivalent Options
%%%%%%%%%%%%%%%%%%

This argument does not have a corresponding flag. It is determined by position within the command.

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

The email address must be the last argument supplied with the command.

Any valid email address may be used. The string must have the format a@b.c or it will be rejected.

Each email address may only be used once in the system. A user may not have multiple accounts or belong to multiple organizations.

At the current time {{{company}}} does not send emails to the specified address.
