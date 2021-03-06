# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server2.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='server2.proto',
  package='blog_proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rserver2.proto\x12\nblog_proto\x1a\x1bgoogle/protobuf/empty.proto\"\x1c\n\x0eGetListRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"6\n\x08\x42logPost\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t2K\n\rGetController\x12:\n\x04List\x12\x1a.blog_proto.GetListRequest\x1a\x14.blog_proto.BlogPost\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_GETLISTREQUEST = _descriptor.Descriptor(
  name='GetListRequest',
  full_name='blog_proto.GetListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='blog_proto.GetListRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=58,
  serialized_end=86,
)


_BLOGPOST = _descriptor.Descriptor(
  name='BlogPost',
  full_name='blog_proto.BlogPost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='blog_proto.BlogPost.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='blog_proto.BlogPost.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='blog_proto.BlogPost.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=88,
  serialized_end=142,
)

DESCRIPTOR.message_types_by_name['GetListRequest'] = _GETLISTREQUEST
DESCRIPTOR.message_types_by_name['BlogPost'] = _BLOGPOST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetListRequest = _reflection.GeneratedProtocolMessageType('GetListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLISTREQUEST,
  '__module__' : 'server2_pb2'
  # @@protoc_insertion_point(class_scope:blog_proto.GetListRequest)
  })
_sym_db.RegisterMessage(GetListRequest)

BlogPost = _reflection.GeneratedProtocolMessageType('BlogPost', (_message.Message,), {
  'DESCRIPTOR' : _BLOGPOST,
  '__module__' : 'server2_pb2'
  # @@protoc_insertion_point(class_scope:blog_proto.BlogPost)
  })
_sym_db.RegisterMessage(BlogPost)



_GETCONTROLLER = _descriptor.ServiceDescriptor(
  name='GetController',
  full_name='blog_proto.GetController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=144,
  serialized_end=219,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='blog_proto.GetController.List',
    index=0,
    containing_service=None,
    input_type=_GETLISTREQUEST,
    output_type=_BLOGPOST,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GETCONTROLLER)

DESCRIPTOR.services_by_name['GetController'] = _GETCONTROLLER

# @@protoc_insertion_point(module_scope)
