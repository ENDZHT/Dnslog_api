# dnslog.py
import requests


class dnslog:
    def __init__(self) -> None:
        self._get_dns_domain_api = 'http://dnslog.cn/getdomain.php'  # 获取子域名
        self._get_dns_record_api = "http://dnslog.cn/getrecords.php"  # 查询dns解析
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
        }
        self._dns = requests.session()  # 初始化一个session对象

        # 获取二级域名
        self._dnssubdomain = self._dns.get(self._get_dns_domain_api).text
        # 标志信息
        self._msg = 'dnstest'

    def getrecords(self):
        """检测是否有dns请求"""
        result = self._dns.get(self._get_dns_record_api,
                               headers=self._headers).text
        print(result)
        if self._msg in result:
            return True
        else:
            return False

    def get_dns_request(self):
        """获取请求的子域名，三级域名"""
        return 'http://'+self._msg+'.'+self._dnssubdomain

    def setmsg(self, msg):
        """设置三级域名标志位"""
        self._msg = msg

    def send(self):
        """发送dns请求"""
        try:
            self._dns.get('http://'+self._msg+'.' +
                          self._dnssubdomain, headers=self._headers)
        except Exception as e:
            pass
