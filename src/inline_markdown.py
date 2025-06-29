import re
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType

#def split_nodes_delimiter(old_nodes, delimiter, text_type):
#    new_nodes = []
#    for textnode in old_nodes:
#        if textnode.text_type != TextType.TEXT:
#            new_nodes.append(textnode)
#            continue
#        split_nodes = []
#        if textnode.text.count(delimiter) % 2 == 1:
#            raise ValueError("Ensure markdown indicators are closed")
#        pieces = textnode.text.split(delimiter)
#        for i, piece in enumerate(pieces):
#            if len(piece) == 0 and i % 2 == 1:
#                raise Exception("Check for duplicate markdown indicator")
#            if i % 2 == 0:
#                split_nodes.append(TextNode(piece, TextType.TEXT))
#            else:
#                split_nodes.append(TextNode(piece, text_type))
#    return new_nodes
#
#def main():
#    node = TextNode("This is text with a `code block` word", TextType.TEXT)
#    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
#    print(new_nodes)
#if __name__ == "__main__":
#    main()

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

:edef split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        split_nodes = []
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_images = extract_markdown_images(old_node)
        if split_images == []
            new_nodes.append(old_node)
            continue
        for split_tuple in split_images:
            split_text = old_node.text.split(f"![{split_tuple[0]}]({split_tuple[1]})")
            while len(split_text) < 1:
                new_nodes.append(TextNode(split_text[0], TextType.TEXT)
                new_nodes.append(TextNode(split_tuple[0], TextType.IMAGE, split_tuple[1])
                split_nodes_image(split_text[1])
def split_nodes_link(old_nodes):

#def main():
#    text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
#    print(extract_markdown_images(text))
## [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
#if __name__ == "__main__":
#    main()
#

#def extract_markdown_links(text):

