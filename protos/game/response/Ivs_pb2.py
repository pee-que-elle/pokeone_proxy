# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Ivs.proto

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
import Evolve_pb2 as Evolve__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Ivs.proto',
  package='PSXAPI.Response35157105',
  syntax='proto2',
  serialized_pb=_b('\n\tIvs.proto\x12\x17PSXAPI.Response35157105\x1a\tbcl.proto\x1a\x0c\x45volve.proto\"\xa8\x01\n\x03Ivs\x12\x1d\n\nPokemonUID\x18\x01 \x01(\x0b\x32\t.bcl.Guid\x12\x10\n\x05Money\x18\x02 \x01(\r:\x01\x30\x12\x0f\n\x04Gold\x18\x03 \x01(\r:\x01\x30\x12\"\n\x07Pokemon\x18\x04 \x01(\x0b\x32\x11.InventoryPokemon\x12;\n\x06Result\x18\x05 \x01(\x0e\x32\".PSXAPI.Response35157105.IvsResult:\x07\x46\x61iled0*2\n\tIvsResult\x12\x0b\n\x07\x46\x61iled0\x10\x00\x12\x0b\n\x07\x43hanged\x10\x01\x12\x0b\n\x07Request\x10\x02')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,Evolve__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_IVSRESULT = _descriptor.EnumDescriptor(
  name='IvsResult',
  full_name='PSXAPI.Response35157105.IvsResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Failed0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Changed', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Request', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=234,
  serialized_end=284,
)
_sym_db.RegisterEnumDescriptor(_IVSRESULT)

IvsResult = enum_type_wrapper.EnumTypeWrapper(_IVSRESULT)
Failed0 = 0
Changed = 1
Request = 2



_IVS = _descriptor.Descriptor(
  name='Ivs',
  full_name='PSXAPI.Response35157105.Ivs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PokemonUID', full_name='PSXAPI.Response35157105.Ivs.PokemonUID', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Money', full_name='PSXAPI.Response35157105.Ivs.Money', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Gold', full_name='PSXAPI.Response35157105.Ivs.Gold', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pokemon', full_name='PSXAPI.Response35157105.Ivs.Pokemon', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Result', full_name='PSXAPI.Response35157105.Ivs.Result', index=4,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=64,
  serialized_end=232,
)

_IVS.fields_by_name['PokemonUID'].message_type = bcl__pb2._GUID
_IVS.fields_by_name['Pokemon'].message_type = Evolve__pb2._INVENTORYPOKEMON
_IVS.fields_by_name['Result'].enum_type = _IVSRESULT
DESCRIPTOR.message_types_by_name['Ivs'] = _IVS
DESCRIPTOR.enum_types_by_name['IvsResult'] = _IVSRESULT

Ivs = _reflection.GeneratedProtocolMessageType('Ivs', (_message.Message,), dict(
  DESCRIPTOR = _IVS,
  __module__ = 'Ivs_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response35157105.Ivs)
  ))
_sym_db.RegisterMessage(Ivs)


# @@protoc_insertion_point(module_scope)