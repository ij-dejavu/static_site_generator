class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag=tag
        self.value=value
        if children is not None:
            self.children=children
        else:
            self.children=[]
        if props is not None:
            self.props=props
        else:
            self.props={}

    def to_html(self):
        raise NotImplementedError("Not implemented yet!")
    
    def props_to_html(self):
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result 
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Must have a value")
        if self.tag is None:
            return self.value
        prop_string=self.props_to_html()
        return f"<{self.tag}{prop_string}>{self.value}</{self.tag}>"