from requests_html import HTMLSession

s = HTMLSession()

q = True
while q:
    query = input('What city are you inquiring about: ')
    url = f'https://www.google.com/search?q=weather+in+{query}&sca_esv=2aa9b945258dbd75&rlz=1C5CHFA_enCA911CA911&sxsrf=ACQVn09gsCDYBuVpbn9HOAYbAQC3KUgRnA%3A1708737843773&ei=M0XZZeneLu6bptQP34S42AI&ved=0ahUKEwipxMTB6MKEAxXujYkEHV8CDisQ4dUDCBA&uact=5&oq=weather+in+toronto&gs_lp=Egxnd3Mtd2l6LXNlcnAiEndlYXRoZXIgaW4gdG9yb250bzIWEAAYgAQYigUYkQIYsQMYgwEYRhiAAjIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIiEAAYgAQYigUYkQIYsQMYgwEYRhiAAhiXBRiMBRjdBNgBAUiE4wdQtsMHWLDfB3AEeAGQAQGYAfcBoAGGE6oBBTUuOS40uAEDyAEA-AEBmAIVoAK8E8ICChAAGEcY1gQYsAPCAgoQIxiABBiKBRgnwgIEECMYJ8ICChAAGIAEGIoFGEPCAhAQABiABBiKBRhDGLEDGIMBwgINEAAYgAQYigUYQxixA8ICExAAGIAEGIoFGEMYsQMYgwEYyQPCAgsQABiABBixAxiDAcICDhAAGIAEGLEDGIMBGJIDwgIWEC4YgAQYFBiHAhixAxiDARjHARjRA8ICEBAAGIAEGBQYhwIYsQMYgwHCAhEQABiABBiKBRiRAhixAxiDAcICDhAAGIAEGIoFGJECGLEDwgIIEAAYgAQYsQOYAwCIBgGQBgi6BgYIARABGBOSBwU4LjkuNA&sclient=gws-wiz-serp'

    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})
    temperature = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    time = r.html.find('div.wob_dts, span.wob_dts ', first=True).text

    answer = f'The Temperature is: {temperature} {unit} This {time} in {query}'
    print(answer)

    print('\n')
    choice = input('Enter Y or y to continue, or N or n to stop: ')
    if choice.lower() == 'y':
        q = True
    elif choice.lower() == 'n':
        q = False
    else:
        print("Invalid Input!!")
