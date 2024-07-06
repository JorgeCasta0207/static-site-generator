

import unittest
from htmlnode import LeafNode



class TestLeafNode(unittest.TestCase):


    def test_leaf_node(self):


        # Test case with tag, value, and props
        node = LeafNode("a", "Click Me!", {"href": "https://www.example.com"})
        expected_output = "<a href='https://www.example.com'>Click Me!</a>"
        print(f"Test Case 1 Output:: {node.to_html()}")  
        self.assertEqual(node.to_html(), expected_output)

       # Test case with tag, value, and empty props
        node = LeafNode("a", "Just text", {})
        expected_output = "<a>Just text</a>"
        self.assertEqual(node.to_html(), expected_output)

        # Test case with no tag and no props, but with value 
        node = LeafNode(None, "This is raw text.")
        expected_output = "This is raw text."
        self.assertEqual(node.to_html(), expected_output)
        

        # Test case with tag, value, no props
        node = LeafNode("p", "This is a paragraph.")
        expected_output = "<p>This is a paragraph.</p>"

if __name__ == "__main__":
    unittest.main()