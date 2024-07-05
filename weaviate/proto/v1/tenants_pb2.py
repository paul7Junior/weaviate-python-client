# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/tenants.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x10v1/tenants.proto\x12\x0bweaviate.v1"\\\n\x11TenantsGetRequest\x12\x12\n\ncollection\x18\x01 \x01(\t\x12)\n\x05names\x18\x02 \x01(\x0b\x32\x18.weaviate.v1.TenantNamesH\x00\x42\x08\n\x06params"\x1d\n\x0bTenantNames\x12\x0e\n\x06values\x18\x01 \x03(\t"E\n\x0fTenantsGetReply\x12\x0c\n\x04took\x18\x01 \x01(\x02\x12$\n\x07tenants\x18\x02 \x03(\x0b\x32\x13.weaviate.v1.Tenant"R\n\x06Tenant\x12\x0c\n\x04name\x18\x01 \x01(\t\x12:\n\x0f\x61\x63tivity_status\x18\x02 \x01(\x0e\x32!.weaviate.v1.TenantActivityStatus*\xb0\x03\n\x14TenantActivityStatus\x12&\n"TENANT_ACTIVITY_STATUS_UNSPECIFIED\x10\x00\x12\x1e\n\x1aTENANT_ACTIVITY_STATUS_HOT\x10\x01\x12\x1f\n\x1bTENANT_ACTIVITY_STATUS_COLD\x10\x02\x12!\n\x1dTENANT_ACTIVITY_STATUS_FROZEN\x10\x04\x12%\n!TENANT_ACTIVITY_STATUS_UNFREEZING\x10\x05\x12#\n\x1fTENANT_ACTIVITY_STATUS_FREEZING\x10\x06\x12!\n\x1dTENANT_ACTIVITY_STATUS_ACTIVE\x10\x07\x12#\n\x1fTENANT_ACTIVITY_STATUS_INACTIVE\x10\x08\x12$\n TENANT_ACTIVITY_STATUS_OFFLOADED\x10\t\x12%\n!TENANT_ACTIVITY_STATUS_OFFLOADING\x10\n\x12%\n!TENANT_ACTIVITY_STATUS_ACTIVATING\x10\x0b"\x04\x08\x03\x10\x03\x42q\n#io.weaviate.client.grpc.protocol.v1B\x14WeaviateProtoTenantsZ4github.com/weaviate/weaviate/grpc/generated;protocolb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.tenants_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n#io.weaviate.client.grpc.protocol.v1B\024WeaviateProtoTenantsZ4github.com/weaviate/weaviate/grpc/generated;protocol"
    _globals["_TENANTACTIVITYSTATUS"]._serialized_start = 314
    _globals["_TENANTACTIVITYSTATUS"]._serialized_end = 746
    _globals["_TENANTSGETREQUEST"]._serialized_start = 33
    _globals["_TENANTSGETREQUEST"]._serialized_end = 125
    _globals["_TENANTNAMES"]._serialized_start = 127
    _globals["_TENANTNAMES"]._serialized_end = 156
    _globals["_TENANTSGETREPLY"]._serialized_start = 158
    _globals["_TENANTSGETREPLY"]._serialized_end = 227
    _globals["_TENANT"]._serialized_start = 229
    _globals["_TENANT"]._serialized_end = 311
# @@protoc_insertion_point(module_scope)
