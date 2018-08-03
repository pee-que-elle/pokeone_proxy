# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Areas.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Areas.proto',
  package='PSXAPI.Response1610063222',
  syntax='proto2',
  serialized_pb=_b('\n\x0b\x41reas.proto\x12\x19PSXAPI.Response1610063222\"^\n\x04\x41rea\x12\x0b\n\x03Map\x18\x01 \x01(\t\x12\x10\n\x08\x41reaName\x18\x02 \x01(\t\x12\x37\n\x07Pokemon\x18\x03 \x03(\x0b\x32&.PSXAPI.Response1610063222.AreaPokemon\"\xf8\x01\n\x0b\x41reaPokemon\x12\x14\n\tPokemonID\x18\x01 \x01(\x05:\x01\x30\x12\x16\n\x07\x46ishing\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x12\n\x03\x44\x61y\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x05Night\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07Morning\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07\x45vening\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x61\n\x07Pokedex\x18\x07 \x01(\x0e\x32\x45.PSXAPI.Response1610063222.PREFIX_AGDFASBV247256079.PokedexEntryState:\tNoneValue\"P\n\x05\x41reas\x12\x14\n\tPokemonID\x18\x01 \x01(\x05:\x01\x30\x12\x31\n\x08\x41reaList\x18\x02 \x03(\x0b\x32\x1f.PSXAPI.Response1610063222.Area\"T\n\x18PREFIX_AGDFASBV247256079\"8\n\x11PokedexEntryState\x12\r\n\tNoneValue\x10\x00\x12\x08\n\x04Seen\x10\x01\x12\n\n\x06\x43\x61ught\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREFIX_AGDFASBV247256079_POKEDEXENTRYSTATE = _descriptor.EnumDescriptor(
  name='PokedexEntryState',
  full_name='PSXAPI.Response1610063222.PREFIX_AGDFASBV247256079.PokedexEntryState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneValue', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Seen', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Caught', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=499,
  serialized_end=555,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV247256079_POKEDEXENTRYSTATE)


_AREA = _descriptor.Descriptor(
  name='Area',
  full_name='PSXAPI.Response1610063222.Area',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Map', full_name='PSXAPI.Response1610063222.Area.Map', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AreaName', full_name='PSXAPI.Response1610063222.Area.AreaName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pokemon', full_name='PSXAPI.Response1610063222.Area.Pokemon', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=42,
  serialized_end=136,
)


_AREAPOKEMON = _descriptor.Descriptor(
  name='AreaPokemon',
  full_name='PSXAPI.Response1610063222.AreaPokemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PokemonID', full_name='PSXAPI.Response1610063222.AreaPokemon.PokemonID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Fishing', full_name='PSXAPI.Response1610063222.AreaPokemon.Fishing', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Day', full_name='PSXAPI.Response1610063222.AreaPokemon.Day', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Night', full_name='PSXAPI.Response1610063222.AreaPokemon.Night', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Morning', full_name='PSXAPI.Response1610063222.AreaPokemon.Morning', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Evening', full_name='PSXAPI.Response1610063222.AreaPokemon.Evening', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pokedex', full_name='PSXAPI.Response1610063222.AreaPokemon.Pokedex', index=6,
      number=7, type=14, cpp_type=8, label=1,
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
  serialized_start=139,
  serialized_end=387,
)


_AREAS = _descriptor.Descriptor(
  name='Areas',
  full_name='PSXAPI.Response1610063222.Areas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PokemonID', full_name='PSXAPI.Response1610063222.Areas.PokemonID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AreaList', full_name='PSXAPI.Response1610063222.Areas.AreaList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=389,
  serialized_end=469,
)


_PREFIX_AGDFASBV247256079 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV247256079',
  full_name='PSXAPI.Response1610063222.PREFIX_AGDFASBV247256079',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV247256079_POKEDEXENTRYSTATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=471,
  serialized_end=555,
)

_AREA.fields_by_name['Pokemon'].message_type = _AREAPOKEMON
_AREAPOKEMON.fields_by_name['Pokedex'].enum_type = _PREFIX_AGDFASBV247256079_POKEDEXENTRYSTATE
_AREAS.fields_by_name['AreaList'].message_type = _AREA
_PREFIX_AGDFASBV247256079_POKEDEXENTRYSTATE.containing_type = _PREFIX_AGDFASBV247256079
DESCRIPTOR.message_types_by_name['Area'] = _AREA
DESCRIPTOR.message_types_by_name['AreaPokemon'] = _AREAPOKEMON
DESCRIPTOR.message_types_by_name['Areas'] = _AREAS
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV247256079'] = _PREFIX_AGDFASBV247256079

Area = _reflection.GeneratedProtocolMessageType('Area', (_message.Message,), dict(
  DESCRIPTOR = _AREA,
  __module__ = 'Areas_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1610063222.Area)
  ))
_sym_db.RegisterMessage(Area)

AreaPokemon = _reflection.GeneratedProtocolMessageType('AreaPokemon', (_message.Message,), dict(
  DESCRIPTOR = _AREAPOKEMON,
  __module__ = 'Areas_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1610063222.AreaPokemon)
  ))
_sym_db.RegisterMessage(AreaPokemon)

Areas = _reflection.GeneratedProtocolMessageType('Areas', (_message.Message,), dict(
  DESCRIPTOR = _AREAS,
  __module__ = 'Areas_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1610063222.Areas)
  ))
_sym_db.RegisterMessage(Areas)

PREFIX_AGDFASBV247256079 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV247256079', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV247256079,
  __module__ = 'Areas_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1610063222.PREFIX_AGDFASBV247256079)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV247256079)


# @@protoc_insertion_point(module_scope)
