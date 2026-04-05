import socket
import time
import subprocess

def ping_host(host):
    print(f"\nPinging {host}...")
    try:
        result = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True)
        if result.returncode == 0:
            print("Host is reachable ✅")
        else:
            print("Host is not reachable ❌")
    except Exception as e:
        print("Error:", e)

def dns_lookup(host):
    print(f"\nPerforming DNS lookup for {host}...")
    try:
        ip = socket.gethostbyname(host)
        print(f"IP Address: {ip}")
    except:
        print("DNS lookup failed ❌")

def check_port(host, port):
    print(f"\nChecking port {port} on {host}...")
    s = socket.socket()
    s.settimeout(2)
    try:
        s.connect((host, port))
        print(f"Port {port} is open ✅")
    except:
        print(f"Port {port} is closed ❌")
    finally:
        s.close()

def response_time(host):
    print(f"\nMeasuring response time for {host}...")
    try:
        start = time.time()
        socket.gethostbyname(host)
        end = time.time()
        print(f"Response Time: {(end - start)*1000:.2f} ms")
    except:
        print("Failed to measure response time ❌")

if __name__ == "__main__":
    host = input("Enter website (e.g., google.com): ")

    dns_lookup(host)
    ping_host(host)
    check_port(host, 80)
    check_port(host, 443)
    response_time(host)