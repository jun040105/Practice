logs = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.1", "10.0.0.1", "10.0.0.1"]

from collections import Counter 

def get_frequent_ips(logs, k):
    counts = Counter(logs)
    result = []
    for ip, count in counts.items():
        if count >= k:
            result.append(ip)

    return sorted(result)

print(get_frequent_ips(logs, 1))
