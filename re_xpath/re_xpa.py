# coding:utf-8
from lxml import etree
# 关于xpath

xml = '''
<A id="a1">
    <B id="b1">
        <C id="c1">
            <B name="b"/>
            <D id="d1"/>
            <E id="e1"/>
            <F id="e2"/>
        </C>
        <C id="c3">
            <E id="e3"/>
            <F id="e4"/>
        </C>
        xxxxx
    </B>
    <B id="b2"/>
    <C id="c2">
        <B/>
        <D id="d2"/>
        <F/>
    </C>
    <E/>
    <a harf = 'www.baidu.com'/>
</A>
'''
# ''.strip()
# print dir(xml)

xl = etree.fromstring(xml)
# print dir(xl)
print xl.xpath('//a/@harf')  # <a herf = ''>xxx</a> ---> //a/@herf
# x = xl.xpath('//E/parent::*')   # list
# print x
# print x[0].tag
# print x[1].tag  # |: 位运算  || 逻辑运算 ---> 逻辑或