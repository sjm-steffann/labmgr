from collections.__init__ import OrderedDict
from ipaddress import IPv4Address, IPv4Interface, IPv4Network, IPv6Address, IPv6Interface, IPv6Network

version = '0.6'

networks = OrderedDict([
    (64500, {
        'role': 'student',
        'valid_prefix_v4': IPv4Network('203.0.113.0/24'),
        'valid_prefix_v6': IPv6Network('2001:db8:1000::/36'),
    }),
    (64501, {
        'role': 'customer',
        'link_address_v4': IPv4Interface('203.0.113.253/31'),
        'link_address_v6': IPv6Interface('2001:db8:1000:fffe::b/127'),
        'peer_asn': 64500,
        'valid_prefix_v4': IPv4Network('192.0.2.0/24'),
        'valid_prefix_v6': IPv6Network('2001:db8:1001::/48'),
        'announced_prefixes_v4': [
            (IPv4Network('192.0.2.0/24'), []),
            (IPv4Network('172.16.66.0/24'), []),
            (IPv4Network('192.168.255.0/24'), []),
        ],
        'announced_prefixes_v6': [
            (IPv6Network('2001:db8:1001::/48'), []),
            (IPv6Network('2001:db8:4567::/48'), []),
            (IPv6Network('2001:db8::/32'), []),
        ],
        'bogus_address_v4': IPv4Address('192.88.99.1'),
        'bogus_address_v6': IPv6Address('3ffe::1'),
        'stolen_address_v4': IPv4Address('203.0.113.3'),
        'stolen_address_v6': IPv6Address('2001:db8:3000::3'),
    }),
    (64502, {
        'role': 'customer',
        'link_address_v4': IPv4Interface('203.0.113.255/31'),
        'link_address_v6': IPv6Interface('2001:db8:1000:ffff::b/127'),
        'peer_asn': 64500,
        'valid_prefix_v4': IPv4Network('198.51.100.0/24'),
        'valid_prefix_v6': IPv6Network('2001:db8:2002::/48'),
        'announced_prefixes_v4': [
            (IPv4Network('198.51.100.0/24'), []),
            (IPv4Network('192.0.2.64/26'), []),
            (IPv4Network('192.0.2.128/25'), []),
        ],
        'announced_prefixes_v6': [
            (IPv6Network('2001:db8:2002::/48'), []),
            (IPv6Network('2001:db8:1001:1000::/52'), []),
        ],
        'bogus_address_v4': IPv4Address('192.88.99.2'),
        'bogus_address_v6': IPv6Address('3ffe::2'),
        'stolen_address_v4': IPv4Address('192.0.2.3'),
        'stolen_address_v6': IPv6Address('2001:db8:1000::3'),
    }),
    (64510, {
        'role': 'transit',
        'link_address_v4': IPv4Interface('192.168.255.254/31'),
        'link_address_v6': IPv6Interface('2001:db8:f000:ffff::a/127'),
        'peer_asn': 64500,
        'valid_prefix_v4': IPv4Network('10.0.0.0/8'),
        'valid_prefix_v6': IPv6Network('2001:db8::/36'),
        'announced_prefixes_v4': [
            (IPv4Network('10.0.0.0/8'), [65001, 65000, 65000]),
            (IPv4Network('172.16.0.0/12'), [65001, 65002]),
            (IPv4Network('192.168.0.0/16'), [65003, 65002]),
            (IPv4Network('203.0.113.64/26'), []),
        ],
        'announced_prefixes_v6': [
            (IPv6Network('2001:db8::/36'), [65001, 65000, 65000]),
            (IPv6Network('2001:db8:1200::/40'), []),
            (IPv6Network('2001:db8:4000::/36'), [65001, 65002]),
            (IPv6Network('2001:db8:5000::/36'), [65003, 65002]),
            (IPv6Network('2001:db8:6000::/36'), [65003, 65002, 65002]),
            (IPv6Network('2001:db8:7000::/36'), [65004, 65004, 65002]),
            (IPv6Network('2001:db8:8000::/36'), [65005, 65004, 65003, 65002]),
            (IPv6Network('2001:db8:9000::/36'), [65003, 65003, 65003, 65003, 65003, 65002]),
            (IPv6Network('2001:db8:a000::/36'), [65007, 65006, 65003, 65003, 65002]),
            (IPv6Network('2001:db8:b000::/36'), [65004, 65003, 65003, 65002]),
            (IPv6Network('2001:db8:c000::/36'), [65007, 65007, 65007, 65007, 65006, 65005, 65004, 65003, 65002]),
            (IPv6Network('2001:db8:d000::/36'), [65007, 65006, 65005, 65004, 65003, 65003, 65003, 65001]),
            (IPv6Network('2001:db8:e000::/36'), [65007, 65006, 65006, 65005, 65004, 65004, 65003, 65002]),
            (IPv6Network('2001:db8:f000::/36'), [65007, 65006, 65005, 65004, 65003, 65002, 65001]),
        ],
        'bogus_address_v4': IPv4Address('192.88.99.10'),
        'bogus_address_v6': IPv6Address('3ffe::10'),
        'stolen_address_v4': IPv4Address('198.51.100.3'),
        'stolen_address_v6': IPv6Address('2001:db8:1001::3'),
    }),

    (64511, {
        'role': 'peer',
        'link_address_v4': IPv4Interface('203.0.113.251/31'),
        'link_address_v6': IPv6Interface('2001:db8:1000:fffd::b/127'),
        'peer_asn': 64500,
        'valid_prefix_v4': None,
        'valid_prefix_v6': IPv6Network('2001:db8:3000::/36'),
        'announced_prefixes_v4': [
            (IPv4Network('0.0.0.0/0'), []),
            (IPv4Network('172.16.0.0/13'), []),
        ],
        'announced_prefixes_v6': [
            (IPv6Network('::/0'), []),
            (IPv6Network('2001:db8:3000::/36'), []),
            (IPv6Network('2001:db8:6000::/36'), [65003]),
            (IPv6Network('2001:db8:7000::/37'), [65004, 65002]),
        ],
        'bogus_address_v4': IPv4Address('192.88.99.11'),
        'bogus_address_v6': IPv6Address('3ffe::11'),
        'stolen_address_v4': IPv4Address('198.51.100.3'),
        'stolen_address_v6': IPv6Address('2001:db8:2002::3'),
    }),
])
