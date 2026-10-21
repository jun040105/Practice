N, K = map(int, input().split())
Nt = 1
Kt = 1
NK = 1

for i in range(N, 0, -1):
    Nt = Nt*i

for i in range(K, 0, -1):
    Kt = Kt*i

for i in range(N-K, 0, -1):
    NK = NK*i

print(Nt//(Kt*NK))