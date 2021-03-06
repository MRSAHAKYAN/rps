# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='game.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ngame.proto\"\x16\n\x06Player\x12\x0c\n\x04name\x18\x01 \x01(\t\"H\n\nRoomConfig\x12\x10\n\x08\x63\x61pacity\x18\x01 \x01(\x05\x12\x11\n\tmax_score\x18\x02 \x01(\x05\x12\x15\n\ronly_computer\x18\x03 \x01(\x08\"M\n\x15RegisterPlayerRequest\x12\x17\n\x06player\x18\x01 \x01(\x0b\x32\x07.Player\x12\x1b\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x0b.RoomConfig\"H\n\x16RegisterPlayerResponse\x12\x17\n\x06status\x18\x01 \x01(\x0e\x32\x07.Status\x12\x15\n\rerror_message\x18\x02 \x01(\t\"\x92\x01\n\x18\x43hooseCombinationRequest\x12\x17\n\x06player\x18\x01 \x01(\x0b\x32\x07.Player\x12\x30\n\x06\x63hoice\x18\x02 \x01(\x0e\x32 .ChooseCombinationRequest.Choice\"+\n\x06\x43hoice\x12\x08\n\x04ROCK\x10\x00\x12\t\n\x05PAPER\x10\x01\x12\x0c\n\x08SCISSORS\x10\x02\"K\n\x19\x43hooseCombinationResponse\x12\x17\n\x06status\x18\x01 \x01(\x0e\x32\x07.Status\x12\x15\n\rerror_message\x18\x02 \x01(\t\"J\n\x12SendWinnersRequest\x12\x18\n\x07winners\x18\x01 \x03(\x0b\x32\x07.Player\x12\x1a\n\treceivers\x18\x02 \x03(\x0b\x32\x07.Player\"\x15\n\x13SendWinnersResponse\".\n\x13RemovePlayerRequest\x12\x17\n\x06player\x18\x01 \x01(\x0b\x32\x07.Player\"\x16\n\x14RemovePlayerResponse*\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x32\xdc\x01\n\x0eRoomController\x12\x41\n\x0eRegisterPlayer\x12\x16.RegisterPlayerRequest\x1a\x17.RegisterPlayerResponse\x12J\n\x11\x43hooseCombination\x12\x19.ChooseCombinationRequest\x1a\x1a.ChooseCombinationResponse\x12;\n\x0cRemovePlayer\x12\x14.RemovePlayerRequest\x1a\x15.RemovePlayerResponse2E\n\tWebServer\x12\x38\n\x0bSendWinners\x12\x13.SendWinnersRequest\x1a\x14.SendWinnersResponseb\x06proto3'
)

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=662,
  serialized_end=689,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
OK = 0
ERROR = 1


_CHOOSECOMBINATIONREQUEST_CHOICE = _descriptor.EnumDescriptor(
  name='Choice',
  full_name='ChooseCombinationRequest.Choice',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROCK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAPER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCISSORS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=369,
  serialized_end=412,
)
_sym_db.RegisterEnumDescriptor(_CHOOSECOMBINATIONREQUEST_CHOICE)


_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Player.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=36,
)


_ROOMCONFIG = _descriptor.Descriptor(
  name='RoomConfig',
  full_name='RoomConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='capacity', full_name='RoomConfig.capacity', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_score', full_name='RoomConfig.max_score', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='only_computer', full_name='RoomConfig.only_computer', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=110,
)


_REGISTERPLAYERREQUEST = _descriptor.Descriptor(
  name='RegisterPlayerRequest',
  full_name='RegisterPlayerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player', full_name='RegisterPlayerRequest.player', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='RegisterPlayerRequest.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=189,
)


_REGISTERPLAYERRESPONSE = _descriptor.Descriptor(
  name='RegisterPlayerResponse',
  full_name='RegisterPlayerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='RegisterPlayerResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='RegisterPlayerResponse.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=263,
)


_CHOOSECOMBINATIONREQUEST = _descriptor.Descriptor(
  name='ChooseCombinationRequest',
  full_name='ChooseCombinationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player', full_name='ChooseCombinationRequest.player', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='choice', full_name='ChooseCombinationRequest.choice', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHOOSECOMBINATIONREQUEST_CHOICE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=412,
)


_CHOOSECOMBINATIONRESPONSE = _descriptor.Descriptor(
  name='ChooseCombinationResponse',
  full_name='ChooseCombinationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ChooseCombinationResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='ChooseCombinationResponse.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=414,
  serialized_end=489,
)


_SENDWINNERSREQUEST = _descriptor.Descriptor(
  name='SendWinnersRequest',
  full_name='SendWinnersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='winners', full_name='SendWinnersRequest.winners', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receivers', full_name='SendWinnersRequest.receivers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=491,
  serialized_end=565,
)


_SENDWINNERSRESPONSE = _descriptor.Descriptor(
  name='SendWinnersResponse',
  full_name='SendWinnersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=567,
  serialized_end=588,
)


_REMOVEPLAYERREQUEST = _descriptor.Descriptor(
  name='RemovePlayerRequest',
  full_name='RemovePlayerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player', full_name='RemovePlayerRequest.player', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=590,
  serialized_end=636,
)


_REMOVEPLAYERRESPONSE = _descriptor.Descriptor(
  name='RemovePlayerResponse',
  full_name='RemovePlayerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=638,
  serialized_end=660,
)

_REGISTERPLAYERREQUEST.fields_by_name['player'].message_type = _PLAYER
_REGISTERPLAYERREQUEST.fields_by_name['config'].message_type = _ROOMCONFIG
_REGISTERPLAYERRESPONSE.fields_by_name['status'].enum_type = _STATUS
_CHOOSECOMBINATIONREQUEST.fields_by_name['player'].message_type = _PLAYER
_CHOOSECOMBINATIONREQUEST.fields_by_name['choice'].enum_type = _CHOOSECOMBINATIONREQUEST_CHOICE
_CHOOSECOMBINATIONREQUEST_CHOICE.containing_type = _CHOOSECOMBINATIONREQUEST
_CHOOSECOMBINATIONRESPONSE.fields_by_name['status'].enum_type = _STATUS
_SENDWINNERSREQUEST.fields_by_name['winners'].message_type = _PLAYER
_SENDWINNERSREQUEST.fields_by_name['receivers'].message_type = _PLAYER
_REMOVEPLAYERREQUEST.fields_by_name['player'].message_type = _PLAYER
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.message_types_by_name['RoomConfig'] = _ROOMCONFIG
DESCRIPTOR.message_types_by_name['RegisterPlayerRequest'] = _REGISTERPLAYERREQUEST
DESCRIPTOR.message_types_by_name['RegisterPlayerResponse'] = _REGISTERPLAYERRESPONSE
DESCRIPTOR.message_types_by_name['ChooseCombinationRequest'] = _CHOOSECOMBINATIONREQUEST
DESCRIPTOR.message_types_by_name['ChooseCombinationResponse'] = _CHOOSECOMBINATIONRESPONSE
DESCRIPTOR.message_types_by_name['SendWinnersRequest'] = _SENDWINNERSREQUEST
DESCRIPTOR.message_types_by_name['SendWinnersResponse'] = _SENDWINNERSRESPONSE
DESCRIPTOR.message_types_by_name['RemovePlayerRequest'] = _REMOVEPLAYERREQUEST
DESCRIPTOR.message_types_by_name['RemovePlayerResponse'] = _REMOVEPLAYERRESPONSE
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:Player)
  })
_sym_db.RegisterMessage(Player)

RoomConfig = _reflection.GeneratedProtocolMessageType('RoomConfig', (_message.Message,), {
  'DESCRIPTOR' : _ROOMCONFIG,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:RoomConfig)
  })
_sym_db.RegisterMessage(RoomConfig)

RegisterPlayerRequest = _reflection.GeneratedProtocolMessageType('RegisterPlayerRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERPLAYERREQUEST,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:RegisterPlayerRequest)
  })
_sym_db.RegisterMessage(RegisterPlayerRequest)

RegisterPlayerResponse = _reflection.GeneratedProtocolMessageType('RegisterPlayerResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERPLAYERRESPONSE,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:RegisterPlayerResponse)
  })
_sym_db.RegisterMessage(RegisterPlayerResponse)

ChooseCombinationRequest = _reflection.GeneratedProtocolMessageType('ChooseCombinationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHOOSECOMBINATIONREQUEST,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:ChooseCombinationRequest)
  })
_sym_db.RegisterMessage(ChooseCombinationRequest)

ChooseCombinationResponse = _reflection.GeneratedProtocolMessageType('ChooseCombinationResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHOOSECOMBINATIONRESPONSE,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:ChooseCombinationResponse)
  })
_sym_db.RegisterMessage(ChooseCombinationResponse)

SendWinnersRequest = _reflection.GeneratedProtocolMessageType('SendWinnersRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDWINNERSREQUEST,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:SendWinnersRequest)
  })
_sym_db.RegisterMessage(SendWinnersRequest)

SendWinnersResponse = _reflection.GeneratedProtocolMessageType('SendWinnersResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDWINNERSRESPONSE,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:SendWinnersResponse)
  })
_sym_db.RegisterMessage(SendWinnersResponse)

RemovePlayerRequest = _reflection.GeneratedProtocolMessageType('RemovePlayerRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPLAYERREQUEST,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:RemovePlayerRequest)
  })
_sym_db.RegisterMessage(RemovePlayerRequest)

RemovePlayerResponse = _reflection.GeneratedProtocolMessageType('RemovePlayerResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPLAYERRESPONSE,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:RemovePlayerResponse)
  })
_sym_db.RegisterMessage(RemovePlayerResponse)



_ROOMCONTROLLER = _descriptor.ServiceDescriptor(
  name='RoomController',
  full_name='RoomController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=692,
  serialized_end=912,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterPlayer',
    full_name='RoomController.RegisterPlayer',
    index=0,
    containing_service=None,
    input_type=_REGISTERPLAYERREQUEST,
    output_type=_REGISTERPLAYERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ChooseCombination',
    full_name='RoomController.ChooseCombination',
    index=1,
    containing_service=None,
    input_type=_CHOOSECOMBINATIONREQUEST,
    output_type=_CHOOSECOMBINATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemovePlayer',
    full_name='RoomController.RemovePlayer',
    index=2,
    containing_service=None,
    input_type=_REMOVEPLAYERREQUEST,
    output_type=_REMOVEPLAYERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROOMCONTROLLER)

DESCRIPTOR.services_by_name['RoomController'] = _ROOMCONTROLLER


_WEBSERVER = _descriptor.ServiceDescriptor(
  name='WebServer',
  full_name='WebServer',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=914,
  serialized_end=983,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendWinners',
    full_name='WebServer.SendWinners',
    index=0,
    containing_service=None,
    input_type=_SENDWINNERSREQUEST,
    output_type=_SENDWINNERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WEBSERVER)

DESCRIPTOR.services_by_name['WebServer'] = _WEBSERVER

# @@protoc_insertion_point(module_scope)
