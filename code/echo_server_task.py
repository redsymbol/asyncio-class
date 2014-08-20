import asyncio

PORT=4242
clients = {}

@asyncio.coroutine
def handle_client(client_reader, client_writer):
    while True:
        data = (yield from client_reader.readline())
        print(data)
        client_writer.write(b'echo:' + data)

def client_connected_handler(client_reader, client_writer):
    task = asyncio.async(handle_client(client_reader, client_writer))
    clients[task] = (client_reader, client_writer)

    def client_done(task):
        del clients[task]

    task.add_done_callback(client_done)

loop = asyncio.get_event_loop()
pending_server = asyncio.start_server(client_connected_handler, 'localhost', PORT)
server = loop.run_until_complete(pending_server)
try:
    loop.run_forever()
finally:
    loop.close()
