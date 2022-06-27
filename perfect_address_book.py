from collections import UserDict
from datetime import datetime
from datetime import date
from itertools import islice
import pickle
import os
import re

class WrongName(Exception):
	"""
	Raised when the name is not valid
	"""
	pass

class BirthdayIncorrect(Exception):
	"""
	Raised when the birthday is not valid
	"""
	pass


class Record:
	def __init__(self, name, phone=None, birthday=None, email=None):
		self.name = name
		self.phones_archive = []
		self.birthday = birthday
		self.emails_archive = []

		if phone:
			self.add_phone(phone)

		if email:
			self.add_email(email)

	def check_phone(self, phone) -> bool:
		if str(phone) in self.phones_archive:
			return True
		return False

	def add_phone(self, phone) -> bool:
		if not self.check_phone(phone):
			self.phones_archive.append(str(phone))
			return True
		return False

	def update_phone(self, phone, new_phone) -> bool:
		if self.check_phone(phone):
			self.delete_phone(phone)
			self.add_phone(new_phone.value)
			return True
		raise ValueError

	def delete_phone(self, phone) -> bool:
		if self.check_phone(phone):
			self.phones_archive.remove(str(phone))
			return True
		return False

	def check_email(self, email) -> bool:
		if str(email) in self.emails_archive:
			return True
		return False

	def add_email(self, email) -> bool:
		if not self.check_email(email):
			self.emails_archive.append(str(email))
			return True
		return False

	def update_email(self, email, new_email) -> bool:
		if self.check_email(email):
			self.delete_email(email)
			self.add_email(new_email.value)
			return True
		raise ValueError

	def delete_email(self, email) -> bool:
		if self.check_email(email):
			self.emails_archive.remove(str(email))
			return True
		return False

	def append_email(self, email):
		if not self.check_email(email):
			self.emails_archive.append(str(email))
			return True

	def check_birthday(self, birthday) -> bool:
		if str(birthday) in self.birthday:
			return True
		return False

	def add_birthday(self, birthday) -> bool:
		if not self.check_birthday(birthday):
			self.birthday = birthday
			return True
		return False

	def __repr__(self):
		return f'{self.name}, {self.phones_archive if self.phones_archive else "No phones"}, ' \
		       f'{self.birthday if self.birthday else "No birthday"}, ' \
		       f'{self.emails_archive if self.emails_archive else "No emails"}'



class Field:
	def __init__(self, value) -> None:
		self.__value = None
		self.value = value


class Name(Field):

	def __repr__(self):
		return self.value

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, value):
		if value.strip() != '':
			self.__value = value
		else:
			raise WrongName


class Phone(Field):

	def __repr__(self):
		return f'{self.__value}'

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, n_value):
		n_value = n_value.strip()
		for ch in n_value:
			if ch not in "0123456789()-+":
				raise ValueError('Phone must be a valid phone number')
		self.__value = n_value


class EMail(Field):
	def __repr__(self):
		return self.value

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, n_value):
		n_value = n_value.strip()
		if not re.match(r'^[a-z0-9_\-\.]+@[a-z0-9_\-\.]+\.[a-z]+$', n_value):
			raise ValueError('Email must be a valid email')
		self.__value = n_value


class Birthday(Field):
	def __repr__(self):
		return self.value

	def __str__(self):
		return self.value

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, b_value):
		if b_value:
			try:
				datetime.strptime(b_value, "%d.%m.%Y")
			except ValueError:
				raise BirthdayIncorrect
		else:
			self.__value = None
		self.__value = b_value


class AddressBook(UserDict):

	def add_record(self, record: Record):
		self.data[record.name.value] = record

	def __next__(self):
		return next(self.iterator())

	def iterator(self, n=2):
		start, page = 0, n
		while True:
			yield dict(islice(self.data.items(), start, n))
			start, n = n, n + page
			if start >= len(self.data):
				break
			gate = input('Нажмите ENTER, чтобы показать следующие...\n')


address_book = AddressBook()

f_name = 'contacts_data.bin'


...


def add_contact(*args):
	name = Name(args[0][0])
	phone = Phone(args[0][1])
	record = Record(name, phone)
	address_book.add_record(record)
	print(f'Контакт {name.value} добавлен в адресную книгу.')


def update_number(*args):
	if address_book:
		name = Name(args[0][0])
		if name.value in address_book:
			address_book[name.value].update_phone(Phone(args[0][1]), Phone(args[0][2]))
			print(f'Номер телефона контакта {name.value} обновлён.')
			print(f'Контакт {name.value} обновлён.')
		else:
			print(f'Контакт {name.value} не найден.')
	else:
		print('Телефонная книга пуста.')


def append_number(*args):
	if address_book:
		name = Name(args[0][0])
		if name.value in address_book:
			address_book[name.value].add_phone(Phone(args[0][1]))
			print(f'Контакт {name.value} обновлён.')
		else:
			print(f'Контакт {name.value} не найден.')
	else:
		print('Телефонная книга пуста.')


def delete_phone_number(*args):
	if address_book:
		name = Name(args[0][0])
		if name.value in address_book:
			address_book[name.value].delete_phone(Phone(args[0][1]))
			print(f'Контакт {name.value} обновлён.')
		else:
			print(f'Контакт {name.value} не найден.')
	else:
		print('Телефонная книга пуста.')


def delete_contact(*args):
	if address_book:
		name = Name(args[0][0])
		if name.value in address_book:
			del address_book[name.value]
			print(f'Контакт {name.value} удалён.')
		else:
			print(f'Контакт {name.value} не найден.')
	else:
		print('Телефонная книга пуста.')


def show_all(*args):
	print('--- Просмотр записей ---')
	if address_book:
		how_much_recs = input('Нажмите "ENTER" чтобы вывести все записи.'
		                      '\nИли введите сколько записей нужно отобразить: \n>>>>')
		if how_much_recs == '':
			how_much_recs = 10000
		for rec in address_book.iterator(int(how_much_recs)):
			while True:
				for name, value in rec.items():
					print(f'Контакт -- {name};\nТелефон(ы): {value.phones};')
				break
	else:
		print("Телефонная книга пуста!")


def search_command(*args) -> None:
	if address_book:
		print('--- Поиск контакта ---')
		search = input('Enter the part of name, number or email: ')
		for name, data in address_book.items():
			if re.search(search, name):
				print(f'Найдено в записи "{name}":')
				print(f'Телефоны контакта: {data.phones}')
				print(f'Адреса электронной почты контакта: {data.email}')

			for number in data.phones:
				if re.search(search, number):
					print(f'Найдено в записи "{name}":')
					print(f'Телефоны контакта: {data.phones}')
					print(f'Адреса электронной почты контакта: {data.email}')

			for email in data.email:
				if re.search(search, email):
					print(f'Найдено в записи "{name}":')
					print(f'Телефоны контакта: {data.phones}')
					print(f'Адреса электронной почты контакта: {data.email}')
					break

		print(f'--- Поиск завершен ---')

	else:
		print('Телефонная книга пуста')


def add_email(*args):
	if address_book:
		name = Name(args[0][0])
		if name.value in address_book:
			address_book[name.value].add_email(EMail(args[0][1]))
			print(f'Контакту {name.value} присвоен email {args[0][1]}.')
		else:
			print(f'Контакт {name.value} не найден.')
	else:
		print('Телефонная книга пуста')


def update_email(*args):
	if address_book:
		name = Name(args[0][0])
		if name.value in address_book:
			address_book[name.value].update_email(EMail(args[0][1]), EMail(args[0][2]))
			print(f'Контакту {name.value} присвоен email {args[0][1]}.')
		else:
			print(f'Контакт {name.value} не найден.')


def append_email(*args):
	if address_book:
		name = Name(args[0][0])
		if name.value in address_book:
			address_book[name.value].add_email(EMail(args[0][1]))
			print(f'Контакту {name.value} добавлен email {args[0][1]}.')
		else:
			print(f'Контакт {name.value} не найден.')


def delete_email(*args):
	if address_book:
		name = Name(args[0][0])
		if name.value in address_book:
			address_book[name.value].delete_email(EMail(args[0][1]))
			print(f'Контакту {name.value} удален email {args[0][1]}.')
		else:
			print(f'Контакт {name.value} не найден.')
	else:
		print('Телефонная книга пуста')


def add_birthday(*args):
	if address_book:
		name = Name(args[0][0])
		if name.value in address_book:
			address_book[name.value].add_birthday(Birthday(args[0][1]))
			print(f'Контакту {name.value} присвоен день рождения {args[0][1]}.')
		else:
			print(f'Контакт {name.value} не найден.')
	else:
		print('Телефонная книга пуста')

def near_bd(*args):
	pass


...


def goodbye(*args) -> None:
	print('До свидания!')
	exit()


def help_command(*args) -> None:
	print(
		'---\n'
		'Доступные команды:\n'
		'add contact <name> - добавить запись\n'
		'show all - просмотреть все записи\n'
		'show near bd - просмотреть количество дней до дня рождения контакта\n'
		'update <name> <old number> <new number> - обновить номер телефона\n'
		'append <name> <new number> - добавить номер телефона\n'
		'delete number <name> <number> - удалить запись\n'
		'здравствуйте, привет, hello, hi - приветствие\n'
		'delete contact <name> - удалить контакт\n'
		'find - поиск записи\n'
		'clear, cls - очистить экран\n'
		'help - помощь\n'
		'exit, выход, quit, q  - выход\n---')


def greetings(*args) -> None:
	clear_screen()
	print('---\nДобро пожаловать в контактную книгу!\nЧем я могу помочь?')


def clear_screen(*args):
	os.system('cls' if os.name == 'nt' else 'clear')


def command_unknown(*args) -> None:
	print('Команда не найдена. Попробуйте ещё раз.')


...


def command_parser(command: str) -> None:
	for func, call in main_commands.items():
		for word in call:
			if command.startswith(word):
				arguments = command.replace(word, '').split()
				func(arguments)
				return None
			continue
	else:
		command_unknown()


main_commands = {
	add_contact: ['add contact'],
	update_number: ['update number'],
	append_number: ['append number'],
	delete_phone_number: ['delete number'],
	add_email: ['add email'],
	update_email: ['update email'],
	append_email: ['append email'],
	delete_email: ['delete email'],
	delete_contact: ['delete contact'],
	show_all: ['show all'],
	near_bd: ['show near bd'],
	search_command: ['find', 'search'],
	help_command: ['help', 'помощь'],
	goodbye: ['exit', 'выход', 'quit', 'q'],
	greetings: ['здравствуйте', 'привет', 'hello', 'hi'],
	clear_screen: ['clear', 'cls']
}



def main():
	greetings()
	try:
		with open(f_name, 'rb') as f:
			address_book.data = pickle.load(f)
	except FileNotFoundError:
		print(f'Файл {f_name} не найден! Cоздаю новый...')
	finally:
		with open(f_name, 'wb') as f:
			pickle.dump(address_book.data, f)
	while True:
		print(address_book['Martisha'].email)
		for name, data in address_book.items():
			print(data)
		command = input('Введите "hello" или "help":\n>>>> ')
		command_parser(command.strip())
		with open(f_name, 'wb') as f:
			pickle.dump(address_book.data, f)


if __name__ == '__main__':
	main()