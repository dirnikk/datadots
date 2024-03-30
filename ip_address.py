import requests

def get_ip_address(request):
    client_ip = request.remote_addr

    # Get public IP address using ifconfig.me
    try:
        public_ip_response = requests.get('https://ifconfig.me/ip')
        public_ip = public_ip_response.text.strip()
    except requests.RequestException as e:
        public_ip = "Error: Unable to retrieve public IP"

    return client_ip, public_ip

