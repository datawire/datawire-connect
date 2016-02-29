About this Document
===================

Welcome to the {{{cli_product}}} Command Line Interface Guide.

Intended Audience
-----------------

This documentation is written for developers who wish to use the {{{cloud_product}}} and {{{discovery_product}}} to perform discovery, health checks, and load balancing for instances of microservices developed using {{{product}}} and {{{language}}}.

Prerequisites
-------------

This documentation makes no assumptions about specific prior knowledge beyond basic familiarity with UNIX.

Conventions
-----------

The Datawire style limits formatting unless it is essential to conveying intended meaning. To that end, Datawire does not use bold or italics for emphasis or to introduce new terms nor do we format names within text in any way.

This document uses the following typographical conventions:

+-----------------------+------------------------------------------------------------+
| Format                | Usage                                                      |
+=======================+============================================================+
|``red monospace fonts``| commands and command syntax                                |
+-----------------------+------------------------------------------------------------+
| .. code-block:: none  | responses to commands                                      |
|                       |                                                            |
|    monospace fonts    |                                                            |
|    without color      |                                                            |
+-----------------------+------------------------------------------------------------+
| .. code-block:: python| code samples                                               |
|                       |                                                            |
|    monospace fonts    |                                                            |
|    colorized for the  |                                                            |
|    current language   |                                                            |
+-----------------------+------------------------------------------------------------+
| <variable>            | variables in commands, syntax, and responses               |
|                       | (anything in commands, syntax, or responses not called out |
|                       | as a variable is a literal value excepting ellipses)       |
+-----------------------+------------------------------------------------------------+
| ellipsis (...)        | optional content not pertinent to current discussion       |
+-----------------------+------------------------------------------------------------+


Known Issues
------------

* Two consecutive dashes may appear as a single endash within the documentation. There are no cases where an endash is intentionally used, so substitute two dashes anytime you see an endash in the document.