import requestGD511

page = 1
def run_spyde():
    requestGD511.page_url(1)# 爬取两次数据确保写入数据库
    requestGD511.page_url(1)# 爬取两次数据确保写入数据库