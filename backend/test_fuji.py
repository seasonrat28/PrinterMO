from app.services.snmp_service import snmp_walk

ip = "10.119.34.21"

oids = [
    "1.3.6.1.2.1.43",
    "1.3.6.1.4.1.2435",
    "1.3.6.1.4.1.1240"
]


for oid in oids:
    print("\n==========", oid, "==========")

    result = snmp_walk(ip, oid)

    for k,v in result.items():
        print(k, "=", v)