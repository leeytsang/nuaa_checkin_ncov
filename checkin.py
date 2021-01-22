import requests
import argparse

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
    data_check='sfzhux=0&zhuxdz=&szgj=&szcs=&szgjcs=&sfjwfh=0&sfyjsjwfh=0&sfjcjwfh=0&sflznjcjwfh=0&sflqjkm=4&jkmys=1&sfjtgfxdq=0&tw=2&sfcxtz=0&sfjcbh=0&sfcxzysx=0&qksm=&sfyyjc=0&jcjgqr=0&remark=&address=%E6%B1%9F%E8%A5%BF%E7%9C%81%E5%90%89%E5%AE%89%E5%B8%82%E5%90%89%E6%B0%B4%E5%8E%BF%E6%96%87%E5%B3%B0%E9%95%87%E6%96%87%E5%8C%96%E4%B8%9C%E8%B7%AF%E9%98%B3%E6%98%8E%E5%9B%AD%E5%B0%8F%E5%8C%BA&geo_api_info=%7B%22type%22%3A%22complete%22%2C%22info%22%3A%22SUCCESS%22%2C%22status%22%3A1%2C%22%24Da%22%3A%22jsonp_695315_%22%2C%22position%22%3A%7B%22Q%22%3A27.21339%2C%22R%22%3A115.14263%2C%22lng%22%3A115.14263%2C%22lat%22%3A27.21339%7D%2C%22message%22%3A%22Get+ipLocation+success.Get+address+success.%22%2C%22location_type%22%3A%22ip%22%2C%22accuracy%22%3Anull%2C%22isConverted%22%3Atrue%2C%22addressComponent%22%3A%7B%22citycode%22%3A%220796%22%2C%22adcode%22%3A%22360822%22%2C%22businessAreas%22%3A%5B%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E6%96%87%E5%8C%96%E4%B8%9C%E8%B7%AF%22%2C%22streetNumber%22%3A%2256%E5%8F%B7%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E6%B1%9F%E8%A5%BF%E7%9C%81%22%2C%22city%22%3A%22%E5%90%89%E5%AE%89%E5%B8%82%22%2C%22district%22%3A%22%E5%90%89%E6%B0%B4%E5%8E%BF%22%2C%22township%22%3A%22%E6%96%87%E5%B3%B0%E9%95%87%22%7D%2C%22formattedAddress%22%3A%22%E6%B1%9F%E8%A5%BF%E7%9C%81%E5%90%89%E5%AE%89%E5%B8%82%E5%90%89%E6%B0%B4%E5%8E%BF%E6%96%87%E5%B3%B0%E9%95%87%E6%96%87%E5%8C%96%E4%B8%9C%E8%B7%AF%E9%98%B3%E6%98%8E%E5%9B%AD%E5%B0%8F%E5%8C%BA%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%7D&area=%E6%B1%9F%E8%A5%BF%E7%9C%81+%E5%90%89%E5%AE%89%E5%B8%82+%E5%90%89%E6%B0%B4%E5%8E%BF&province=%E6%B1%9F%E8%A5%BF%E7%9C%81&city=%E5%90%89%E5%AE%89%E5%B8%82&sfzx=0&sfjcwhry=0&sfjchbry=0&sfcyglq=0&gllx=&glksrq=&jcbhlx=&jcbhrq=&bztcyy=4&sftjhb=0&sftjwh=0&sftjwz=0&sfjcwzry=0&jcjg=&created_uid=0&date=20210122&uid=236672&created=1611280207&jcqzrq=&sfjcqz=&szsqsfybl=0&sfsqhzjkk=0&sqhzjkkys=&sfygtjzzfj=0&gtjzzfjsj=&id=13602299&gwszdd=&sfyqjzgc=&jrsfqzys=&jrsfqzfy=&fxzrwjtw=&fxjrcjtw=1&fxjrzjtw=&ismoved=0'
    cres = requests.post(url=checkinUrl,headers=HEADERS,data =data_check,cookies=req.cookies.get_dict())
    print(cres.text)
