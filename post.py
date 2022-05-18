# creating the Post class so that when we use the api GET request we are take that JSON data and
# create an object, using the Post class, and assign the id, title, subtitle, and body
# by creating a class and assigning all that at the start, it will only need to do it once for each user
# and not have to call the api every single time someone clicks on one of the blogs

class Post:
    def __init__(self, post_id, post_title, post_subtitle, post_body):
        self.id = post_id
        self.title = post_title
        self.subtitle = post_subtitle
        self.body = post_body



