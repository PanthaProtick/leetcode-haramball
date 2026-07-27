from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        queue = deque([(startGene, 0)])
        visited = set([startGene])

        while queue:
            current_gene, moves = queue.popleft()

            if current_gene == endGene:
                return moves

            for i in range(len(current_gene)):
                for char in "ACGT":
                    if char != current_gene[i]:
                        next_gene = current_gene[:i] + char + current_gene[i+1:]
                        
                        if next_gene in bank_set and next_gene not in visited:
                            visited.add(next_gene)
                            queue.append((next_gene, moves + 1))

        return -1