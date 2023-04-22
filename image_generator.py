from PIL import Image, ImageDraw, ImageFont
from image_utils import ImageText
import textwrap
import imghdr
import io
import tweepy
import time
import nouns
import random
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)

auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

def function_that_tweets():
	num_nouns = len(nouns.Noun_list)

	main_font = 'Futura_Book.ttf'

	meme = Image.open('vault.png')

	gun_text = nouns.Noun_list[random.randrange(num_nouns)]

	gun_text_wrapped = "\n".join(textwrap.wrap(gun_text, width = 30))

	line_count = gun_text_wrapped.count('\n')

	gun_font_size = 22
	gun_text_point = (100,580)

	if not(line_count):
		gun_font_size = 24
		gun_text_point = (105, 600)

	rectangle_image = Image.new('RGBA', meme.size, (0,0,0,0))

	rectangle_draw_buffer = ImageDraw.Draw(rectangle_image, 'RGBA')

	rectangle_draw_buffer.text(gun_text_point, gun_text_wrapped, font = ImageFont.truetype(main_font, gun_font_size), align = "center")

	bullet_text = nouns.Noun_list[random.randrange(num_nouns)]

	bullet_text_wrapped = "\n".join(textwrap.wrap(bullet_text, width = 25))

	line_count = bullet_text_wrapped.count('\n')

	bullet_font_size = 22
	bullet_text_point = (265,435)

	if not(line_count):
		bullet_font_size = 24
		bullet_text_point = (270, 450)

	rectangle_image_2 = Image.new('RGBA', meme.size, (0,0,0,0))

	rectangle_draw_buffer_2 = ImageDraw.Draw(rectangle_image_2, 'RGBA')


	rectangle_draw_buffer_2.text(bullet_text_point, bullet_text_wrapped, font = ImageFont.truetype(main_font, bullet_font_size), align = "center")

	rectangle_image_2 = rectangle_image_2.rotate(45)


	meme = Image.alpha_composite(meme, rectangle_image)
	meme = Image.alpha_composite(meme, rectangle_image_2)

	tweet = '{} can miss me with that {} shit'.format(gun_text, bullet_text)

	def convertToPNG(im):
	   with BytesIO() as f:
	      im.save(f, format='PNG')
	      return f.getvalue()

	meme.save('tweet.png', 'PNG')

	api.update_with_media(filename = 'tweet.png', status = tweet)

while(True):
	function_that_tweets()
	time.sleep(random.randrange(15500, 43200))