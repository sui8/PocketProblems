import json
import random

path = "problems.json"

def start(ans):
    try:
        with open(path, "r", encoding="utf-8") as f:
            read = json.load(f)

    except Exception as e:
        print("エラーが発生しました。")
        print(e)
        init()


    if ans == "1":
        count = int(input("演習回数を入力してください: "))

        ac_count = 0
        wa_count = 0

        for i in range(count):
            num = random.choice([0, len(read)-1])
            ask = read[num]
            print(f'[{ask["number"]}] {ask["name"]} (正答率: {round((read[num]["ac"] / (read[num]["ac"] + read[num]["wa"]))*100)}%)')
            print("---------------")
            print(f'{ask["text"]}\n')
            yourans = input("> ")

            if yourans == ask["answer"]:
                print("\n正解")
                print(f'解説: {ask["explaination"]}\n')
                read[num]["ac"] += 1
                ac_count += 1

            else:
                print("\n不正解")
                print(f'解説: {ask["explaination"]}\n')
                read[num]["wa"] += 1
                wa_count += 1


    else:
        init()

    print("演習が終了しました")
    print(f"演習した問題: {count}問  正解: {ac_count}問  不正解: {wa_count}問  正答率: {round((ac_count / count)*100)}%")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(read, f)

    print("演習記録を保存しました")

    con_ans = input("続けて演習しますか (y/n): ")

    if con_ans.lower() == "y":
        start(ans)

    else:
        init()




def init():
    print("Pocket Problems")
    print("------------------------------")
    print(f"選択中の問題ファイル: {path}")
    print("[1] ランダム演習")
    print("[2] 問題番号から演習 (準備中)")
    print("[3] 不正解率が高い問題から演習 (準備中)")
    print("[4] 統計を見る")
    print("[0] 終了する")

    ans = input("> ")

    if ans == "1" or ans == "2" or ans == "3":
        start(ans)

    elif ans == "4":
        ac_count = 0
        wa_count = 0

        try:
            with open(path, "r", encoding="utf-8") as f:
                read = json.load(f)

        except Exception as e:
            print("エラーが発生しました。")
            print(e)
            init()

        else:
            for i in range(len(read)):
                ac_count += read[i]["ac"]
                wa_count += read[i]["wa"]

            print("\n統計情報")
            print("---------------")
            print(f"総演習数: {ac_count+wa_count}問  正解: {ac_count}問  不正解: {wa_count}問")
            print(f"正答率: {round((ac_count / (ac_count+wa_count))*100)}%\n")
            init()

    else:
        exit(0)


init()
