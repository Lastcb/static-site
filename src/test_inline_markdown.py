import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node

from textnode import TextType, TextNode

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
class TestSplitNodesDelimiter(unittest.TestCase):
    def test_delimiter_func(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "This is text with a ")

    def test_raise_err(self):
        node = TextNode("This is text with **bold wording", TextType.TEXT)
        self.assertRaises( Exception, split_nodes_delimiter, [node], "**", TextType.BOLD)

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)


    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [hyperlink](https://www.google.com)"
        )
        self.assertListEqual([("hyperlink", "https://www.google.com")], matches)
    
    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with multiple [hyperlink](https://www.google.com) [hyperlink2](https://www.youtube.com) links."
        )
        self.assertListEqual([("hyperlink", "https://www.google.com"), ("hyperlink2", "https://www.youtube.com")], matches)

    def test_extract_markdown_links_special_chars(self):
        matches = extract_markdown_links(
            "This is text with special [hyp3rl%$#@!](https://www.g%^&*le.com) link"
        )
        self.assertListEqual([("hyp3rl%$#@!", "https://www.g%^&*le.com")], matches)

    def test_extract_only_markdown_links(self):
        matches = extract_markdown_links(
                "This is text with a [hyperlink](https://www.google.com) and and image ![alt text](https://www.imgur.com)"
        )
        self.assertListEqual([("hyperlink", "https://www.google.com")], matches)

    def test_no_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with a hyperlink https://www.google.com"
            )
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()   
