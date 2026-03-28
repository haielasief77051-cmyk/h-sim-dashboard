import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

# ==========================================
# 1. الإعدادات الهيكلية والهوية البصرية
# ==========================================
st.set_page_config(
    page_title="H-SIM Digital Lab | مختبر الهائل الرقمي",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تصميم الواجهة بأسلوب أكاديمي فخم (Royal Blue & Matte Gold)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        text-align: right;
        background-color: #0d1117;
        color: #e0e0e0;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        background-color: #1a237e;
        padding: 10px;
        border-radius: 10px 10px 0 0;
    }

    h1, h2, h3 { 
        color: #ffca28; 
        border-bottom: 1px solid #30363d;
        padding-bottom: 10px;
    }

    .report-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 15px;
        border-right: 5px solid #ffca28;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. نظام التبويبات الاستراتيجية
# ==========================================
tab_phi, tab_dash = st.tabs(["🏛️ المرجعية المعرفية للنموذج", "📊 مختبر التشخيص القياسي"])

# --- التبويب الأول: فلسفة الأركان والجسور ---
with tab_phi:
    st.markdown('<div class="report-card">', unsafe_allow_html=True)
    st.title("نظام الهائل للتكامل الاستراتيجي (H-SIM Framework)")
    st.write("""
    يعمل إطار **H-SIM** كأداة جراحية لتشخيص التدفقات المؤسسية. يرتكز النموذج على تحليل ستة جسور حيوية تربط بين أركان المنظمة، 
    حيث يمثل كل جسر مساراً انتقالياً للقيمة والقدرات والنتائج.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col_p1, col_p2 = st.columns([1, 1])
    
    with col_p1:
        st.subheader("📌 مصفوفة تعريف الأركان")
        pillars_desc = {
            "الركن": ["S - السياق", "V - القيمة", "A - القدرات", "R - النتائج"],
            "البعد الاستراتيجي": ["الملاءمة البيئية", "التميز التنافسي", "الكفاءة التشغيلية", "الاستدامة المؤسسية"],
            "المقصد": ["التكيف", "الريادة", "التمكين", "البقاء"]
        }
        st.table(pd.DataFrame(pillars_desc))

    with col_p2:
        st.subheader("🔗 تعريف الجسور الستة")
        st.markdown("""
        * **جسر الملاءمة:** يقيس مدى استجابة وعود القيمة لضغوط السياق الخارجي.
        * **جسر التنفيذ:** يقيس كفاءة تحويل الوعود الاستراتيجية إلى ممارسات تشغيلية.
        * **جسر التميز:** يقيس قدرة الإمكانيات الداخلية على خلق ميزة تنافسية فريدة.
        * **جسر الكفاءة:** يقيس جودة تحويل الموارد والأنشطة إلى نتائج مالية ملموسة.
        * **جسر الاستدامة:** يقيس مدى إعادة تدوير النتائج لبناء وتعزيز القدرات المستقبلية.
        * **جسر القيمة المالية:** يقيس الأثر المرتد للنتائج على مكانة المنظمة في سياقها العام.
        """)

# --- التبويب الثاني: مختبر التشخيص الرقمي ---
with tab_dash:
    st.sidebar.header("🕹️ لوحة التحكم في الجسور")
    st.sidebar.markdown("---")
    
    # مدخلات الجسور بالمسميات المصححة
    s_v = st.sidebar.slider("1. جسر الملاءمة (S ➔ V)", 0.0, 10.0, 4.47)
    v_a = st.sidebar.slider("2. جسر التنفيذ (V ➔ A)", 0.0, 10.0, 1.95)
    a_v = st.sidebar.slider("3. جسر التميز (A ➔ V)", 0.0, 10.0, 2.13)
    a_r = st.sidebar.slider("4. جسر الكفاءة (A ➔ R)", 0.0, 10.0, 1.75)
    r_a = st.sidebar.slider("5. جسر الاستدامة (R ➔ A)", 0.0, 10.0, 1.05)
    v_s = st.sidebar.slider("6. جسر القيمة المالية (V ➔ S)", 0.0, 10.0, 3.50)

    # حساب المؤشرات المحورية
    eri = (v_a + a_v) / 2 # Execution Readiness
    vci = (s_v + a_r) / 2 # Value Consistency
    ssi = (r_a + v_s) / 2 # Strategic Sustainability
    iii = (v_a + r_a + a_v + s_v) / 4 # Internal Integration

    # 1. عرض العدادات القياسية
    st.subheader("📈 مؤشرات التكامل الكلية")
    fig_ind = make_subplots(rows=1, cols=4, specs=[[{'type': 'indicator'}]*4])
    
    m_indicators = [
        ("جاهزية التنفيذ (ERI)", eri), ("اتساق القيمة (VCI)", vci),
        ("معامل الاستدامة (SSI)", ssi), ("التكامل البنيوي (III)", iii)
    ]

    for i, (label, val) in enumerate(m_indicators):
        fig_ind.add_trace(go.Indicator(
            mode="gauge+number", value=val,
            title={'text': f"<span style='font-size:0.9em;color:#ffca28'>{label}</span>"},
            gauge={'axis': {'range': [0, 10]}, 'bar': {'color': "#ffca28"},
                   'steps': [{'range': [0, 4], 'color': "#7f1d1d"}, {'range': [4, 7], 'color': "#9a3412"}, {'range': [7, 10], 'color': "#14532d"}]}
        ), row=1, col=i+1)
    
    fig_ind.update_layout(height=300, template='plotly_dark', margin=dict(t=30, b=20, l=20, r=20))
    st.plotly_chart(fig_ind, use_container_width=True)

    # 2. الجداول التشخيصية المحسنة
    st.markdown("---")
    st.subheader("📋 التقرير التحليلي لكفاءة الجسور")
    
    def get_status(score):
        if score < 4: return "حرجة (نزيف استراتيجي) 🚨", "تطلب تدخل جراحي فوري لإعادة التصميم."
        if score < 7: return "هشة (ضعف تدفق) ⚠️", "يحتاج المسار إلى مأسسة وتحسين سياسات."
        return "سليمة (تكامل مستقر) ✅", "المسار يحقق التدفق الأمثل، يوصى بالاستدامة."

    bridge_names = ["جسر الملاءمة", "جسر التنفيذ", "جسر التميز", "جسر الكفاءة", "جسر الاستدامة", "جسر القيمة المالية"]
    bridge_paths = ["S ➔ V", "V ➔ A", "A ➔ V", "A ➔ R", "R ➔ A", "V ➔ S"]
    bridge_scores = [s_v, v_a, a_v, a_r, r_a, v_s]
    diagnostics = [get_status(s) for s in bridge_scores]

    df_final = pd.DataFrame({
        "الجسر التشخيصي": bridge_names,
        "المسار البنيوي": bridge_paths,
        "درجة التكامل": bridge_scores,
        "الحالة المؤسسية": [d[0] for d in diagnostics],
        "التوصية المقترحة": [d[1] for d in diagnostics]
    })

    st.dataframe(df_final.style.format({"درجة التكامل": "{:.2f}"})
                 .highlight_min(subset=['درجة التكامل'], color='#450a0a'), 
                 use_container_width=True)

    # 3. الرادار الاستراتيجي
    st.markdown("---")
    st.subheader("🎯 بصمة الاتزان الاستراتيجي (H-SIM Radar)")
    fig_radar = go.Figure(go.Scatterpolar(
        r=[s_v, (v_a+v_s)/2, (a_v+a_r)/2, r_a, s_v],
        theta=['Context (S)', 'Value (V)', 'Activities (A)', 'Results (R)', 'Context (S)'],
        fill='toself', line_color='#ffca28', fillcolor='rgba(26, 35, 126, 0.4)'
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10], tickfont=dict(size=10, color="white"))),
        template='plotly_dark', margin=dict(t=40, b=40)
    )
    st.plotly_chart(fig_radar, use_container_width=True)

    # 4. التصدير
    st.download_button("📥 تصدير التقرير النهائي (CSV)", df_final.to_csv(index=False).encode('utf-8-sig'), "h_sim_diagnostic.csv", "text/csv")

st.sidebar.markdown("---")
st.sidebar.caption("نظام مدعوم بنموذج التكامل الاستراتيجي - H-SIM Framework")
