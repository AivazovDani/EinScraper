from bs4 import BeautifulSoup
from pyairtable import Api
from seleniumbase import SB
import random



# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-encoding': 'gzip, deflate, br, zstd',
#     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,bg;q=0.7',
#     'cache-control': 'max-age=0',
#     'cookie': 'route=1764496756.177.34.806353|1ca372b33d2bad9524c20eaf607b64ca; _ga=GA1.1.1825842709.1764147692; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22207300fc-be69-4310-88f8-2a170e3629e6%5C%22%2C%5B1764147692%2C104000000%5D%5D%22%5D%5D%5D; _ax_token=JGM06qQmvM.z2y2adAv5K3KjUJ; _gcl_au=1.1.922352133.1764147693; _ga=GA1.3.1825842709.1764147692; axeptio_all_vendors=facebook_pixel%2Ccloudflare%2CCloudFlare%2Cvimeo%2Cgoogle_analytics%2Ceffinity%2Coptomaton_ug%2Csojern%2Cspotad%2Cmediamath%2Cwidespace%2Cadsense%2Cgetquanty%2CGetQuanty%2Coct8ne%2Csnapengage%2Cfastbase%2Cshiny_stat; axeptio_authorized_vendors=facebook_pixel%2Ccloudflare%2CCloudFlare%2Cvimeo%2Cgoogle_analytics%2Ceffinity%2Coptomaton_ug%2Csojern%2Cspotad%2Cmediamath%2Cwidespace%2Cadsense%2Cgetquanty%2CGetQuanty%2Coct8ne%2Csnapengage%2Cfastbase%2Cshiny_stat; cluid=DB347A09-C2ED-04F5-D743-B539A05F7019; _jsuid=2441425787; __gpi=UID=000012ceb713ca78:T=1764147693:RT=1764155541:S=ALNI_MbhA5t0cb1aSYRZcYiOE-Eu4hLQyw; _k_cty_lang=en_BG; ROUTEID=.; timezoneoffset=-120; timezonename=Europe/Sofia; route=1764496757.838.34.948976|1ca372b33d2bad9524c20eaf607b64ca; _gid=GA1.3.1712152202.1764496757; JSESSIONID=1F7AA743D70C7DD0632CD5714E1BD22F; eqy_sessionid=0c066946faa68638bf09c636cb1021e1; __gads=ID=6958b18ac1b2df11:T=1764147693:RT=1764499217:S=ALNI_MYSp9w-vBcM-ggtvKZgkyePuF1EPQ; __eoi=ID=31a7c3527b279356:T=1764147693:RT=1764499217:S=AA-AfjaH6ldECUBWVdseYAeKtfY-; _ga_3XPJBXM25M=GS2.3.s1764498740$o5$g1$t1764499220$j55$l0$h0; _ga_F7YPZ3JHHR=GS2.3.s1764498741$o4$g1$t1764499220$j55$l0$h0; kp_uuid=9a94deec-9295-4466-8e21-e6217fedaa1d; _fbp=fb.1.1764499225803.290367230983073659; datadome=NfQNhJ9MPT6fu1BrnDDM8et8jvh5KmXcQSYs327dq0WRWNyiVzYq2vkw~VLYPEIuXicXnkh1_AXEKd1~l49swpys4eKxRmoFMxgi7Illu79gjiqNynQv1hCjzynhCaji; axeptio_cookies=%7B%22%24%24token%22%3A%22JGM06qQmvM.z2y2adAv5K3KjUJ%22%2C%22%24%24date%22%3A%222025-11-30T10%3A43%3A27.182Z%22%2C%22%24%24cookiesVersion%22%3A%7B%22name%22%3A%22en%22%2C%22identifier%22%3A%2266f42241ea82808f5cae18a6%22%7D%2C%22%24%24scope%22%3A%22persistent%22%2C%22%24%24duration%22%3A190%2C%22%24%24completed%22%3Atrue%2C%22facebook_pixel%22%3Atrue%2C%22cloudflare%22%3Atrue%2C%22CloudFlare%22%3Atrue%2C%22vimeo%22%3Atrue%2C%22google_analytics%22%3Atrue%2C%22effinity%22%3Atrue%2C%22optomaton_ug%22%3Atrue%2C%22sojern%22%3Atrue%2C%22spotad%22%3Atrue%2C%22mediamath%22%3Atrue%2C%22widespace%22%3Atrue%2C%22adsense%22%3Atrue%2C%22getquanty%22%3Atrue%2C%22GetQuanty%22%3Atrue%2C%22oct8ne%22%3Atrue%2C%22snapengage%22%3Atrue%2C%22fastbase%22%3Atrue%2C%22shiny_stat%22%3Atrue%7D; _ga_H9RY6SXL1H=GS2.1.s1764498689$o6$g1$t1764499407$j60$l0$h0; _ga_6C5YNEXRW2=GS2.1.s1764498689$o6$g1$t1764499407$j60$l0$h0; _ga_YFM4S8XBVP=GS2.1.s1764498689$o6$g1$t1764499407$j60$l0$h1829434547',
#     'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1'
# }

def scrape(PROXY, FORM_URL_ORIGIN):

    AIRTABLE_API = 'YOUR_API_KEY'
    AIRTABLE_BASE_ID = "appRupVoBVAzn0bMw"
    AIRTABLE_TABLE_NAME = 'Entities'

    api = Api(AIRTABLE_API)
    table = api.table(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME)

    FORM_URL = 'https://search.sunbiz.org/Inquiry/CorporationSearch/ByName'
    info_address = {}
    info_ein = {}
    info_name = {}

    with SB(uc=True, proxy=PROXY) as sb:    
        sb.activate_cdp_mode(FORM_URL_ORIGIN)
        sb.wait_for_element('a.company-list-link', timeout=30)
        result = []

        while True:
            html_content = sb.get_page_source()
            soup = BeautifulSoup(html_content, 'html.parser')

            listings = soup.find_all('a', class_="company-list-link w-inline-block")

            for listing in listings:
                company_status = listing.find(class_='company-list-status')
                is_active = company_status.find('span').text

                if is_active == "Active":
                    company_name = ' '.join(listing.find(class_='company-list-heading').text.split())
                    result.append(company_name)

            try:
                next_url = sb.get_attribute('a.next.page-btn', 'href')
                sb.open(next_url)
                sb.sleep(random.uniform(3, 5))
            except:
                print("No more pages")
                print(result)
                break

        sb.sleep(random.uniform(3, 5))
        sb.open(FORM_URL)
        sb.wait_for_element('div.editor-field', timeout=15)
        company_list = result

        for company in company_list:
            company_name = company

            sb.sleep(random.uniform(1, 3))
            sb.type("#SearchTerm", company)
            sb.sleep(random.uniform(1, 3))
            sb.click('input[value="Search Now"]')
            sb.sleep(random.uniform(4, 5))

            sb.click('a[title="Go to Detail Screen"]')
            # tag - > attribute
            sb.sleep(5)

            status = sb.find_element('.detailSection.filingInformation label[for="Detail_Status"] + span').text


            if status == "ACTIVE":
                ein = sb.find_element('label[for="Detail_FeiEinNumber"] + span').text
                    
                address = ""

                all_spans = sb.find_elements(".detailSection span")
      
                for i, span in enumerate(all_spans):
                    if span.text.strip() == "Principal Address":
                        address = all_spans[i + 1].text.strip()
                        print(address)
                        sb.sleep(random.uniform(1, 3))
                        sb.go_back()
                        sb.sleep(random.uniform(1, 3))
                        sb.go_back()
                        break

                info_address["Address"] = address.strip()
                info_ein["EIN/VAT"] = ein
                info_name["Name"] = company_name

                table.create({
                    "Address": info_address["Address"],
                    "EIN/VAT": info_ein["EIN/VAT"],
                    "Name": info_name["Name"]
                })

def main():
    FORM_URL_ORIGIN = 'https://www.flcompanyregistry.com/Incorporation-Date/2019-01-01/'

    PROXIES = [
        # list of proxies
    ]

    PROXY = random.choice(PROXIES)

    scrape(PROXY, FORM_URL_ORIGIN)

if __name__ == "__main__":
    main()



    






