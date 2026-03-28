import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(
    page_title="H-SIM Digital Lab | مختبر الهائل الرقمي",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص المظهر (Royal Blue & Gold)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        text-align: right;
        background-color: #0d1117; 
        color: #ffffff;
    }
    .main { background-color: #0d1117; }
    .stMetric {
        background-color: #1a237e; 
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        border: 1px solid #ffca28;
    }
    h1, h2, h3 { color: #ffca28; font-weight: 700; }
    .stButton>button {
        color: #0d1117; background-color: #ffca28;
        border-radius: 20px; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. نظام التبويبات
tabs = st.tabs(["🏠 فلسفة إطار الهائل", "📊 لوحة المؤشرات الذكية (H-SIM)"])

# --- التبويب الأول: الفلسفة وجدول الأركان ---
with tabs[0]:
    st.title("🚀 مختبر الهائل للتكامل الاستراتيجي (H-SIM)")
    st.subheader("من أجل إدارة تدرك 'بؤرة التكامل' قبل 'طموح التوسع'")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        يأتي إطار **H-SIM** ليعيد تعريف الأداء من خلال **التكامل الهيكلي** بين أربعة أركان حيوية. 
        المنظمة ليست أقساماً منفصلة، بل هي **جسور تدفق**. إذا انكسر جسر واحد، يبدأ النزيف الاستراتيجي.
        """)
        
        # جدول الأركان (ثابت كمرجع)
        pillars_data = {
            "الركن": ["S - السياق", "V - القيمة", "A - القدرات", "R - النتائج"],
            "الوصف": ["الظروف الخارجية وضغوط السوق", "الوعود الاستراتيجية والميزة", "العمليات والتكنولوجيا والموارد", "الأداء المالي والأثر"],
            "الهدف الاستراتيجي": ["الملاءمة (Alignment)", "التميز (Distinction)", "الكفاءة (Efficiency)", "الاستدامة (Sustainability)"]
        }
        st.markdown("### 📋 مصفوفة توصيف الأركان")
        st.table(pd.DataFrame(pillars_data))
    
    with col2:
        st.info("**مبدأ الهائل:** التكامل ليس خياراً، بل هو قانون البقاء في عصر التحول الرقمي.")

# --- التبويب الثاني: لوحة المؤشرات والتحليل الديناميكي ---
with tabs[1]:
    st.title("📊 لوحة القيادة الرقمية")
    
    # القائمة الجانبية للمدخلات
    st.sidebar.header("📥 إدخال قيم الجسور (1-10)")
    v_a = st.sidebar.slider("V -> A (التنفيذ)", 0.0, 10.0, 1.95)
    a_v = st.sidebar.slider("A -> V (التميز)", 0.0, 10.0, 2.13)
    r_a = st.sidebar.slider("R -> A (الاستدامة)", 0.0, 10.0, 1.05)
    a_r = st.sidebar.slider("A -> R (الكفاءة)", 0.0, 10.0, 1.75)
    s_v = st.sidebar.slider("S -> V (الملاءمة)", 0.0, 10.0, 4.47)
    v_s = st.sidebar.slider("V -> S (التأثير)", 0.0, 10.0, 3.50)

    # حساب المؤشرات
    eri, vci, ssi, iii = (v_a+a_v)/2, (s_v+a_r)/2, (r_a+v_s)/2, (v_a+r_a+a_v+s_v)/4

    # عرض العدادات
    fig_gauges = make_subplots(rows=2, cols=2, specs=[[{'type': 'indicator'}]*2]*2)
    indicators = [
        {"l": "جاهزية التنفيذ (ERI)", "v": eri}, {"l": "اتساق القيمة (VCI)", "v": vci},
        {"l": "الاستدامة (SSI)", "v": ssi}, {"l": "التكامل الداخلي (III)", "v": iii}
    ]
    for i, ind in enumerate(indicators):
        row, col = (i // 2) + 1, (i % 2) + 1
        fig_gauges.add_trace(go.Indicator(
            mode="gauge+number", value=ind["v"], title={'text': f"<b>{ind['l']}</b>"},
            gauge={'axis': {'range': [0, 10]}, 'bar': {'color': "#ffca28"},
                   'steps': [{'range': [0, 4], 'color': "#ff4d4d"}, {'range': [4, 7], 'color': "#ffa64d"}, {'range': [7, 10], 'color': "#4dff4d"}]}
        ), row=row, col=col)
    fig_gauges.update_layout(height=400, template='plotly_dark', margin=dict(t=40, b=10, l=20, r=20))
    st.plotly_chart(fig_gauges, use_container_width=True)

    # الرادار والمصفوفة
    st.markdown("---")
    c_radar, c_matrix = st.columns([1, 1])
    with c_radar:
        st.subheader("🎯 رادار الاتزان")
        fig_r = go.Figure(go.Scatterpolar(r=[s_v, (v_a+v_s)/2, (a_v+a_r)/2, r_a, s_v],
            theta=['S', 'V', 'A', 'R', 'S'], fill='toself', line_color='#ffca28'))
        fig_r.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10], tickfont=dict(size=10))),
                            template='plotly_dark', showlegend=False, margin=dict(t=30, b=30))
        st.plotly_chart(fig_r, use_container_width=True)
    
    with c_matrix:
        st.subheader("🌡️ مصفوفة النزيف")
        m_data = np.zeros((4,4)); m_data[0,1], m_data[1,2], m_data[2,3], m_data[3,2], m_data[2,1], m_data[1,0] = s_v, v_a, a_r, r_a, a_v, v_s
        np.fill_diagonal(m_data, 10)
        fig_h = px.imshow(m_data, x=['S','V','A','R'], y=['S','V','A','R'], color_continuous_scale='RdYlGn', zmin=0, zmax=10, text_auto='.1f')
        fig_h.update_layout(template='plotly_dark', margin=dict(t=30, b=30))
        st.plotly_chart(fig_h, use_container_width=True)

    # --- جدول تحليل الجسور الاستشارية (الجديد والمهم) ---
    st.markdown("---")
    st.subheader("📑 التقرير التحليلي لجودة الجسور (Bridge Diagnostics)")
    
    # وظيفة لتحديد الحالة والتوصية
    def get_advice(score, bridge):
        if score < 4: return "حرجة 🚨", "فجوة حادة؛ تتطلب تدخل جراحي لإعادة الهيكلة."
        if score < 7: return "هشة ⚠️", "ضعف في التدفق؛ يحتاج إلى تحسين السياسات."
        return "سليمة ✅", "تدفق مستقر؛ حافظ على معايير الجودة."

    bridge_names = ["V -> A (التنفيذ)", "A -> V (التميز)", "R -> A (الاستدامة)", "A -> R (الكفاءة)", "S -> V (الملاءمة)", "V -> S (التأثير)"]
    scores = [v_a, a_v, r_a, a_r, s_v, v_s]
    results = [get_advice(s, b) for s, b in zip(scores, bridge_names)]
    
    df_analysis = pd.DataFrame({
        "الجسر الاستراتيجي": bridge_names,
        "الدرجة": scores,
        "الحالة التشخيصية": [r[0] for r in results],
        "التوصية المقترحة": [r[1] for r in results]
    })

    st.dataframe(df_analysis.style.format({"الدرجة": "{:.2f}"}), use_container_width=True)

    # التصدير
    st.download_button("📥 تحميل التقرير (CSV)", df_analysis.to_csv(index=False).encode('utf-8-sig'), "h_sim_report.csv", "text/csv")
