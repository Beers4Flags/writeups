#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Xiomara's CTF 2017 - The Shopkeeper Quizz - Misc/Programming 200 PTS
#Write Up : Berurier - Beer4Flags

#Gaben is love, Gaben is life. Who doesn't love DoTA. Well, one of our admins loves dota so much that he decided to write a challenge based on the game. 
#Prove your might, and maybe we will get convinced you are just another n00b. Quick hands, brain, and skills recommended.
#nc 139.59.61.220 6666	

#So this challenge is about finding stuff about items in dota2 ^^

#I'm trying to improve my python and parsing skill, this isn't the best way to solve this challenge. 
#Dont mind the shitty variable names !

#OK THERE MIGHT A BIT TOO MUCH IMPORTS
#that's because I took a script I made for basis : a wiki parser for the cryptoquizz from Insomni'hack Teaser 2017.
import sys,os
import struct
import asyncio
import json, pprint, re, datetime
import mwparserfromhell
import requests, socket
import urllib

#Ok in this function, we're sending the Name of the Item
def nametoprice (name) :
	#Ok, so my last price was using a wiki parser, i've got the idea to take the price information from dota2.gamepedia.com
	#It's a mediawiki designed to share all the knowledge about this game.
	#The regular Item Page wasn't obvious enough to parse, so...
	#Let's use a Special Page, easier to Parse, to find the price of an item "Special : Browse" 
	url = "http://dota2.gamepedia.com/Special:Browse/"+name
	#Don't forget to put an User-Agent, or you'll get a 403 ERROR
	req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	#Let's get the content of this page !
	con = urllib.request.urlopen( req )
	#Let's use the mwparserfromhell to put it on string format. 
	#This is a library designed to get information from mediawiki... 
	#But I don't think I used it at full potential.
	code = mwparserfromhell.parse(con)
	
	if 'Item cost' in code :
	#OK THIS IS THE DIRTY PARSING TIME, If you're not friendly with regex !
	#I'm splitting the data I want by using what i know that is Before and Behind the data i'm looking for.
		code2 = code.split('Item cost')
		code3 = code2[1].split('smwb-value')
		code4 = code3[1].split('&')
		code5 = code4[0][2::]
		code5 = code5.replace(',','')
	else :
	#If there is no price, we return the value 0.
		code5 = '0'
	#After few test, i've got errors for 2 Items, that I hardcoded.. BUT HARDCODING IS BAD M'KAY !
	if 'Flying_Courier' in name : code5 = '150'
	#The Tango(Shared) Was tricky because, there isn't any price data in dota2.gamepedia.com 
	#I've found it on another price after looking for it for a long time
	if 'Tango_(Shared)' in name : code5 = '30'
	code5 += '\n'
	return(code5)

#In this function we're getting the Recipe price for each items, a different price asked in the quizz.
#It wasn't really clear on the regular page to spot the difference between the item cost and the recipe price of an item.
# That's where our Special:Browse page is useful.
def recipetoprice (name) :
	url = "http://dota2.gamepedia.com/Special:Browse/"+name
	req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	con = urllib.request.urlopen( req )
	code = mwparserfromhell.parse(con)
	if 'Recipe cost' in code :
		code2 = code.split('Recipe cost')
		code3 = code2[1].split('smwb-value')
		code4 = code3[1].split('&')
		code5 = code4[0][2::]
		code5 = code5.replace(',','')
	else :
	# There was a lot of recipes for items that didn't cost anything, so there wasn't any recipe cost
	#But the quizz was asking for them anyway, so we put a 0 price ^^
		code5 = '0'
	code5 += '\n'
	return(code5)

# After 240 Iteration, the challenge changed, after asking for a price, it asked for the "internal name"
# After some researches, i've found that it was the name of the item variable in the game.
# This function isn't very effective, because splitting with the Item name can give you fake results.
def internaltoprice(cheat,Zboub) :
	code2 = cheat.split(Zboub)
	# And because I was lazy, i've looked for the last item name ommission in the page.
	code3 = code2[-1]
	code3 = code3.split("<code>")
	code4 = code3[1]
	code4 = code4.split("</code>")
	return(code4[0])

#So in this function, we're taking the name that we received in the Socket
#And we're translate into Item_Name form to be added to the item link.
def rec_to_name1 (zboub) :
	#zbib=zboub[69::]
	zbib=str(zboub)
	zbib=zbib[2::]
	zbib=zbib.split(' ?')
	zbib=zbib[0]
	zbib=zbib.replace('Recipe: ','')
	zbib=zbib.replace(' ','_')
	print(zbib)
	return zbib

if __name__ == '__main__':

	url = "http://dota2.gamepedia.com/Cheats"
	req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	con = urllib.request.urlopen( req )
	cheatpage = mwparserfromhell.parse(con)
	#In order to increase the speed time of this script, we're making only one request for the internal name.
	
	#we're connect to the socket
	s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	s.connect( ( '139.59.61.220', 6666) )
	
	#let's receive our first message
	zboub = s.recv(100)
	zboub = zboub[69::]
	#Calling the name geting function
	zbib = rec_to_name1(zboub)
	#If it's a recipe, call the recipe to price func... ok you get it
	if "Recipe" in str(zboub) :
		zbab = recipetoprice(zbib)
	else :
		zbab=nametoprice(zbib)
	print(zbab)
	s.send(zbab.encode())
	# I made a big iteration, but after 480 right answers you've got the flag :p
	for i in range(1000)	 :
		print(i)
		zboub2 = s.recv(110)
		print(zboub2)
		zboub2 = str(zboub2)
		
		# Ok, i should have made another loop for the internal name 
		if "internal" in zboub2 : 
			zboub2 = zboub2.split('name o')
			zbib = rec_to_name1(zboub2[1])
			
			# Ok, I WAS BORED BY DISCOVERING I ALSO NEEDED TO RETURN THE INTERNAL NAME AFTER 240 GOOD PRICES =X 
			# so i hardcoded all the item names i wasn't getting right with my parser instead of improving it :p
			
			if 'Electrified' in zbib : zbib = zbib.replace('Electrified','Electric')
			zbab=internaltoprice(cheatpage, zbib)
			if "Shiva" in zbib : zbab="item_shivas_guard"
			if "Tango" in zbib : 
				if "Shared" not in zbib : zbab="item_tango"
			if "Sange" in zbib :
				if "Yasha" not in zbib : zbab="item_sange"
			if "Animal_Courier" in zbib : zbab = "item_courier"
			if "Sage's_Mask" in zbib : zbab = "item_sobi_mask"
			if "Aghanim's_Scepter" in zbib : zbab = "item_ultimate_scepter"
			if "Eul's_Scepter_of_Divinity" in zbib : zbab = "item_cyclone"
			if "Heaven's_Halberd" in zbib : zbab = "item_heavens_halberd"
			if "Linken's_Sphere" in zbib : zbab = "item_sphere"
			if "Poor_Man's_Shield" in zbib : zbab = "item_poor_mans_shield"
			if "Vladmir's_Offering" in zbib : zbab="item_vladmir"
			if "Arcane_Boots" in zbib : zbab ="item_arcane_boots"
			if "Diffusal_Blade" in zbib : zbab = "item_diffusal_blade"
			if "Dagon" in zbib : zbab = "item_dagon"
			if "Flying_Courier" in zbib : zbab = "item_flying_courier"
			if "Clarity" in zbib : zbab = "item_clarity"
			if "Observer_Ward" in zbib : zbab = "item_ward_observer"
			if "Sentry_Ward" in zbib : 
				if "Observer" not in zbib : zbab = "item_ward_sentry"
			if "Boots_of_Travel" in zbib : zbab = "item_travel_boots"
			if "Necronomicon" in zbib : zbab = "item_necronomicon"
			if "Desolator" in zbib : zbab = "item_desolator"
			if "Recipe" in zboub2[1] : zbab = zbab[:5]+'recipe_'+zbab[5:]
			zbab += '\n'
		else :		
			# So if the quiz wanted the item / recipe price ! let's call the function
			zboub2 = zboub2.split('cost o')
			zbib = rec_to_name1(zboub2[1])
			if "Recipe" in zboub2[1] :
				zbab = recipetoprice(zbib)
			else :
				# Also, there was an error in the gamepedia about an item name not the same with the bot
				# It wasn't the author of this challenge fault, he was directly taking his data from the Dota2 API.
				# That's what I should have done in the beginning :D 
				# But i didn't thought they were available and thought the API was only about multiplayer
				if 'Electrified' in zbib : zbib = zbib.replace('Electrified','Electric')
				zbab=nametoprice(zbib)
		print(zbab)
		s.send(zbab.encode())
		
		
