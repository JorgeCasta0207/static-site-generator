


class TextNode:

    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    #Checking other is an instance of TextNode, if it is comparing it to self and other
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url 
        )
    
    # Representing the TextNode
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    