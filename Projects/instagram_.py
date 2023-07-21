# pip install instabot
from instabot import Bot
bot=Bot()
bot.login(username="avinash_1558",password="8286585455")
# bot.follow("rohitsharma10093")
# bot.unfollow("rohitsharma10093")
# bot.upload_photo("url")
# bot.send_messages("hi","rohitsharma10093")
# bot.send_messages("hi",["rohitsharma10093",""])
follower=bot.get_user_followers("avinash_1558")
# follower=bot.get_user_following("avinash_1558")
for f in follower:
    print(bot.get_user_info(f))
print("hey")