import bpy

# Enable the Node Wrangler add-on
bpy.ops.preferences.addon_enable(module='node_wrangler')

def delete_unused_nodes(material):
    node_tree = material.node_tree
    nodes_to_remove = []

    for node in node_tree.nodes:
        if not node.outputs:
            continue

        has_linked_output = any([output.is_linked for output in node.outputs])

        if not has_linked_output:
            nodes_to_remove.append(node)

    for node in nodes_to_remove:
        node_tree.nodes.remove(node)

# Iterate through all materials in the blend file
for material in bpy.data.materials:
    if material.use_nodes:
        delete_unused_nodes(material)
