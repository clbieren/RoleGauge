import os
import json

base_dir = r"c:\Users\clbie\Desktop\Projects\RoleGauge\knowledge-base"
roles_dir = os.path.join(base_dir, "roles", "network-engineer")
skills_dir = os.path.join(base_dir, "skills", "network-engineer")
evidence_dir = os.path.join(base_dir, "evidence", "network-engineer")

for d in [roles_dir, skills_dir, evidence_dir]:
    os.makedirs(d, exist_ok=True)

roles = {
    "junior": {
        "role_id": "network_engineer", "level": "junior", "title": "Junior Network Engineer",
        "description": "Entry-level.", "experience_range": "0-2 years",
        "skills": [
            {"skill_id": "ne_fundamentals", "importance": 0.95, "rationale": "Core"},
            {"skill_id": "ne_osi_tcpip", "importance": 0.9, "rationale": "Core"},
            {"skill_id": "ne_switching_lan", "importance": 0.85, "rationale": "Core"},
            {"skill_id": "ne_addressing_routing", "importance": 0.8, "rationale": "Core"},
            {"skill_id": "ne_wireless", "importance": 0.6, "rationale": "Basic understanding"},
            {"skill_id": "ne_services_observability", "importance": 0.5, "rationale": "Basic"},
            {"skill_id": "ne_network_security", "importance": 0.4, "rationale": "Basic"}
        ],
        "scoring": {"method": "weighted_average", "description": "Standard scoring", "thresholds": {}}
    },
    "mid": {
        "role_id": "network_engineer", "level": "mid", "title": "Mid-level Network Engineer",
        "description": "Mid-level.", "experience_range": "2-5 years",
        "skills": [
            {"skill_id": "ne_addressing_routing", "importance": 0.95, "rationale": "Core"},
            {"skill_id": "ne_switching_lan", "importance": 0.9, "rationale": "Core"},
            {"skill_id": "ne_network_security", "importance": 0.85, "rationale": "Core"},
            {"skill_id": "ne_services_observability", "importance": 0.85, "rationale": "Core"},
            {"skill_id": "ne_osi_tcpip", "importance": 0.8, "rationale": "Important"},
            {"skill_id": "ne_wireless", "importance": 0.7, "rationale": "Important"},
            {"skill_id": "ne_fundamentals", "importance": 0.5, "rationale": "Assumed mastered"}
        ],
        "scoring": {"method": "weighted_average", "description": "Standard scoring", "thresholds": {}}
    },
    "senior": {
        "role_id": "network_engineer", "level": "senior", "title": "Senior Network Engineer",
        "description": "Senior-level.", "experience_range": "5+ years",
        "skills": [
            {"skill_id": "ne_addressing_routing", "importance": 0.95, "rationale": "Core BGP/MPLS expected"},
            {"skill_id": "ne_network_security", "importance": 0.9, "rationale": "Core VPN/IPSec design"},
            {"skill_id": "ne_services_observability", "importance": 0.9, "rationale": "Core"},
            {"skill_id": "ne_switching_lan", "importance": 0.85, "rationale": "Important"},
            {"skill_id": "ne_wireless", "importance": 0.8, "rationale": "Important"},
            {"skill_id": "ne_osi_tcpip", "importance": 0.5, "rationale": "Assumed mastered"},
            {"skill_id": "ne_fundamentals", "importance": 0.2, "rationale": "Assumed mastered"}
        ],
        "scoring": {"method": "weighted_average", "description": "Standard scoring", "thresholds": {}}
    }
}

for level, data in roles.items():
    with open(os.path.join(roles_dir, f"{level}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

ne_fundamentals = {
  "skill_id": "ne_fundamentals",
  "name": "Network Fundamentals",
  "category": "networking",
  "description": "Cabling, media types, network topologies, and basic physical layer concepts.",
  "subskills": [
    {"id": "cabling", "name": "Cabling Types", "description": "UTP, STP, Fiber Optic cables.", "keywords": ["UTP", "Fiber", "Cat5e", "Cat6", "SFP"]},
    {"id": "topologies", "name": "Network Topologies", "description": "Star, Mesh, Ring, Bus topologies.", "keywords": ["Star topology", "Mesh topology", "Ring topology"]},
    {"id": "media_access", "name": "Media Access Control", "description": "CSMA/CD and CSMA/CA.", "keywords": ["CSMA/CD", "CSMA/CA", "Collision domain"]},
    {"id": "power_over_ethernet", "name": "PoE", "description": "Understanding IEEE 802.3af/at/bt.", "keywords": ["PoE", "Power over Ethernet", "802.3af", "802.3at"]},
    {"id": "data_centers", "name": "Data Center Architecture", "description": "Spine-leaf, Three-tier architecture.", "keywords": ["Spine-leaf", "Three-tier", "Core", "Distribution", "Access"]},
    {"id": "wan_basics", "name": "WAN Basics", "description": "Leased lines, DSL, Cable, Metro Ethernet.", "keywords": ["WAN", "Metro Ethernet", "Leased Line"]},
    {"id": "cloud_connectivity", "name": "Cloud Connectivity", "description": "Direct Connect, ExpressRoute basics.", "keywords": ["Direct Connect", "ExpressRoute", "Cloud interconnect"]},
    {"id": "network_racks", "name": "Rack and Power", "description": "UPS, PDUs, RU sizing.", "keywords": ["Rack unit", "PDU", "UPS", "patch panel"]}
  ],
  "evidence": {
    "github": [
      {"signal": "Mentions SFP modules or cabling specs in infra docs", "detection": "content_analysis", "pattern": "SFP\\+|10GBASE-T|Twinax", "strength": 0.6, "maps_to": ["ne_fundamentals.cabling"]}
    ],
    "cv": [
      {"signal": "Physical network design, cabling, and rack installation", "strength": 0.7, "maps_to": ["ne_fundamentals.cabling", "ne_fundamentals.network_racks", "ne_fundamentals.wan_basics"]}
    ],
    "linkedin": [
      {"signal": "Data Center infrastructure endorsed", "strength": 0.5, "maps_to": ["ne_fundamentals.data_centers", "ne_fundamentals.topologies"]}
    ]
  },
  "levels": {
    "junior": {"expected_subskills": ["cabling", "topologies", "media_access", "network_racks"], "description": "Understands physical layers, cabling, and basic rack operations."},
    "mid": {"expected_subskills": ["power_over_ethernet", "wan_basics"], "description": "Can manage PoE budgets and basic WAN links."},
    "senior": {"expected_subskills": ["data_centers", "cloud_connectivity"], "description": "Designs scalable data center architectures and cloud interconnects."}
  }
}

ne_osi_tcpip = {
  "skill_id": "ne_osi_tcpip",
  "name": "OSI & TCP/IP Models",
  "category": "networking",
  "description": "Packet analysis, headers, and protocol encapsulation.",
  "subskills": [
    {"id": "osi_model", "name": "OSI Model", "description": "All 7 layers.", "keywords": ["OSI Model", "Application layer", "Transport layer", "Network layer", "Data link layer"]},
    {"id": "tcp_ip_model", "name": "TCP/IP Model", "description": "DoD model.", "keywords": ["TCP/IP", "Internet layer"]},
    {"id": "tcp_vs_udp", "name": "TCP vs UDP", "description": "Three-way handshake, windowing, multiplexing.", "keywords": ["TCP", "UDP", "Three-way handshake", "Windowing", "Connectionless"]},
    {"id": "icmp", "name": "ICMP", "description": "Ping, traceroute mechanics.", "keywords": ["ICMP", "Ping", "Traceroute", "Echo request"]},
    {"id": "arp", "name": "ARP", "description": "Address Resolution Protocol.", "keywords": ["ARP", "MAC address", "Address Resolution Protocol"]},
    {"id": "packet_analysis", "name": "Packet Analysis", "description": "Using Wireshark/tcpdump to read PCAPs.", "keywords": ["Wireshark", "tcpdump", "PCAP", "packet capture"]},
    {"id": "mtu_fragmentation", "name": "MTU & Fragmentation", "description": "Path MTU discovery, IP fragmentation.", "keywords": ["MTU", "Fragmentation", "PMTUD", "DF bit"]},
    {"id": "qos_dscp", "name": "QoS & DSCP", "description": "Traffic marking and queuing.", "keywords": ["QoS", "DSCP", "CoS", "Traffic shaping"]}
  ],
  "evidence": {
    "github": [
      {"signal": "Scripts invoking tcpdump", "detection": "content_analysis", "pattern": "tcpdump -i|pcap", "strength": 0.8, "maps_to": ["ne_osi_tcpip.packet_analysis"]},
      {"signal": "Scripts tuning MTU", "detection": "content_analysis", "pattern": "mtu 1500|mtu 9000", "strength": 0.7, "maps_to": ["ne_osi_tcpip.mtu_fragmentation"]}
    ],
    "cv": [
      {"signal": "Protocol troubleshooting, Wireshark, QoS", "strength": 0.7, "maps_to": ["ne_osi_tcpip.packet_analysis", "ne_osi_tcpip.tcp_vs_udp", "ne_osi_tcpip.qos_dscp"]}
    ],
    "linkedin": [
      {"signal": "TCP/IP or Wireshark endorsed", "strength": 0.5, "maps_to": ["ne_osi_tcpip.tcp_ip_model", "ne_osi_tcpip.packet_analysis"]}
    ]
  },
  "levels": {
    "junior": {"expected_subskills": ["osi_model", "tcp_ip_model", "arp", "icmp"], "description": "Understands layer separation, basic protocols, and ping mechanics."},
    "mid": {"expected_subskills": ["tcp_vs_udp", "mtu_fragmentation"], "description": "Deep understanding of transport layer mechanics and fragmentation."},
    "senior": {"expected_subskills": ["packet_analysis", "qos_dscp"], "description": "Can perform deep packet inspection and design QoS policies."}
  }
}

ne_addressing_routing = {
  "skill_id": "ne_addressing_routing",
  "name": "Addressing & Routing",
  "category": "networking",
  "description": "IPv4/IPv6 subnetting, static routing, OSPF, BGP, EIGRP, and MPLS.",
  "subskills": [
    {"id": "ipv4_subnetting", "name": "IPv4 Subnetting", "description": "VLSM, CIDR.", "keywords": ["IPv4", "Subnetting", "VLSM", "CIDR"]},
    {"id": "ipv6_addressing", "name": "IPv6", "description": "SLAAC, IPv6 subnets.", "keywords": ["IPv6", "SLAAC", "NDP"]},
    {"id": "static_routing", "name": "Static Routing", "description": "Default routes, floating static routes.", "keywords": ["ip route", "0.0.0.0", "Floating static route"]},
    {"id": "ospf", "name": "OSPF", "description": "Single and Multi-area OSPF, LSAs.", "keywords": ["OSPF", "Area 0", "LSA", "Link State", "router ospf"]},
    {"id": "eigrp", "name": "EIGRP", "description": "Feasible successors, DUAL algorithm.", "keywords": ["EIGRP", "DUAL", "Feasible successor", "router eigrp"]},
    {"id": "bgp", "name": "BGP", "description": "eBGP, iBGP, Path attributes.", "keywords": ["BGP", "Autonomous System", "AS Number", "router bgp", "eBGP", "iBGP"]},
    {"id": "route_redistribution", "name": "Route Redistribution", "description": "Metrics, route maps, prefix lists.", "keywords": ["redistribute", "route-map", "prefix-list", "metric"]},
    {"id": "mpls", "name": "MPLS", "description": "Label switching, VRFs, L3VPN.", "keywords": ["MPLS", "VRF", "Label switching", "L3VPN", "CE router"]}
  ],
  "evidence": {
    "github": [
      {"signal": "BGP config", "detection": "content_analysis", "pattern": "router bgp \\d+", "strength": 0.9, "maps_to": ["ne_addressing_routing.bgp"]},
      {"signal": "OSPF config", "detection": "content_analysis", "pattern": "router ospf \\d+", "strength": 0.8, "maps_to": ["ne_addressing_routing.ospf"]},
      {"signal": "EIGRP config", "detection": "content_analysis", "pattern": "router eigrp \\d+", "strength": 0.8, "maps_to": ["ne_addressing_routing.eigrp"]},
      {"signal": "MPLS VRF config", "detection": "content_analysis", "pattern": "ip vrf|vrf definition", "strength": 0.9, "maps_to": ["ne_addressing_routing.mpls"]},
      {"signal": "Static route config", "detection": "content_analysis", "pattern": "ip route 0\\.0\\.0\\.0", "strength": 0.6, "maps_to": ["ne_addressing_routing.static_routing"]}
    ],
    "cv": [
      {"signal": "BGP, MPLS, OSPF protocol design", "strength": 0.7, "maps_to": ["ne_addressing_routing.bgp", "ne_addressing_routing.ospf", "ne_addressing_routing.mpls", "ne_addressing_routing.eigrp"]},
      {"signal": "IPv6 migration or addressing", "strength": 0.6, "maps_to": ["ne_addressing_routing.ipv6_addressing", "ne_addressing_routing.ipv4_subnetting"]}
    ],
    "linkedin": [
      {"signal": "BGP endorsed", "strength": 0.5, "maps_to": ["ne_addressing_routing.bgp"]}
    ]
  },
  "levels": {
    "junior": {"expected_subskills": ["ipv4_subnetting", "static_routing", "ipv6_addressing"], "description": "Can subnet IPv4/IPv6 networks and configure static routes."},
    "mid": {"expected_subskills": ["ospf", "eigrp"], "description": "Can configure IGPs like OSPF and EIGRP."},
    "senior": {"expected_subskills": ["bgp", "route_redistribution", "mpls"], "description": "Can design service provider level networks using BGP and MPLS."}
  }
}

ne_switching_lan = {
  "skill_id": "ne_switching_lan",
  "name": "Switching & LAN",
  "category": "networking",
  "description": "VLANs, STP, Trunking, EtherChannel.",
  "subskills": [
    {"id": "vlans", "name": "VLANs", "description": "802.1Q, Access ports.", "keywords": ["VLAN", "802.1Q", "switchport mode access"]},
    {"id": "trunking", "name": "Trunking", "description": "ISL, 802.1Q trunks, Native VLAN.", "keywords": ["Trunk", "Native VLAN", "switchport mode trunk"]},
    {"id": "vtp", "name": "VTP / DTP", "description": "VLAN Trunking Protocol, Dynamic Trunking.", "keywords": ["VTP", "DTP", "Dynamic desirable"]},
    {"id": "stp", "name": "Spanning Tree Protocol", "description": "STP, RSTP, MSTP, BPDU.", "keywords": ["STP", "RSTP", "MSTP", "BPDU", "Root bridge", "spanning-tree"]},
    {"id": "etherchannel", "name": "EtherChannel", "description": "LACP, PAgP.", "keywords": ["EtherChannel", "LACP", "PAgP", "Port-channel"]},
    {"id": "inter_vlan_routing", "name": "Inter-VLAN Routing", "description": "Router on a stick, SVI.", "keywords": ["Router on a stick", "SVI", "interface vlan"]},
    {"id": "layer2_security", "name": "Layer 2 Security", "description": "Port security, DHCP snooping, ARP inspection.", "keywords": ["Port security", "DHCP snooping", "Dynamic ARP inspection", "DAI"]},
    {"id": "high_availability", "name": "First Hop Redundancy", "description": "HSRP, VRRP, GLBP.", "keywords": ["HSRP", "VRRP", "GLBP", "Standby"]}
  ],
  "evidence": {
    "github": [
      {"signal": "VLAN/Trunking config", "detection": "content_analysis", "pattern": "switchport mode (access|trunk)", "strength": 0.8, "maps_to": ["ne_switching_lan.vlans", "ne_switching_lan.trunking"]},
      {"signal": "STP config", "detection": "content_analysis", "pattern": "spanning-tree mode", "strength": 0.8, "maps_to": ["ne_switching_lan.stp"]},
      {"signal": "Etherchannel config", "detection": "content_analysis", "pattern": "channel-group \\d+ mode active", "strength": 0.8, "maps_to": ["ne_switching_lan.etherchannel"]},
      {"signal": "L2 Security", "detection": "content_analysis", "pattern": "ip dhcp snooping|switchport port-security", "strength": 0.7, "maps_to": ["ne_switching_lan.layer2_security"]},
      {"signal": "FHRP config", "detection": "content_analysis", "pattern": "standby \\d+ ip|vrrp \\d+ ip", "strength": 0.8, "maps_to": ["ne_switching_lan.high_availability"]}
    ],
    "cv": [
      {"signal": "LAN design, STP tuning, VTP domains", "strength": 0.6, "maps_to": ["ne_switching_lan.vlans", "ne_switching_lan.stp", "ne_switching_lan.vtp"]},
      {"signal": "Inter-VLAN routing and router-on-a-stick", "strength": 0.6, "maps_to": ["ne_switching_lan.inter_vlan_routing"]}
    ],
    "linkedin": [
      {"signal": "Switching endorsed", "strength": 0.4, "maps_to": ["ne_switching_lan.vlans"]}
    ]
  },
  "levels": {
    "junior": {"expected_subskills": ["vlans", "trunking", "vtp", "inter_vlan_routing"], "description": "Can configure basic VLANs, inter-vlan routing, and trunk links."},
    "mid": {"expected_subskills": ["stp", "etherchannel"], "description": "Can configure spanning tree topologies and port-channels."},
    "senior": {"expected_subskills": ["layer2_security", "high_availability"], "description": "Can design secure and highly available LAN switching environments using FHRPs."}
  }
}

ne_wireless = {
  "skill_id": "ne_wireless",
  "name": "Wireless Networking",
  "category": "networking",
  "description": "802.11 standards, WPA2/3, controllers, APs.",
  "subskills": [
    {"id": "rf_principles", "name": "RF Principles", "description": "Frequencies, bands, interference.", "keywords": ["RF", "2.4GHz", "5GHz", "Interference", "Signal strength"]},
    {"id": "standards_80211", "name": "802.11 Standards", "description": "a/b/g/n/ac/ax (WiFi 6).", "keywords": ["802.11ac", "802.11ax", "WiFi 6", "MIMO"]},
    {"id": "ap_modes", "name": "AP Modes", "description": "Autonomous, Lightweight (CAPWAP).", "keywords": ["Autonomous AP", "Lightweight AP", "CAPWAP", "WLC"]},
    {"id": "wireless_security", "name": "Wireless Security", "description": "WPA2, WPA3, 802.1X, EAP.", "keywords": ["WPA2", "WPA3", "802.1X", "EAP-TLS"]},
    {"id": "wlc_config", "name": "WLC Configuration", "description": "Cisco/Aruba wireless controller configuration.", "keywords": ["WLC", "Wireless LAN Controller", "SSID"]},
    {"id": "roaming", "name": "Roaming", "description": "Client roaming, seamless transition.", "keywords": ["Roaming", "Fast BSS transition", "802.11r"]},
    {"id": "site_survey", "name": "Site Survey", "description": "Predictive and active RF site surveys.", "keywords": ["Site survey", "Ekahau", "Heatmap"]},
    {"id": "troubleshooting", "name": "Wireless Troubleshooting", "description": "Interference, co-channel interference.", "keywords": ["Co-channel interference", "SNR", "RSSI"]}
  ],
  "evidence": {
    "github": [
      {"signal": "WLC config scripts", "detection": "content_analysis", "pattern": "config wlan|capwap", "strength": 0.8, "maps_to": ["ne_wireless.wlc_config"]},
      {"signal": "802.1X security configs", "detection": "content_analysis", "pattern": "dot1x system-auth-control", "strength": 0.8, "maps_to": ["ne_wireless.wireless_security"]}
    ],
    "cv": [
      {"signal": "Wireless deployment, Ekahau surveys, roaming optimization", "strength": 0.7, "maps_to": ["ne_wireless.wlc_config", "ne_wireless.standards_80211", "ne_wireless.site_survey", "ne_wireless.roaming"]},
      {"signal": "RF interference troubleshooting", "strength": 0.6, "maps_to": ["ne_wireless.rf_principles", "ne_wireless.troubleshooting", "ne_wireless.ap_modes"]}
    ],
    "linkedin": [
      {"signal": "Wireless Networking endorsed", "strength": 0.5, "maps_to": ["ne_wireless.wlc_config"]}
    ]
  },
  "levels": {
    "junior": {"expected_subskills": ["rf_principles", "standards_80211", "ap_modes"], "description": "Understands WiFi bands, standards, and AP types."},
    "mid": {"expected_subskills": ["wireless_security", "troubleshooting"], "description": "Can secure wireless networks and troubleshoot basic interference."},
    "senior": {"expected_subskills": ["wlc_config", "roaming", "site_survey"], "description": "Can architect enterprise wireless networks and perform Ekahau surveys."}
  }
}

ne_network_security = {
  "skill_id": "ne_network_security",
  "name": "Network Security (Infrastructure)",
  "category": "networking",
  "description": "Focuses on the physical and logical configuration of security devices (Cisco ACL syntax, IPSec tunnel setup, VPN device configuration).",
  "subskills": [
    {"id": "acls", "name": "Access Control Lists", "description": "Standard, Extended, IPv6 ACLs syntax.", "keywords": ["access-list", "permit ip", "deny tcp", "access-group"]},
    {"id": "nat", "name": "NAT/PAT", "description": "Network Address Translation configuration.", "keywords": ["ip nat inside", "ip nat outside", "PAT", "NAT overload"]},
    {"id": "firewall_config", "name": "Firewall Configuration", "description": "Cisco ASA, Palo Alto, Fortinet rules.", "keywords": ["Cisco ASA", "Palo Alto", "FortiGate", "Security policy", "zone-based firewall"]},
    {"id": "vpn_ipsec", "name": "IPsec VPNs", "description": "Site-to-Site, IKEv1, IKEv2, Phase 1 & 2.", "keywords": ["IPsec", "IKEv2", "crypto map", "crypto isakmp", "crypto ipsec transform-set"]},
    {"id": "vpn_remote", "name": "Remote Access VPN", "description": "AnyConnect, SSL VPNs.", "keywords": ["AnyConnect", "SSL VPN", "Remote access"]},
    {"id": "aaa", "name": "AAA / TACACS+", "description": "Radius, TACACS+ device administration.", "keywords": ["AAA", "TACACS+", "RADIUS", "aaa new-model"]},
    {"id": "dmvpn", "name": "DMVPN", "description": "Dynamic Multipoint VPN, NHRP.", "keywords": ["DMVPN", "NHRP", "mGRE", "multipoint GRE"]},
    {"id": "macsec", "name": "MACsec", "description": "802.1AE Layer 2 encryption.", "keywords": ["MACsec", "802.1AE", "MKA"]}
  ],
  "evidence": {
    "github": [
      {"signal": "IPsec crypto config", "detection": "content_analysis", "pattern": "crypto isakmp|crypto ipsec", "strength": 0.9, "maps_to": ["ne_network_security.vpn_ipsec"]},
      {"signal": "ACL config", "detection": "content_analysis", "pattern": "access-list \\d+ (permit|deny)", "strength": 0.8, "maps_to": ["ne_network_security.acls"]},
      {"signal": "NAT config", "detection": "content_analysis", "pattern": "ip nat inside source|nat \\(inside,outside\\)", "strength": 0.8, "maps_to": ["ne_network_security.nat"]},
      {"signal": "AAA config", "detection": "content_analysis", "pattern": "aaa new-model|tacacs-server", "strength": 0.8, "maps_to": ["ne_network_security.aaa"]},
      {"signal": "DMVPN config", "detection": "content_analysis", "pattern": "tunnel mode gre multipoint|ip nhrp", "strength": 0.9, "maps_to": ["ne_network_security.dmvpn"]},
      {"signal": "MACsec config", "detection": "content_analysis", "pattern": "macsec network-link", "strength": 0.9, "maps_to": ["ne_network_security.macsec"]}
    ],
    "cv": [
      {"signal": "Firewall management or Site-to-Site VPN experience", "strength": 0.7, "maps_to": ["ne_network_security.firewall_config", "ne_network_security.vpn_ipsec"]},
      {"signal": "AnyConnect/Remote VPN deployments", "strength": 0.6, "maps_to": ["ne_network_security.vpn_remote"]},
      {"signal": "DMVPN architecture or MACsec encryption", "strength": 0.7, "maps_to": ["ne_network_security.dmvpn", "ne_network_security.macsec"]}
    ],
    "linkedin": [
      {"signal": "IPsec or Firewalls endorsed", "strength": 0.5, "maps_to": ["ne_network_security.firewall_config", "ne_network_security.vpn_ipsec"]}
    ]
  },
  "levels": {
    "junior": {"expected_subskills": ["acls", "nat", "aaa"], "description": "Can write basic access lists, configure NAT, and setup AAA device auth."},
    "mid": {"expected_subskills": ["firewall_config", "vpn_remote"], "description": "Can manage firewall policies and remote access gateways."},
    "senior": {"expected_subskills": ["vpn_ipsec", "dmvpn", "macsec"], "description": "Can design and deploy complex DMVPN and site-to-site IPsec architectures."}
  }
}

ne_services_observability = {
  "skill_id": "ne_services_observability",
  "name": "Network Services & Observability",
  "category": "networking",
  "description": "DNS, DHCP, SNMP, NetFlow, and network automation tools.",
  "subskills": [
    {"id": "dhcp", "name": "DHCP", "description": "DHCP pools, relays, IP helpers.", "keywords": ["ip dhcp pool", "ip helper-address", "DHCP relay"]},
    {"id": "dns", "name": "DNS", "description": "A records, CNAME, DNS resolution.", "keywords": ["DNS", "ip name-server", "A record"]},
    {"id": "ntp", "name": "NTP", "description": "Network Time Protocol.", "keywords": ["NTP", "ntp server", "ntp peer"]},
    {"id": "snmp", "name": "SNMP", "description": "SNMPv2c, SNMPv3, traps.", "keywords": ["SNMP", "snmp-server", "SNMPv3", "MIB", "OID"]},
    {"id": "netflow", "name": "NetFlow / sFlow", "description": "Traffic visibility.", "keywords": ["NetFlow", "sFlow", "ip flow ingress"]},
    {"id": "syslog", "name": "Syslog", "description": "Logging levels, remote logging.", "keywords": ["Syslog", "logging trap", "logging host"]},
    {"id": "automation_python", "name": "Python Automation", "description": "Netmiko, Napalm, Nornir.", "keywords": ["netmiko", "napalm", "nornir", "paramiko"]},
    {"id": "automation_ansible", "name": "Ansible for Network", "description": "Ansible ios_config, nxos_config modules.", "keywords": ["ios_config", "nxos_config", "ansible-playbook"]}
  ],
  "evidence": {
    "github": [
      {"signal": "Python network automation", "detection": "dependency_extraction", "pattern": "netmiko|napalm|nornir", "strength": 0.9, "maps_to": ["ne_services_observability.automation_python"]},
      {"signal": "Ansible network modules", "detection": "content_analysis", "pattern": "ios_config:|nxos_config:", "strength": 0.8, "maps_to": ["ne_services_observability.automation_ansible"]},
      {"signal": "SNMP/Netflow config", "detection": "content_analysis", "pattern": "snmp-server|ip flow-export", "strength": 0.8, "maps_to": ["ne_services_observability.snmp", "ne_services_observability.netflow"]},
      {"signal": "DHCP/DNS config", "detection": "content_analysis", "pattern": "ip dhcp pool|ip name-server", "strength": 0.8, "maps_to": ["ne_services_observability.dhcp", "ne_services_observability.dns", "ne_services_observability.ntp", "ne_services_observability.syslog"]}
    ],
    "cv": [
      {"signal": "Network automation experience with python/ansible", "strength": 0.7, "maps_to": ["ne_services_observability.automation_python", "ne_services_observability.automation_ansible"]},
      {"signal": "Network monitoring rollout", "strength": 0.6, "maps_to": ["ne_services_observability.snmp", "ne_services_observability.netflow", "ne_services_observability.syslog"]}
    ],
    "linkedin": [
      {"signal": "Network Automation endorsed", "strength": 0.5, "maps_to": ["ne_services_observability.automation_python"]}
    ]
  },
  "levels": {
    "junior": {"expected_subskills": ["dhcp", "dns", "ntp", "syslog"], "description": "Can configure basic IP services and logging."},
    "mid": {"expected_subskills": ["snmp", "netflow"], "description": "Can configure monitoring and flow tracking protocols."},
    "senior": {"expected_subskills": ["automation_python", "automation_ansible"], "description": "Can automate network provisioning and configuration using Python or Ansible."}
  }
}

skills = [ne_fundamentals, ne_osi_tcpip, ne_addressing_routing, ne_switching_lan, ne_wireless, ne_network_security, ne_services_observability]

for sk in skills:
    with open(os.path.join(skills_dir, f"{sk['skill_id']}.json"), "w", encoding="utf-8") as f:
        json.dump(sk, f, indent=2)

# 3. GLOBAL EVIDENCE FILES
github_evidence = {
  "source_id": "github",
  "name": "GitHub Repository Analysis - Network Engineer",
  "description": "Global parsing rules. NOTE: Specific evidence mappings (regex patterns) are stored within individual skill files, NOT here. The validate_composite_keys.py script scans both to verify coverage. This prevents duplicating regexes across files.",
  "preprocessing_pipeline": {
    "steps": [
      {
        "step": 1,
        "name": "file_tree_scan",
        "target_files": [{"pattern": "*.cfg|*.conf|*.txt|*.yml", "skill": "all", "priority": "high"}]
      },
      {
        "step": 2,
        "name": "dependency_extraction",
        "relevant_dependencies": {"network_automation": ["netmiko", "napalm", "nornir", "paramiko", "ncclient"]}
      }
    ]
  },
  "ai_analysis_instructions": {"tasks": ["Map to composite keys"]}
}

cv_evidence = {
    "source_id": "cv",
    "name": "CV Analysis",
    "description": "CV parsing for Network Engineer. Specific keyword mappings are maintained inside the individual skill JSONs."
}

linkedin_evidence = {
    "source_id": "linkedin",
    "name": "LinkedIn Analysis",
    "description": "LinkedIn parsing for Network Engineer. Specific keyword mappings are maintained inside the individual skill JSONs."
}

# 4. HAND-CRAFTED ASSESSMENTS
# We map hand-crafted assessment questions in the global assessment.json
# No loop generation here! Only unique, technology-specific scenarios.
handcrafted_questions = {
    "ne_fundamentals.cabling": [{"level": "junior", "type": "scenario", "question": "A link between two switches 300 meters apart is flapping. What type of SFP and cabling would you deploy to ensure a stable 10G connection?", "expected_answer_keywords": ["Single-mode fiber", "Multi-mode fiber", "SFP+", "10GBASE-LR", "10GBASE-SR", "attenuation"]}],
    "ne_fundamentals.topologies": [{"level": "junior", "type": "scenario", "question": "Compare a traditional three-tier network architecture with a spine-leaf topology. Why is spine-leaf preferred in modern data centers?", "expected_answer_keywords": ["East-West traffic", "North-South traffic", "Spine", "Leaf", "Latency", "Scalability", "ECMP"]}],
    "ne_fundamentals.media_access": [{"level": "junior", "type": "scenario", "question": "Explain the difference between CSMA/CD and CSMA/CA, and identify which environments use them.", "expected_answer_keywords": ["Collision Detection", "Collision Avoidance", "Ethernet", "Wireless", "Half-duplex", "Jam signal"]}],
    "ne_fundamentals.network_racks": [{"level": "junior", "type": "scenario", "question": "You are provisioning a new switch in a rack. Explain what a 'U' (Rack Unit) is and how you would calculate power requirements for dual-PSU switches.", "expected_answer_keywords": ["Rack Unit", "1.75 inches", "PDU", "Redundancy", "A/B power feeds"]}],
    "ne_fundamentals.power_over_ethernet": [{"level": "mid", "type": "scenario", "question": "A new WiFi 6 AP is connected to a switch port but fails to boot fully, showing a power warning. What IEEE standard does it likely require, and how do you check the PoE budget?", "expected_answer_keywords": ["802.3at", "802.3bt", "PoE+", "LLDP power negotiation", "show power inline"]}],
    "ne_fundamentals.wan_basics": [{"level": "mid", "type": "scenario", "question": "You need to connect a remote branch office. Compare the use of a leased line versus Metro Ethernet in terms of encapsulation and handoff.", "expected_answer_keywords": ["Metro Ethernet", "Leased line", "Demarcation point", "CPE", "Ethernet handoff", "VLAN tag"]}],
    "ne_fundamentals.data_centers": [{"level": "senior", "type": "scenario", "question": "Design a Layer 3 routing fabric for a spine-leaf data center. Which routing protocol would you use for the underlay and why?", "expected_answer_keywords": ["eBGP", "OSPF", "Underlay", "ECMP", "Fast convergence", "ASN per leaf"]}],
    "ne_fundamentals.cloud_connectivity": [{"level": "senior", "type": "scenario", "question": "Explain the BGP peering requirements and VLAN dot1q tagging needed to establish an AWS Direct Connect or Azure ExpressRoute from an on-premise edge router.", "expected_answer_keywords": ["Direct Connect", "ExpressRoute", "eBGP", "Private ASN", "802.1Q", "VNI"]}],
    
    "ne_osi_tcpip.osi_model": [{"level": "junior", "type": "scenario", "question": "At which OSI layer does a MAC address operate, and at which layer does an IP address operate? How do they interact?", "expected_answer_keywords": ["Data Link Layer", "Layer 2", "Network Layer", "Layer 3", "ARP", "Encapsulation"]}],
    "ne_osi_tcpip.tcp_ip_model": [{"level": "junior", "type": "scenario", "question": "Map the OSI model to the 4-layer TCP/IP (DoD) model. Which OSI layers combine into the TCP/IP Application layer?", "expected_answer_keywords": ["Application", "Presentation", "Session", "TCP/IP Application layer"]}],
    "ne_osi_tcpip.arp": [{"level": "junior", "type": "scenario", "question": "A host wants to communicate with an IP on the same subnet but doesn't know the MAC address. Describe the ARP broadcast process.", "expected_answer_keywords": ["ARP Request", "Broadcast MAC", "FF:FF:FF:FF:FF:FF", "ARP Reply", "Unicast"]}],
    "ne_osi_tcpip.icmp": [{"level": "junior", "type": "scenario", "question": "You execute a traceroute command. Explain how the TTL field in the IP header and ICMP Time Exceeded messages are used to discover the path.", "expected_answer_keywords": ["TTL", "Time to Live", "ICMP Time Exceeded", "Type 11", "Echo Request", "Hop count"]}],
    "ne_osi_tcpip.tcp_vs_udp": [{"level": "mid", "type": "scenario", "question": "During a file transfer, a router drops several packets due to congestion. Explain how TCP recovers from this compared to UDP.", "expected_answer_keywords": ["TCP Retransmission", "Sequence numbers", "Acknowledgments", "ACK", "Window sliding", "UDP connectionless"]}],
    "ne_osi_tcpip.mtu_fragmentation": [{"level": "mid", "type": "scenario", "question": "A GRE tunnel is dropping large packets. Explain Path MTU Discovery (PMTUD) and the role of the 'Don't Fragment' (DF) bit.", "expected_answer_keywords": ["PMTUD", "ICMP Fragmentation Needed", "Type 3 Code 4", "DF bit", "MSS adjustment", "TCP Adjust-MSS"]}],
    "ne_osi_tcpip.packet_analysis": [{"level": "senior", "type": "scenario", "question": "You capture a PCAP of a failing TCP connection. The client sends a SYN, the server replies with SYN-ACK, but the client sends an RST. What could cause this?", "expected_answer_keywords": ["Asymmetric routing", "Stateful firewall", "TCP RST", "Out of state", "Sequence number mismatch"]}],
    "ne_osi_tcpip.qos_dscp": [{"level": "senior", "type": "scenario", "question": "Voice traffic is experiencing jitter. How would you configure DSCP marking and a strict priority queue (LLQ) to prioritize RTP packets?", "expected_answer_keywords": ["DSCP EF", "Expedited Forwarding", "LLQ", "Strict priority", "Class-map", "Policy-map", "RTP"]}],
    
    "ne_addressing_routing.ipv4_subnetting": [{"level": "junior", "type": "scenario", "question": "Given the network 192.168.1.0/24, subnet it to provide exactly 30 usable host IPs per subnet. What is the new subnet mask and CIDR notation?", "expected_answer_keywords": ["/27", "255.255.255.224", "32 addresses", "30 usable", "Block size"]}],
    "ne_addressing_routing.ipv6_addressing": [{"level": "junior", "type": "scenario", "question": "Explain how a host generates its own IPv6 address using SLAAC and the EUI-64 format.", "expected_answer_keywords": ["SLAAC", "Stateless Address Autoconfiguration", "Router Advertisement", "NDP", "MAC address", "FFFE"]}],
    "ne_addressing_routing.static_routing": [{"level": "junior", "type": "scenario", "question": "You need to configure a backup route to the internet that only becomes active if the primary link fails. How do you configure a floating static route?", "expected_answer_keywords": ["Administrative Distance", "AD", "ip route 0.0.0.0 0.0.0.0", "Higher metric", "Backup path"]}],
    "ne_addressing_routing.ospf": [{"level": "mid", "type": "scenario", "question": "Two OSPF routers are stuck in the EXSTART state. What is the most common cause for this adjacency failure and how do you fix it?", "expected_answer_keywords": ["MTU mismatch", "ip mtu", "ip ospf mtu-ignore", "Database Description", "DBD packets"]}],
    "ne_addressing_routing.eigrp": [{"level": "mid", "type": "scenario", "question": "An EIGRP route is stuck in the ACTIVE state. Explain the DUAL algorithm's process for querying neighbors and how to prevent SIA (Stuck in Active).", "expected_answer_keywords": ["DUAL", "Feasible Successor", "Query packet", "SIA timer", "EIGRP stub", "Query boundary"]}],
    "ne_addressing_routing.bgp": [{"level": "senior", "type": "scenario", "question": "You are receiving a BGP prefix from two different ISPs. How do you manipulate the Local Preference and AS-Path Prepending attributes to prefer ISP-A for outbound traffic and ISP-B for inbound?", "expected_answer_keywords": ["Local Preference", "Outbound traffic", "AS-Path Prepending", "Inbound traffic", "route-map", "BGP best path selection"]}],
    "ne_addressing_routing.route_redistribution": [{"level": "senior", "type": "scenario", "question": "When redistributing routes between OSPF and EIGRP, routing loops can occur. How do you use route tags and route-maps to prevent this?", "expected_answer_keywords": ["Route tagging", "route-map", "match tag", "deny", "Administrative Distance", "Suboptimal routing"]}],
    "ne_addressing_routing.mpls": [{"level": "senior", "type": "scenario", "question": "Explain the control plane and data plane operations of an MPLS L3VPN. What role do Route Distinguishers (RD) and Route Targets (RT) play?", "expected_answer_keywords": ["VRF", "Route Distinguisher", "RD", "Route Target", "RT", "MP-BGP", "Label Distribution Protocol", "LDP", "VPNv4"]}],

    "ne_switching_lan.vlans": [{"level": "junior", "type": "scenario", "question": "A PC is connected to a switch port but cannot reach the gateway. The port shows 'up/up'. What commands would you use to verify the VLAN assignment and MAC address learning?", "expected_answer_keywords": ["show vlan brief", "show mac address-table", "switchport access vlan", "show interface status"]}],
    "ne_switching_lan.trunking": [{"level": "junior", "type": "scenario", "question": "You connect two switches, but VLANs are not passing between them. Explain how to check for Native VLAN mismatches and verify the 802.1Q trunk status.", "expected_answer_keywords": ["show interfaces trunk", "switchport mode trunk", "Native VLAN mismatch", "CDP neighbor", "encapsulation dot1q"]}],
    "ne_switching_lan.vtp": [{"level": "junior", "type": "scenario", "question": "A new switch is added to the network, and suddenly all VLANs are deleted. Explain VTP revision numbers and how to prevent this.", "expected_answer_keywords": ["VTP revision number", "VTP transparent mode", "VTP domain", "Higher revision", "Configuration override"]}],
    "ne_switching_lan.inter_vlan_routing": [{"level": "junior", "type": "scenario", "question": "Describe the configuration steps to implement 'Router on a Stick' for VLANs 10 and 20 using a single physical router interface.", "expected_answer_keywords": ["Subinterface", "encapsulation dot1q 10", "ip address", "Default gateway", "Trunk port"]}],
    "ne_switching_lan.stp": [{"level": "mid", "type": "scenario", "question": "A user plugs an unmanaged switch into two wall jacks, creating a loop. How do you configure STP PortFast and BPDU Guard to mitigate this instantly?", "expected_answer_keywords": ["spanning-tree portfast", "spanning-tree bpduguard enable", "err-disable", "Broadcast storm", "Root bridge"]}],
    "ne_switching_lan.etherchannel": [{"level": "mid", "type": "scenario", "question": "You configure an LACP Port-Channel between two switches, but it stays in a 'suspended' state. What parameters must match on the physical ports for EtherChannel to form?", "expected_answer_keywords": ["Speed", "Duplex", "Allowed VLANs", "Native VLAN", "channel-group mode active", "show etherchannel summary"]}],
    "ne_switching_lan.layer2_security": [{"level": "senior", "type": "scenario", "question": "An attacker is running a rogue DHCP server. Explain how DHCP Snooping and Dynamic ARP Inspection (DAI) work together to block this and protect the ARP cache.", "expected_answer_keywords": ["DHCP Snooping binding database", "Trusted ports", "Untrusted ports", "DAI", "ip arp inspection", "Man-in-the-middle"]}],
    "ne_switching_lan.high_availability": [{"level": "senior", "type": "scenario", "question": "You have two core switches acting as gateways using HSRP. If the active switch loses its uplink to the internet, how do you ensure the standby switch takes over the active role automatically?", "expected_answer_keywords": ["HSRP", "Standby track", "Tracking objects", "Decrement priority", "Preempt", "Virtual IP"]}],

    "ne_wireless.rf_principles": [{"level": "junior", "type": "scenario", "question": "A user complains about slow WiFi in an open office. You notice they are connected to 2.4GHz instead of 5GHz. Compare the propagation and interference characteristics of both bands.", "expected_answer_keywords": ["2.4GHz", "5GHz", "Attenuation", "Non-overlapping channels", "Microwave interference", "Penetration"]}],
    "ne_wireless.standards_80211": [{"level": "junior", "type": "scenario", "question": "Explain the key performance benefits of 802.11ax (WiFi 6) over 802.11ac, specifically focusing on handling high client density.", "expected_answer_keywords": ["OFDMA", "BSS Coloring", "Target Wake Time", "TWT", "MU-MIMO", "Spatial streams"]}],
    "ne_wireless.ap_modes": [{"level": "junior", "type": "scenario", "question": "What is the difference between an Autonomous AP and a Lightweight AP, and how does CAPWAP function in a controller-based architecture?", "expected_answer_keywords": ["WLC", "CAPWAP tunnel", "Split MAC architecture", "Centralized management", "Autonomous AP"]}],
    "ne_wireless.wireless_security": [{"level": "mid", "type": "scenario", "question": "How does WPA3's SAE (Simultaneous Authentication of Equals) provide better security against offline dictionary attacks compared to WPA2's 4-way handshake?", "expected_answer_keywords": ["SAE", "Dragonfly handshake", "WPA3", "Forward secrecy", "Offline dictionary attack", "4-way handshake"]}],
    "ne_wireless.troubleshooting": [{"level": "mid", "type": "scenario", "question": "Two APs on the same floor are transmitting on Channel 1 at full power. Explain the impact of co-channel interference (CCI) and how it affects the CSMA/CA backoff timers.", "expected_answer_keywords": ["Co-channel interference", "CCI", "Clear Channel Assessment", "CCA", "Airtime contention", "Noise floor"]}],
    "ne_wireless.wlc_config": [{"level": "senior", "type": "scenario", "question": "You are configuring a new Cisco WLC for an enterprise. Explain how you map a WLAN (SSID) to a dynamic interface, and how that traffic is trunked to the core switch.", "expected_answer_keywords": ["Dynamic interface", "WLAN ID", "VLAN tagging", "LAG", "Link Aggregation", "Distribution system port"]}],
    "ne_wireless.roaming": [{"level": "senior", "type": "scenario", "question": "Voice over WiFi clients are dropping calls when walking between APs. Explain how 802.11r (Fast BSS Transition) and 802.11k optimize the roaming process.", "expected_answer_keywords": ["802.11r", "Fast transition", "FT", "802.11k", "Neighbor report", "Authentication delay", "PMK caching"]}],
    "ne_wireless.site_survey": [{"level": "senior", "type": "scenario", "question": "When performing an active site survey with tools like Ekahau, what SNR (Signal-to-Noise Ratio) and RSSI thresholds are generally recommended for VoWLAN?", "expected_answer_keywords": ["RSSI", "-65 dBm", "-67 dBm", "SNR", "25 dB", "Cell overlap", "Secondary coverage"]}],

    "ne_network_security.acls": [{"level": "junior", "type": "scenario", "question": "Write an extended Cisco IPv4 ACL command to block host 192.168.1.50 from reaching web server 10.0.0.5 on port 443, while allowing everything else.", "expected_answer_keywords": ["access-list", "deny tcp host 192.168.1.50 host 10.0.0.5 eq 443", "permit ip any any", "implicit deny"]}],
    "ne_network_security.nat": [{"level": "junior", "type": "scenario", "question": "Users on the inside network (10.0.0.0/24) cannot reach the internet. Detail the commands needed to configure NAT Overload (PAT) on the exit router interface.", "expected_answer_keywords": ["ip nat inside", "ip nat outside", "ip nat inside source list 1 interface GigabitEthernet0/0 overload", "access-list 1 permit 10.0.0.0"]}],
    "ne_network_security.aaa": [{"level": "junior", "type": "scenario", "question": "You want to centralize SSH login credentials for all routers. Explain the difference between RADIUS and TACACS+ in terms of protocol, encryption, and authorization separation.", "expected_answer_keywords": ["TACACS+", "TCP", "Full packet encryption", "Command authorization", "RADIUS", "UDP", "Password only encryption"]}],
    "ne_network_security.firewall_config": [{"level": "mid", "type": "scenario", "question": "Traffic from a DMZ zone to an Internal zone is being blocked by a Palo Alto firewall. Where in the security policy would you look, and how does stateful inspection handle the return traffic?", "expected_answer_keywords": ["Security rule", "Zone-based", "DMZ to Internal", "Stateful firewall", "Connection table", "Return traffic allowed automatically"]}],
    "ne_network_security.vpn_remote": [{"level": "mid", "type": "scenario", "question": "Remote workers complain they cannot reach local network printers when connected to the corporate AnyConnect SSL VPN. Explain split-tunneling and how to configure it.", "expected_answer_keywords": ["Split tunneling", "Tunnel-all", "split-include", "ACL", "Routing table", "VPN client"]}],
    "ne_network_security.vpn_ipsec": [{"level": "senior", "type": "scenario", "question": "A Site-to-Site IPsec VPN is failing at Phase 1. What ISAKMP/IKE parameters must strictly match on both peers for Phase 1 to complete successfully?", "expected_answer_keywords": ["Pre-shared key", "PSK", "Encryption algorithm", "Hashing algorithm", "Diffie-Hellman group", "DH group", "Lifetime"]}],
    "ne_network_security.dmvpn": [{"level": "senior", "type": "scenario", "question": "In a DMVPN Phase 3 deployment, spoke-to-spoke tunnels are not forming. Explain the role of NHRP resolution requests and what command enables NHS redirect on the hub.", "expected_answer_keywords": ["NHRP", "Next Hop Resolution Protocol", "mGRE", "ip nhrp redirect", "ip nhrp shortcut", "Spoke-to-spoke"]}],
    "ne_network_security.macsec": [{"level": "senior", "type": "scenario", "question": "You are deploying MACsec on an inter-switch fiber link. How does 802.1AE differ from IPsec in terms of the OSI layer it operates on, and what protocol manages the keys?", "expected_answer_keywords": ["Layer 2", "Hop-by-hop encryption", "MKA", "MACsec Key Agreement", "802.1X", "IPsec is Layer 3"]}],

    "ne_services_observability.dhcp": [{"level": "junior", "type": "scenario", "question": "Clients in VLAN 10 cannot get an IP address because the DHCP server is in VLAN 20. How do you resolve this at the routing boundary?", "expected_answer_keywords": ["ip helper-address", "DHCP Relay", "Broadcast to unicast", "UDP port 67", "SVI"]}],
    "ne_services_observability.dns": [{"level": "junior", "type": "scenario", "question": "A router can ping 8.8.8.8 but cannot ping 'google.com'. What configuration command is missing to enable name resolution on the device?", "expected_answer_keywords": ["ip name-server", "ip domain-lookup", "DNS resolution"]}],
    "ne_services_observability.ntp": [{"level": "junior", "type": "scenario", "question": "Logs on two switches show different timestamps for the same spanning-tree event. How do you synchronize them securely?", "expected_answer_keywords": ["NTP", "ntp server", "Stratum", "NTP authentication", "Clock sync"]}],
    "ne_services_observability.syslog": [{"level": "junior", "type": "scenario", "question": "You want to send only critical alerts to a remote Syslog server, but keep debugging messages local. Explain syslog severity levels and how to configure this filtering.", "expected_answer_keywords": ["Severity levels", "0 to 7", "logging trap critical", "logging buffered debugging", "logging host"]}],
    "ne_services_observability.snmp": [{"level": "mid", "type": "scenario", "question": "You are migrating from SNMPv2c to SNMPv3. What are the three primary security enhancements introduced in SNMPv3?", "expected_answer_keywords": ["Authentication", "Encryption", "Privacy", "authPriv", "HMAC", "AES", "Username"]}],
    "ne_services_observability.netflow": [{"level": "mid", "type": "scenario", "question": "A network link is heavily congested, but SNMP only shows bandwidth utilization, not the source/destination IPs. How do you configure NetFlow to identify the top talkers?", "expected_answer_keywords": ["ip flow ingress", "ip flow-export destination", "Flow collector", "Source IP", "Destination IP", "Port numbers"]}],
    "ne_services_observability.automation_python": [{"level": "senior", "type": "scenario", "question": "You need to push a configuration change to 100 Cisco IOS devices. Compare writing a script using Netmiko vs Napalm for this specific task.", "expected_answer_keywords": ["Netmiko", "CLI scraping", "SSH", "Napalm", "Configuration replacement", "Declarative", "Rollback"]}],
    "ne_services_observability.automation_ansible": [{"level": "senior", "type": "scenario", "question": "In an Ansible playbook targeting NX-OS switches, how does the 'nxos_config' module achieve idempotency when applying a list of commands?", "expected_answer_keywords": ["Idempotency", "Gathering facts", "Compare config", "Only apply if changed", "nxos_config"]}],
}

assessment_evidence = {
    "source_id": "assessment",
    "name": "Adaptive Technical Assessment - Network Engineer",
    "description": "Questions for Network Engineer skills. Fully hand-crafted for each specific technology.",
    "sample_questions_by_composite_key": handcrafted_questions,
    "scoring_rules_reference": {
        "source": "knowledge-base/scoring/engine.json",
        "description": "Scoring rules for assessment are defined in engine.json"
    }
}

with open(os.path.join(evidence_dir, "github.json"), "w", encoding="utf-8") as f:
    json.dump(github_evidence, f, indent=2)
with open(os.path.join(evidence_dir, "cv.json"), "w", encoding="utf-8") as f:
    json.dump(cv_evidence, f, indent=2)
with open(os.path.join(evidence_dir, "linkedin.json"), "w", encoding="utf-8") as f:
    json.dump(linkedin_evidence, f, indent=2)
with open(os.path.join(evidence_dir, "assessment.json"), "w", encoding="utf-8") as f:
    json.dump(assessment_evidence, f, indent=2)

print("Network Engineer KB successfully generated with deeply handcrafted evidence.")
