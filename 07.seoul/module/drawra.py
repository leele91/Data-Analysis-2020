import numpy as np
import pandas as pd
import seaborn as sns

draw_korea_ra = pd.read_excel('./data/draw_korea_raw(수정01).xlsx', encoding='EUC-KR')
draw_korea_ra

draw_korea_st = pd.DataFrame(draw_korea_ra.stack())
draw_korea_st.reset_index(inplace=True)
draw_korea_st.rename(columns={'level_0':'y', 'level_1':'x', 0:'ID'}, inplace=True)
draw_korea_st

draw_korea = draw_korea_st