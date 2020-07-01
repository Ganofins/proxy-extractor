from bs4 import BeautifulSoup

def _extract_proxies_free_proxy_list_net(html_content, https):
    """Function to extract proxies from https://free-proxy-list.net/"""
    
    proxy_list = []
    proxy = {}
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.select("#proxylisttable")[0]
    for each_tr in table.select("tr"):
        table_td = each_tr.select("td")
        if len(table_td) > 3:
            if https == True:
                if str(table_td[6].text.upper()) == "YES":
                    proxy = {
                        "ip" : table_td[0].text,
                        "port" : table_td[1].text,
                        "country" : table_td[3].text,
                        "anonymity" : table_td[4].text,
                        "https" : table_td[6].text
                    }
            else:
                proxy = {
                    "ip" : table_td[0].text,
                    "port" : table_td[1].text,
                    "country" : table_td[3].text,
                    "anonymity" : table_td[4].text,
                    "https" : table_td[6].text
                }

            proxy_list.append(proxy)
    
    return proxy_list