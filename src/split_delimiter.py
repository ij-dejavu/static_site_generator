from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) == 1:
            if node.text == "":
                continue
            new_nodes.append(node)
            continue
        
        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter in: '{node.text}'")
                    
        for i in range(len(parts)):
            if i % 2==0:
                if parts[i]=="":
                    continue 
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                if parts[i]=="":
                    continue
                new_nodes.append(TextNode(parts[i], text_type))
    return new_nodes

