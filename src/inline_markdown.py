from textnode import TextNode, TextType
import re


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes



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



def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        current_text = node.text
        images = extract_markdown_images(current_text)

        if len(images) == 0:
            new_nodes.append(node)
            continue
        
        for alt, url in images:
            markdown_string = f"![{alt}]({url})"
            sections = current_text.split(markdown_string,1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            current_text = sections[1]

        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        current_text = node.text
        links = extract_markdown_links(current_text)

        if len(links) == 0:
            new_nodes.append(node)
            continue
                   
        for alt, url in links:
            markdown_string = f"[{alt}]({url})"
            sections = current_text.split(markdown_string,1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url))
            current_text = sections[1]

        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes



def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
