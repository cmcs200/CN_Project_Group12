# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\" \n\rClientRequest\x12\x0f\n\x07request\x18\x01 \x03(\t\"\"\n\x0e\x43lientResponse\x12\x10\n\x08response\x18\x01 \x01(\t2I\n\x15\x43lientProviderRequest\x12\x30\n\rDBMakeRequest\x12\x0e.ClientRequest\x1a\x0f.ClientResponseb\x06proto3')



_CLIENTREQUEST = DESCRIPTOR.message_types_by_name['ClientRequest']
_CLIENTRESPONSE = DESCRIPTOR.message_types_by_name['ClientResponse']
ClientRequest = _reflection.GeneratedProtocolMessageType('ClientRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTREQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ClientRequest)
  })
_sym_db.RegisterMessage(ClientRequest)

ClientResponse = _reflection.GeneratedProtocolMessageType('ClientResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTRESPONSE,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:ClientResponse)
  })
_sym_db.RegisterMessage(ClientResponse)

_CLIENTPROVIDERREQUEST = DESCRIPTOR.services_by_name['ClientProviderRequest']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CLIENTREQUEST._serialized_start=18
  _CLIENTREQUEST._serialized_end=50
  _CLIENTRESPONSE._serialized_start=52
  _CLIENTRESPONSE._serialized_end=86
  _CLIENTPROVIDERREQUEST._serialized_start=88
  _CLIENTPROVIDERREQUEST._serialized_end=161
# @@protoc_insertion_point(module_scope)
