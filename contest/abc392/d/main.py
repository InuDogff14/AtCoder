import sys
from itertools import combinations

def solve():
    # 入力処理
    input = sys.stdin.read
    data = input().split("\n")
    
    # サイコロの数
    N = int(data[0])

    # 各サイコロの情報
    dice = []
    prob = []  # 各サイコロの目の確率を記録する辞書リスト
    
    index = 1
    for _ in range(N):
        values = list(map(int, data[index].split()))
        K = values[0]
        faces = values[1:]
        
        dice.append(set(faces))  # 出目の集合
        face_prob = {face: faces.count(face) / K for face in set(faces)}  # 出目の確率辞書
        prob.append(face_prob)
        
        index += 1
    
    # 確率の最大値を求める
    max_probability = 0.0
    
    # 2つのサイコロを選ぶ
    for i, j in combinations(range(N), 2):
        common_faces = dice[i] & dice[j]  # 共通する出目のセット
        
        # その出目が出る確率を計算
        probability = sum(prob[i][x] * prob[j][x] for x in common_faces)
        
        # 最大値を更新
        max_probability = max(max_probability, probability)
    
    # 結果を出力
    print(f"{max_probability:.15f}")

solve()