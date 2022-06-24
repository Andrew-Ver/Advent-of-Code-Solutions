def decipher_packet(packet_str: str) -> int:
    packet = ''.join([bin(int(c, base=16))[2:].zfill(4) for c in packet_str])
    
    packet_ver = int(packet[:3], base=2)
    packet_ID = int(packet[3:6], base=2)
    if packet_ver != 4:
        length_ID = packet[6]
        if length_ID == '0':
            length_of_subpackets = int(packet[7:(8+12)], base=2)
        else:
            length_of_subpackets = int(packet[7:(8+15)], base=2)
    else:
        length_of_subpackets = 0
        
    return packet

print(decipher_packet('8A004A801A8002F478'))

#To do later
