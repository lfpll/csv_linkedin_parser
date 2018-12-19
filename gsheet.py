from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from secure_vars import SPREADSHEET_ID, SCOPES, RANGE_NAME
import itertools


def fix_url(url):
	if url.find('http') > -1:
		return url
	return 'http://' + url


def gen_list(credentials_file, sheet_id, range, scope):
	"""Shows basic usage of the Sheets API.
	Prints values from a sample spreadsheet.
	"""
	# The file token.json stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	store = file.Storage('token.json')
	creds = store.get()
	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets(credentials_file, scope)
		creds = tools.run_flow(flow, store)
	service = build('sheets', 'v4', http=creds.authorize(Http()))

	# Call the Sheets API
	sheet = service.spreadsheets()
	result = sheet.values().get(spreadsheetId=sheet_id,
	                            range=range).execute()
	values = result.get('values', [])

	if not values:
		print('No data found.')
	else:
		return values
	# Print columns A and E, which correspond to indices 0 and 4.


def return_list():
	linkedin_list = gen_list(credentials_file='./credentials.json', sheet_id=SPREADSHEET_ID, range=RANGE_NAME,
	                         scope=SCOPES)
	linkedin_list = list(filter(lambda x: x.find('linkedin') > -1, list(itertools.chain.from_iterable(linkedin_list))))
	return [fix_url(url) for url in linkedin_list]
