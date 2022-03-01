import discord
import random
from random import choice
from discord.ext import commands
from create_deck import *
from check import *
from eval import *
from symbol_repl import *

client = commands.Bot(command_prefix = '~')

@client.event
async def on_ready():
	print('Bot is ready')

@client.command()
async def shutdown(ctx):
	await ctx.bot.logout()

@client.command()
async def blackjack(ctx):
	sendStr = ""
	again = 'y'
	yourHand = ''
	dealerHand = ''
	pushes = 0
	blackjacks = 0

	deck = create_deck()

	random.shuffle(deck)

	#print("Shuffled deck: ", deck)
	#print('first item: ' + deck[0])

	dealer_hand = []
	player1_hand = []

	#Deals out first two cards to player and dealer
	cardnum = 0
	player1_hand += [symbol_repl(deck[cardnum])]
	cardnum += 1
	dealer_hand += [symbol_repl(deck[cardnum])]
	cardnum += 1
	player1_hand += [symbol_repl(deck[cardnum])]
	cardnum += 1
	dealer_hand += [symbol_repl(deck[cardnum])]
	cardnum += 1

	#Gives value to hands
	p1_value = eval(player1_hand)
	d_value = eval(dealer_hand)

	yourHand = 'Your cards: ' + ' '.join(player1_hand) + ' Value: ' + str(p1_value)
	sendStr += yourHand
	dealerHand = 'Dealer cards: ?? ' + ' '.join(dealer_hand[0]) + 'Value: ???'
	sendStr += "\n" + dealerHand

	choice = ''

	while(p1_value <= 21):

		p1_value = eval(player1_hand)

		#Checks for blackjack
		if(p1_value == 21):
			sendStr += "\nYou have blackjack!"
			await ctx.send(sendStr)
			blackjacks+=1 #May remove
			break

		#Hitting
		else:
			sendStr += "\nHit or Stand? (h/s): "
			await ctx.send(sendStr)

			#Waits for user to hit or stand
			print('Flag 1') #remove
			msg = await client.wait_for("message", check=check)
			print('Flag 2') #remove
			if(msg.content.lower() == 'h'):
				player1_hand += [symbol_repl(deck[cardnum])]
				cardnum += 1
				p1_value = eval(player1_hand)
				yourHand = 'Your cards: ' + ' '.join(player1_hand) + ' Value: ' + str(p1_value)
				await ctx.send(yourHand)


			#Standing
			elif(msg.content.lower() == 's'):
				p1_value = eval(player1_hand)
				break

	#If you bust
	else:
		await ctx.send(f'\nBust!')
		dealerHand = 'Dealer cards: ' + ' '.join(dealer_hand) + 'Value: ', str(d_value)
		await ctx.send(dealerHand)

	#Dealer Rough Bot
	hits = 0
	while(d_value < 17):
		dealer_hand += [symbol_repl(deck[cardnum])]
		cardnum +=1
		d_value = eval(dealer_hand)
		await ctx.send(f'\n*Dealer hits*')
		hits+=1
		dealerHand = 'Dealer cards: ' + ' '.join(dealer_hand) + 'Value: ', str(d_value)
		await ctx.send(dealerHand)

	else:
		if(hits==0):
			dealerHand = 'Dealer cards: ' + ' '.join(dealer_hand) + 'Value: ', str(d_value)
			await ctx.send(dealerHand)

	if(d_value == 21):
		await ctx.send(f'Dealer has blackjack!')
		blackjacks += 1

	if(p1_value == 21):
		await ctx.send(f'Player 1 has blackjack!')
		blackjacks += 1

	#Checks to see who wins or loses
	if((d_value <= 21) and (d_value > p1_value) or (p1_value > 21)):
		await ctx.send(f'\nDealer wins.')

	elif((p1_value <= 21) and (p1_value > d_value) or (d_value > 21)):
		yourHand = 'Your cards: ' + ' '.join(player1_hand) + ' Value: ' + str(p1_value)
		await ctx.send(yourHand)
		await ctx.send(f'\nPlayer wins.')

	else:
		yourHand = 'Your cards: ' + ' '.join(player1_hand) + ' Value: ' + str(p1_value)
		await ctx.send(yourHand)
		dealerHand = 'Dealer cards: ' + ' '.join(dealer_hand) + 'Value: ', str(d_value)
		await ctx.send(dealerHand)
		await ctx.send(f'\nPush')

client.run('Token Goes Here')
