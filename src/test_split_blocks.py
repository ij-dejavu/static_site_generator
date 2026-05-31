import unittest

from markdown_blocks import markdown_to_blocks

class TestSplitBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_single_block(self):
        md = "Just a single block of text"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just a single block of text"])

    def test_multiple_blank_lines(self):
        md = """\
First block


Second block



Third block
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block", "Third block"])

    def test_leading_and_trailing_whitespace(self):
        md = """\
   First block with spaces    

Second block with trailing newline   
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["First block with spaces", "Second block with trailing newline"],
        )

    def test_list_block(self):
        md = """\
- Item one
- Item two
- Item three
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["- Item one\n- Item two\n- Item three"])

    def test_heading_and_paragraph(self):
        md = """\
# Heading

This is a paragraph with **bold** and _italic_ text
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["# Heading", "This is a paragraph with **bold** and _italic_ text"],
        )

    def test_text_starting_and_ending_with_newlines(self):
        md = """

Paragraph surrounded by blank lines

"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Paragraph surrounded by blank lines"])

    def test_whitespace_only_block(self):
        md = "First\n\n   \n\nSecond"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First", "Second"])



if __name__ == "__main__":
    unittest.main()