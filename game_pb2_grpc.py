# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import game_pb2 as game__pb2


class RoomControllerStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterPlayer = channel.unary_unary(
                '/RoomController/RegisterPlayer',
                request_serializer=game__pb2.RegisterPlayerRequest.SerializeToString,
                response_deserializer=game__pb2.RegisterPlayerResponse.FromString,
                )
        self.ChooseCombination = channel.unary_unary(
                '/RoomController/ChooseCombination',
                request_serializer=game__pb2.ChooseCombinationRequest.SerializeToString,
                response_deserializer=game__pb2.ChooseCombinationResponse.FromString,
                )
        self.RemovePlayer = channel.unary_unary(
                '/RoomController/RemovePlayer',
                request_serializer=game__pb2.RemovePlayerRequest.SerializeToString,
                response_deserializer=game__pb2.RemovePlayerResponse.FromString,
                )


class RoomControllerServicer(object):
    """The greeting service definition.
    """

    def RegisterPlayer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChooseCombination(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemovePlayer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RoomControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterPlayer': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPlayer,
                    request_deserializer=game__pb2.RegisterPlayerRequest.FromString,
                    response_serializer=game__pb2.RegisterPlayerResponse.SerializeToString,
            ),
            'ChooseCombination': grpc.unary_unary_rpc_method_handler(
                    servicer.ChooseCombination,
                    request_deserializer=game__pb2.ChooseCombinationRequest.FromString,
                    response_serializer=game__pb2.ChooseCombinationResponse.SerializeToString,
            ),
            'RemovePlayer': grpc.unary_unary_rpc_method_handler(
                    servicer.RemovePlayer,
                    request_deserializer=game__pb2.RemovePlayerRequest.FromString,
                    response_serializer=game__pb2.RemovePlayerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RoomController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RoomController(object):
    """The greeting service definition.
    """

    @staticmethod
    def RegisterPlayer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RoomController/RegisterPlayer',
            game__pb2.RegisterPlayerRequest.SerializeToString,
            game__pb2.RegisterPlayerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChooseCombination(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RoomController/ChooseCombination',
            game__pb2.ChooseCombinationRequest.SerializeToString,
            game__pb2.ChooseCombinationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemovePlayer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RoomController/RemovePlayer',
            game__pb2.RemovePlayerRequest.SerializeToString,
            game__pb2.RemovePlayerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class WebServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendWinners = channel.unary_unary(
                '/WebServer/SendWinners',
                request_serializer=game__pb2.SendWinnersRequest.SerializeToString,
                response_deserializer=game__pb2.SendWinnersResponse.FromString,
                )


class WebServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendWinners(self, request, context):
        """Когда RoomController что-то сообщает Flask'у (webserver'у)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WebServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendWinners': grpc.unary_unary_rpc_method_handler(
                    servicer.SendWinners,
                    request_deserializer=game__pb2.SendWinnersRequest.FromString,
                    response_serializer=game__pb2.SendWinnersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'WebServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WebServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendWinners(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/WebServer/SendWinners',
            game__pb2.SendWinnersRequest.SerializeToString,
            game__pb2.SendWinnersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
