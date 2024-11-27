from concurrent import futures
import grpc
import proto_pb2
import proto_pb2_grpc
from grpc_reflection.v1alpha import reflection


class MessagingServiceServicer(proto_pb2_grpc.MessagingServiceServicer):
    def __init__(self):
        self.public_keys = {}  # Almacena llaves públicas {cliente: (e, n)}
        self.messages = {}     # Cola de mensajes por receptor {receiver_id: [messages]}

    def RegisterPublicKey(self, request, context):
        # Registrar la llave pública del cliente
        self.public_keys[request.sender] = (request.e, request.n)
        print(f"Registered public key for {request.sender}: e={request.e}, n={request.n}")
        return proto_pb2.Response(status="Public key registered.")

    def RequestPublicKey(self, request, context):
        # Proveer la llave pública del cliente solicitado
        client_id = request.sender
        if client_id in self.public_keys:
            e, n = self.public_keys[client_id]
            print(f"Providing public key for {client_id}: e={e}, n={n}")
            return proto_pb2.PublicKey(e=e, n=n)
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, f"Public key for {client_id} not found.")

    def SendMessage(self, request, context):
        # Agregar el mensaje cifrado a la cola del receptor
        if request.receiver not in self.messages:
            self.messages[request.receiver] = []  # Crear una cola para el receptor si no existe
        self.messages[request.receiver].append(request)
        print(f"Message from {request.sender} queued for {request.receiver}")
        return proto_pb2.Response(status="Message received and queued.")

    def ReceiveMessages(self, request, context):
        # Enviar mensajes solo al receptor conectado
        receiver_id = request.sender
        print(f"{receiver_id} is ready to receive messages.")
        while True:
            if receiver_id in self.messages and self.messages[receiver_id]:
                yield self.messages[receiver_id].pop(0)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto_pb2_grpc.add_MessagingServiceServicer_to_server(MessagingServiceServicer(), server)
    # Registrar los servicios con reflexión
    services = (
    proto_pb2.DESCRIPTOR.services_by_name['MessagingService'].full_name,
    reflection.SERVICE_NAME,
    )

    reflection.enable_server_reflection(services, server)

    server.add_insecure_port('[::]:50051')
    print("Server is running on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()