Introduction
============

The {{{cli_product}}} command line interface (CLI) provides a mechanism for creating and managing organizations, users, and services in the {{{cloud_product}}}.

For this purpose, an organization is a group of one or more users who work together to develop one or more microservices using the {{{cloud_product}}}. Organizations are created with a single member who can then invite additional members to participate in the group. Once these new users accept the invitation they, too, can invite other people into the organization. Similarly, any member can remove another member from the organization (including the original member). Users can belong to more than one organization but all of their actions within {{{cloud_product}}} are tied to a specific organization; each organization-user combination is effectively a different role with different permissions within the system.

[[JMK Remove from group is not yet supported]]

[[JMK Need to test user behavior in multiple organizations. It could be that from DW perspective a user can only belong to one organization and may have multiple user accounts for different organizations. ETA: Tested. User can only belong to one organization. Only one user per email in the system right now]]

Those permissions are managed using authentication tokens that contain information about the organization-user combination and grant permission to act upon the organization's services in the {{{cloud_product}}}. Tokens expire after ^^^^; at that point a new token can be requested if needed.

[[JMK They don't expire now but should before we ship. Details TBD]]

Tokens are stored in the file system of the requesting device; they are not explicitly passed as parameters or headers in API calls to the {{{cloud_product}}}. The only way to use a token from multiple devices is to physically copy the file.

[[JMK will copying the file work? check that]]

[[JMK need info to cover the topics below

-- keys vs tokens
-- user flows/what do people actually do with the tokens/how does this tie into the product as a whole
]]