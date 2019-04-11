import requests
	
# html block example
"""
<div class="gallery">
	<a href="gallery/test_images/image1.jpg" class="big">
	<img src="gallery/test_images/thumbs/thumb1.jpg" alt="" title="">
	</a>
</div>
"""
# get images links from enduser
def gallery(*args):

	images_links = []

	for link in args:
		images_links.append(link)


	generated_html = render(images_links)
	return generated_html

# convert images & thumbs into html code
def render(images):
	blocks = ""
	for image in images:
		temp = """
		<div class="gallery">
			<a href="{}" class="big">
			<img src="{}" alt="{}" title="" width="300" height="300">
			</a>
		</div>
		""".format(image, image, image)
		blocks += temp
	return blocks

print(gallery(
	"""
	https://images.pexels.com/photos/457881/pexels-photo-457881.jpeg, 
	https://geographical.co.uk/media/k2/items/cache/d0d5caef53a97465ee5797663b3cd459_XL.jpg, 
	https://3ezfh222wf7f3501pa3arzc0-wpengine.netdna-ssl.com/wp-content/uploads/2017/09/lost-at-sea-island-holiday-caribbean-palm-trees-pb.jpg
	"""
))

