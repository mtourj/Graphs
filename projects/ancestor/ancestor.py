
def earliest_ancestor(ancestors, starting_node):
    parents = []

    for relationship in ancestors:
        if relationship[1] == starting_node:
            parents.append(relationship)

    while len(parents) > 0:
        ancestor = parents.pop()
        earlier_ancestor = earliest_ancestor(ancestors, ancestor[0])
        if earlier_ancestor > -1:
            parents.append((earlier_ancestor, ancestor[0]))
        elif len(parents) == 0:
            return ancestor[0]

    return -1
