create-service
~~~~~~~~~~~~~~

The create-service command registers a new service with the {{{discovery_product}}} and generates  a service token for it.

.. ifconfig:: 'draft' in conditions
       
   [[JMK add more info about what tokens do/how they are used once available]]

Syntax
++++++

The basic syntax of the create-service command is:

``{{{cli_command}}} create-service <serviceName>``

The full syntax (excepting :doc:`top level arguments<topLevel>`) is:

``{{{cli_command}}} ... create-service -h``

or

``{{{cli_command}}} ... create-service {{{dash_dash}}}verify <serviceName>``

More information about each command argument can be found under :ref:`arguments <createServiceArguments>`.

Expected Response
+++++++++++++++++

Successful calls will result in the following response:

.. code-block:: none
   
   Creating service <serviceName> in <orgId>...
   ...created!
   svc_token = '<serviceToken>'

where <orgId> is the user's organization ID and <serviceToken> is the current service token.

Common Error States
+++++++++++++++++++

A common error state is trying to create a service with the same name as an existing service within the user's scope. You will need to choose another name and try again if this happens.

Another common error state is trying to use status without being logging in first. Only logged in users can create new services.

.. _createServiceArguments:

Arguments
+++++++++

The following arguments are supported for the create-service command:

* :ref:`-h <generalH>`
* :ref:`{{{dash_dash}}}verify <generalVerify>`
* :ref:`\<serviceName\> <createServiceName>`

-h
&&

-h is described under :ref:`general command arguments <generalH>`.

{{{dash_dash}}}verify
&&&&&&&&&&&&&&&&&&&&&

{{{dash_dash}}}verify is described under :ref:`general command arguments <generalVerify>`.

.. _createServiceName:

<serviceName>
&&&&&&&&&&&&&

Required. Indicates a handle for the new service.

Equivalent Options
%%%%%%%%%%%%%%%%%%

This argument does not have a corresponding flag. It is determined by position within the command.

Constraints and Usage Notes
%%%%%%%%%%%%%%%%%%%%%%%%%%%

The service name must be the last argument supplied with the command.

The service name must be unique within the user's scope. If another service with the supplied name already exists the request will be rejected.

.. ifconfig:: 'draft' in conditions
    
   [[JMK: scope is currently the user but should be the org. See issue #3]]

Any UTF-8 string may be used for the name. Quotes must be used around the value if it includes spaces or apostrophes.

.. ifconfig:: 'draft' in conditions
    
   [[JMK: Add any length restrictions]]
