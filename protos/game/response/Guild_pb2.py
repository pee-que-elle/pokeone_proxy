# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Guild.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bcl_pb2 as bcl__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Guild.proto',
  package='PSXAPI.Response31',
  syntax='proto2',
  serialized_pb=_b('\n\x0bGuild.proto\x12\x11PSXAPI.Response31\x1a\tbcl.proto\"\xa3\x02\n\x05Guild\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\x17\n\x04\x43hat\x18\x03 \x01(\x0b\x32\t.bcl.Guid\x12/\n\x07Members\x18\x04 \x03(\x0b\x32\x1e.PSXAPI.Response31.GuildMember\x12\x31\n\x04Rank\x18\x05 \x01(\x0e\x32\x1c.PSXAPI.Response31.GuildRank:\x05Unset\x12\x13\n\x08\x45mblemId\x18\x06 \x01(\r:\x01\x30\x12\x1a\n\x0fMembersTotalMax\x18\x07 \x01(\x05:\x01\x30\x12\x1c\n\x11MembersCurrentMax\x18\x08 \x01(\x05:\x01\x30\x12\x16\n\x0bUpgradeGold\x18\t \x01(\r:\x01\x30\x12\x17\n\x0cUpgradeMoney\x18\n \x01(\r:\x01\x30\"\xb1\x01\n\x0bGuildMember\x12\x10\n\x08Username\x18\x01 \x01(\t\x12\x31\n\x04Rank\x18\x02 \x01(\x0e\x32\x1c.PSXAPI.Response31.GuildRank:\x05Unset\x12\x15\n\x06Online\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\x05Since\x18\x04 \x01(\x0b\x32\r.bcl.TimeSpan\x12\x16\n\x07Removed\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x10\n\x05Level\x18\x06 \x01(\r:\x01\x30*G\n\tGuildRank\x12\t\n\x05Unset\x10\x00\x12\x0b\n\x07\x43reator\x10\x01\x12\t\n\x05\x41\x64min\x10\x02\x12\r\n\tModerator\x10\x03\x12\x08\n\x04User\x10\x04')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_GUILDRANK = _descriptor.EnumDescriptor(
  name='GuildRank',
  full_name='PSXAPI.Response31.GuildRank',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unset', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Creator', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Admin', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Moderator', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='User', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=519,
  serialized_end=590,
)
_sym_db.RegisterEnumDescriptor(_GUILDRANK)

GuildRank = enum_type_wrapper.EnumTypeWrapper(_GUILDRANK)
Unset = 0
Creator = 1
Admin = 2
Moderator = 3
User = 4



_GUILD = _descriptor.Descriptor(
  name='Guild',
  full_name='PSXAPI.Response31.Guild',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='PSXAPI.Response31.Guild.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Message', full_name='PSXAPI.Response31.Guild.Message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Chat', full_name='PSXAPI.Response31.Guild.Chat', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Members', full_name='PSXAPI.Response31.Guild.Members', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Rank', full_name='PSXAPI.Response31.Guild.Rank', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EmblemId', full_name='PSXAPI.Response31.Guild.EmblemId', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MembersTotalMax', full_name='PSXAPI.Response31.Guild.MembersTotalMax', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MembersCurrentMax', full_name='PSXAPI.Response31.Guild.MembersCurrentMax', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='UpgradeGold', full_name='PSXAPI.Response31.Guild.UpgradeGold', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='UpgradeMoney', full_name='PSXAPI.Response31.Guild.UpgradeMoney', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=337,
)


_GUILDMEMBER = _descriptor.Descriptor(
  name='GuildMember',
  full_name='PSXAPI.Response31.GuildMember',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Username', full_name='PSXAPI.Response31.GuildMember.Username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Rank', full_name='PSXAPI.Response31.GuildMember.Rank', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Online', full_name='PSXAPI.Response31.GuildMember.Online', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Since', full_name='PSXAPI.Response31.GuildMember.Since', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Removed', full_name='PSXAPI.Response31.GuildMember.Removed', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Level', full_name='PSXAPI.Response31.GuildMember.Level', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=340,
  serialized_end=517,
)

_GUILD.fields_by_name['Chat'].message_type = bcl__pb2._GUID
_GUILD.fields_by_name['Members'].message_type = _GUILDMEMBER
_GUILD.fields_by_name['Rank'].enum_type = _GUILDRANK
_GUILDMEMBER.fields_by_name['Rank'].enum_type = _GUILDRANK
_GUILDMEMBER.fields_by_name['Since'].message_type = bcl__pb2._TIMESPAN
DESCRIPTOR.message_types_by_name['Guild'] = _GUILD
DESCRIPTOR.message_types_by_name['GuildMember'] = _GUILDMEMBER
DESCRIPTOR.enum_types_by_name['GuildRank'] = _GUILDRANK

Guild = _reflection.GeneratedProtocolMessageType('Guild', (_message.Message,), dict(
  DESCRIPTOR = _GUILD,
  __module__ = 'Guild_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response31.Guild)
  ))
_sym_db.RegisterMessage(Guild)

GuildMember = _reflection.GeneratedProtocolMessageType('GuildMember', (_message.Message,), dict(
  DESCRIPTOR = _GUILDMEMBER,
  __module__ = 'Guild_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response31.GuildMember)
  ))
_sym_db.RegisterMessage(GuildMember)


# @@protoc_insertion_point(module_scope)