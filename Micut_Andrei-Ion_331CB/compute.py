# Micut Andrei-Ion, Grupa 331CB
# calculez matricea delta
def compute_delta(substring, nr_chars):

    delta = []

    # realizez umplerea matricei cu 0-uri
    for i in range(len(substring) + 1):
        array = []
        for j in range(0, nr_chars):
            array.append(0)
        delta.append(array)

    # in matricea delta va fi introdusa o valoare cuprinsa intre 0 si len(substring)
    q = 0
    while q <= len(substring):
        i = 0
        while i < nr_chars:
            delta[q][i] = next_state(substring, q, i)
            i = i + 1
        q = q + 1
    return delta

# se va calcula in matrice, pe pozitia q si idx,
# o valoare cuprinsa intre o si len(substring)


def next_state(substring, q, idx):

    if q < len(substring):
        if idx == ord(substring[q]):
            return q + 1

    i = 0
    # in longest_prefix se va gasi urmatoarea stare
    longest_prefix = q

    # pornesc de la valoarea cea mai mare si ma voi opri
    # cand gasesc prefixul(sufixul)
    while longest_prefix >= 0:
        if idx == ord(substring[longest_prefix - 1]):
            while i < longest_prefix - 1:
                if substring[i] != substring[q + i + 1 - longest_prefix]:
                    break
                i = i + 1
            if i + 1 == longest_prefix:
                return longest_prefix
        longest_prefix = longest_prefix - 1
    return 0