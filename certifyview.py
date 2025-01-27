import ssl
import socket
import datetime
import pyfiglet
import shutil
from colorama import Fore, Style


def get_terminal_width():
    """Get the current width of the terminal."""
    return shutil.get_terminal_size().columns


def print_ascii_art():
    """Generate and print ASCII art with dynamic resizing."""
    terminal_width = max(get_terminal_width(), 40)  # Ensure a minimum width for readability
    ascii_art = pyfiglet.figlet_format("CertifyView", width=terminal_width - 4)
    colored_ascii_art = f"{Fore.YELLOW}{ascii_art}{Style.RESET_ALL}"
    print(colored_ascii_art)

    # Add the author's name (small signature)
    signature = f"{Fore.YELLOW}~ by CyberDude404{Style.RESET_ALL}"
    print(signature.center(terminal_width))


class CertificateChecker:
    def __init__(self, hostname):
        self.hostname = hostname

    def get_certificate_info(self):
        try:
            context = ssl.create_default_context()
            with socket.create_connection((self.hostname, 443), timeout=10) as sock:
                ip_address = sock.getpeername()[0]
                with context.wrap_socket(sock, server_hostname=self.hostname) as ssock:
                    cert = ssock.getpeercert()
        except (socket.timeout, ssl.SSLError, ConnectionError) as e:
            raise ValueError(f"Unable to fetch certificate for {self.hostname}: {e}")

        subject = dict(item[0] for item in cert['subject'])
        issuer = dict(item[0] for item in cert['issuer'])
        valid_from = datetime.datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y GMT")
        valid_to = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y GMT")
        remaining_days = (valid_to - datetime.datetime.now()).days

        return {
            'ip_address': ip_address,
            'subject': subject,
            'issuer': issuer,
            'valid_from': valid_from,
            'valid_to': valid_to,
            'remaining_days': remaining_days
        }

    def print_certificate_info(self):
        field_mapping = {
            'commonName': 'Common Name',
            'countryName': 'Country',
            'stateOrProvinceName': 'State/Province',
            'localityName': 'City/Locality',
            'organizationName': 'Organization'
        }

        try:
            cert_info = self.get_certificate_info()

            print(f"{Fore.GREEN}SSL Certificate Information for {self.hostname}:{Style.RESET_ALL}\n")

            # Print resolved IP address
            print(f"{Fore.CYAN}Resolves to:{Style.RESET_ALL} {Fore.YELLOW}{cert_info['ip_address']}{Style.RESET_ALL}")

            # Print issuer details
            issuer_common_name = cert_info['issuer'].get('commonName', 'Unknown')
            print(f"{Fore.CYAN}The certificate was issued by:{Style.RESET_ALL} {Fore.MAGENTA}{issuer_common_name}{Style.RESET_ALL}")

            # Print remaining validity days
            print(f"{Fore.CYAN}The certificate will expire in:{Style.RESET_ALL} {Fore.RED}{cert_info['remaining_days']} days{Style.RESET_ALL}")

            # Print validity dates
            print(f"{Fore.CYAN}Validity Start Date:{Style.RESET_ALL} {Fore.GREEN}{cert_info['valid_from']}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Validity End Date:{Style.RESET_ALL} {Fore.RED}{cert_info['valid_to']}{Style.RESET_ALL}")

            # Print hostname verification
            hostname_match = "correctly listed" if self.hostname in cert_info['subject'].get('commonName', '') else "not listed"
            print(f"{Fore.CYAN}The hostname ({self.hostname}) is {hostname_match} in the certificate.{Style.RESET_ALL}")

        except ValueError as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")


def main():
    try:
        print_ascii_art()
        hostname = input(f"{Fore.CYAN}Enter the website address to query (e.g., www.example.com): {Style.RESET_ALL}").strip()
        if not hostname:
            hostname = "www.example.com"
            print(f"{Fore.YELLOW}No input provided. Using default hostname: {hostname}{Style.RESET_ALL}")

        checker = CertificateChecker(hostname)
        checker.print_certificate_info()

    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Thank you for using{Style.RESET_ALL}")
        exit(0)


if __name__ == "__main__":
    main()
