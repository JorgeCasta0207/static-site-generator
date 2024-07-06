

import unittest
from htmlnode import LeafNode



class TestLeafNode(unittest.TestCase):


    def test_leaf_node(self):

       
        node = LeafNode("a", "Just text", {})
        expected_output = "<a>Just text</a>"
        self.assertEqual(node.to_html(), expected_output)

        node = LeafNode(None, "This is raw text.")
        expected_output = "This is raw text."
        self.assertEqual(node.to_html(), expected_output)
        
        node = LeafNode("p", "This is a paragraph.")
        expected_output = "<p>This is a paragraph.</p>"

if __name__ == "__main__":
    unittest.main()