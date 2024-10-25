import unittest


# Example Phonebook class implementation (for reference)
class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if name in self.contacts:
            raise ValueError("Contact already exists")
        self.contacts[name] = phone

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            raise ValueError("Contact does not exist")

    def search_contact(self, name):
        if name in self.contacts:
            return {name: self.contacts[name]}
        else:
            raise ValueError("Contact not found")

    def update_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
        else:
            raise ValueError("Contact not found")

    def list_contacts(self):
        return self.contacts


# Unit tests for the Phonebook class
class TestPhonebook(unittest.TestCase):

    def setUp(self):
        """Set up a new Phonebook instance before each test."""
        self.phonebook = Phonebook()

    def test_add_contact(self):
        """Test adding a contact to the phonebook."""
        self.phonebook.add_contact("Alice", "123456789")
        self.assertIn("Alice", self.phonebook.contacts)
        self.assertEqual(self.phonebook.contacts["Alice"], "123456789")

    def test_add_duplicate_contact(self):
        """Test adding a duplicate contact raises an error."""
        self.phonebook.add_contact("Bob", "987654321")
        with self.assertRaises(ValueError):
            self.phonebook.add_contact("Bob", "111222333")

    def test_delete_contact(self):
        """Test deleting a contact from the phonebook."""
        self.phonebook.add_contact("Charlie", "555666777")
        self.phonebook.delete_contact("Charlie")
        self.assertNotIn("Charlie", self.phonebook.contacts)

    def test_delete_non_existent_contact(self):
        """Test deleting a contact that does not exist raises an error."""
        with self.assertRaises(ValueError):
            self.phonebook.delete_contact("NonExistent")

    def test_search_contact(self):
        """Test searching for a contact in the phonebook."""
        self.phonebook.add_contact("David", "111222333")
        result = self.phonebook.search_contact("David")
        self.assertEqual(result, {"David": "111222333"})

    def test_search_non_existent_contact(self):
        """Test searching for a non-existent contact raises an error."""
        with self.assertRaises(ValueError):
            self.phonebook.search_contact("Unknown")

    def test_update_contact(self):
        """Test updating an existing contact's phone number."""
        self.phonebook.add_contact("Eve", "444555666")
        self.phonebook.update_contact("Eve", "777888999")
        self.assertEqual(self.phonebook.contacts["Eve"], "777888999")

    def test_update_non_existent_contact(self):
        """Test updating a non-existent contact raises an error."""
        with self.assertRaises(ValueError):
            self.phonebook.update_contact("Ghost", "000111222")

    def test_list_contacts(self):
        """Test listing all contacts in the phonebook."""
        self.phonebook.add_contact("Alice", "123456789")
        self.phonebook.add_contact("Bob", "987654321")
        contacts = self.phonebook.list_contacts()
        self.assertEqual(contacts, {"Alice": "123456789", "Bob": "987654321"})


# Run the tests
if __name__ == "__main__":
    unittest.main()
