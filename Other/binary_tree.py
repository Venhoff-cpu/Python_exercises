# not completed
def solution(T):
    x = T.x
    left_node = T.l
    right_node = T.r
    visible_nodes = 0

    if left_node == right_node is None:
        return visible_nodes

    if left_node.x >= x:
        visible_nodes += 1
    elif left_node is not None:
        return solution(left_node)

    if right_node.x >= x:
        visible_nodes +=1
    elif right_node is not None:
        return solution(right_node)


solution((5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None)))
