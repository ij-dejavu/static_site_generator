import unittest

from inline_markdown import extract_markdown_images, extract_markdown_links

class TestImagesAndLinks(unittest.TestCase):
    def test_single_image(self):
        text = "![cat](https://example.com/cat.jpg)"
        expected = [("cat", "https://example.com/cat.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_multiple_images(self):
        text = "![one](url1) and ![two](url2)"
        expected = [("one", "url1"), ("two", "url2")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_image_with_special_chars(self):
        text = "![a l*t!](https://weird.url/img.png)"
        expected = [("a l*t!", "https://weird.url/img.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_image_with_nested_brackets(self):
        text = "![alt [inner]](https://example.com)"
        expected = [("alt [inner]", "https://example.com")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_image_with_missing_parts(self):
        text = "![no url]() and ![](no alt)"
        expected = [("no url", ""), ("", "no alt")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_image_with_extra_spaces(self):
        text = "![ spaced ]( https://example.com/img.png )"
        expected = [(" spaced ", " https://example.com/img.png ")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_single_link(self):
        text = "[Google](https://google.com)"
        expected = [("Google", "https://google.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_multiple_links(self):
        text = "[One](url1) and [Two](url2)"
        expected = [("One", "url1"), ("Two", "url2")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_link_with_nested_brackets(self):
        text = "[Click [here]](https://example.com)"
        expected = [("Click [here]", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_link_with_empty_text_or_url(self):
        text = "[](https://no-text.com) and [no-url]()"
        expected = [("", "https://no-text.com"), ("no-url", "")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_link_with_special_chars(self):
        text = "[!@#$%^&*()_+](https://symbols.com)"
        expected = [("!@#$%^&*()_+", "https://symbols.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_image_does_not_match_link(self):
        text = "![alt](https://image.com) [text](https://link.com)"
        expected = [("text", "https://link.com")]
        self.assertEqual(extract_markdown_links(text), expected)


if __name__ == "__main__":
    unittest.main()