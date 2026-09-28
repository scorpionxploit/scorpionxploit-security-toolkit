from toolkit.subnet_calc import calculate_subnet

def test_subnet_cidr_calculation():
    res = calculate_subnet("192.168.1.0/24")
    assert res["usable_hosts"] == 254
    assert res["broadcast_address"] == "192.168.1.255"
    assert res["netmask"] == "255.255.255.0"
