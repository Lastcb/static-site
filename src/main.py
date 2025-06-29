from textnode import TextNode, TextType

def main():
    dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(dummy)
    print(TextType.TEXT)
    
if __name__ == "__main__":
    main()
