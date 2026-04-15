from cf101 import config_template


def test_config_template_includes_i2p_dns_and_proxy_routing():
    rendered = config_template.format(
        client_ipv4="172.16.0.2",
        client_ipv6="2606:4700:110:8765::2",
        privKey="priv",
        peer_pub="pub",
    )

    assert "fake-ip-filter-mode: rule" in rendered
    assert "DOMAIN-SUFFIX,i2p,fake-ip" in rendered
    assert 'name: "i2p-http"' in rendered
    assert "type: http" in rendered
    assert "port: 4444" in rendered
    assert 'name: "i2p-socks"' in rendered
    assert "type: socks5" in rendered
    assert "port: 4447" in rendered
    assert "- name: i2p" in rendered
    assert '- DOMAIN-SUFFIX,i2p,i2p' in rendered
