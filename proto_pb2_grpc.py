# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import proto_pb2 as proto__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in proto_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MessagingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterPublicKey = channel.unary_unary(
                '/MessagingService/RegisterPublicKey',
                request_serializer=proto__pb2.PublicKey.SerializeToString,
                response_deserializer=proto__pb2.Response.FromString,
                _registered_method=True)
        self.RequestPublicKey = channel.unary_unary(
                '/MessagingService/RequestPublicKey',
                request_serializer=proto__pb2.ClientRequest.SerializeToString,
                response_deserializer=proto__pb2.PublicKey.FromString,
                _registered_method=True)
        self.SendMessage = channel.unary_unary(
                '/MessagingService/SendMessage',
                request_serializer=proto__pb2.Message.SerializeToString,
                response_deserializer=proto__pb2.Response.FromString,
                _registered_method=True)
        self.ReceiveMessages = channel.unary_stream(
                '/MessagingService/ReceiveMessages',
                request_serializer=proto__pb2.ClientRequest.SerializeToString,
                response_deserializer=proto__pb2.Message.FromString,
                _registered_method=True)


class MessagingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterPublicKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestPublicKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveMessages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessagingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterPublicKey': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPublicKey,
                    request_deserializer=proto__pb2.PublicKey.FromString,
                    response_serializer=proto__pb2.Response.SerializeToString,
            ),
            'RequestPublicKey': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestPublicKey,
                    request_deserializer=proto__pb2.ClientRequest.FromString,
                    response_serializer=proto__pb2.PublicKey.SerializeToString,
            ),
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=proto__pb2.Message.FromString,
                    response_serializer=proto__pb2.Response.SerializeToString,
            ),
            'ReceiveMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.ReceiveMessages,
                    request_deserializer=proto__pb2.ClientRequest.FromString,
                    response_serializer=proto__pb2.Message.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MessagingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('MessagingService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MessagingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterPublicKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/MessagingService/RegisterPublicKey',
            proto__pb2.PublicKey.SerializeToString,
            proto__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RequestPublicKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/MessagingService/RequestPublicKey',
            proto__pb2.ClientRequest.SerializeToString,
            proto__pb2.PublicKey.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/MessagingService/SendMessage',
            proto__pb2.Message.SerializeToString,
            proto__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReceiveMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/MessagingService/ReceiveMessages',
            proto__pb2.ClientRequest.SerializeToString,
            proto__pb2.Message.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
