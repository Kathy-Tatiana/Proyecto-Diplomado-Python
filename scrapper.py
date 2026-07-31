import requests as rq
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pprint import pprint

ruta_raiz = "https://www.plusvalia.com/venta/casas"

urls_ciudad = [
    "pichincha/quito",
    "guayas/guayaquil",
    "manabi/manta",
    "tungurahua/banos-de-agua-santa"
]
city = urls_ciudad[0]

# request = rq.get(f"{ruta_raiz}/{city}")

# if request.status_code == 200:
#     html = request.text
#     soup = BeautifulSoup(html, "lxml")
#     pprint(soup.prettify())
# else:
#     pass

options = Options()
options.add_experimental_option(
    "detach",
    True
)

driver = webdriver.Chrome(options=options)
driver.get(
    f"{ruta_raiz}/{city}"
    f"{ruta_raiz}/{city}"
)

tag_properties = driver.find_elements(
    By.CSS_SELECTOR,
    'div.postingsList-module__postings-container > div.postingsList-module__card-container > data-qa *= ["PROPERTY"]'
)

for pro in tag_properties:
    
    tag_price = pro.find_elements