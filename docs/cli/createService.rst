create-service
~~~~~~~~~~~~~~

The create-service command registers a new service with the {{{discovery_product}}} and generates  a service token for it.

[[JMK add more info about what tokens do/how they are used once available]]

Syntax
++++++

The basic syntax of the create-service command is:

``dwc create-service <serviceName>``

The full syntax (excepting :doc:`top level arguments<topLevel>`) is:

``dwc ... create-service -h --verify <serviceName>``

More information about each command argument can be found under :ref:`arguments <createServiceArguments>`.

Expected Response
+++++++++++++++++

Successful calls will result in the following response:

.. code-block:: none
   
   Creating service service1 in <orgId>...
   ...created!
   svc_token = '<serviceToken>'

where <orgId> is the user's organization ID and <serviceToken> is the current service token.

Common Error States
+++++++++++++++++++

The most likely error state is trying to use status without being logging in first. Only logged in users can create new services.

.. _createServiceArguments:

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

Service names should be unique. If a new service is created with the same name as an existing service the creating user can access, the existing service is disassociated with the account and can no longer be accessed.

[[JMK IMO we should enforce name uniqueness. See issue #4]]

Any UTF-8 string may be used for the name. Quotes must be used around the value if it includes spaces. The name may be up to XXX characters long.

[[JMK test this]]
