from textnode import  text_node_to_html_node
from htmlnode import  ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            children.append(paragraph_to_html_node(block))
        elif block_type == BlockType.QUOTE:
            children.append(quote_to_html_node(block))
        elif block_type == BlockType.UNORDERED_LIST:
            children.append(unordered_list_to_html_node(block))
        elif block_type == BlockType.ORDERED_LIST:
            children.append(ordered_list_to_html_node(block))
        elif block_type == BlockType.HEADING:
            children.append(heading_to_html_node(block))
        elif block_type == BlockType.CODE:
            children.append(code_to_html_node(block))
    return ParentNode('div', children)    

def markdown_to_blocks(markdown):
    block_strings = markdown.split('\n\n')
    blocks = []
    for block in block_strings:
        stripped = block.strip()
        if stripped:
            blocks.append(stripped)
    return blocks


def block_to_block_type(block):

    if block.startswith('#'):
        start = block.split(" ")[0]
        if len(start) < 7 and start.count('#') == len(start):
            return BlockType.HEADING
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    
    for line in block.split('\n'):
        if not line.startswith('>'):
            break
    else:
        return BlockType.QUOTE

    for line in block.split('\n'):
        if not line.startswith('- '):
            break
    else:
        return BlockType.UNORDERED_LIST
    
    nr = 1
    for line in block.split('\n'):
        if line.startswith(f'{nr}. '):
            nr += 1
        else:
            break
    else:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

 

def paragraph_to_html_node(block):
    lines = block.split('\n')
    clear_block = " ".join(lines)

    children = text_to_children(clear_block)
    return ParentNode("p", children)

def quote_to_html_node(block):
    clear_lines = []
    for line in block.split('\n'):
        clear_lines.append(line.lstrip('> '))
    clear_block = " ".join(clear_lines)
    
    children = text_to_children(clear_block)
    return ParentNode("blockquote", children)

def unordered_list_to_html_node(block):
    nodes_list = []
    for line in block.split('\n'):
        clear_line = line.lstrip('- ')
        child = ParentNode('li',text_to_children(clear_line))
        nodes_list.append(child)
    
    return ParentNode("ul", nodes_list)

def ordered_list_to_html_node(block):
    nodes_list = []
    for line in block.split('\n'):
        clear_line = line.split('. ', 1)[1]
        child = ParentNode('li',text_to_children(clear_line))
        nodes_list.append(child)
    
    return ParentNode("ol", nodes_list)

def heading_to_html_node(block):
    count = 0
    for i in block:
        if i == '#':
            count += 1
        else:
            break

    clean_block = block[count:].lstrip()
    tag = f"h{count}"
    children = text_to_children(clean_block)
    return ParentNode(tag, children)

def code_to_html_node(block):
    lines = block.split('\n')[1:-1]
    code_text = "\n".join(lines) + "\n"

    return ParentNode("pre", [LeafNode('code', code_text)])


def text_to_children(text):
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes
