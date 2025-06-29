import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_uneq(self):
        node = TextNode("This is text for a url", TextType.LINK, "www.google.com")
        node2 = TextNode("url", TextType.LINK, "www.google.com")
        self.assertNotEqual(node, node2)
    
    def test_url_uneq(self):
        node = TextNode("This is text for a url", TextType.LINK)
        node2 = TextNode("This is text for a url", TextType.LINK, "www.google.com")
        self.assertNotEqual(node, node2)
    
    def test_text_type_uneq(self):
        node = TextNode("No url here", TextType.LINK)
        node2 = TextNode("No url here", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
            )

if __name__ == "__main__":
    unittest.main()
