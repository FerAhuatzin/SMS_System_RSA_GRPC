import grpc
from concurrent import futures
import Messaging.message_pb2 as pb2
import Messaging.message_pb2_grpc as pb2_grpc

# Diccionario para asociar ID de usuario con su stream de mensajes
active_clients = {}
public_keys = {}

class MessagingService(pb2_grpc.MessagingServiceServicer):
    def AddPublicKey(self, request, context):
        # Guardar clave pública en el diccionario
        public_keys[request.user.id] = pb2.PublicKey(n=request.key.n, e=request.key.e)
        print(f"Clave pública registrada para el usuario {request.user.id}")
        return pb2.Response(status="PublicKey registered successfully.")

    def GetPublicKey(self, request, context):
        # Recuperar clave pública del diccionario
        public_key = public_keys.get(request.id)
        
        if public_key is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"No public key found for user ID {request.id}")
            return pb2.PublicKey()  # Retorna un objeto vacío en caso de error
        
        return public_key

    def SendMessage(self, request, context):
        receiver_id = request.sender  # Asumiendo que el ID del receptor está en el campo `sender`

        # Verificar si el receptor está conectado
        if receiver_id in active_clients:
            # Agregar el mensaje a la cola del receptor
            active_clients[receiver_id].append(request)
            return pb2.Response(status="Message delivered successfully.")
        else:
            # Si el receptor no está conectado, retornar un error
            return pb2.Response(status="Receiver not connected.")

    def ReceiveMessages(self, request, context):
        user_id = context.peer()  # Identificador único del cliente
        print(f"Cliente conectado: {user_id}")

        # Crear una cola de mensajes específica para este cliente
        if user_id not in active_clients:
            active_clients[user_id] = []

        try:
            while True:
                # Si hay mensajes pendientes en la cola del cliente, enviarlos
                if active_clients[user_id]:
                    message = active_clients[user_id].pop(0)
                    yield message  # Enviar mensaje al cliente conectado
        except grpc.RpcError:
            # Manejar la desconexión del cliente
            if user_id in active_clients:
                del active_clients[user_id]
            print(f"Cliente desconectado: {user_id}")



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MessagingServiceServicer_to_server(MessagingService(), server)
    server.add_insecure_port("[::]:50051")
    print("Servidor ejecutándose en el puerto 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
