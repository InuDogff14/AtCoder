def is_valid_parentheses(s: str) -> str:
    # 括弧のペアを辞書で定義
    pair = {')': '(', ']': '[', '>': '<'}
    
    stack = []
    
    # 文字列の各文字を処理
    for char in s:
        if char in '([{<' :
            stack.append(char)  # 開き括弧をスタックに積む
        elif char in ')]}>':
            if not stack or stack[-1] != pair[char]:
                return "No"  # スタックが空またはペアが合わない場合
            stack.pop()  # ペアが合えばスタックから取り出す
    
    # スタックが空ならばカラフル括弧列、そうでなければNo
    return "Yes" if not stack else "No"

# 標準入力を取得
S = input().strip()

# 結果を出力
print(is_valid_parentheses(S))