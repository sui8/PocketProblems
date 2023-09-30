import json

path = "problems.json"

def addProblem():
    number = input("問題番号を入力してください: ")
    name = input("問題の分類を入力してください: ")
    print("問題文を入力してください:")

    text = []
    
    while True:
        line = input()
        
        if line:
            text.append(line)
            
        else:
            break
    
    answer = input("回答を入力してください: ")
    explanation = input("解説を入力してください (オプション): ")

    if not explanation:
        explanation = "解説はありません"

    try:
        with open(path, "r", encoding="utf-8") as f:
            read = json.load(f)

    except Exception as e:
        print("エラーが発生しました。")
        print(e)
        
    newdata = {"number": number, "name": name, "text": text, "answer": answer, "explaination": explanation, "ac": 0, "wa": 0}
    save = [read, newdata]
        
    with open(path, "w", encoding="utf-8") as f:
        json.dump(save, f)

    ans = input("問題を追加しました。続けて追加しますか (y/n): ")

    if ans.lower() == "y":
        addProblem()

    else:
        init()




def init():
    print("Pocket Problems 問題追加ツール")
    print("------------------------------")
    print("メニューから番号を選択してください")
    print("[1] 問題追加")
    print("[0] 終了する")

    ans = input("> ")

    if ans == "1":
        addProblem()

    else:
        exit(0)

init()
