#! /usr/bin/python3
# coding:utf-8

from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

class Baidu(unittest.TestCase):
    '''对百度搜索功能进行测试'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.baidu.com/'
    def test_baidu_seach(self):
        '''测试HTMLTestRunner的搜索'''
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(2)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id('su').click()
        time.sleep(2)
        self.assertEqual(driver.title,'HTMLTestRunner_百度搜索')
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(Baidu("test_baidu_seach"))
    fp = open('./result.html','wb')
    runner = HTMLTestRunner(
        stream = fp,
        title = '百度搜索测试报告',
        description = '用例执行报告')
    runner.run(test_suite)
    fp.close()
