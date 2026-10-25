"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet


def build_feed():
    # Create your accounts and posts, then call their methods.
    # Return the two lists: return users, posts
    User1 = User("JeffTheGreat")
    User2 = User("JohnDaGoat")
    Tweet1 = Tweet("JeffTheGreat", "I love #Halloween")
    Tweet2 = Tweet("JeffTheGreat", "Pumkin pie is Great")
    Tweet3 = Tweet("JohnDaGoat", "Chocolate is the best candy")
    User1.follow()
    User2.follow()
    User2.unfollow()
    Tweet1.like()
    Tweet2.like()
    Tweet3.like()
    Tweet1.unlike()
    return [User1, User2], [Tweet1,Tweet2, Tweet3]


def main():
    # Call build_feed and display the returned objects and hashtags.
    users, posts = build_feed()
    for user in users:
        print(users)
        
    for post in posts:
        print(post)
        print(post.hashtags())
        
   



if __name__ == '__main__':
    main()
