import bs4 as bs
import urllib.request

#class="yt-simple-endpoint style-scope ytd-mini-channel-renderer"

"""
    <ytd-mini-channel-renderer class="style-scope ytd-vertical-channel-section-renderer">
    
    <a id="channel-info" class="yt-simple-endpoint style-scope ytd-mini-channel-renderer" href="/user/Studiounplugged">
      <yt-img-shadow height="24" width="24" class="style-scope ytd-mini-channel-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="" height="24" width="24" src="https://yt3.ggpht.com/a-/AAuE7mCO7MgOsZ2r9OtM7zZIG06RUdQBnmifLqI5CQ=s88-mo-c-c0xffffffff-rj-k-no"></yt-img-shadow>
      <span class="title style-scope ytd-mini-channel-renderer">Being Indian Music</span>
    </a>

    <div id="subscribe" class="style-scope ytd-mini-channel-renderer"><ytd-subscribe-button-renderer class="style-scope ytd-mini-channel-renderer" button-style="COMPACT_GRAY">
    
    <paper-button noink="" class="style-scope ytd-subscribe-button-renderer" role="button" tabindex="0" animated="" aria-disabled="false" elevation="0" aria-label="Subscribe to Being Indian Music.">
      <yt-formatted-string class="style-scope ytd-subscribe-button-renderer">Subscribe</yt-formatted-string>
    </paper-button>
    <div id="notification-preference-toggle-button" class="style-scope ytd-subscribe-button-renderer" hidden=""></div>
  </ytd-subscribe-button-renderer></div>
  </ytd-mini-channel-renderer>
  """

 #['ux-thumb-wrap', 'yt-uix-sessionlink', 'spf-link']


"""
channellink =[]

for a in soup.find_all('a'):
	a=dict(a.attrs)
	if "class" in a:
		if a["class"] == ['ux-thumb-wrap', 'yt-uix-sessionlink', 'spf-link']:
			channellink.append(a["href"])

print(channellink)

['yt-uix-sessionlink', 'yt-uix-tile-link', 'spf-link']
"""

#<span class="title style-scope ytd-mini-channel-renderer">Being Indian Music</span>




def channellist(link):
	source = urllib.request.urlopen(link).read()
	
	soup = bs.BeautifulSoup(source,'lxml')
	
	channel=[]
	
	channelname=[]	
	
	for a in soup.find_all('a'):	
	
		attrs= dict(a.attrs)
	
		if "class" in attrs:
	
			if attrs['class']==['yt-uix-sessionlink', 'yt-uix-tile-link', 'spf-link']:
	
				channel.append("https://www.youtube.com"+attrs['href'])
	
				channelname.append(attrs['title'])

	return zip(channel,channelname)

#"https://www.youtube.com/user/EminemMusic"

def bfs(link,iter=1):

	dictionary={}
	
	dictionary[link]='start'
	
	qu=[link]
	count=0
	rejected=0

	for i in range(iter):

		second=[]

		for l in qu:

			channel = channellist(l)

			for a,b in channel:
				if a not in dictionary:
					dictionary[a]=b
					second.append(a)
					count=count+1
				else:
					rejected=rejected+1

		qu=second

	
	print("no of "+str(count))
	print("no of "+str(rejected))


	return dictionary

dictionary=bfs("https://www.youtube.com/user/EminemMusic",2)

for key,value in dictionary.items():
	print(key+"  "+value)













