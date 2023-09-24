# -*- coding: utf-8 -*-
"""
@Author   : 大南瓜
@Time     : 2023/9/22 13:35
@File     : BaiduKeywordCall.py
@Project  : baidukeyword
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import requests
from BaiduKeyword import Ui_MainWindow
from urllib.parse import quote
from lxml import etree


class BaiduKeywordCall(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def get_words(self):
        self.keyword=self.ui.keywordlineEdit.text()
        print(self.keyword)
        words=[]
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        }
        url = f"http://www.baidu.com/s?wd={quote(self.keyword)}&f=8&rsv_enter=0&rn=10&mod=1&isbd=1&isid=f5a3135000028383&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&rsv_pq=c1c131e24a66bc79&rsv_t=029d7vezH5oteQlAcN9sK02SDGuvgDntJgzOfGbzAUq%2B%2BT367Hfx3AN1vztoiDVpFLmm&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&inputT=723443&rsv_sug4=723443&rsv_sid=undefined&_ss=1&clist=&hsug=&f4s=1&csor=0&_cr1=35521&oq="
        r = requests.get(url, headers=headers, timeout=5)
        # print(r.text)
        r.encoding = 'utf-8'
        doc = etree.HTML(r.text)
        relate_search = doc.xpath('//div[@id="rs_new"]//a//text()')
        print(relate_search)
        for word in relate_search:
            self.ui.keywordtextEdit.append(word)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = BaiduKeywordCall()
    win.show()
    sys.exit(app.exec_())
