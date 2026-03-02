# EinScraper

For the specific use case, we will need to bypass Cloudflare, cause we’re scraping a government website. Our normal selenium won’t work, cause it’s easily detected. We’ll use a Selenium-based tool, which is an improved version. We don’t want to be bloked so that’s why we’ll use proxy rotation on a random choice. First, we’ll import the libraries (in our case, 3 - BS4, SB, and random). Then we’ll need our URL as a constant. The good thing about this website is that it is structured very well in the URL part. We can filter companies by year, month, and date. So we don’t need to navigate multiple pages; we can just go to the page with companies and scrape that one. Then we have our list with proxies, the proxies are structured this way: username:password@host:port. Then we want to rotate them on each run, so we create a random function that gets a proxy at random from our list. The idea is to scrape active companies and append them to a list, then import that list as a function in my second script so I can access every company by index. First, we need to initialise our setup so we can open the browser. We’ll use the formula, where it’s important to pass the uc=True (Undetected-Chromedriver = True). This is a specialized browser automation setting designed to bypass anti-bot detection systems like Cloudflare, Imperva, and DataDome.  Then pass our Proxy as well.

with SB(uc=True, proxy=PROXY) as sb:

with → When we're done, close everything automatically; otherwise, we need to close it manually with sb.quit()
SB → open a Chrome browser instance using SeleniumBase
uc=True → make Chrome look like a real human browser so Cloudflare doesn't block us
proxy=PROXY → use this IP address instead of your real one so the website doesn't know it's you
as sb → give this browser the nickname sb so we can control it later in the code
Then we need to open our URL with the command activate_cdp_mode(). Then we wait till the container we want becomes visible on the page, otherwise we need to guesswork with sb.sleep() when it will render. Then the main logic is to create a while loop, cause we’ll be checking every page with company lists, and after there are no pages left, we jsut except with a print. First, we need to parse our HTML. So we need to extract it first with get_page_source(). Then we need to parse it with BeautifulSoup.
Then we need to find all the containers where the info we want is using the structured now HTML and find_all(). We search for an <a> tag and a class inside.
Then we loop through every listing and search for the company status. The company status is nested inside a <div> class, and the status we want is inside an element with a <span> tag, so we take the element and add .text to extract only the text.
Then we check if the company status is “Active”. If it’s active, we need to split any unnecessary characters. Then we recieve numer of string element and we need to combine them with a ‘ ’.join(). So it can be one element in our list, instead of a few separate ones. Then the only thing that was kinda a rookie mistake from me was that I was trying to open the button on the bottom of the page as a URL instead of clicking it. Then Claude told me to use the arrow and get the href link from the <a> tag. Find the "Next" button on the page and grab its link, save it as next_url
Example: next_url = "/Incorporation-Date/2019-01-01/2"
Wait a random amount of time between 2 and 5 seconds before doing anything else
random.uniform(2, 5) picks a random decimal number like 3.27 or 4.81 — looks more human than always waiting exactly 2 seconds!
That’s it, not that complex, but there are a few smart things we done. The main issue was to find that seleniumbase library and to learn how it operates

