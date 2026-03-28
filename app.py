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
    page_title="نظام الهائل للتكامل الاستراتيجي | H-SIM Lab",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تصميم الواجهة (Royal Blue & Matte Gold) بأسلوب احترافي
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
        gap: 10px;
        background-color: #1a237e;
        padding: 10px;
        border-radius: 10px 10px 0 0;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: transparent;
        color: #ffffff;
        font-weight: 600;
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

# --- التبويب الأول: فلسفة الأركان ---
with tab_phi:
    st.markdown('<div class="report-card">', unsafe_allow_html=True)
    st.title("نظام الهائل للتكامل الاستراتيجي (H-SIM Framework)")
    st.write("""
    يُعد إطار **H-SIM** أداة تشخيصية متقدمة تهدف إلى قياس "بؤرة التكامل" داخل المنظمات. 
    يرتكز النموذج على فرضية أن الخلل التنظيمي ليس نتاج ضعف الأقسام، بل هو نتاج تآكل **جسور التدفق** بين أربعة أركان حيوية.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col_p1, col_p2 = st.columns([1, 1])
    
    with col_p1:
        st.subheader("📌 مصفوفة تعريف الأركان (Pillars Matrix)")
        pillars_desc = {
            "الركن": ["S - السياق (Context)", "V - القيمة (Value)", "A - القدرات (Activities)", "R - النتائج (Results)"],
            "البعد الاستراتيجي": ["الملاءمة البيئية", "التميز التنافسي", "الكفاءة التشغيلية", "الاستدامة المؤسسية"],
            "تركيز القياس": ["الفرص والتهديدات", "وعود العلامة التجارية", "الموارد والتكنولوجيا", "العائد المالي والأثر"]
        }
        st.table(pd.DataFrame(pillars_desc))

    with col_p2:
        st.subheader("🔗 فلسفة الجسور (Bridge Logic)")
        st.info("""
        تعتمد قوة المنظمة على **كفاءة التدفق** عبر 6 جسر أساسية. 
        فالخلل في جسر (V -> A) يعني "عجزاً تنفيذياً"، بينما الخلل في (R -> A) يعني "تآكلاً في الأصول" يهدد البقاء.
        تُقاس هذه الجسور عبر استبيانات معيارية تعكس الواقع الميداني.
        """)

# --- التبويب الثاني: لوحة القيادة والتحليل ---
with tab_dash:
    st.sidebar.header("🕹️ مدخلات القياس الميداني")
    st.sidebar.markdown("---")
    
    # تحديد المعاملات (Sliders)
    v_a = st.sidebar.slider("V ➔ A (كفاءة حوكمة التنفيذ)", 0.0, 10.0, 1.95)
    a_v = st.sidebar.slider("A ➔ V (القدرة على الابتكار والتميز)", 0.0, 10.0, 2.13)
    r_a = st.sidebar.slider("R ➔ A (إعادة استثمار النتائج/الاستدامة)", 0.0, 10.0, 1.05)
    a_r = st.sidebar.slider("A ➔ R (كفاءة تحويل القدرات لنتائج)", 0.0, 10.0, 1.75)
    s_v = st.sidebar.slider("S ➔ V (الاستجابة لمتغيرات السوق)", 0.0, 10.0, 4.47)
    v_s = st.sidebar.slider("V ➔ S (التأثير في الهوية الذهنية)", 0.0, 10.0, 3.50)

    # حساب المؤشرات الكلية
    eri = (v_a + a_v) / 2
    vci = (s_v + a_r) / 2
    ssi = (r_a + v_s) / 2
    iii = (v_a + r_a + a_v + s_v) / 4

    # 1. عرض المؤشرات المحورية
    st.subheader("📈 مؤشرات التكامل الاستراتيجي الكلية")
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
    
    fig_ind.update_layout(height=300, template='plotly_dark', margin=dict(t=20, b=20))
    st.plotly_chart(fig_ind, use_container_width=True)

    # 2. التحليل الجرافيكي (الرادار والمصفوفة)
    st.markdown("---")
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.subheader("🎯 رادار الاتزان البنيوي")
        fig_radar = go.Figure(go.Scatterpolar(
            r=[s_v, (v_a+v_s)/2, (a_v+a_r)/2, r_a, s_v],
            theta=['S', 'V', 'A', 'R', 'S'], fill='toself', line_color='#ffca28'
        ))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10], tickfont=dict(size=10))),
                                template='plotly_dark', showlegend=False, margin=dict(t=30, b=30))
        st.plotly_chart(fig_radar, use_container_width=True)

    with c2:
        st.subheader("🌡️ مصفوفة فجوات النزيف التدفيقي")
        m_map = np.zeros((4,4)); m_map[0,1], m_map[1,2], m_map[2,3], m_map[3,2], m_map[2,1], m_map[1,0] = s_v, v_a, a_r, r_a, a_v, v_s
        np.fill_diagonal(m_map, 10)
        fig_h = px.imshow(m_map, x=['S','V','A','R'], y=['S','V','A','R'], color_continuous_scale='RdYlGn', zmin=0, zmax=10, text_auto='.1f')
        fig_h.update_layout(template='plotly_dark', margin=dict(t=30, b=30))
        st.plotly_chart(fig_h, use_container_width=True)

    # 3. التقرير التشخيصي التفصيلي للجداول
    st.markdown("---")
    st.subheader("📋 تقرير تشخيص كفاءة الجسور الاستراتيجية")
    
    def analyze_bridge(score):
        if score < 4: return "فجوة حادة (Critical Leak) 🚨", "تتطلب إعادة هيكلة فورية للمسار الاستراتيجي."
        if score < 7: return "هشاشة هيكلية (Fragile) ⚠️", "يحتاج المسار إلى مأسسة وتجويد العمليات."
        return "تدفق مستقر (Balanced) ✅", "المسار يحقق التكامل المطلوب، يوصى بالتحسين المستمر."

    bridges = ["V ➔ A", "A ➔ V", "R ➔ A", "A ➔ R", "S ➔ V", "V ➔ S"]
    bridge_scores = [v_a, a_v, r_a, a_r, s_v, v_s]
    analysis_results = [analyze_bridge(s) for s in bridge_scores]

    df_report = pd.DataFrame({
        "الجسر الاستراتيجي": bridges,
        "الدرجة المعيارية": bridge_scores,
        "التشخيص المؤسسي": [r[0] for r in analysis_results],
        "التوصية الاستشارية": [r[1] for r in analysis_results]
    })

    # عرض الجدول بتنسيق احترافي
    st.dataframe(df_report.style.format({"الدرجة المعيارية": "{:.2f}"}), use_container_width=True)

    # 4. خلاصة الباحث (Export Section)
    st.markdown("---")
    avg_total = sum(bridge_scores) / 6
    st.markdown(f"""
    ### 📝 ملخص الحالة العامة
    بناءً على المعطيات الميدانية، استقر مؤشر التكامل الكلي عند **({avg_total:.2f}/10)**. 
    هذا يشير إلى وجود **{"انقطاع في تدفق القيمة" if avg_total < 5 else "حالة تكامل متوسطة تحتاج لضبط"}**.
    """)
    
    st.download_button(
        label="📥 تصدير التقرير التشخيصي النهائي (CSV)",
        data=df_report.to_csv(index=False).encode('utf-8-sig'),
        file_name='H-SIM_Diagnostic_Report.csv',
        mime='text/csv'
    )

st.sidebar.markdown("---")
st.sidebar.info("تم تطوير هذا النظام كجزء من أبحاث دكتوراه في الإدارة الاستراتيجية - نموذج H-SIM")
