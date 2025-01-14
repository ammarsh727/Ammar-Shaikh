import unittest
import os
import sys
import json

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from collection_manager import CollectionManager, Perfume

class TestCollectionManager(unittest.TestCase):
    def setUp(self):
        self.manager = CollectionManager()
        self.test_perfume = Perfume("Test Perfume", "Test Brand", "Floral", 50.0)
        # Clear any existing data
        if os.path.exists('perfumes.json'):
            os.remove('perfumes.json')

    def tearDown(self):
        # Clean up after tests
        if os.path.exists('perfumes.json'):
            os.remove('perfumes.json')

    # Existing tests
    def test_add_perfume(self):
        initial_count = len(self.manager.collection)
        self.manager.add_perfume(self.test_perfume)
        self.assertEqual(len(self.manager.collection), initial_count + 1)
        self.assertEqual(self.manager.collection[0]['name'], "Test Perfume")

    def test_edit_perfume(self):
        self.manager.add_perfume(self.test_perfume)
        self.manager.edit_perfume(0, name="Updated Perfume")
        self.assertEqual(self.manager.collection[0]['name'], "Updated Perfume")

    def test_delete_perfume(self):
        self.manager.add_perfume(self.test_perfume)
        initial_count = len(self.manager.collection)
        self.manager.delete_perfume(0)
        self.assertEqual(len(self.manager.collection), initial_count - 1)

    def test_view_perfumes(self):
        self.manager.add_perfume(self.test_perfume)
        collection = self.manager.view_perfumes()
        self.assertEqual(len(collection), 1)
        self.assertEqual(collection[0]['name'], "Test Perfume")

    # Integration Tests
    def test_data_persistence(self):
        """Test that data is correctly saved to and loaded from JSON file"""
        self.manager.add_perfume(self.test_perfume)
        
        # Create new manager instance to test loading
        new_manager = CollectionManager()
        self.assertEqual(len(new_manager.collection), 1)
        self.assertEqual(new_manager.collection[0]['name'], "Test Perfume")

    # File I/O Tests
    def test_file_operations(self):
        """Test file handling with non-existent file"""
        if os.path.exists('perfumes.json'):
            os.remove('perfumes.json')
        new_manager = CollectionManager()
        self.assertEqual(len(new_manager.collection), 0)

    # Empty Collection Tests
    def test_empty_collection_view(self):
        """Test viewing an empty collection"""
        collection = self.manager.view_perfumes()
        self.assertEqual(len(collection), 0)

    def test_empty_collection_delete(self):
        """Test deleting from an empty collection"""
        initial_count = len(self.manager.collection)
        self.manager.delete_perfume(0)
        self.assertEqual(len(self.manager.collection), initial_count)

    def test_empty_collection_edit(self):
        """Test editing in an empty collection"""
        initial_collection = self.manager.view_perfumes()
        self.manager.edit_perfume(0, name="New Name")
        after_collection = self.manager.view_perfumes()
        self.assertEqual(initial_collection, after_collection)

    # Index Out of Range Tests
    def test_invalid_index_edit(self):
        """Test editing with invalid index"""
        self.manager.add_perfume(self.test_perfume)
        original_name = self.manager.collection[0]['name']
        self.manager.edit_perfume(99, name="Should Not Update")
        self.assertEqual(self.manager.collection[0]['name'], original_name)

    def test_invalid_index_delete(self):
        """Test deleting with invalid index"""
        self.manager.add_perfume(self.test_perfume)
        initial_count = len(self.manager.collection)
        self.manager.delete_perfume(99)
        self.assertEqual(len(self.manager.collection), initial_count)

if __name__ == '__main__':
    unittest.main()
