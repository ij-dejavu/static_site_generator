import unittest

from markdown_blocks import block_to_block_type, BlockType


class BlockToBlockTypeTests(unittest.TestCase):
    def test_paragraph(self):
        block = "This is just a normal paragraph with some text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading(self):
        block = "### My heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_too_many_hashes(self):
        block = "####### Not valid"
        # 7 hashes should not be a heading
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_block(self):
        block = "```\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> This is a quote\n> Another line"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_block_with_non_quote_line(self):
        block = "> First line\nNot a quote"
        # Mixed lines should fall back to paragraph
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        block = "- Item one\n- Item two\n- Item three"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_with_bad_line(self):
        block = "- Item one\nNot a list item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_numbering(self):
        block = "1. First\n3. Wrong numbering"
        # Numbers must increment correctly, so this should be a paragraph
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_starting_wrong(self):
        block = "2. Starts at two\n3. Next"
        # Must start at 1
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_single_line_code_block(self):
        block = "```print('hi')```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_heading_missing_space(self):
        block = "##No space"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_incomplete_code_block(self):
        block = "```\nprint('hi')"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote_block_with_blank_line_fails(self):
        block = "> line one\n\n> line two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_invalid_format(self):
        block = "1) Not valid\n2. Valid form"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_mixed_list_not_valid(self):
        block = "1. First\n- Second"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_single_line_ordered_list(self):
        block = "1. Only one item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

if __name__ == "__main__":
    unittest.main()