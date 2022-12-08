with open('data08.txt') as f:
    data = f.readline().split()

ls_metadata = []

def foo(start_pos):
    pos = start_pos

    value = 0
    child_values = []
    total_len_child_node = 0
    len_child_node = 0

    num_children = int(data[pos])
    pos += 1
    num_metadata = int(data[pos])

    pos += 1
    for id_child in range(num_children):
        len_child_node, child_value= foo(pos + total_len_child_node)
        total_len_child_node += len_child_node
        child_values.append(int(child_value))

    for id_metadata in range(num_metadata):
        metadata = int(data[pos + total_len_child_node + id_metadata])
        if num_children == 0:
            value += metadata
        else:
            try:
                value += child_values[metadata-1]
            except:
                pass
        ls_metadata.append(int(metadata))
    len_node = 2 +  num_metadata + total_len_child_node
    return len_node, value

len_data, value_root_node = foo(0)
print('Sum of all metadata is:',sum(ls_metadata))
print('Value of root node is:', value_root_node)

