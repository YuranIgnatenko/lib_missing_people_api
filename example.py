
def main() -> None:
	def test_sledkom():
		parser = ParserSledcom()
		ar1 = parser.get_array_people(DICT_URLS_SLEDCOM["БЕЗ ВЕСТИ"])
		for people in ar1:
			print("GET ARRAY PEOPLE",people.date_create, people.url_image, people.description)

	def test_mvd():
		parser = ParserMvd()
		ar1 = parser.get_array_people(URL_SITE_MVD)
		for people in ar1:
			print("GET ARRAY PEOPLE",people.date_create, people.url_image, people.description)

	def test_liza_alert():
		parser = ParserLizaAlert()
		ar1 = parser.get_array_people(URL_SITE_LIZAALERT)
		for people in ar1:
			print("GET ARRAY PEOPLE",people.date_create, people.url_image, people.description)

	test_sledkom()
	test_mvd()
	test_liza_alert()

if __name__ == "__main__":
	main()