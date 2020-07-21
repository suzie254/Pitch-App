
 
from app.models import Comment
from app import db
import unittest

class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Pitch class
    '''
    def setUp(self):
        self.user_clin = User(username = 'clin',password = '121212', email = 'clin@gmail.com')
        self.new_comment = Comment(pitch_id=12345,pitch_title='Review pitching',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='working',user = self.user_James ) 

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_id,12345)
        self.assertEquals(self.new_comment.pitch_title,'Review for pitching')
        self.assertEquals(self.new_comment.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_comment.pitch_comment,'working')
        self.assertEquals(self.new_comment.user,self.user_James) 

    def test_save_comment(self): 
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)
        
if __name__ == '__main__':
    unittest.main()