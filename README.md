# scrapy-hr.tencent
使用scrapy简单抓取腾讯招聘信息

爬虫名：tencent

开始爬虫：scrapy crawl tencent

pipeline.py

爬取结果将在指令目录下生成一个tencent.json的文件

def __init__(self):
    self.f = open('tencent.json', 'w', encoding='utf-8')

def process_item(self, item, spider):
    content =  json.dumps(dict(item), ensure_ascii=False) +", \n"
    self.f.write(content)
    return item
    
tencent.json (截取部分)

{"title": "SA-腾讯社交广告商业化产品经理（产品形态设计方向 深圳）", "url": "position_detail.php?id=34993&keywords=&tid=0&lid=0", "category": "产品/项目类", "num": "1", "area": "深圳", "time": "2018-01-15"}, 

{"title": "16175-海外游戏运营经理（深圳）", "url": "position_detail.php?id=36047&keywords=&tid=0&lid=0", "category": "产品/项目类", "num": "1", "area": "深圳", "time": "2018-01-15"}, 

{"title": "15605-火影忍者3D角色(深圳)", "url": "position_detail.php?id=35302&keywords=&tid=0&lid=0", "category": "设计类", "num": "1", "area": "深圳", "time": "2018-01-15"}, 

{"title": "14137-WXG财务管理（广州）", "url": "position_detail.php?id=33250&keywords=&tid=0&lid=0", "category": "职能类", "num": "1", "area": "广州", "time": "2018-01-15"}, 

{"title": "OMG236-腾讯视频android高级工程师（深圳）", "url": "position_detail.php?id=28731&keywords=&tid=0&lid=0", "category": "技术类", "num": "1", "area": "深圳", "time": "2018-01-15"}, 

{"title": "OMG236-视频推荐后台开发工程师（深圳）", "url": "position_detail.php?id=28722&keywords=&tid=0&lid=0", "category": "技术类", "num": "1", "area": "深圳", "time": "2018-01-15"}, 

{"title": "OMG236-视频推荐算法工程师(北京)", "url": "position_detail.php?id=28718&keywords=&tid=0&lid=0", "category": "技术类", "num": "1", "area": "北京", "time": "2018-01-15"}, 

tencent.py

自动识别下一页的属性状态，判断是否为最后一页

def parse(self, response):
    node_list = response.xpath("//tr[@class='odd' or @class='even']")
    for index, node in enumerate(node_list):
        items = TencentItem()        
        title = node.xpath("./td[1]/a/text()").extract()[0]        
        url = node.xpath("./td[1]/a/@href").extract()[0]        
        if len(node.xpath("./td[2]/text()")):        
            category = node.xpath("./td[2]/text()").extract()[0]
        else:
            category = ""
        num = node.xpath("./td[3]/text()").extract()[0]
        area = node.xpath("./td[4]/text()").extract()[0]
        time = node.xpath("./td[5]/text()").extract()[0]
        items['title'] = title
        items['url'] = url
        items['category'] = category
        items['num'] = num
        items['area'] = area
        items['time'] = time
        yield items
    is_next = response.xpath("//a[@id='next' and @class='noactive']").extract()
    if not len(is_next):
        node_next = response.xpath("//a[@id='next']/@href").extract()[0]
        url = self.baseURL + node_next
        print(url)
        yield scrapy.Request(url, callback=self.parse)
