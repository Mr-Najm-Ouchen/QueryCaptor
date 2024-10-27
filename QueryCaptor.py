from scapy.all import sniff, DNSQR, IP
from scapy.layers.http import HTTPRequest
from urllib.parse import urlparse, parse_qs, unquote

def extract_search_query(url):
    query = urlparse(url).query
    query_params = parse_qs(query)
    search_query = query_params.get('q') or query_params.get('query')
    if search_query:
        return unquote(search_query[0])
    return None

def process_packet(packet):
    if packet.haslayer(DNSQR):
        dns_query = packet[DNSQR].qname.decode()
        print(f"[+] DNS request detected for domain: {dns_query}")

    elif packet.haslayer(HTTPRequest):
        host = packet[HTTPRequest].Host.decode()
        path = packet[HTTPRequest].Path.decode()
        url = f"http://{host}{path}"

        print(f"[+] HTTP request detected: {url}")
        search_query = extract_search_query(url)
        if search_query:
            print(f"    [+] Search query: {search_query}")

def start_sniffing():
    print("Listening for network packets...")
    try:
        sniff(filter="tcp port 80 or udp port 53", prn=process_packet, store=False)
    except PermissionError:
        print("Please run the tool with administrator privileges (sudo).")

start_sniffing()
