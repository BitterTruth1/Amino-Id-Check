import os
import asyncio
from aminofix.asyncfix import Client
from colorama import Fore
from pyfiglet import Figlet
async def logo():
	os.system("clear")
	print(Fore.LIGHTYELLOW_EX + Figlet(font="speed").renderText("Amino\nId\nCheck")+"made by @xaquake\ntelegram: https://t.me/aminoxarl\n")
async def main():
	await logo()
	while True:
		try:
			link = await Client().get_from_code(input("link: "))
			try:
				Id = link.json["extensions"]["community"]["ndcId"]
			except:
				Id = link.objectId
			with open("Ids.txt","a+") as id:
				id.write(f"{Id}\n")
			await logo()
			print(Id)
		except Exception as e:
			print(e)
asyncio.get_event_loop().run_until_complete(main())