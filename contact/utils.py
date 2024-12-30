from ipaddress import ip_address, ip_network

# Example list of suspicious IP ranges (Update with real data if needed)
SUSPICIOUS_IP_RANGES = [
    '192.168.0.0/24',  # Example local IP range
    '10.0.0.0/8',      # Example internal IP range
]

def get_client_ip(request):
    """Extracts the client's IP address from the request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def is_suspicious_ip(ip):
    """Checks if the given IP falls in suspicious IP ranges."""
    try:
        ip = ip_address(ip)
        for network in SUSPICIOUS_IP_RANGES:
            if ip in ip_network(network):
                return True
    except ValueError:
        # Invalid IP address format
        return True
    return False
