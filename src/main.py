from textnode import TextNode, TextType

def main():
    node = TextNode("Hello, world!", TextType.BOLD, None)
    print(node)

main()