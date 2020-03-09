from unittest import TestCase
from unittest.mock import patch, Mock

# In our test, we want to mock out the unpredictable API call and 
# only test that a Blog object’s posts method returns posts. 
# We will need to patch all Blog objects’ posts methods as follows.
class TestBlog(TestCase):
    @patch('main.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable  end  of the  western  spiral  arm  of  the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
        
        # Additional assertions
        #assert MockBlog is main.Blog # The mock is equivalent to the original

        # The mock was called
        #assert MockBlog.called

        # We called the posts method with no arguments
        #blog.posts.assert_called_with() 

        # We called the posts method once with no arguments
        #blog.posts.assert_called_once_with() 

        # This assertion is False and will fail 
        # since we called blog.posts with no arguments
        # blog.posts.assert_called_with(1, 2, 3)

        # Reset the mock object
        #blog.reset_mock() 

        # After resetting, posts has not been called.
        #blog.posts.assert_not_called() 