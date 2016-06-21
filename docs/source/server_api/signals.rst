.. _server-signals-label:

Server Signals
==============

Overview
--------

Server signals are used by the server to dispatch events to subscribed handlers.
This allows plugins to subscribe specific functions to be executed when a
particular event occurs. These signals are defined in the
:py:mod:`~server.signals` module.

.. _server-signals-database-label:

Database Table Signals
----------------------

.. autodata:: king_phisher.server.signals.db_authenticated_sessions_delete
   :annotation:

.. _server-signals-request-handler-label:

Request Handler Signals
-----------------------

Signals which are emitted for events specific to individual HTTP requests. These
signals use the respective instance of
:py:class:`~king_phisher.server.server.KingPhisherRequestHandler` as the sender.

.. autodata:: king_phisher.server.signals.credentials_received
   :annotation:
   :noindex:

.. autodata:: king_phisher.server.signals.request_received
   :annotation:
   :noindex:

.. autodata:: king_phisher.server.signals.rpc_user_logged_in
   :annotation:
   :noindex:

.. autodata:: king_phisher.server.signals.rpc_user_logged_out
   :annotation:
   :noindex:

.. autodata:: king_phisher.server.signals.visit_received
   :annotation:
   :noindex:

.. _server-signals-server-label:

Server Signals
--------------

Signals which are emitted for a
:py:class:`~king_phisher.server.server.KingPhisherServer` instance.

.. autodata:: king_phisher.server.signals.server_initialized
   :annotation:
   :noindex:
