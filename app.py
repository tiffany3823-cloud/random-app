import streamlit as s,pandas as p
D={"힙합":["바람막이","카고팬츠","볼캡","스니커즈"],"귀여움":["가디건","스커트","니삭스","메리제인"],"화려함":["트위드","슬랙스","액세서리","부츠"],"캐주얼":["데님재킷","티셔츠","치노팬츠","운동화"]}
g=s.selectbox("성별",["남","여"])
sn=s.selectbox("계절",["봄","여름","가을","겨울"])
st=s.selectbox("스타일",list(D))
v=s.text_input("목적")
if s.button("추천"):
 if not v:s.warning("목적 입력!")
 else:
  sc=60 if"면접"in v else 100 if v in"데이트페스티벌"else 80
  s.write(f"[{g}/{sn}/{st}] {sc}점")
  s.dataframe(p.DataFrame({"구분":["상","하","잡","신"],"추천":D[st]}))
