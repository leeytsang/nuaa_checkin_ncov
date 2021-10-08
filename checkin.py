import requests
import argparse
import time

parser = argparse.ArgumentParser(description='Auto Check In for NUAA NCOV')
parser.add_argument('-u', dest='username', action='store', default='your username',  help='your username in nuaa')
parser.add_argument('-p', dest='password', action='store', default='your password', help='your password in nuaa')
args = parser.parse_args()
if __name__ == '__main__':
    username='username='+args.username
    pwd = 'password='+args.password
    loginData =username+'&'+pwd
    HEADERS = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    req = requests.post(url="https://m.nuaa.edu.cn/uc/wap/login/check",headers=HEADERS,data=loginData)
    checkinUrl ='https://m.nuaa.edu.cn/ncov/wap/default/save';
    date_str='&date='+ time.strftime("%Y%m%d", time.localtime())
    create_str='&created='+ str(time.time())
    data_check='sfzhux=0&zhuxdz=&szgj=&szcs=&szgjcs=&sfjwfh=0&sfyjsjwfh=0&sfjcjwfh=0&sflznjcjwfh=0&sflqjkm=4&jkmys=1&sfjtgfxdq=0&nuaaxgymjzqk=1&dyzjzsj=&bfhzjyq=0&hxyxjzap=0&yjzjsj=&sftjlkjc=&lkjctlsj=&sfsylkjcss=&gjzsftjlkjc=&gjzlkjctlsj=&gjzsfsylkjcss=&ifhxjc=&hsjconetime=&hsjconeplace=&hsjconejg=&hsjctwotime=&hsjctwoplace=&hsjctwojg=&hsjcthreetime=&hsjcthreeplace=&hsjcthreejg=&hsjcfourtime=&hsjcfourplace=&hsjcfourjg=&ywchxjctime=&hsjclist=%7B%7D&njrddz=%E6%AD%A3%E5%BE%B7%E5%AD%A6%E9%99%A2&gzczxq=2&ifznqgfxljs=&iflsqgfxljs=&zrwjtw=1&jrzjtw=1&jrlvymjrq=&ifcyglq=0&wskmyy=&zhycjgdqifjn=&dqsfzgfxszqs=0&gqsfyzgfxljs=0&gqsfyqzfhryjc=0&sfyjwljqyhg=0&id=20032889&uid=236672&tw=2&sfcxtz=0&sfyyjc=0&jcjgqr=0&jcjg=&sfjcbh=0&sfcxzysx=0&qksm=&remark=&address=%E6%B1%9F%E8%8B%8F%E7%9C%81%E5%8D%97%E4%BA%AC%E5%B8%82%E6%B1%9F%E5%AE%81%E5%8C%BA%E7%A7%A3%E9%99%B5%E8%A1%97%E9%81%93%E5%8D%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6%E5%B0%86%E5%86%9B%E8%B7%AF%E6%A0%A1%E5%8C%BA%E5%92%8C%E5%9B%AD%E9%A3%9F%E5%A0%82&area=%E6%B1%9F%E8%8B%8F%E7%9C%81+%E5%8D%97%E4%BA%AC%E5%B8%82+%E6%B1%9F%E5%AE%81%E5%8C%BA&province=%E6%B1%9F%E8%8B%8F%E7%9C%81&city=%E5%8D%97%E4%BA%AC%E5%B8%82&geo_api_info=%7B%22type%22%3A%22complete%22%2C%22info%22%3A%22SUCCESS%22%2C%22status%22%3A1%2C%22dEa%22%3A%22jsonp_773302_%22%2C%22position%22%3A%7B%22Q%22%3A31.93527%2C%22R%22%3A118.79575%2C%22lng%22%3A118.79575%2C%22lat%22%3A31.93527%7D%2C%22message%22%3A%22Get+ipLocation+success.Get+address+success.%22%2C%22location_type%22%3A%22ip%22%2C%22accuracy%22%3Anull%2C%22isConverted%22%3Atrue%2C%22addressComponent%22%3A%7B%22citycode%22%3A%22025%22%2C%22adcode%22%3A%22320115%22%2C%22businessAreas%22%3A%5B%7B%22name%22%3A%22%E5%BC%80%E5%8F%91%E5%8C%BA%22%2C%22id%22%3A%22320115%22%2C%22location%22%3A%7B%22Q%22%3A31.925973%2C%22R%22%3A118.80980399999999%2C%22lng%22%3A118.809804%2C%22lat%22%3A31.925973%7D%7D%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E9%9D%99%E6%B7%AE%E8%A1%97%22%2C%22streetNumber%22%3A%2262%E5%8F%B7%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E6%B1%9F%E8%8B%8F%E7%9C%81%22%2C%22city%22%3A%22%E5%8D%97%E4%BA%AC%E5%B8%82%22%2C%22district%22%3A%22%E6%B1%9F%E5%AE%81%E5%8C%BA%22%2C%22township%22%3A%22%E7%A7%A3%E9%99%B5%E8%A1%97%E9%81%93%22%7D%2C%22formattedAddress%22%3A%22%E6%B1%9F%E8%8B%8F%E7%9C%81%E5%8D%97%E4%BA%AC%E5%B8%82%E6%B1%9F%E5%AE%81%E5%8C%BA%E7%A7%A3%E9%99%B5%E8%A1%97%E9%81%93%E5%8D%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6%E5%B0%86%E5%86%9B%E8%B7%AF%E6%A0%A1%E5%8C%BA%E5%92%8C%E5%9B%AD%E9%A3%9F%E5%A0%82%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%7D&sfzx=1&sfjcwhry=0&sfcyglq=0&gllx=&glksrq=&jcbhlx=&jcbhrq=&sftjwh=0&sftjhb=0&fxyy=%E6%8C%89%E6%97%B6%E8%BF%94%E6%A0%A1&bztcyy=5&fjsj=0&created_uid=0&sfjchbry=0&sfjcqz=&jcqzrq=&jcwhryfs=&jchbryfs=&xjzd=&sfsfbh=0&sfjcwzry=0&sftjwz=0&jhfjrq=&jhfjjtgj=&jhfjhbcc=&jhfjsftjwh=0&jhfjsftjhb=0&szsqsfybl=0&sfygtjzzfj=0&gtjzzfjsj=&sfsqhzjkk=0&sqhzjkkys=&is_fx_log=0&fxzrwjtw=&fxjrcjtw=1&fxjrzjtw=&fxsfzx=0&fxsfcyglq=0&fxsfcxtz=0&sfjzxg=0&skmcolor=1&skmimg=&ifjrglkjc=&gtjjsfhm=&gtjzsfhzl=&sffhddjjgc=&ifjgzgfxq=&jgzgfxrq=&jgzgfxdq=&jgzgfxxxdz=&newwchsjccs=&dsdecjcsj=&dsdechsjcjgtype=&dsdrchsjcdd=&dsdechsjcjg=&zhyccjcsj=&zhycchsjcjgtype=&zhycchsjcdd=&zhycchsjcjg=&gwszdd=&sfyqjzgc=&jrsfqzys=&jrsfqzfy=&ismoved=0'
    data_check = data_check + date_str + create_str
    cres = requests.post(url=checkinUrl,headers=HEADERS,data =data_check,cookies=req.cookies.get_dict())
    print(cres.text)
