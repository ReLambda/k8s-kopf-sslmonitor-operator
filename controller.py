import kopf
# import kubernetes
import ssl
import socket
import datetime

@kopf.on.login()
def login_fn(**kwargs):
    return kopf.login_with_service_account(**kwargs) or kopf.login_with_kubeconfig(**kwargs)

# register a function to be called when a resource is created.
@kopf.on.create('nabinchhetri.com', 'v1', 'sslmonitor')
# register a function to be called periodically.
@kopf.timer('nabinchhetri.com', 'v1', 'sslmonitor', interval=5.0)
def create_fn(spec, patch, logger, **kwargs):
    expiry_date = get_ssl_expiry_date(spec['domain_name'])
    patch.metadata.annotations['ExpiryDate'] = str(expiry_date)
    days_remaining = (expiry_date - datetime.datetime.now())
    patch.metadata.annotations['DaysRemaining'] = str(days_remaining) + " "


def get_ssl_expiry_date(domain_name):
    print(f"\nChecking certifcate for server {domain_name}")
    context = ssl.create_default_context()
    with socket.create_connection((domain_name, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain_name) as _sock:
            certificate = _sock.getpeercert()
            certExpires = datetime.datetime.strptime(
                    certificate["notAfter"], "%b %d %H:%M:%S %Y %Z")
        return certExpires