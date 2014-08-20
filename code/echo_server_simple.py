import asyncio
PORT = 4242
class SimpleEchoProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        print('Connection made')
        # We keep the transport object, so we can
        # write to it later.
        self.transport = transport
    def data_received(self, data):
        print(data)
        # This is why we kept the transport when
        # making the connection.
        self.transport.write(b'echo:')
        self.transport.write(data)
    def connection_lost(self, exc):
        print("Connection lost! Closing server...")
        # This variable "server" will be in global scope by
	# the time the method is invoked.
        server.close()

loop = asyncio.get_event_loop()
pending_server = loop.create_server(SimpleEchoProtocol, 'localhost', PORT)
server = loop.run_until_complete(pending_server)
loop.run_until_complete(server.wait_closed())
