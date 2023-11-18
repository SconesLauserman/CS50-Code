import requests
import sys
from ast import literal_eval as string_to_dict_converter


try:
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    coindesk_API_response = requests.get(url)
    response_as_dict = string_to_dict_converter(coindesk_API_response.text)
    current_price = response_as_dict["bpi"]["USD"]["rate"]
    print("$" + "{:,}".format(float(current_price.replace(",", "")) * float(sys.argv[1])))
except Exception:
    sys.exit(1)
