# -*- coding: utf-8 -*-
import os
import glob
from distutils import dir_util

"""
    DDRsort.py

    ソートしたい譜面フォルダが集まっているフォルダで実行してください。
"""

SaveList = []
NumList = []
lines = []
#ディレクトリ下のすべてのフォルダ内にあるsmを検索、1つずつ処理を行う
path = glob.glob("./*")

def main():

    count = 0
    playcount = ""

    for var in range(len(path)):

        #print(playcount)
        SaveList = []
        NumList = []
        lines = []

        test = glob.glob(path[count] + "/*.sm")
        print(test)
        if not test:
            test = glob.glob(path[count] + "/*.ssc")
            if not test:
                count += 1
                continue
        try:
            file = open(test[0],encoding="utf-8")
            lines = file.readlines()
        except:
            print(lines)
            print("エラー発生")

        #smファイル内のdance-singleの場所をリストにしてすべて返す
        SaveList = [i for i, x in enumerate(lines) if x == '     dance-single:\n']

        #レベルを返す
        for i in SaveList:
            NumList.append(i + 3)

        for var in range(len(SaveList)):
            result = LevelSearch(NumList[var],lines)
            if result == True:
                break
        
        if result == True:
            os.mkdir('../level15' + path[count])
            dir_util.copy_tree(path[count], '../level15' + path[count])

        count += 1
        playcount += "."


    print("すべて終了しました！")   
    
    file.close()


#譜面内のレベルを検索する
def LevelSearch(x,lines):
    Level = lines[x].strip()
    if Level == "15:":
        return True

if __name__ == "__main__":
    main()