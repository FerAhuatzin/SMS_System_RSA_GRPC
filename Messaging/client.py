import grpc
import proto_pb2
import proto_pb2_grpc
import threading
import time

# Parámetros de RSA
p = 61  # Número primo 1
q = 53  # Número primo 2
n = p * q  # Módulo
phi = (p - 1) * (q - 1)  # Totiente de Euler
e = 17  # Exponente público
d = pow(e, -1, phi)  # Exponente privado (inverso modular de e)

# Llave pública (e, n) y privada (d, n)
public_key = (e, n)
private_key = (d, n)

# Función para cifrar mensajes
def encrypt_message(message, public_key):
    plaintext_blocks = [ord(char) for char in message]
    ciphertext_blocks = []
    e, n = public_key

    print("\nEncryption:")
    for P in plaintext_blocks:
  
        C = pow(P, e, n)  # C = P^e mod n
        
        ciphertext_blocks.append(C)
        print(f'Plaintext block: {P} -> Encrypted result: {C} (P^{e} mod {n})')

    return ciphertext_blocks

# Función para descifrar mensajes
def decrypt_message(ciphertext_blocks, private_key):
    decrypted_blocks = []
    d, n = private_key

    print("\nDecryption:")
    for C in ciphertext_blocks:
        
        P = pow(C, d, n)  # P = C^d mod n
        
        decrypted_blocks.append(chr(P))
        print(f'Ciphertext block: {C} -> Recovered plaintext block: {P}')

    return ''.join(decrypted_blocks)

# Serialización y deserialización de bloques
def serialize_ciphertext(ciphertext_blocks):
    return ','.join(map(str, ciphertext_blocks)).encode('utf-8')

def deserialize_ciphertext(ciphertext_bytes):
    return list(map(int, ciphertext_bytes.decode('utf-8').split(',')))

# Función para enviar mensajes
def send_messages(stub, client_id, receiver_id):
    while True:
        message = input("Enter a message to send: ")

        # Solicita la llave pública del receptor
        response = stub.RequestPublicKey(proto_pb2.ClientRequest(sender=receiver_id))
        recipient_public_key = (response.e, response.n)

        # Cifra el mensaje
        ciphertext_blocks = encrypt_message(message, recipient_public_key)

        # Serializa los bloques y envía al servidor
        response = stub.SendMessage(
            proto_pb2.Message(
                sender=client_id,
                receiver=receiver_id,
                content=serialize_ciphertext(ciphertext_blocks),
            )
        )
        print(f"Server responded: {response.status}")

# Función para recibir mensajes
def receive_messages(stub, client_id):
    try:
        for message in stub.ReceiveMessages(proto_pb2.ClientRequest(sender=client_id)):
            # Deserializa y descifra
            ciphertext_blocks = deserialize_ciphertext(message.content)
            decrypted_message = decrypt_message(ciphertext_blocks, private_key)
            print(f"Message from {message.sender}: {decrypted_message}")
    except grpc.RpcError as e:
        print(f"Error receiving messages: {e}")

def run():
    # Solicitar información del cliente
    client_id = input("Enter your client ID: ")
    role = input("Enter your role (sender/receiver): ")

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = proto_pb2_grpc.MessagingServiceStub(channel)

        # Registrar la llave pública
        stub.RegisterPublicKey(proto_pb2.PublicKey(
            sender=client_id,
            e=public_key[0],
            n=public_key[1],
        ))
        print(f"Public key registered for {client_id}.")

        if role == "sender":
            receiver_id = input("Enter the receiver ID: ")
            send_messages(stub, client_id, receiver_id)
        elif role == "receiver":
            print("Waiting for messages...")
            receive_messages(stub, client_id)
        else:
            print("Invalid role. Exiting.")

if __name__ == '__main__':
    run()
