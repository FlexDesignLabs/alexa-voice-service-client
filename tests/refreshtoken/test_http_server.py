from unittest.mock import call, Mock, patch

from avs_client.refreshtoken import http_server, handlers


@patch.object(handlers.AmazonAlexaServiceLoginHandler, '__init__',
              return_value=None)
@patch.object(http_server.AmazonLoginHttpServer, 'server_bind', Mock)
def test_http_server_passes_args(mock__init__):
    server = http_server.AmazonLoginHttpServer(
        server_address=('localhost', 9000),
        RequestHandlerClass=handlers.AmazonAlexaServiceLoginHandler,
        client_id='client-id-here',
        client_secret='client-secret-here',
        device_type_id='device-type-id-here',
    )

    request = Mock()
    client_address = Mock()
    server.finish_request(request=request, client_address=client_address)

    assert mock__init__.call_count == 1
    assert mock__init__.call_args == call(
        request=request,
        client_address=client_address,
        server=server,
        client_id='client-id-here',
        client_secret='client-secret-here',
        device_type_id='device-type-id-here',
    )
