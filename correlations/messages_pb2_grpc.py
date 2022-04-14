# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import messages_pb2 as messages__pb2


class ClientProviderRequestStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DBMakeRequest = channel.unary_unary(
                '/ClientProviderRequest/DBMakeRequest',
                request_serializer=messages__pb2.ClientRequest.SerializeToString,
                response_deserializer=messages__pb2.ClientResponse.FromString,
                )


class ClientProviderRequestServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DBMakeRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientProviderRequestServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DBMakeRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.DBMakeRequest,
                    request_deserializer=messages__pb2.ClientRequest.FromString,
                    response_serializer=messages__pb2.ClientResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ClientProviderRequest', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClientProviderRequest(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DBMakeRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientProviderRequest/DBMakeRequest',
            messages__pb2.ClientRequest.SerializeToString,
            messages__pb2.ClientResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)