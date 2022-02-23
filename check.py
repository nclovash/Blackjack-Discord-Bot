def check(msg):
	return msg.author == ctx.author and msg.channel == ctx.channel and \
    msg.content.lower() in ["h", "s", "n"]