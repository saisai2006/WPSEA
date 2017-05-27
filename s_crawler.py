import requests
import time
import ctypes
#import sys
from bs4 import BeautifulSoup

def train_spider():
    #print(sys.executable)
    read_input_link_file_path = "C:\\Users\\family\\PycharmProjects\\SProject\\inputLink.tab"
    read_input_link_file = open(read_input_link_file_path, 'r')
    url = str(read_input_link_file.readline())
    read_input_link_file.close()
    url = url.replace('ÿþ', '')
    url = url.strip()
    source_code = requests.get(url)
    #ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "FIRST STOP", 1)
    if source_code.status_code != 200:
        ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "Status Code ERROR", 1)
        exit()
    #else:
    #    ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "Status Code SUCCESS", 1)

    plain_text = source_code.text
    #soup = BeautifulSoup(source_code.content, "html.parser")
    soup = BeautifulSoup(plain_text, "html.parser")
    spans_H4 = soup.find_all('h4')
    testCounter = 0
    ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "Status Code SUCCESS", 1)
    for spanH4 in spans_H4:
        #if str(spanH4.get_text()).count("price") > 0:
        ctypes.windll.user32.MessageBoxW(0, source_code.status_code, spanH4.get_text() + " ", 1)
        if spanH4.get_text() == "\n":
            ctypes.windll.user32.MessageBoxW(0, source_code.status_code, " GET CHILD? ", 1)
            for child in spanH4.children:
                ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "child " + child.get_text(), 1)
        # testCounter = testCounter + 1
        # if testCounter > 10:
        #     exit()
    exit()
    spans_redSalePrice = soup.find_all('h4', {'class' : 'redSalePrice'})
    spans_productPriceBig = soup.find_all('li', {'class': 'product-price-big'})
    spans_HotBuy = soup.find_all('span', {'class': 'span22 offset1'})
    spans_Shipping = soup.find_all('div', {'class': 'product-fulfillment-max-ships-for'})
    spans_Shipping2ND = soup.find_all('span', {'class': 'free'})
    #spans_PriceWrapper = soup.find_all('span', {'class': 'price-wrapper'})
    redSalePrice = ""
    productPriceBig = ""
    #priceWrapper = ""
    count_redSale = 0
    count_productPrice = 0
    #count_priceWrapper = 0
    text_file_path = "C:\\Users\\family\\PycharmProjects\\SProject\\redSalePrice.txt"
    #pagesourcenotfound_path = "C:\\Users\\family\\PycharmProjects\\SProject\\notFound.txt"
    hotBuy = ""
    shippingType = ""
    for spanShip in spans_Shipping:
        shippingType = shippingType + spanShip.get_text()
        shippingType = shippingType.replace("\t", "")
        shippingType = " ".join(shippingType.split())
        shippingType = shippingType.strip()
    for spanShip2ND in spans_Shipping2ND:
        shippingType = shippingType + spanShip2ND.get_text()
        shippingType = shippingType.replace("\t", "")
        shippingType = " ".join(shippingType.split())
        shippingType = shippingType.strip()
    #ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "shippingType " + shippingType, 1)
    if shippingType == "":
        shippingType = "N/A"
    for spanhotBuy in spans_HotBuy:
        hotBuy = hotBuy + spanhotBuy.get_text()
        hotBuy = hotBuy.replace("\t", "")
        hotBuy = hotBuy.strip()
    #ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "hotBuy " + hotBuy, 1)
    if hotBuy == "":
        hotBuy = "N/A"
    #for spanpricewrapper in spans_PriceWrapper:
    #    priceWrapper = priceWrapper + spanpricewrapper.get_text()
    #    priceWrapper = priceWrapper.strip()
    #    count_priceWrapper += 1
    #    ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "spanpricewrapper found! " + priceWrapper, 1)
    for spanproductprice in spans_productPriceBig:
        productPriceBig = productPriceBig + spanproductprice.get_text()
        productPriceBig = productPriceBig.strip()
        count_productPrice += 1
        ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "spanproductpriceBig found! " + productPriceBig, 1)
    productPriceBig = productPriceBig #+ priceWrapper
    for spanredSale in spans_redSalePrice:
        redSalePrice = redSalePrice + spanredSale.get_text()
        redSalePrice = redSalePrice.strip()
        count_redSale += 1
        ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "spanredSale found! " + redSalePrice, 1)
    text_file = open(text_file_path, 'w')
    text_file.write("redPrice\tbuyType\tshippingInfo\tproductPriceBig\n")
    text_file.write(redSalePrice + "\t" + hotBuy + "\t" + shippingType + "\t" + productPriceBig)
    text_file.close()
    #if count_redSale == 1:
    #    text_file = open(text_file_path, 'w')
    #    text_file.write("redPrice\tbuyType\tshippingInfo\tproductPriceBig\n")
    #    text_file.write(redSalePrice + "\t" + hotBuy + "\t" + shippingType + "\t" + productPriceBig)
    #    text_file.close()
    #    ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "Price found!", 1)
    #elif count_redSale == 0:
    #    text_file = open(text_file_path, 'w')
    #    text_file.write("redPrice\tbuyType\tshippingInfo\tproductPriceBig\n")
    #    text_file.write("0"  + "\t" + hotBuy + "\t" + shippingType + "\t" + productPriceBig)
    #    text_file.close()
    #    print(plain_text)
        #print(plain_text, pagesourcenotfound_path)
        #ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "not found! " + str(plain_text), 1)
        #text_file2 = open(pagesourcenotfound_path, 'w')
        #text_file2.write(plain_text)
        #text_file2.close()
    #    ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "Price NOT found!", 1)
    #elif count_redSale > 1:
    #    text_file = open(text_file_path, 'w')
    #    text_file.write("redPrice\tbuyType\tshippingInfo\tproductPriceBig\n")
    #    text_file.write("1"  + "\t" + hotBuy + "\t" + shippingType + "\t" + productPriceBig)
    #    text_file.close()
    #    ctypes.windll.user32.MessageBoxW(0, source_code.status_code, "Multiple price found!  " + str(count_redSale), 1)
    source_code.close()

train_spider()