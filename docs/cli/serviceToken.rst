service-token
~~~~~~~~~~~~~

The service-token command returns a valid token for the requested service provided the requesting user has access to the service.

.. 
   
   JMK: currently only the user who created the service can see it/get a token.
   That may change. See issue #3

Syntax
++++++

The basic syntax of the create-service command is:

``{{{cli_command}}} service-token <serviceName>``

The full syntax (excepting :doc:`top level arguments<topLevel>`) is:

``{{{cli_command}}} ... service-token -h --verify <serviceName>``

More information about each command argument can be found under :ref:`arguments <serviceTokenArguments>`.

Expected Response
+++++++++++++++++

Successful calls will result in the following response:

.. code-block:: none
   
   svc_token = '<serviceToken>'

where <serviceToken> is the current service token for the requested service.

Common Error States
+++++++++++++++++++

A common error state is trying to access a service that either doesn't exist or that the current user does not have permission to access.

Another common error state is trying to use status without being logging in first. Only logged in users can create new services.

.. _serviceTokenArguments:

Arguments
+++++++++

The following arguments are supported for the create-service command:

* -h
* --verify
* <serviceName>

-h
&&

-h is described under :ref:`general command arguments <generalH>`.

--verify
&&&&&&&&

--verify is described under :ref:`general command arguments <generalVerify>`.

.. _serviceTokenName:

<serviceName>
&&&&&&&&&&&&&

Required. Indicates a handle for the new service.

Equivalent Options
%%%%%%%%%%%%%%%%%%

This argument does not have a corresponding flag. It is determined by position within the command.

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

The service name must be the last argument supplied with the command.

Any UTF-8 string may be used for the name. Quotes must be used around the value if it includes spaces.

.. JMK: add any length restrictions
