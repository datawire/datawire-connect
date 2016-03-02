Introduction
============

The {{{cli_product}}} command line interface (CLI) provides a mechanism for creating and managing organizations, users, and services in the {{{discovery_product}}}. This allows {{{product}}} to handle load balancing and service discovery via the {{{cloud_product}}}.

For this purpose, an organization is a group of one or more users who work together to develop one or more microservices using {{{product}}}. Organizations are created with a single member who can then invite additional members to participate in the group. Once these new users accept the invitation they, too, can invite other people into the organization. At the current time, users may only belong to a single organization.

.. ifconfig:: 'draft' in conditions
    
   [[JMK: Future functionality]]
   
   Similarly, any member can remove another member from the organization (including the    original member). Users can belong to more than one organization but all of their actions within {{{cloud_product}}} are tied to a specific organization; each organization-user combination is effectively a different role with different permissions within the system.
   
   [[JMK: End future functionality]]

Any user in an organization can create services for that organization by default. These services are registered and assigned a handle (by the user creating them) which is used by the {{{discovery_product}}} to manage instances of the service. Service tokens can be generated via the {{{cli_product}}} CLI that tell the {{{discovery_product}}} that a particular request is allowed to interact with the service and its discovery information. These tokens expire after 14 days; at that point new tokens can be requested and distributed as needed.

.. ifconfig:: 'draft' in conditions
   
   [[JMK: Are we going to have some type of automatic refresh mechanism?]]

