Usage Flows
===========

While the overall flow through the {{{cli_product}}} Command Line Interface and the {{{discovery_product}}} should be the same for most users, it does not have to be a continuous path and different users may enter the flow at different points. This page attempts to pinpoint some of those entry points and the likely actions you'll need to take at each.

* :ref:`New to {{{product}}} - Create a New Organization <createNewOrg>`
* :ref:`Prototyping - Create a New Service <createNewService>`
* :ref:`Expanding Beyond Prototype - Add New Users <addUser>`
* :ref:`Expanding Beyond Prototype - Get New Service Tokens <getServiceToken>`
* :ref:`Hooking It Together - Access {{{discovery_product}}} <useServiceToken>`

.. _createNewOrg:

New to {{{product}}} - Create a New Organization
------------------------------------------------

If you are new to {{{product}}} or have not used {{{discovery_product}}} before, the first step is creating an organization in the system. This organization will automatically contain one user - its creator - and more can be added later.

To create a new organization, use the following command:

``dwc create-org <organizationName> <name> <email>``

substituting your organization name, name, and email address for the variables above. You may use spaces and apostrophes in the names if you surround them with double quotes (").

You should get the following response to your request:

.. code-block:: none
   
   Now logged in as [<orgId>]<email>

where <orgId> is an identifier assigned by {{{company}}} and <email> is the email address you supplied in the request.

Once this is done, you may either :ref:`add additional users <addUser>` to your organization or :ref:`start creating services <createNewService>` per the directions below.

For example, Eliza runs an online advice application and wants to start using the {{{discovery_product}}} with microservices she's building. She might create an organization using the following command:

``dwc create-org "Eliza's Automated Advice Avatar" "Eliza Bethean" eliza@bethean.com``

Eliza will get prompted to enter a password twice as follows:

.. code-block:: none
   
   Password for eliza@bethean.com @ Eliza's Automated Advice Avatar: 
   Again: 

And if the two supplied values agree, she might get this response indicating that her organization and user have been created in the system:

.. code-block:: none
   
   Now logged in as [LSLYJQ8228]eliza@bethean.com

Now that her organization and user exist in the system, Eliza can start creating some associated services. She can also add her employee Tom to the Eliza's Automated Advice Avatar organization.

.. _createNewService:

Prototyping - Create a New Service
----------------------------------

Once you have an account with {{{company}}}, the next step is to create a service in the system. You must be logged in to create services; if you are not already logged in, do so using the login command as follows:

``dwc login <email>``

substituting your email address for the variable above.

After entering your password at the prompt, you should get the following response indicating a successful login:

.. code-block:: none
   
   Now logged in as [<orgId>]<email>

At this point, you can create a new service as follows:

``dwc create-service <serviceName>``

substituting your service name for the variable above. You may use spaces and apostrophes in the name if you surround it with double quotes (").

You should get a service token in response indicating that the service was successfully created:

.. code-block:: none
   
   Creating service <serviceName> in <orgId>...
   ...created!
   svc_token = '<token>'

At this point you can :ref:`use the token <useServiceToken>` to access this service in the {{{discovery_product}}}.

For example, Eliza may want to add a service that emits advice to the lovelorn from an underlying database of possible suggestions. She might use the following command to do so:

``dwc create-service "Advice for the lovelorn"``

Which results in the following response:

.. code-block:: none
   
   Creating service Advice for the lovelorn in LSLYJQ8228...
   ...created!
   svc_token = '<token>'

Of course, "Advice for the lovelorn" is a pretty unwieldy name - Eliza will have to use that whole string each time she needs to reference the service. She might have been better off choosing a shorter name like "Lovelorn" or "Emit Lovelorn" that still clearly identifies what the service does but is easier to use.

Regardless, now that she has a token for the service she can start using it with the {{{discovery_product}}}.

.. _addUser:

Expanding Beyond Prototype - Add New Users
------------------------------------------

The ultimate goal of the {{{cli_product}}} command line interface is to generate tokens for use with the {{{discovery_product}}}. These tokens are used outside of the CLI and not everyone who needs tokens necessarily needs access to the CLI. Each organization should decide on a policy regarding how to generate and distribute tokens including which users need access to the token generation process.

If your organization decides that multiple users should be able to generate or retrieve tokens, the original member of an organization may invite one or more additional users and those users may also invite additional users into the organization. Basically, to invite users into an organization, you must be logged in as an existing member of the organization.

If you are not already logged in, do so using the login command as follows:

``dwc login <email>``

substituting your email address for the variable above.

After entering your password at the prompt, you should get the following response indicating a successful login:

.. code-block:: none
   
   Now logged in as [<orgId>]<email>

At this point, you can invite a new user into your organization as follows:

``dwc invite-user <email>``

Substituting their email address for the variable above. You should get the following response:

.. code-block:: none

   Inviting <email> to <orgId>...``
   Success! Send them:
   
   dwc accept-invitation '<invitationCode>'

where <invitationCode> is an identifier generated by the {{{cli_product}}} CLI to verify that the user has the right to join the organization.

{{{company}}} does not send the invitation for you - at this point you are responsible for sending the new user the command they need to create their account (as returned in the response). It is up to your organization to decide the correct means for doing so; any policies regarding what is or not appropriate to do with an invitation code are entirely up to you. Note that while anyone can use the code to join your organization, the account it creates has the original email address of the intended recipient affiliated with it; logging in after account creation requires knowledge of that address.

.. ifconfig:: 'draft' in publish_state

   [[JMK: Should I lose the note? It may do more harm than good to give people
   ideas on how to hijack a new account.]]

One the new user has the invitation code and installs the {{{cli_product}}}, they can submit the invitation command as follows:

``dwc accept-invitation <invitationCode>``

They will be asked to supply their full name and enter their password twice. Assuming the passwords agree, the invitation will be processed and a new account created, resulting in the new user being logged in to your organization as follows:

.. code-block:: none
   
   Accepting invitation...   
   Now logged in as [<orgId>]<email>

He can then :ref:`create services <createNewService>` or invite additional users at will.

For example, Eliza can add her employee Tom Terrific to the Eliza's Automated Advice Avatar organization as follows:

``dwc invite-user tom@bethean.com``

She might get the following response:

.. code-block:: none
   
   Inviting tom@bethean.com to LSLYJQ8228...
   Success! Send them:
   
   dwc accept-invitation '<inviteCode>'

She sends Tom the last line of the response via IM and, after setting up {{{cli_product}}} he runs the command:

``dwc accept-invitation '<inviteCode>'``

He enters his name when prompted, enters his desired password twice, then is told he's logged into the organization as follows:

.. code-block:: none
   
   Full Name: Tom Terrific
   Password: 
   Again: 
   Accepting invitation...
   Now logged in as [LSLYJQ8228]tom@bethean.com

At this point he has the same access and privileges as Eliza.

.. _getServiceToken:

Expanding Beyond Prototype - Get New Service Tokens
---------------------------------------------------

In order to get service tokens for an application, you must be logged in to the organization owning the service and have access to the service.

.. ifconfig:: 'draft' in publish_state
 
   [[JMK: At the current time you can only see services you created. 
   This should change to seeing services created within your org (see issue #3). 
   Also, there is a bug that prevents people from seeing services created in 
   previous user sessions or generating tokens for them (see issue #28).]]

If you are not already logged in, do so using the login command as follows:

``dwc login <email>``

substituting your email address for the variable above.

After entering your password at the prompt, you should get the following response indicating a successful login:

.. code-block:: none
   
   Now logged in as [<orgId>]<email>

At this point, you can request tokens for any existing service as follows:

``dwc service-token <serviceName>``

substituting your service name for the variable above. If the name has spaces or apostrophes you must surround it with double quotes (").

You should get a valid service token for that service in response:

.. code-block:: none
   
   svc_token = '<token>'

You can :ref:`use that token <useServiceToken>` to access this service in the {{{discovery_product}}}.

For example, Eliza wants to generate a new token for one of her services. It's been a while since she's needed to interact with the service and can't remember its exact name. She looks up her available services using the status command as follows:

``dwc status``

and gets the following response:

.. code-block:: none
   
   Logged in as [LSLYJQ8228]eliza@bethean.com:
   
   Capabilities:
   - dw:admin0: Organization administator
   - dw:reqSvc0: Able to request service tokens
   - dw:user0: User
   
   Services defined:
   - Advice to the annoyingly perfect
   - Advice to the lovelorn
   - Advice to the perpetually grumpy

She wants to get a token for Advice to the perpetually grumpy and requests one as follows:

``dwc service-token "Advice to the perpetually grumpy"``

receiving a response like the following:

.. code-block:: none
   
   svc_token = '<token>'

She can now use the token with the {{{discovery_product}}}.

.. _useServiceToken:

Hooking It Together - Access {{{discovery_product}}}
----------------------------------------------------

You can set up your services written in the {{{language}}} language to use the {{{discovery_product}}} to handle service availability and load balancing. Passing service token generated through the {{{cli_product}}} CLI from services using {{{language}}} tells the {{{discovery_product}}} that requests are authorized to access the particular service in question. {{{language}}} uses Resolver objects to determine how to connect to services within the {{{discovery_product}}}. 

{{{product}}} includes a library to facilitate these connections. The {{{token_service_file}}} library (found in GitHub under {{{github_main_repo}}}/{{{library_subdirectory}}}) defines a DiscoveryConsumer resolver object that expects the service token as the argument to its constructor. Options for the resolver are defined in the {{{discovery_service_file}}} library (found in GitHub under {{{github_discovery_repo}}}/{{{library_subdirectory}}}).

Your service name as set when creating the service is also required as an argument to the RPC Client constructor. In your {{{language}}} file defining your service library, you define this client as follows:

.. code-block:: javascript
   
   class <service>Client extends Client, <serviceInterface> {}

where <service> is generally the name of your service (by convention; this is not a strict requirement) and <serviceInterface> is the name of the interface defined to define the RPC interaction being used.

To instantiate this client in Python (for example), you would do the following:

.. code-block:: python
   :emphasize-lines: 1,5
   
   import <myLibrary>
   
   ...
   
   <myClient> = myLibrary.<service>Client("<serviceName>") 

where <myLibrary> is the name of the {{{language}}} library defining the RPC contract for your service, <myClient> is your local handle to the new <service>Client client instance and <serviceName> is the name of the service as defined using the create-service CLI call.

Then you need to set the resolver used by that client instance to an instance of the DiscoveryConsumer resolver that was also passed <serviceName> at creation. You will also need to set some options using a GatewayOptions object as defined in {{{discovery_service_file}}}. Continuing the Python example above, this could be done as follows:

.. code-block:: python
   :emphasize-lines: 2,3,11,12,14
   
   import <myLibrary>
   from datawire_connect.resolver import DiscoveryConsumer
   from datawire_discovery.client import GatewayOptions
   
   ...
   
   <myClient> = myLibrary.<service>Client("<serviceName>") 
   
   ...
    
   <options> = GatewayOptions(<token>)
   <options>.gatewayHost = "disco.datawire.io"
   
   <myClient>.setResolver(DiscoveryConsumer(options))

where <options> is a local handle to the options object being passed to the resolver, and <token> is the service token obtained using the {{{cli_product}}} CLI commands (either create-service or service-token).

At this point, your service should be able to use the {{{discovery_product}}} to handle its service discovery and load balancing. If your service token expires, use the service-token command to retrieve a new one and place the new value into the existing code.

.. ifconfig:: 'draft' in publish_state
 
   [[JMK: the current gatewayHost default value is wrong and needs to be set as above
   This should not be necessary in future versions. See discovery issue #2.]]
   
   [[JMK: Are we going to start supporting refresh tokens so you don't need to manually
   get new tokens? We need a better story around this, or if we have one it needs to 
   be communicated to me]]

For example, Eliza might create an advice.q {{{language}}} library for all of her services to use containing the following:

.. code-block:: javascript
   
   ...

   interface adviceInterface {
   ...
   }

   class adviceClient extends Client, adviceInterface {}

   ...

If she wrote her Advice to the annoyingly perfect service in Python, advicetoperfect.py might include the following code:

.. code-block:: python
   
   import advice
   from datawire_connect.resolver import DiscoveryConsumer
   from datawire_discovery.client import GatewayOptions
   
   ...
   
   perfectClient = advice.adviceClient("Advice to the annoyingly perfect") 
   
   ...
    
   options = GatewayOptions(<token>)
   options.gatewayHost = "disco.datawire.io"
   
   perfectClient.setResolver(DiscoveryConsumer(options))
