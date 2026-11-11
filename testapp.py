%%writefile app.py
import streamlit as st

# ページ設定
st.set_page_config(page_title="マイ・クイズアプリ", page_icon="🎯", layout="centered")

# サイドバー
with st.sidebar:
    st.header("⚙️ 設定・情報")
    if st.button("🔄 最初からやり直す"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()

st.title("🎯 挑戦！オリジナル三択クイズ")
st.markdown("---")

# クイズデータ
questions = [
    {
        "question": "日本で一番高い山の名前は？",
        "options": ["富士山", "北岳", "槍ヶ岳"],
        "answer": 0
    },
    {
        "question": "プログラミング言語「Python」の名前の由来となった生き物は？",
        "options": ["恐竜", "ニシキヘビ（パイソン）", "イルカ"],
        "answer": 1
    },
    {
        "question": "次のうち、Pythonだけで簡単にWebアプリが作れるツールはどれ？",
        "options": ["Photoshop", "Streamlit", "Excel"],
        "answer": 1
    },
    {
        "question": "世界で一番面積が大きい国はどこ？",
        "options": ["中国", "アメリカ", "ロシア"],
        "answer": 2
    }
]

# 状態の初期化
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False

# クイズ画面の処理
if st.session_state.current_q < len(questions):
    q_data = questions[st.session_state.current_q]
    
    progress = (st.session_state.current_q) / len(questions)
    st.progress(progress, text=f"進捗: 第 {st.session_state.current_q + 1} 問 / 全 {len(questions)} 問")
    
    st.subheader(q_data["question"])
    selected = st.radio("選択してください：", q_data["options"], key=f"q_{st.session_state.current_q}")
    
    if not st.session_state.answered:
        if st.button("✨ この答えで決定！", type="primary"):
            st.session_state.answered = True
            selected_idx = q_data["options"].index(selected)
            if selected_idx == q_data["answer"]:
                st.success("🎉 正解です！素晴らしい！")
                st.session_state.score += 1
            else:
                correct_text = q_data["options"][q_data["answer"]]
                st.error(f"❌ 残念！正解は「{correct_text}」でした。")
            st.rerun()
    else:
        if st.button("👉 次の問題へ進む"):
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.rerun()

else:
    st.balloons()
    st.success("🏆 すべての問題が終了しました！お疲れ様でした！")
    
    final_score = st.session_state.score
    total = len(questions)
    st.metric(label="あなたの最終スコア", value=f"{final_score} / {total} 問正解")
    
    if final_score == total:
        st.balloons()
        st.markdown("### 👑 パーフェクト達成！おめでとうございます！")
    elif final_score >= total / 2:
        st.markdown("### 👍 よくできました！あと一歩で全問正解です！")
    else:
        st.markdown("### 💪 もう一度挑戦してリベンジしよう！")
        
    if st.button("🔄 もう一度最初から遊ぶ"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()