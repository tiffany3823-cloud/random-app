import ipywidgets as w, pandas as pd
from IPython.display import clear_output as c, display as d

D = {
    "힙합": ["바람막이", "카고팬츠", "볼캡", "스니커즈"],
    "귀여움": ["가디건", "스커트", "니삭스", "메리제인"],
    "화려함": ["트위드", "슬랙스", "액세서리", "부츠"],
    "캐주얼": ["데님재킷", "티셔츠", "치노팬츠", "운동화"],
}
g, s, st, p, b, o = (
    w.Dropdown(options=["남", "여"]),
    w.Dropdown(options=["봄", "여름", "가을", "겨울"]),
    w.Dropdown(options=list(D)),
    w.Text(placeholder="목적"),
    w.Button(description="추천"),
    w.Output(),
)


def f(x):
    with o:
        c()
        v = p.value
        sc = 60 if "면접" in v else 100 if v in "데이트페스티벌" else 80
        print(
            f"[{g.value}/{s.value}/{st.value}] {sc}점" if v else "목적 입력!"
        )
        v and d(pd.DataFrame({"구분": ["상", "하", "잡", "신"], "추천": D[st.value]}))


b.on_click(f)
d(g, s, st, p, b, o)
