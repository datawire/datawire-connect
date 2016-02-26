Usage Flows
===========

While the overall flow through the {{{cli_product}}} Command Line Interface and the {{{discovery_product}}} should be the same for most users, it does not have to be a continuous path and different users may enter the flow at different points. This page attempts to pinpoint some of those entry points and the likely actions you'll need to take at each.

* :ref:`New to {{{product}}} - create a new organization <createNewOrg>`
* :ref:`Prototyping - create a new service <createNewService>`
* :ref:`Expanding Beyond Prototype - add new users <addUser>`
* :ref:`Expanding Beyond Prototype - get new service tokens <getServiceToken>`
* :ref:`Hooking It Together - access {{{discovery_product}}} <useServiceToken>`

.. _createNewOrg:

Create a New Organization
-------------------------

If you are new to {{{product}}} or have not used {{{discovery_product}}} before, the first step is creating an organization in the system. This organization will automatically contain one user - its creator - and more can be added later.

To create a new organization, use the following command:

``dwc create-org <organizationName> <name> <email>``

substituting your organization name, name, and email address for the variables above. You may use spaces and apostrophes in the names if you surround them with double quotes (").

You should get the following response to your request:

.. code-block:: none
   
   Now logged in as [<orgId>]<email>

where <orgId> is an identifier assigned by {{{company}}} and <email> is the email address you supplied in the request.

Once this is done, you may either add additional users to your organization or start creating services per the directions below.

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

Create a New Service
--------------------

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

At this point you can use the token to access this service in the {{{discovery_product}}}.

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

Add New Users
-------------

The ultimate goal of the {{{cli_product}}} command line interface is to generate tokens for use with the {{{discovery_product}}}. These tokens are used outside of the CLI and not everyone who needs tokens necessarily needs access to the CLI. Each organization should decide on a policy regarding how to generate and distribute tokens including which users need access to the token generation process.

If your organization decides that multiple users should be able to generate or retrieve tokens, the original member of an organization may invite one or more additional users and those users may also invite additional users into the organization. Basically, to invite users into an organization, you must be logged in as an existing member of the organization.

if you are not already logged in, do so using the login command as follows:

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

..
   JMK: Should I lose the note? It may do more harm than good to give people ideas on how to hijack a new account.

One the new user has the invitation code and installs the {{{cli_product}}}, they can submit the invitation command as follows:

``dwc accept-invitation <invitationCode>``

They will be asked to supply their full name and enter their password twice. Assuming the passwords agree, the invitation will be processed and a new account created, resulting in the new user being logged in to your organization as follows:

.. code-block:: none
   
   Accepting invitation...   
   Now logged in as [<orgId>]<email>

He can then create services or invite additional users at will.

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

Get New Service Tokens
----------------------

1. login
2. request token

then use it to access discovery product

.. _useServiceToken:

Access {{{discovery_product}}}
------------------------------

1. get token if you do not already have one
2. set up resolver
3. plug token in
