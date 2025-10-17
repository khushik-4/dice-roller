 # dice_roller.py
# A tiny Dice Roller Game


import streamlit as st
import random
import time

# 🌸 Page styling (Light Pink Theme)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #fbc2eb 0%, #fcd6e8 100%);
    color: #333;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
h1, h2, h3, h4, h5, h6, p {
    color: #333;
    text-align: center;
}
.stButton > button {
    background-color: #ff4b8b;
    color: black;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-size: 1.1rem;
    font-weight: bold;
    transition: 0.3s;
}
.stButton > button:hover {
    background-color: #ff2e74;
    transform: scale(1.05);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 🎯 Title
st.title("🎲 Dice Roller Game")

st.write("Choose how many dice you want to roll and click the button!")

# 🧠 Initialize roll history
if "history" not in st.session_state:
    st.session_state.history = []

# 🎲 Dice faces
dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

# 📌 Number of dice selector
num_dice = st.slider("Number of dice to roll", 1, 3, 1)

# 🎞️ Roll button with animation
if st.button("Roll Dice 🎲"):
    placeholder = st.empty()

    # 🌀 Rolling animation
    for _ in range(10):
        faces = " ".join(random.choice(list(dice_faces.values())) for _ in range(num_dice))
        placeholder.markdown(
            f"<h1 style='font-size: 100px;'>{faces}</h1>",
            unsafe_allow_html=True
        )
        time.sleep(0.1)

    # 🎯 Final result
    results = [random.randint(1, 6) for _ in range(num_dice)]
    total = sum(results)
    faces_final = " ".join(dice_faces[r] for r in results)

    placeholder.markdown(
        f"<h1 style='font-size: 100px;'>{faces_final}</h1>",
        unsafe_allow_html=True
    )
    st.success(f"🎯 You rolled {num_dice} dice → Results: {results}  |  Total: {total}")

    # 📝 Save to history
    st.session_state.history.append({
        "dice": num_dice,
        "results": results,
        "total": total
    })

else:
    st.info("Press the button to start rolling!")

# 📜 Roll history panel
st.subheader("📜 Roll History")
if st.session_state.history:
    for i, entry in enumerate(reversed(st.session_state.history), 1):
        st.write(f"Roll {len(st.session_state.history) - i + 1}: 🎲 {entry['dice']} dice → {entry['results']} | Total: {entry['total']}")
else:
    st.write("No rolls yet — start playing!")
