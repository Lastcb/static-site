import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node

from textnode import TextType, TextNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        node2 =' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), node2)

    def test_prop_none(self):
        node = HTMLNode(props=None)
        node2 = ""
        self.assertEqual(node.props_to_html(), node2)
    
    def test_single_prop_dict(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        node2 =' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), node2)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leat_plain_text(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_value_error(self):
        self.assertRaises(ValueError, LeafNode(None, None).to_html)
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_raise_error_parentnode_no_tag(self):
        self.assertRaises(ValueError, ParentNode(None, ["span", "child"]).to_html)
    
    def test_raise_error_empty_children(self):
        self.assertRaises(ValueError, ParentNode("p", []).to_html)

    def test_raise_error_empty_grandchildren(self):
        self.assertRaises(ValueError, ParentNode("div", [ParentNode("span", [])]).to_html)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a set of code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a set of code")

    def test_link(self):
        node = TextNode("Link name", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link name")
        self.assertEqual(html_node.props["href"], "www.google.com")

    def test_image(self):
        node = TextNode("picture of google", TextType.IMAGE, "www.google.com/picture")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "www.google.com/picture")
        self.assertEqual(html_node.props["alt"], "picture of google")

if __name__ == "__main__":
    unittest.main()   
    


