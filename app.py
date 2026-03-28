import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# 1. إعدادات الصفحة والهوية البصرية (Custom CSS)
st.set_page_config(
    page_title="H-SIM Digital Lab | مختبر الهائل الرقمي",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص المظهر عبر CSS (Royal Blue & Gold branding + Cairo Arabic Font)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        text-align: right;
        background-color: #0d1117; 
        color: #ffffff;
    }

    .main {
        background-color: #0d1117;
    }

    .stMetric {
        background-color: #1a237e; 
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        border: 1px solid #ffca28;
    }

    h1, h2, h3 { 
        color: #ffca28; 
        font-weight: 700; 
    }

    .stButton>button {
        color: #0d1117;
        background-color: #ffca28;
        border-radius: 20px;
        font-weight: bold;
        border: none;
    }
    
    .stSlider > div > div > div > div {
        color: #ffca28;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. نظام التبويبات (Navigation)
tabs = st.tabs(["🏠 فلسفة إطار الهائل", "📊 لوحة المؤشرات الذكية (H-SIM)"])

# --- التبويب الأول: صفحة الترحيب والفلسفة ---
with tabs[0]:
    st.title("🚀 مرحباً بك في مختبر الهائل للتكامل الاستراتيجي (H-SIM)")
    st.subheader("من أجل إدارة تدرك 'بؤرة التكامل' قبل 'طموح التوسع'")
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### **لماذا إطار الهائل؟**
        تعاني معظم المنظمات من **'وهم النمو'**؛ حيث تظن أن زيادة المبيعات تعني النجاح، بينما الحقيقة قد تكون نزيفاً داخلياً حاداً. 
        يأتي إطار **H-SIM** ليعيد تعريف الأداء من خلال **التكامل الهيكلي** بين أربعة أركان حيوية:
        
        * **S - السياق (Context):** فهم ضغوط السوق والبيئة الخارجية.
        * **V - القيمة (Value):** جوهر الوعود التي تقدمها المنظمة للعميل.
        * **A - القدرات (Activities):** المحرك التشغيلي والمهارات والتقنيات.
        * **R - النتائج (Results):** المخرجات المالية والأثر المحقق.
        
        ### **جوهر الفلسفة: التدفق (The Flow)**
        المنظمة ليست أقساماً، بل هي **جسور تدفق**. إذا انكسر جسر واحد، فإن المنظمة تبدأ في أكل أصولها حتى تنهار.
        """)
    
    with col2:
        st.info("**مبدأ الهائل:** التكامل ليس خياراً، بل هو قانون البقاء في عصر التحول الرقمي.")
    
    st.success("👈 انتقل الآن إلى تبويب 'لوحة المؤشرات الذكية' للبدء في تشخيص منظمتك.")

# --- التبويب الثاني: لوحة المؤشرات ---
with tabs[1]:
    st.title("📊 لوحة القيادة الرقمية (Digital Dashboard)")
    
    # القائمة الجانبية
    st.sidebar.header("📥 إدخال قيم الجسور (1-10)")
    v_a = st.sidebar.slider("V -> A (التنفيذ)", 0.0, 10.0, 1.95)
    a_v = st.sidebar.slider("A -> V (التميز)", 0.0, 10.0, 2.13)
    r_a = st.sidebar.slider("R -> A (الاستدامة)", 0.0, 10.0, 1.05)
    a_r = st.sidebar.slider("A -> R (الكفاءة)", 0.0, 10.0, 1.75)
    s_v = st.sidebar.slider("S -> V (الملاءمة)", 0.0, 10.0, 4.47)
    v_s = st.sidebar.slider("V -> S (التأثير)", 0.0, 10.0, 3.50)

    # حساب المؤشرات
    eri = (v_a + a_v) / 2
    vci = (s_v + a_r) / 2
    ssi = (r_a + v_s) / 2
    iii = (v_a + r_a + a_v + s_v) / 4

    indicators = [
        {"label": "جاهزية التنفيذ (ERI)", "value": eri, "info": "شلل تنفيذي" if eri < 3 else "آلية فعالة"},
        {"label": "اتساق القيمة (VCI)", "value": vci, "info": "هدر تشغيلي" if vci < 4 else "قيمة متسقة"},
        {"label": "الاستدامة (SSI)", "value": ssi, "info": "خطر مستقبلي" if ssi < 3 else "نمو مستدام"},
        {"label": "التكامل الداخلي (III)", "value": iii, "info": "قطيعة تنظيمية" if iii < 3 else "تكامل هيكلي"}
    ]

    # رسم العدادات
    fig_gauges = make_subplots(rows=2, cols=2, specs=[[{'type': 'indicator'}]*2]*2)
    for i, ind in enumerate(indicators):
        row, col = (i // 2) + 1, (i % 2) + 1
        fig_gauges.add_trace(go.Indicator(
            mode = "gauge+number", value = ind["value"],
            title = {'text': f"<b>{ind['label']}</b><br><span style='font-size:0.8em;color:gray'>{ind['info']}</span>"},
            gauge = {
                'axis': {'range': [0, 10]}, 
                'bar': {'color': "#ffca28"},
                'steps': [
                    {'range': [0, 3], 'color': "#ff4d4d"},
                    {'range': [3, 6], 'color': "#ffa64d"},
                    {'range': [6, 10], 'color': "#4dff4d"}
                ]}
        ), row=row, col=col)
    
    fig_gauges.update_layout(height=450, template='plotly_dark', margin=dict(t=50, b=20, l=30, r=30))
    st.plotly_chart(fig_gauges, use_container_width=True)

    st.markdown("---")
    col_radar, col_matrix = st.columns([1, 1])

    with col_radar:
        st.subheader("🎯 رادار الاتزان (Equilibrium)")
        s_score = s_v 
        v_score = (v_a + v_s) / 2
        a_score = (a_v + a_r) / 2
        r_score = r_a
        
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=[s_score, v_score, a_score, r_score, s_score],
            theta=['Context (S)', 'Value (V)', 'Activities (A)', 'Results (R)', 'Context (S)'],
            fill='toself', line_color='#ffca28', fillcolor='rgba(26, 35, 126, 0.5)'
        ))
        
        # التصحيح الحاسم لهيكلية الرادار هنا
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 10], color="white", tickfont=dict(size=10)),
                angularaxis=dict(color="white", tickfont=dict(size=11))
            ),
            showlegend=False, template='plotly_dark',
            margin=dict(t=40, b=40, l=40, r=40)
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    with col_matrix:
        st.subheader("🌡️ مصفوفة النزيف (Matrix)")
        matrix_data = np.zeros((4, 4))
        matrix_data[0, 1], matrix_data[1, 2], matrix_data[2, 3] = s_v, v_a, a_r
        matrix_data[3, 2], matrix_data[2, 1], matrix_data[1, 0] = r_a, a_v, v_s
        np.fill_diagonal(matrix_data, 10)

        fig_heatmap = px.imshow(
            matrix_data, x=['S', 'V', 'A', 'R'], y=['S', 'V', 'A', 'R'],
            color_continuous_scale='RdYlGn', zmin=0, zmax=10, text_auto='.1f'
        )
        fig_heatmap.update_layout(template='plotly_dark', margin=dict(t=40, b=40, l=40, r=40))
        st.plotly_chart(fig_heatmap, use_container_width=True)

    st.markdown("---")
    avg_score = (eri + vci + ssi + iii) / 4
    if avg_score < 4:
        st.error(f"مؤشر الهائل الكلي: {avg_score:.2f} - الحالة: نزيف استراتيجي حاد.")
    elif avg_score < 7:
        st.warning(f"مؤشر الهائل الكلي: {avg_score:.2f} - الحالة: هشاشة هيكلية.")
    else:
        st.success(f"مؤشر الهائل الكلي: {avg_score:.2f} - الحالة: تكامل صحي.")

st.sidebar.markdown("---")
st.sidebar.success("✅ تم تحديث النظام بنجاح")
