# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import snowdrop_pb2 as snowdrop__pb2


class EchoStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EchoMe = channel.unary_unary(
                '/snowdrop.Echo/EchoMe',
                request_serializer=snowdrop__pb2.EchoRequest.SerializeToString,
                response_deserializer=snowdrop__pb2.EchoResponse.FromString,
                )


class EchoServicer(object):
    """Missing associated documentation comment in .proto file"""

    def EchoMe(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EchoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EchoMe': grpc.unary_unary_rpc_method_handler(
                    servicer.EchoMe,
                    request_deserializer=snowdrop__pb2.EchoRequest.FromString,
                    response_serializer=snowdrop__pb2.EchoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'snowdrop.Echo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Echo(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def EchoMe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/snowdrop.Echo/EchoMe',
            snowdrop__pb2.EchoRequest.SerializeToString,
            snowdrop__pb2.EchoResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
