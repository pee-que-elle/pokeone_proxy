# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ZonePokemon.proto

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
  name='ZonePokemon.proto',
  package='MAPAPI.Response657516655',
  syntax='proto2',
  serialized_pb=_b('\n\x11ZonePokemon.proto\x12\x18MAPAPI.Response657516655\"\xac\x01\n\x19PREFIX_AGDFASBV1132188208\"\x8e\x01\n\x0e\x42\x61\x63kgroundType\x12\t\n\x05Grass\x10\x00\x12\t\n\x05Water\x10\x01\x12\x08\n\x04\x43\x61ve\x10\x02\x12\n\n\x06Indoor\x10\x03\x12\x07\n\x03Gym\x10\x04\x12\x0b\n\x07IceCave\x10\x05\x12\x0f\n\x0b\x43rystalCave\x10\x06\x12\x08\n\x04Snow\x10\x07\x12\x08\n\x04\x43ity\x10\x08\x12\n\n\x06\x44\x65sert\x10\t\x12\t\n\x05Ocean\x10\n\"g\n\x19PREFIX_AGDFASBV1234176120\"J\n\x0e\x45ncounterTimes\x12\x07\n\x03\x44\x61y\x10\x00\x12\t\n\x05Night\x10\x01\x12\x0b\n\x07Morning\x10\x02\x12\x0b\n\x07\x45vening\x10\x03\x12\n\n\x06\x41lways\x10\x04\"_\n\x18PREFIX_AGDFASBV384257891\"C\n\x0b\x46ishingType\x12\r\n\tNoneValue\x10\x00\x12\n\n\x06OldRod\x10\x01\x12\x0b\n\x07GoodRod\x10\x02\x12\x0c\n\x08SuperRod\x10\x03\"m\n\x18PREFIX_AGDFASBV118691837\"Q\n\x06Rarity\x12\n\n\x06\x43ommon\x10\x00\x12\x0c\n\x08Uncommon\x10\x01\x12\x08\n\x04Rare\x10\x02\x12\x08\n\x04\x45pic\x10\x03\x12\x0c\n\x08Mythical\x10\x04\x12\x0b\n\x07Special\x10\x05\"t\n\x08ZoneItem\x12\x11\n\x06ItemID\x18\x01 \x01(\x05:\x01\x30\x12U\n\nItemRarity\x18\x02 \x01(\x0e\x32\x39.MAPAPI.Response657516655.PREFIX_AGDFASBV118691837.Rarity:\x06\x43ommon\"\xd9\x04\n\x0bZonePokemon\x12\x14\n\tPokemonID\x18\x01 \x01(\x05:\x01\x30\x12\x17\n\x0c\x41verageLevel\x18\x02 \x01(\x05:\x01\x30\x12\x18\n\rLevelVariance\x18\x03 \x01(\x05:\x01\x30\x12^\n\rEncounterTime\x18\x04 \x01(\x0e\x32\x42.MAPAPI.Response657516655.PREFIX_AGDFASBV1234176120.EncounterTimes:\x03\x44\x61y\x12Q\n\x06Rarity\x18\x05 \x01(\x0e\x32\x39.MAPAPI.Response657516655.PREFIX_AGDFASBV118691837.Rarity:\x06\x43ommon\x12\x31\n\x05Items\x18\x06 \x03(\x0b\x32\".MAPAPI.Response657516655.ZoneItem\x12Z\n\x07\x46ishing\x18\x07 \x01(\x0e\x32>.MAPAPI.Response657516655.PREFIX_AGDFASBV384257891.FishingType:\tNoneValue\x12\x0e\n\x06Script\x18\x08 \x01(\t\x12\x14\n\x05Party\x18\t \x01(\x08:\x05\x66\x61lse\x12\x1f\n\x10SpecialEncounter\x18\n \x01(\x08:\x05\x66\x61lse\x12_\n\x0c\x42\x61\x63kgroundID\x18\x0b \x01(\x0e\x32\x42.MAPAPI.Response657516655.PREFIX_AGDFASBV1132188208.BackgroundType:\x05Grass\x12\x17\n\x08\x44isabled\x18\x0c \x01(\x08:\x05\x66\x61lse')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREFIX_AGDFASBV1132188208_BACKGROUNDTYPE = _descriptor.EnumDescriptor(
  name='BackgroundType',
  full_name='MAPAPI.Response657516655.PREFIX_AGDFASBV1132188208.BackgroundType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Grass', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Water', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Cave', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Indoor', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Gym', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IceCave', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CrystalCave', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Snow', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='City', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Desert', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Ocean', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=78,
  serialized_end=220,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1132188208_BACKGROUNDTYPE)

_PREFIX_AGDFASBV1234176120_ENCOUNTERTIMES = _descriptor.EnumDescriptor(
  name='EncounterTimes',
  full_name='MAPAPI.Response657516655.PREFIX_AGDFASBV1234176120.EncounterTimes',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Day', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Night', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Morning', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Evening', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Always', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=251,
  serialized_end=325,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1234176120_ENCOUNTERTIMES)

_PREFIX_AGDFASBV384257891_FISHINGTYPE = _descriptor.EnumDescriptor(
  name='FishingType',
  full_name='MAPAPI.Response657516655.PREFIX_AGDFASBV384257891.FishingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneValue', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OldRod', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GoodRod', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SuperRod', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=355,
  serialized_end=422,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV384257891_FISHINGTYPE)

_PREFIX_AGDFASBV118691837_RARITY = _descriptor.EnumDescriptor(
  name='Rarity',
  full_name='MAPAPI.Response657516655.PREFIX_AGDFASBV118691837.Rarity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Common', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Uncommon', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Rare', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Epic', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Mythical', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Special', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=452,
  serialized_end=533,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV118691837_RARITY)


_PREFIX_AGDFASBV1132188208 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1132188208',
  full_name='MAPAPI.Response657516655.PREFIX_AGDFASBV1132188208',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1132188208_BACKGROUNDTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=220,
)


_PREFIX_AGDFASBV1234176120 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1234176120',
  full_name='MAPAPI.Response657516655.PREFIX_AGDFASBV1234176120',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1234176120_ENCOUNTERTIMES,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=325,
)


_PREFIX_AGDFASBV384257891 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV384257891',
  full_name='MAPAPI.Response657516655.PREFIX_AGDFASBV384257891',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV384257891_FISHINGTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=422,
)


_PREFIX_AGDFASBV118691837 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV118691837',
  full_name='MAPAPI.Response657516655.PREFIX_AGDFASBV118691837',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV118691837_RARITY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=424,
  serialized_end=533,
)


_ZONEITEM = _descriptor.Descriptor(
  name='ZoneItem',
  full_name='MAPAPI.Response657516655.ZoneItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ItemID', full_name='MAPAPI.Response657516655.ZoneItem.ItemID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ItemRarity', full_name='MAPAPI.Response657516655.ZoneItem.ItemRarity', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=535,
  serialized_end=651,
)


_ZONEPOKEMON = _descriptor.Descriptor(
  name='ZonePokemon',
  full_name='MAPAPI.Response657516655.ZonePokemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PokemonID', full_name='MAPAPI.Response657516655.ZonePokemon.PokemonID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AverageLevel', full_name='MAPAPI.Response657516655.ZonePokemon.AverageLevel', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LevelVariance', full_name='MAPAPI.Response657516655.ZonePokemon.LevelVariance', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EncounterTime', full_name='MAPAPI.Response657516655.ZonePokemon.EncounterTime', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Rarity', full_name='MAPAPI.Response657516655.ZonePokemon.Rarity', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Items', full_name='MAPAPI.Response657516655.ZonePokemon.Items', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Fishing', full_name='MAPAPI.Response657516655.ZonePokemon.Fishing', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Script', full_name='MAPAPI.Response657516655.ZonePokemon.Script', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Party', full_name='MAPAPI.Response657516655.ZonePokemon.Party', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpecialEncounter', full_name='MAPAPI.Response657516655.ZonePokemon.SpecialEncounter', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BackgroundID', full_name='MAPAPI.Response657516655.ZonePokemon.BackgroundID', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Disabled', full_name='MAPAPI.Response657516655.ZonePokemon.Disabled', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=654,
  serialized_end=1255,
)

_PREFIX_AGDFASBV1132188208_BACKGROUNDTYPE.containing_type = _PREFIX_AGDFASBV1132188208
_PREFIX_AGDFASBV1234176120_ENCOUNTERTIMES.containing_type = _PREFIX_AGDFASBV1234176120
_PREFIX_AGDFASBV384257891_FISHINGTYPE.containing_type = _PREFIX_AGDFASBV384257891
_PREFIX_AGDFASBV118691837_RARITY.containing_type = _PREFIX_AGDFASBV118691837
_ZONEITEM.fields_by_name['ItemRarity'].enum_type = _PREFIX_AGDFASBV118691837_RARITY
_ZONEPOKEMON.fields_by_name['EncounterTime'].enum_type = _PREFIX_AGDFASBV1234176120_ENCOUNTERTIMES
_ZONEPOKEMON.fields_by_name['Rarity'].enum_type = _PREFIX_AGDFASBV118691837_RARITY
_ZONEPOKEMON.fields_by_name['Items'].message_type = _ZONEITEM
_ZONEPOKEMON.fields_by_name['Fishing'].enum_type = _PREFIX_AGDFASBV384257891_FISHINGTYPE
_ZONEPOKEMON.fields_by_name['BackgroundID'].enum_type = _PREFIX_AGDFASBV1132188208_BACKGROUNDTYPE
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1132188208'] = _PREFIX_AGDFASBV1132188208
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1234176120'] = _PREFIX_AGDFASBV1234176120
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV384257891'] = _PREFIX_AGDFASBV384257891
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV118691837'] = _PREFIX_AGDFASBV118691837
DESCRIPTOR.message_types_by_name['ZoneItem'] = _ZONEITEM
DESCRIPTOR.message_types_by_name['ZonePokemon'] = _ZONEPOKEMON

PREFIX_AGDFASBV1132188208 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1132188208', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1132188208,
  __module__ = 'ZonePokemon_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response657516655.PREFIX_AGDFASBV1132188208)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1132188208)

PREFIX_AGDFASBV1234176120 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1234176120', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1234176120,
  __module__ = 'ZonePokemon_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response657516655.PREFIX_AGDFASBV1234176120)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1234176120)

PREFIX_AGDFASBV384257891 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV384257891', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV384257891,
  __module__ = 'ZonePokemon_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response657516655.PREFIX_AGDFASBV384257891)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV384257891)

PREFIX_AGDFASBV118691837 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV118691837', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV118691837,
  __module__ = 'ZonePokemon_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response657516655.PREFIX_AGDFASBV118691837)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV118691837)

ZoneItem = _reflection.GeneratedProtocolMessageType('ZoneItem', (_message.Message,), dict(
  DESCRIPTOR = _ZONEITEM,
  __module__ = 'ZonePokemon_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response657516655.ZoneItem)
  ))
_sym_db.RegisterMessage(ZoneItem)

ZonePokemon = _reflection.GeneratedProtocolMessageType('ZonePokemon', (_message.Message,), dict(
  DESCRIPTOR = _ZONEPOKEMON,
  __module__ = 'ZonePokemon_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response657516655.ZonePokemon)
  ))
_sym_db.RegisterMessage(ZonePokemon)


# @@protoc_insertion_point(module_scope)
