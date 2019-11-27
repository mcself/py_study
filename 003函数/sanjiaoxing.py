#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sjx(a,h):
    if h == 0:
        return '三角形不存在'
    else:
        p = (a*h)/2
        return '三角形面积为%.2f(结果保留两位小数)'%p

print(sjx(5,0))
print(sjx(5,8.71))
