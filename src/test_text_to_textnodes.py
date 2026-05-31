import unittest

from textnode import TextNode, TextType
from inline_markdown import text_to_textnodes

class TextNode_to_HTMLNode(unittest.TestCase):
    def test_plain_text(self):
        text = "Just plain text"
        result = text_to_textnodes(text)
        expected = [TextNode("Just plain text", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_bold_text(self):
        text = "This is **bold** text"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_italic_text(self):
        text = "This is _italic_ text"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_code_text(self):
        text = "This is `code` text"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_image(self):
        text = "Here is an ![alt text](https://example.com/img.png)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("Here is an ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://example.com/img.png"),
        ]
        self.assertEqual(result, expected)

    def test_link(self):
        text = "Click [here](https://example.com) now"
        result = text_to_textnodes(text)
        expected = [
            TextNode("Click ", TextType.TEXT),
            TextNode("here", TextType.LINK, "https://example.com"),
            TextNode(" now", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_mixed_all_types(self):
        text = "This is **bold**, _italic_, `code`, ![img](https://img.com) and [link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(", ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "https://img.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)

    def test_image_at_start(self):
        text = "![start](https://start.com) then text"
        result = text_to_textnodes(text)
        expected = [
            TextNode("start", TextType.IMAGE, "https://start.com"),
            TextNode(" then text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_link_at_end(self):
        text = "Go to [end](https://end.com)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("Go to ", TextType.TEXT),
            TextNode("end", TextType.LINK, "https://end.com"),
        ]
        self.assertEqual(result, expected)

    def test_multiple_bold_instances(self):
        text = "This is **bold1** and **bold2** text"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold1", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold2", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_only_markdown_element(self):
        text = "**boldonly**"
        result = text_to_textnodes(text)
        expected = [TextNode("boldonly", TextType.BOLD)]
        self.assertEqual(result, expected)

        text = "_italiconly_"
        result = text_to_textnodes(text)
        expected = [TextNode("italiconly", TextType.ITALIC)]
        self.assertEqual(result, expected)

        text = "`codeonly`"
        result = text_to_textnodes(text)
        expected = [TextNode("codeonly", TextType.CODE)]
        self.assertEqual(result, expected)

        text = "![img](https://img.com)"
        result = text_to_textnodes(text)
        expected = [TextNode("img", TextType.IMAGE, "https://img.com")]
        self.assertEqual(result, expected)

        text = "[link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [TextNode("link", TextType.LINK, "https://boot.dev")]
        self.assertEqual(result, expected)

    def test_text_starting_and_ending_with_delimiter(self):
        text = "**bold** in the middle **end**"
        result = text_to_textnodes(text)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" in the middle ", TextType.TEXT),
            TextNode("end", TextType.BOLD),
        ]
        self.assertEqual(result, expected)

        text = "_italic_ start and _finish_"
        result = text_to_textnodes(text)
        expected = [
            TextNode("italic", TextType.ITALIC),
            TextNode(" start and ", TextType.TEXT),
            TextNode("finish", TextType.ITALIC),
        ]
        self.assertEqual(result, expected)

        text = "`code` then more `stuff`"
        result = text_to_textnodes(text)
        expected = [
            TextNode("code", TextType.CODE),
            TextNode(" then more ", TextType.TEXT),
            TextNode("stuff", TextType.CODE),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()