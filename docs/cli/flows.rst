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

substituting your organization name, name, and email address for the variables above. You may use spaces in the names if you surround them with single quotes (').

You should get the following response to your request:

.. code-block:: none
   
   Now logged in as [<orgId>]<email>

where <orgId> is an identifier assigned by {{{company}}} and <email> is the email address you supplied in the request.

Once this is done, you may either add additional users to your organization or start creating services per the directions below.

.. _createNewService:

Create a New Service
--------------------

1. login
2. create service

then use the token to access discovery product

.. _addUser:

Add New Users
-------------

1. login
2. invite user
3. send to invited user
3. they accept invite and create account in your org

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
