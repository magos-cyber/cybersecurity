# Cybersecurity Toolkit

Custom security tools for penetration testing, vulnerability assessment, incident response, and compliance.

## Categories

### Penetration Testing
| Tool | Description |
|------|-------------|
| `dir-buster.py` | Directory brute-forcing |
| `subdomain-enum.py` | Subdomain enumeration |
| `xss-scanner.py` | Reflected XSS detection |
| `ssh-bruteforce.py` | SSH password guessing |
| `wordpress-enum.py` | WordPress user enumeration |
| `vuln-scanner.sh` | Service vulnerability checks |
| `web-recon.sh` | Web application reconnaissance |
| `sql-injection-scanner.py` | SQL injection detection |
| `command-injection.py` | Command injection testing |
| `password-audit.sh` | Password policy testing |

### Network Analysis
| Tool | Description |
|------|-------------|
| `port-scan-async.py` | Async port scanner |
| `dns-enum.py` | DNS enumeration |
| `packet-capture.sh` | Packet capture utility |
| `traffic-analyzer.py` | Network traffic analysis |
| `traffic-monitor.sh` | Network traffic monitoring |
| `arp-spoof-detect.py` | ARP spoofing detection |
| `sniff.py` | Packet sniffer |
| `dns-tunnel-detect.py` | DNS tunneling detection |

### Vulnerability Assessment
| Tool | Description |
|------|-------------|
| `cve-checker.py` | Check packages for CVEs |
| `cve-lookup.py` | Lookup CVE details |
| `config-audit.py` | Configuration security audit |
| `dependency-checker.py` | Check dependencies for vulnerabilities |
| `headers-check.py` | Security headers analysis |
| `cors-check.py` | CORS misconfiguration detection |
| `ssl-auditor.py` | SSL/TLS configuration audit |

### Incident Response
| Tool | Description |
|------|-------------|
| `forensics-collector.sh` | Collect forensic evidence |
| `evidence-collector.py` | Automated evidence collection |
| `memory-dump-analyzer.py` | Memory dump string extraction |
| `process-analyzer.py` | Analyze suspicious processes |
| `log-analyzer.py` | Security log analysis |
| `malware-scan.sh` | Malware scanning |
| `disk-forensics.py` | Disk forensics analysis |

### Threat Intelligence
| Tool | Description |
|------|-------------|
| `ioc-checker.py` | Check IPs/domains/hashes |
| `ip-checker.py` | IP reputation check |
| `domain-checker.py` | Domain reputation check |
| `reputation-check.py` | Reputation verification |
| `threat-feed-aggregator.py` | Aggregate threat feeds |
| `domain-reputation.py` | Full domain reputation check |

### OSINT
| Tool | Description |
|------|-------------|
| `email-enum.py` | Email address enumeration |
| `social-media-scan.py` | Social media profile search |
| `breach-check.py` | Check accounts against breaches |
| `ip-geolocation.py` | Geolocate IP addresses |

### Compliance Audits
| Tool | Description |
|------|-------------|
| `cis-benchmark.sh` | CIS benchmark compliance |
| `policy-check.py` | Security policy validation |
| `gdpr-check.py` | GDPR data protection check |
| `sox-check.py` | SOX compliance checklist |
| `pci-dss-check.py` | PCI DSS compliance validation |

### Cryptography
| Tool | Description |
|------|-------------|
| `password-strength.py` | Password strength evaluation |
| `hash-cracker.py` | Dictionary hash cracking |
| `password-generator.py` | Secure password generation |
| `checksum-verifier.py` | File checksum verification |
| `file-encryptor.py` | File encryption/decryption |

### Wordlists
| File | Description |
|------|-------------|
| `common-passwords.txt` | Common passwords for testing |
| `subdomains.txt` | Common subdomain names |
| `extensions.txt` | Common file extensions |

## Requirements

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Penetration testing
python penetration-testing/dir-buster.py example.com -w wordlists/subdomains.txt
python penetration-testing/xss-scanner.py "http://example.com?name=test"

# Network analysis
python network-analysis/port-scan-async.py 192.168.1.1 -s 1 -e 1024
python network-analysis/arp-spoof-detect.py

# Incident response
./incident-response/forensics-collector.sh
python incident-response/evidence-collector.py

# Threat intelligence
python threat-intelligence/domain-reputation.py example.com
python threat-intelligence/threat-feed-aggregator.py -i feeds.txt

# OSINT
python osint/email-enum.py example.com --hunter-key KEY
python osint/breach-check.py -e user@example.com --apikey KEY

# Compliance
python compliance/gdpr-check.py /var/www
python compliance/pci-dss-check.py
```

## Disclaimer

**Use only on systems you own or have explicit written permission to test.** These tools are for educational and authorized security testing purposes only. The authors are not responsible for misuse.

## License

MIT
