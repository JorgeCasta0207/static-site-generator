
class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = {} if children is None else children
        self.props = {} if props is None else props

    

    def To_HTML(self):
        return NotImplementedError
    
    
    # Returns string that represents HTML attributes
    def Props_To_HTML(self):
        html_attributes = ""
        for key, value in self.props.items():
            html_attributes += f' {key}="{value}"'
        return html_attributes
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"