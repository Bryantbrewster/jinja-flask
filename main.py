from flask import Flask, render_template
from post import Post
import requests

# creating the Flask app
app = Flask(__name__)


# creates an empty list that will eventually be appended with the blog post objects
blog_data_list = []
# getting the api data (where each element contains  id, title, subtitle, and body data)
api_url = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(url=api_url)
json_blog_data = response.json()
# loops through the json data (each iteration being a different post), and creates an object that assigns the
# id, title, subtitle, and body data so that it can be called with someone like post.title
for blog_post in json_blog_data:
    blog = Post(
        post_id=blog_post["id"],
        post_title=blog_post["title"],
        post_subtitle=blog_post["subtitle"],
        post_body=blog_post["body"]
    )
    # appends the objects (blog posts) to the empty list for later use
    blog_data_list.append(blog)


# the home page, which renders the index.html template, and passes in the blog_data_list (all the posts as objects)
# so that the index.html file can use that data
@app.route('/')
def home():
    return render_template("index.html", blogs=blog_data_list)

# the get_blog function & its decorator are invoked when someone clicks on the "Read" hyperlink on the
# index page. Whatever the id was on the post that was clicked on is passed in as clicked_post_id in the URL and
# function. The function creates an empty "chosen_post" which will later be filled with the data of the correct
# post (the post the user is trying to read). Then a for loop iterates through the blog_data_list containing the objects
# of all the post data. It checks the id vs. the id of the post that the user clicked on until the finds the right one.
# Once the IDs match and the correct post's data is found, it assigns that iteration's data to the chosen_post variable.
# Then the render_template is invoked to send the user to the post.html file, with the chosen_post data passed in so
# that the correct posts data will be displayed on the next page.
@app.route('/post/<int:clicked_post_id>')
def get_blog(clicked_post_id):
    chosen_post = None
    for i in blog_data_list:
        if i.id == clicked_post_id:
            chosen_post = i
    return render_template("post.html", post=chosen_post)



if __name__ == "__main__":
    app.run(debug=True)
