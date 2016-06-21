#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  king_phisher/server/signals.py
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the project nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import blinker

# database signals
db_authenticated_sessions_delete = blinker.NamedSignal(
	'db-authenticated-sessions-delete',
	"""
	Emitted before a
	:py:class:`~king_phisher.server.server.database.models.AuthenticatedSessions`
	instance is deleted.

	:param target: The target object instance.
	:param connection: The SQLAlchemy connection object which is being used to emit the SQL statements for the instance.
	:param mapper: The Mapper object which is the target of the event.
	:type mapper: :py:class:`sqlalchemy.orm.mapper.Mapper`
	"""
)

db_authenticated_sessions_insert = blinker.NamedSignal(
	'db-authenticated-sessions-insert'
)

db_authenticated_sessions_update = blinker.NamedSignal(
	'db-authenticated-sessions-update'
)

db_users_delete = blinker.NamedSignal(
	'db-users-delete'
)

db_users_insert = blinker.NamedSignal(
	'db-users-insert'
)

db_users_update = blinker.NamedSignal(
	'db-users-update'
)

# server signals
server_initialized = blinker.NamedSignal(
	'server-initialized',
	"""
	Sent when a new instance of
	:py:class:`~king_phisher.server.server.KingPhisherServer` is initialized.

	:param server: The newly initialized server instance.
	"""
)

# handler signals
request_received = blinker.NamedSignal(
	'request-received',
	"""
	Sent when a new HTTP request has been received and is about to be processed.

	:param request_handler: The handler for the received request.
	"""
)

credentials_received = blinker.NamedSignal(
	'credentials-received',
	"""
	Sent when a new pair of credentials have been submitted.

	:param request_handler: The handler for the received request.
	:param str username: The username of the credentials that were submitted.
	:param str password: The password of the credentials that were submitted.
	"""
)

rpc_method_call = blinker.NamedSignal(
	'rpc-method-call',
	"""
	Sent when a new RPC request has been received and it's corresponding method
	is about to be called.

	:param request_handler: The handler for the received request.
	:param str method: The RPC method which is about to be executed.
	:param tuple args: The arguments that are to be passed to the method.
	:param dict kwargs: The key word arguments that are to be passed to the method.
	"""
)

rpc_user_logged_in = blinker.NamedSignal(
	'rpc-user-logged-in',
	"""
	Sent when a new RPC user has successfully logged in and created a new
	authenticated session.

	:param request_handler: The handler for the received request.
	:param str session: The session ID of the newly logged in user.
	:param str name: The username of the newly logged in user.
	"""
)

rpc_user_logged_out = blinker.NamedSignal(
	'rpc-user-logged-out',
	"""
	Sent when an authenticated RPC user has successfully logged out and
	terminated their authenticated session.

	:param request_handler: The handler for the received request.
	:param str session: The session ID of the user who has logged out.
	:param str name: The username of the user who has logged out.
	"""
)

visit_received = blinker.NamedSignal(
	'visit-received',
	"""
	Sent when a new visit is received on a landing page. This is only emitted
	when a new visit entry is added to the database.

	:param request_handler: The handler for the received request.
	"""
)
