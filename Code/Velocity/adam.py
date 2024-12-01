import socket
import threading

def listen_for_packets(sock, port):
    """
    Function to listen for incoming UDP packets.
    """
    while True:
        try:
            data, addr = sock.recvfrom(1024)  # Buffer size of 1024 bytes
            hex_data = data.hex()
            print(f"\nReceived from {addr}: {data.hex()} (raw bytes)")
            if data[0] == 0x00:
                print("Laser Packet!\n")
                linenum = True
                return data, linenum
        except Exception as e:
            print(f"Error receiving packet: {e}")
            break

def send_packets(sock, ip_address, port, data, linenum):
    """
    Function to send UDP packets.
    """
    print(f"Sending UDP packets to {ip_address}:{port}")
    while True:
        try:
            if linenum: 
                message = data
            else :
                message = input("Enter the message to send (type 'exit' to quit): ")
                if message.lower() == 'exit':
                    print("Exiting...")
                    break
                else :
                    message = message.hex()
            # Convert message to bytes and send
            message_bytes = message.encode()
            sock.sendto(message_bytes, (ip_address, port))
            print(f"Sent: {message_bytes.hex()} (raw bytes)")
        except Exception as e:
            print(f"Error sending packet: {e}")
            break         

def main():
    # Configuration
    port = 1337
    ip_address = "0.0.0.0"  # Listen on all interfaces
    data = 0
    linenum = False

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip_address, port))

    print(f"Listening for UDP packets on {ip_address}:{port}")

    # Start listening thread
    listener_thread = threading.Thread(target=listen_for_packets, args=(sock,), daemon=True)
    listener_thread.start()

    # Start sending packets from the main thread
    send_packets(sock, "10.104.132.201", port, data, linenum)

    sock.close()
    print("Socket closed.")

if __name__ == "__main__":
    main()