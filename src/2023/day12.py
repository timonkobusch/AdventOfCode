def p1(lines):
    def generate_combinations(length, blocks, partial, results):

        if not blocks:
            # If no more blocks to place, fill the rest with '.'
            results.append(partial + '.' * (length - len(partial)))
            return results

        if len(partial) > 0:
            # Add a separator '.' if this is not the first block
            partial += '.'

        for i in range(len(partial), length - sum(blocks) - len(blocks) + 2):
            new_partial = partial + '.' * (i - len(partial)) + '#' * blocks[0]
            generate_combinations(length, blocks[1:], new_partial, results)

        return results


    def get_arrangements(s, s_groups_):
        a = 0
        for c in generate_combinations(len(s), s_groups_, "", []):
            for i in range(len(s)):
                if c[i] == '.' and s[i] == '#' or s[i] == '.' and c[i] == '#':
                    break
            else:
                a += 1

        return a

    print("")
    ans = 0
    for line in lines:
        (symbols, s_groups) = line.split()
        s_groups = [int(x) for x in s_groups.split(',')]
        ans += get_arrangements(symbols, s_groups)

    return ans