status
~~~~~~

The status command provides information on the currently logged in user including organization ID, user ID, and the tokens for any services they created.

.. ifconfig:: 'draft' in conditions
    
   [[JMK: depending on resolution of issue #3 may contain additional tokens/service
   info for other services in the org]]

Syntax
++++++

The basic syntax of the accept-invitation command is:

``{{{cli_command}}} status``

The full syntax (excepting :doc:`top level arguments<topLevel>`) is:

``{{{cli_command}}} ... status -h --verify``

More information about each command argument can be found under :ref:`arguments <statusArguments>`.

Expected Response
+++++++++++++++++

The status response is split into three sections: basic user information, user capabilities, and available services.

The basic user information consists of the user's organization ID and email address. The user capabilities indicates a list of the user's capabilities including their administrator status (at the current time all users are administrators), their ability to use services (available by default), and their status as users (all responses should indicate that the user is, in fact, a user). The list of available services provides a handle to each of the services accessible by the user (at the current time, the services he created) or an indication that no services are available. These service handles can then be used to request service tokens for available services as needed.

The full format for a user is:

.. code-block:: none
   
   Logged in as [<orgId>]<emailAddress>:
   
   Capabilities:
   - dw:admin0: Organization administator
   - dw:reqSvc0: Able to request service tokens
   - dw:user0: User
   
   <serviceList>

where <orgId> is the organization ID of your organization, <emailAddress> is the email address supplied in the request, and <serviceList> is one of the following:

.. code-block:: none
   
   No services defined

or 

.. code-block:: none
   
   Services defined:
   - <serviceHandle1>
   - <serviceHandle2>
   ...
   - <serviceHandleN>

where each <serviceHandleK> is the name of a service available to the user. The services are listed alphabetical order.

Users who do not have permission to access services will not have the line about requesting services in their status response.

.. ifconfig:: 'draft' in conditions
      
   [[JMK: where does a user token come in here?
   we're not returning it excepting in status and don't seem to require its use anywhere]]

Common Error States
+++++++++++++++++++

The most likely error state is trying to use status without being logging in first. Since status returns the current user's state in the system, it requires a valid, logged in current user.

.. ifconfig:: 'draft' in conditions
    
   [[JMK: the current error message could use improvement. See issue #6]]

.. _statusArguments:

Arguments
+++++++++

The following arguments are supported for the invite-user command:

* :ref:`-h <generalH>`
* :ref:`--verify <generalVerify>`

-h
&&

-h is described under :ref:`general command arguments <generalH>`.

--verify
&&&&&&&&

--verify is described under :ref:`general command arguments <generalVerify>`.

