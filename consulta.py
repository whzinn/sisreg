from requests import post

fim = '''
</table></center>
</body>
'''

comeco = '''
<style>
    body {
            overflow-x:hidden;
            margin: 50px;
            padding: 50px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
            color: #333;
            font-size: 50px;
            text-align: center;
            background-color: #f8f9fa;
        }
        header {
            padding: 10px;
            height: 91px;
            margin: 0 0 32px;
            background-color: #00005f;
            color: #fff;
        }
        table {
            max-width: 860px;
            width: 92%;
            border-collapse: collapse;
            line-height: 20px;
            margin: 0 auto 48px;
            table-layout: fixed;
        }
        td {
            padding: 20px;
            vertical-align: top;
            border: 1px solid #EEE;
            font-size: 14px;
            background-color: #fff;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }
        .title {
            padding: 16px 0;
            font-size: 20px;
            font-weight: bold;
            background-color: #faf7eb;
            text-align: center;
        }
        .td_titulo_tabela {
            padding: 12px 0;
            font-weight: bold;
            background-color: #2f7bea;
            text-align: center;
            font-size: 19px;
            color:#ffffff;
            border-top-left-radius:5px;
            border-top-right-radius: 5px;
        }
        .td_titulo_campo {
            padding: 12px 0;
            font-weight: bold;
            background-color: #2f7bea;
            text-align: center;
            font-size: 19px;
            color:#ffffff;
            border-top-left-radius:5px;
            border-top-right-radius: 5px;
        .subtitle {
            padding: 12px 0;
            font-weight: bold;
            background-color: #2f7bea;
            text-align: center;
            font-size: 19px;
            color:#ffffff;
            border-top-left-radius:5px;
            border-top-right-radius: 5px;
        }
        .key {
            font-size: 140%;
            width: 240px;
            font-weight: bold;
        }
        header {
            height: 91px;
            margin: 0 0 32px;
            background-color:#2f7bea;
            color: #fff;
        .logo{
            border-radius: 100px;
        }
        .dado{
            font-size:150%;
            width: 240px;
        }
</style>

<body>
<center><table width='50%' class='table_listagem'>
'''

headers = {
    "Host": "sisregiii.saude.gov.br",
    "Connection": "keep-alive",
    "Content-Length": "206",
    "Cache-Control": "max-age=0",
    "sec-ch-ua": '''"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"''',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '''"Android"''',
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://sisregiii.saude.gov.br",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://sisregiii.saude.gov.br/cgi-bin/cadweb50?standalone=1",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

data = "nu_cns=01204341133&nome_paciente=&nome_mae=&dt_nascimento=&uf_nasc=&mun_nasc=&uf_res=&mun_res=&sexo=&etapa=DETALHAR&url=&standalone=1"

url = "https://sisregiii.saude.gov.br/cgi-bin/cadweb50?standalone=1"

def consulta(cpf):
    data = f"nu_cns={cpf}&nome_paciente=&nome_mae=&dt_nascimento=&uf_nasc=&mun_nasc=&uf_res=&mun_res=&sexo=&etapa=DETALHAR&url=&standalone=1"
    c = open("cookie.txt")
    cookie = c.read()
    c.close()
    headers["Cookie"]=cookie
    d = post(url,data=data,headers=headers).text
    s2 = "</table></center>"
    s1 = "<center><table width='75%' class='table_listagem'>"
    d = d.split(s2)[0]
    d = d.split(s1)[1]
    d = comeco + d
    d = d + fim
    return d
