#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/23 17:51
# @Author  : buttogo
# @File    : update_adcodes.py
# @Desc    :
import numpy as np
import pandas as pd


# 模拟台湾地区的编码（非官方），便于解析相应地址
taiwan_mock_adcode = [
    {"adcode": "710100000000", "name": "台北市", "longitude": None, "latitude": None},
    {"adcode": "710200000000", "name": "新北市", "longitude": None, "latitude": None},
    {"adcode": "710300000000", "name": "桃园市", "longitude": None, "latitude": None},
    {"adcode": "710400000000", "name": "台中市", "longitude": None, "latitude": None},
    {"adcode": "710500000000", "name": "台南市", "longitude": None, "latitude": None},
    {"adcode": "710600000000", "name": "高雄市", "longitude": None, "latitude": None},
    {"adcode": "710700000000", "name": "基隆市", "longitude": None, "latitude": None},
    {"adcode": "710800000000", "name": "新竹市", "longitude": None, "latitude": None},
    {"adcode": "710900000000", "name": "嘉义市", "longitude": None, "latitude": None},
    {"adcode": "711000000000", "name": "宜兰县", "longitude": None, "latitude": None},
    {"adcode": "711100000000", "name": "新竹县", "longitude": None, "latitude": None},
    {"adcode": "711200000000", "name": "苗栗县", "longitude": None, "latitude": None},
    {"adcode": "711300000000", "name": "彰化县", "longitude": None, "latitude": None},
    {"adcode": "711400000000", "name": "南投县", "longitude": None, "latitude": None},
    {"adcode": "711500000000", "name": "云林县", "longitude": None, "latitude": None},
    {"adcode": "711600000000", "name": "嘉义县", "longitude": None, "latitude": None},
    {"adcode": "711700000000", "name": "屏东县", "longitude": None, "latitude": None},
    {"adcode": "711800000000", "name": "花莲县", "longitude": None, "latitude": None},
    {"adcode": "711900000000", "name": "台东县", "longitude": None, "latitude": None},
    {"adcode": "712000000000", "name": "澎湖县", "longitude": None, "latitude": None},
]


def update_adcode_with_nation():
    adcodes = pd.read_csv("./resources/adcodes.csv")
    countries = pd.read_csv("./resources/country_names.csv", sep="|")

    # 添加台湾地区的编码
    taiwan = pd.DataFrame(taiwan_mock_adcode)
    adcodes = pd.concat([adcodes, taiwan])

    # 模拟和添加国家的编码
    countries["adcode"] = countries.index + 1
    countries["adcode"] = countries["adcode"].apply(lambda x: str(x).zfill(12))
    countries["longitude"] = np.nan
    countries["latitude"] = np.nan
    countries.rename(columns={"country_name": "name"}, inplace=True)
    adcodes = pd.concat(
        [adcodes, countries[["adcode", "name", "longitude", "latitude"]]]
    )

    # 筛选过段的区县，减少误配
    filtered = adcodes[
        ~(
            (adcodes["name"].str.endswith("区") | adcodes["name"].str.endswith("县"))
            & (adcodes["name"].str.len() < 3)
        )
    ]

    filtered.to_csv("./resources/adcodes_new.csv", index=False)


if __name__ == "__main__":
    update_adcode_with_nation()
