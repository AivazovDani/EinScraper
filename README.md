# EinScraper

A web scraper for a government company registry website. The main challenge here was bypassing Cloudflare, since it's a government website with anti-bot protection — normal Selenium gets detected easily. We use SeleniumBase which is an improved version of Selenium built to handle exactly this.

We also don't want to get blocked, so we use proxy rotation with a random choice on each run.

---

## Libraries used

- `seleniumbase` — Cloudflare bypass + browser automation
- `beautifulsoup4` — HTML parsing
- `random` — proxy rotation + human-like wait times

---

## How the website is structured

The good thing about this website is that it's structured very well in the URL part. We can filter companies by year, month, and date directly from the URL — so we don't need to navigate multiple pages manually, we can just go straight to the page we want and scrape it.

---

## Proxy rotation

We have a list of proxies structured like this:
```
username:password@host:port
```

On each run we pick one at random using a simple function — so the website doesn't see the same IP every time.

---

## How it works — step by step

**1. Browser setup**

```python
with SB(uc=True, proxy=PROXY) as sb:
```

- `with` → when we're done, close everything automatically — otherwise we'd have to call `sb.quit()` manually
- `SB` → open a Chrome browser instance using SeleniumBase
- `uc=True` → Undetected-Chromedriver mode, makes Chrome look like a real human browser so Cloudflare doesn't block us
- `proxy=PROXY` → use a proxy IP instead of our real one so the website doesn't know it's us
- `as sb` → give this browser the nickname `sb` so we can control it in the code

**2. Open the page**

We open the URL using `activate_cdp_mode()`. Then we wait until the container we want becomes visible on the page — instead of guessing with `sb.sleep()` when it will render.

**3. Main scraping loop**

We use a `while` loop because we're checking every page of company listings. When there are no more pages, we just `except` with a print and stop.

On each page:
- Extract the HTML with `get_page_source()`
- Parse it with BeautifulSoup
- Find all listing containers using `find_all()` — searching for an `<a>` tag with a specific class

**4. Filter active companies**

For each listing we look for the company status. It's nested inside a `<div>` class, and the actual status text is inside a `<span>` tag — so we grab that element and use `.text` to extract only the text.

We check if the status is `"Active"`. If it is, we split out any unnecessary characters and combine the parts with `' '.join()` so each company becomes one clean element in our list instead of a few separate ones.

**5. Pagination**

A rookie mistake I made early on was trying to open the next page button as a URL instead of clicking it. The fix was to grab the `href` from the `<a>` tag on the "Next" button instead:

```python
next_url = "/Incorporation-Date/2019-01-01/2"
```

**6. Human-like delays**

Between each page we wait a random amount of time:

```python
random.uniform(2, 5)
```

This picks a random decimal like `3.27` or `4.81` — looks much more human than always waiting exactly 2 seconds.

---

## Output

Active companies are appended to a list, which is then imported as a function in a second script — so we can access every company by index.

---

## Smart things done here

- Using SeleniumBase with `uc=True` to bypass Cloudflare without getting blocked
- Proxy rotation on every run so the website doesn't track our IP
- Waiting for elements to appear instead of guessing load times with `sleep()`
- Random delays between pages to mimic human behaviour
- Grabbing the "Next" button `href` instead of trying to construct the URL manually

The main challenge was finding the SeleniumBase library and learning how it operates — once that clicked, the rest wasn't that complex.
