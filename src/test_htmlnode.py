
import unittest
from htmlnode import HTMLNode





class TestHTMLNode(unittest.TestCase):


    # Checking if props_to_html method works by giving us props in HTML format
    def test_props_to_html(self):
        node = HTMLNode("div", "Hello World", [], {"id": "my-div"})
        generated_node = node.Props_To_HTML()
        expected_props = ' id="my-div"'
        self.assertEqual(generated_node, expected_props)






if __name__ == "__main__":
    unittest.main()
