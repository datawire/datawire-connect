status
~~~~~~

The status command provides information on the currently logged in user including organization ID, user ID, and the tokens for any services they created.

[[JMK depending on resolution of issue #3 may contain additional tokens/service info for other services in the org]]

Syntax
++++++

The basic syntax of the accept-invitation command is:

``dwc status``

The full syntax including all optional arguments is:

``dwc status -h --verify``

More information about each argument can be found under :ref:`arguments <acceptInvitationArguments>`.

Expected Response
+++++++++++++++++

Successful calls will result in the following response:

.. code-block:: none
   
   {
       "orgID":"<orgId>", 
       "orgs":{
           "<orgId>":{
               "email":"<emailAddress>",
               "service_tokens":{ 
                  "service1":"<service1Token>",
                  "service2":"<service2Token>"
               },
               "user_token":"<userToken>" 
           } 
       }
   } 


where <orgId> is the user's organization ID, <emailAddress> is their email address, each <serviceKToken> is a service token, and <userToken> is the current user token.

[[JMK where does a user token come in here? we're not returning it excepting in status and don't seem to require its use anywhere]]

Common Error States
+++++++++++++++++++

The most likely error state is trying to use status without being logging in first. Since status returns the current user's state in the system, it requires a valid, logged in current user.

[[JMK the current error message could use improvement. See issue #6]]

.. _statusArguments:

Arguments
+++++++++

The following arguments are supported for the invite-user command:

* -h
* --verify

-h
&&

-h is described under :ref:`general command arguments <generalH>`.

--verify
&&&&&&&&

--verify is described under :ref:`general command arguments <generalVerify>`.

