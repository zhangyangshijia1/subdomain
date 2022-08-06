
import requests

  # 扫描子域的功能

def domain_scanner(domain_name,sub_domnames):

    print('----正在扫描子域字典,显示扫描子域后的URL----')
    
    print('----博客：www.smallhao.com----')


    for subdomain in sub_domnames:
        url = f"https://{subdomain}.{domain_name}"

        try:
            requests.get(url)
            print(f'[+] {url}')

        except requests.ConnectionError:

            pass

  # main function

if __name__ == '__main__':

    dom_name = input("请输入你需要查询的域名:")

    with open('subnames_big.txt','r') as file:

        name = file.read()

        sub_dom = name.splitlines()

    domain_scanner(dom_name,sub_dom)
