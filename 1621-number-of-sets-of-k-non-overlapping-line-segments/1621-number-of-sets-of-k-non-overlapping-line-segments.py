class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        N = n + k - 1
        R = 2 * k

        # factorials
        fact = [1] * (N + 1)

        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD

        # nCr = fact[N] / (fact[R] * fact[N-R])
        # Fermat's Little Theorem for modular inverse
        ans = fact[N]
        ans = ans * pow(fact[R], MOD - 2, MOD) % MOD
        ans = ans * pow(fact[N - R], MOD - 2, MOD) % MOD

        return ans