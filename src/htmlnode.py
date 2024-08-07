
class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = {} if children is None else children
        self.props = {} if props is None else props

    

    def to_html(self):
        return NotImplementedError
    
    
    # Returns string that represents HTML attributes
    def props_to_html(self):
        html_attributes = ""
        for key, value in self.props.items():
            html_attributes += f' {key}="{value}"'
        return html_attributes
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):

        super().__init__(tag, value)
        self.props = props or {}

    # Turns LeafNode into HTML representation
    def to_html(self):

        html_attributes = ""


        if self.value is None:
            raise ValueError("Value Required In LeafNode")
        

        if self.tag is None:
            return self.value
        

        if self.props:
            for key, value in self.props.items():
                html_attributes += f" {key}='{value}'"
    

        if html_attributes: 
            return f"<{self.tag}{html_attributes}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        




class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):

        if not children:
            raise ValueError("Children required for ParentNode")
        
        super().__init__(tag, children)
        self.props = props or {}

    # Turns ParentNode into HTML representation
    def to_html(self):

        if not self.tag:
            raise ValueError("Tag not provided")
        
        if not self.children:
            raise ValueError("Children not provided")
        

        html_representation = ""

        for child in self.children:
            child_html = child.to_html()
            html_representation +=  child_html

        if html_representation:
            return f"<{self.tag}>{html_representation}</{self.tag}>"


        


            


        

        




        