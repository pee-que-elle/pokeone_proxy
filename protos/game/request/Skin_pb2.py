# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Skin.proto

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
  name='Skin.proto',
  package='PSXAPI.Request1385765255',
  syntax='proto2',
  serialized_pb=_b('\n\nSkin.proto\x12\x18PSXAPI.Request1385765255\"\xcc\x01\n\x04Skin\x12Y\n\x06\x41\x63tion\x18\x01 \x01(\x0e\x32>.PSXAPI.Request1385765255.PREFIX_AGDFASBV2088671386.SkinAction:\tNoneValue\x12\x13\n\x08SpriteID\x18\x02 \x01(\x05:\x01\x30\x12T\n\x04Type\x18\x03 \x01(\x0e\x32;.PSXAPI.Request1385765255.PREFIX_AGDFASBV210560920.SkinType:\tNoneValue\"L\n\x19PREFIX_AGDFASBV2088671386\"/\n\nSkinAction\x12\r\n\tNoneValue\x10\x00\x12\x07\n\x03\x42uy\x10\x01\x12\t\n\x05\x45quip\x10\x02\"h\n\x18PREFIX_AGDFASBV210560920\"L\n\x08SkinType\x12\r\n\tNoneValue\x10\x00\x12\n\n\x06\x43lothe\x10\x01\x12\x07\n\x03Hat\x10\x02\x12\t\n\x05Mount\x10\x03\x12\x08\n\x04Surf\x10\x04\x12\x07\n\x03\x46ly\x10\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREFIX_AGDFASBV2088671386_SKINACTION = _descriptor.EnumDescriptor(
  name='SkinAction',
  full_name='PSXAPI.Request1385765255.PREFIX_AGDFASBV2088671386.SkinAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneValue', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Buy', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Equip', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=276,
  serialized_end=323,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV2088671386_SKINACTION)

_PREFIX_AGDFASBV210560920_SKINTYPE = _descriptor.EnumDescriptor(
  name='SkinType',
  full_name='PSXAPI.Request1385765255.PREFIX_AGDFASBV210560920.SkinType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneValue', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Clothe', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Hat', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Mount', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Surf', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Fly', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=353,
  serialized_end=429,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV210560920_SKINTYPE)


_SKIN = _descriptor.Descriptor(
  name='Skin',
  full_name='PSXAPI.Request1385765255.Skin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Action', full_name='PSXAPI.Request1385765255.Skin.Action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpriteID', full_name='PSXAPI.Request1385765255.Skin.SpriteID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Type', full_name='PSXAPI.Request1385765255.Skin.Type', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=41,
  serialized_end=245,
)


_PREFIX_AGDFASBV2088671386 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV2088671386',
  full_name='PSXAPI.Request1385765255.PREFIX_AGDFASBV2088671386',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV2088671386_SKINACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=323,
)


_PREFIX_AGDFASBV210560920 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV210560920',
  full_name='PSXAPI.Request1385765255.PREFIX_AGDFASBV210560920',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV210560920_SKINTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=429,
)

_SKIN.fields_by_name['Action'].enum_type = _PREFIX_AGDFASBV2088671386_SKINACTION
_SKIN.fields_by_name['Type'].enum_type = _PREFIX_AGDFASBV210560920_SKINTYPE
_PREFIX_AGDFASBV2088671386_SKINACTION.containing_type = _PREFIX_AGDFASBV2088671386
_PREFIX_AGDFASBV210560920_SKINTYPE.containing_type = _PREFIX_AGDFASBV210560920
DESCRIPTOR.message_types_by_name['Skin'] = _SKIN
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV2088671386'] = _PREFIX_AGDFASBV2088671386
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV210560920'] = _PREFIX_AGDFASBV210560920

Skin = _reflection.GeneratedProtocolMessageType('Skin', (_message.Message,), dict(
  DESCRIPTOR = _SKIN,
  __module__ = 'Skin_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request1385765255.Skin)
  ))
_sym_db.RegisterMessage(Skin)

PREFIX_AGDFASBV2088671386 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV2088671386', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV2088671386,
  __module__ = 'Skin_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request1385765255.PREFIX_AGDFASBV2088671386)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV2088671386)

PREFIX_AGDFASBV210560920 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV210560920', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV210560920,
  __module__ = 'Skin_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request1385765255.PREFIX_AGDFASBV210560920)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV210560920)


# @@protoc_insertion_point(module_scope)
