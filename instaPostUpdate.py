# pip install instabot

# To upload instagram post using Python

# import instabot
from instabot import Bot

# creating an instance for Bot()
mybot = Bot()

# login to upload the post
username = input("Enter your instagram username: ").strip()
user_password = input("Enter your password: ")

mybot.login(username = username, password = user_password)

image = input("Enter the name of the image you want to upload(with extension[.jpg or .jpeg]): ")
if not '.jpg' or '.jpeg' in image:
    image = image + '.jpg'

caption = input("enter the caption: ")
mybot.upload_photo(image, caption = caption)


