
josnItem = ''

# ((u'\u77f3\u6797\uff08\u738b\u7518AD001\uff08\u738b\u8f69\uff09\uff09', 23493L, Decimal('66576.00'),
#   Decimal('4649.82'), u'6.98%', 43L, Decimal('1636'), Decimal('127'), u'7.76%', Decimal('854'),
#   Decimal('136'), Decimal('489.53'), Decimal('77.96'), Decimal('1.07'), Decimal('3006.82'),
#   Decimal('7538.84'), Decimal('10545.66'), Decimal('245.25'),
#   u'15.84%', Decimal('108.14'), Decimal('-2018.90'), Decimal('23'), u'2.69%'),)

josnItem = ((u'\u77f3\u6797\uff08\u738b\u7518AD001\uff08\u738b\u8f69\uff09\uff09', 23493L, 66576.00,
            4649.82, u'6.98%', 43L, 1636, 127, u'7.76%', 854, 136, 489.53, 77.96, 1.07, 3006.82,
             7538.84, 10545.66, 245.25, u'15.84%', 108.14, -2018.90, '23', u'2.69%'),)
print len(josnItem[0])
print [dict(zip(range(len(josnItem[0])), josnItem[0]))][0][3]
