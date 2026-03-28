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
# ملاحظة: تم تعديل unsafe_allow_html=True لضمان تحميل التصميم
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        text-align: right;
        background-color: #0d1117; /* Midnight Blue base */
        color: #ffffff;
    }

    .main {
        background-color: #0d1117;
    }

    .stMetric {
        background-color: #1a237e; /* Royal Blue */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        border: 1px solid #ffca28; /* Gold border */
    }

    h1, h2, h3 { 
        color: #ffca28; /* Gold titles */ 
        font-weight: 700; 
    }

    /* تخصيص الأزرار */
    .stButton>button {
        color: #0d1117;
        background-color: #ffca28; /* Gold button */
        border-radius: 20px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #fff8e1;
    }

    /* تحسين القائمة الجانبية */
    .css-163utfM {
        background-color: #1a237e;
        color: #ffffff;
    }
    .stSlider > div > div > div > div {
        color: #ffca28; /* Gold slider handle */
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
        المنظمة ليست أقساماً، بل هي **جسور تدفق**. إذا انكسر جسر واحد (مثل جسر الاستدامة بين النتائج والقدرات)، فإن المنظمة تبدأ في أكل أصولها حتى تنهار.
        هذا التطبيق هو **مشّرطك الجراحي** لتشخيص هذه التدفقات.
        """)
    
    with col2:
        st.info("**مبدأ الهائل:** التكامل ليس خياراً، بل هو قانون البقاء في عصر التحول الرقمي.")
        # يمكن هنا إضافة صورة شعار الإطار لاحقاً
    
    st.success("👈 انتقل الآن إلى تبويب 'لوحة المؤشرات الذكية' للبدء في تشخيص منظمتك.")

# --- التبويب الثاني: لوحة المؤشرات (المحرك الرقمي الكامل) ---
with tabs[1]:
    st.title("📊 لوحة القيادة الرقمية (Digital Dashboard)")
    st.markdown("تحكم في الجسور لمشاهدة تأثير التكامل فورياً.")
    
    # القائمة الجانبية (Sidebar) للمدخلات (6 جسور أساسية - حالة شركة ألفا محملة افتراضياً)
    st.sidebar.header("📥 إدخال قيم الجسور (1-10)")
    st.sidebar.markdown("قم بتحريك المؤشرات بناءً على نتائج الاستبيان الميداني")
    
    v_a = st.sidebar.slider("V -> A (التنفيذ / كفاءة التشغيل)", 0.0, 10.0, 1.95, key='v_a')
    a_v = st.sidebar.slider("A -> V (التميز / القدرة التنافسية)", 0.0, 10.0, 2.13, key='a_v')
    r_a = st.sidebar.slider("R -> A (الاستدامة / إعادة البناء)", 0.0, 10.0, 1.05, key='r_a')
    a_r = st.sidebar.slider("A -> R (الكفاءة / تحويل القدرات)", 0.0, 10.0, 1.75, key='a_r')
    s_v = st.sidebar.slider("S -> V (الملاءمة / دراسة السوق)", 0.0, 10.0, 4.47, key='s_v')
    v_s = st.sidebar.slider("V -> S (التأثير / العلامة التجارية)", 0.0, 10.0, 3.50, key='v_s')

    # --- 1. حساب المؤشرات الأربعة الأساسية ---
    eri = (v_a + a_v) / 2 # جاهزية التنفيذ
    vci = (s_v + a_r) / 2 # اتساق القيمة
    ssi = (r_a + v_s) / 2 # الاستدامة
    iii = (v_a + r_a + a_v + s_v) / 4 # التكامل الداخلي

    indicators = [
        {"label": "جاهزية التنفيذ (ERI)", "value": eri, "info": "شلل تنفيذي" if eri < 3 else "آلية فعالة"},
        {"label": "اتساق القيمة (VCI)", "value": vci, "info": "هدر تشغيلي" if vci < 4 else "قيمة متسقة"},
        {"label": "الاستدامة (SSI)", "value": ssi, "info": "خطر مستقبلي" if ssi < 3 else "نمو مستدام"},
        {"label": "التكامل الداخلي (III)", "value": iii, "info": "قطيعة تنظيمية" if iii < 3 else "تكامل هيكلي"}
    ]

    # رسم العدادات الأربعة في الأعلى (High-contrast gold bars)
    fig_gauges = make_subplots(
        rows=2, cols=2, 
        specs=[[{'type': 'indicator'}]*2]*2, 
        vertical_spacing=0.15,
        horizontal_spacing=0.1
    )

    for i, ind in enumerate(indicators):
        row, col = (i // 2) + 1, (i % 2) + 1
        fig_gauges.add_trace(go.Indicator(
            mode = "gauge+number", 
            value = ind["value"],
            title = {'text': f"<b>{ind['label']}</b><br><span style='font-size:0.8em;color:gray'>{ind['info']}</span>"},
            gauge = {
                'axis': {'range': [0, 10]}, 
                'bar': {'color': "#ffca28"}, # Gold bar
                'steps': [
                    {'range': [0, 3], 'color': "#ff4d4d"}, # Red
                    {'range': [3, 6], 'color': "#ffa64d"}, # Orange
                    {'range': [6, 10], 'color': "#4dff4d"} # Green
                ],
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                    'value': ind["value"]
                }
            }
        ), row=row, col=col)
    
    fig_gauges.update_layout(height=500, margin=dict(t=50, b=50, l=50, r=50), template='plotly_dark')
    st.plotly_chart(fig_gauges, use_container_width=True)

    # --- 2. رادار الاتزان ومصفوفة النزيف (Middle Section) ---
    st.markdown("---")
    col_radar, col_matrix = st.columns([1, 1])

    with col_radar:
        # رسم رادار الاتزان بين الأركان (Pillars Equilibrium)
        st.subheader("🎯 رادار الاتزان بين الأركان (Pillars Equilibrium)")
        
        # حساب قيم الأركان بناءً على التدفقات المباشرة المرتبطة بها (S: Context, V: Value, A: Activities, R: Results)
        s_score = s_v 
        v_score = (v_a + v_s) / 2
        a_score = (a_v + a_r) / 2
        r_score = r_a
        
        pillars_values = [s_score, v_score, a_score, r_score]
        pillars_labels = ['Context (S)', 'Value (V)', 'Activities (A)', 'Results (R)']

        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=pillars_values + [pillars_values[0]],
            theta=pillars_labels + [pillars_labels[0]],
            fill='toself',
            name='الاتزان الاستراتيجي',
            line_color='#ffca28', # Gold line
            fillcolor='rgba(26, 35, 126, 0.5)' # Translucent Royal Blue fill
        ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 10], color="white", font=dict(size=10)),
                angularaxis=dict(color="white")
            ),
            showlegend=False,
            template='plotly_dark',
            margin=dict(t=50, b=50)
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    with col_matrix:
        # رسم مصفوفة النزيف الحرارية (H-SIM Heatmap Matrix)
        st.subheader("🌡️ مصفوفة النزيف الحرارية (H-SIM Matrix)")
        st.markdown("الخلايا الحمراء والبرتقالية تشير لفجوات التدفق.")

        # تجهيز مصفوفة 4x4 (S, V, A, R) وتعبئة قيم الجسور الأساسية
        # mapping indices: S=0, V=1, A=2, R=3
        matrix_data = np.zeros((4, 4))
        # Filling specific bridge values from sliders (normalize to 1-10)
        matrix_data[0, 1] = s_v  # S->V
        matrix_data[1, 2] = v_a  # V->A
        matrix_data[2, 3] = a_r  # A->R
        matrix_data[3, 2] = r_a  # R->A
        matrix_data[2, 1] = a_v  # A->V
        matrix_data[1, 0] = v_s  # V->S
        # Diagonals set to 10 for self-alignment
        np.fill_diagonal(matrix_data, 10)

        matrix_df = pd.DataFrame(matrix_data, columns=['S', 'V', 'A', 'R'], index=['S', 'V', 'A', 'R'])

        fig_heatmap = px.imshow(
            matrix_df,
            labels=dict(x="إلى الركن", y="من الركن", color="كفاءة الجسر"),
            x=['S', 'V', 'A', 'R'],
            y=['S', 'V', 'A', 'R'],
            color_continuous_scale='RdYlGn', # Red-Yellow-Green gradient
            zmin=0, zmax=10,
            text_auto='.1f' # Display values on grid
        )
        
        fig_heatmap.update_layout(
            template='plotly_dark',
            xaxis=dict(tickfont=dict(color='white')),
            yaxis=dict(tickfont=dict(color='white')),
            margin=dict(t=50, b=50)
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)

    # --- 3. التفسير النوعي الآلي وتحميل البيانات (Bottom Section) ---
    st.markdown("---")
    st.subheader("📝 التفسير النوعي الآلي (Automated Diagnostic)")

    col_diagnostic, col_export = st.columns([2, 1])

    with col_diagnostic:
        # توليد نصوص تفسيرية بناءً على المؤشرات
        diagnostic_text = ""
        avg_score = (eri + vci + ssi + iii) / 4
        
        if avg_score < 4:
            st.error(f"مؤشر الهائل الكلي: {avg_score:.2f} - المنظمة في مرحلة 'النزيف الاستراتيجي'. مطلوب تدخل جراحي لإعادة بناء الجسور.")
            if eri < 3: st.warning("جاهزية التنفيذ (ERI) حرجة جداً: المنظمة عاجزة عن تحويل القيمة الوعود إلى واقع.")
            if ssi < 3: st.warning("الاستدامة (SSI) حرجة: النزيف في جسر R->A يهدد مأسسة النتائج المستقبلية.")
        elif avg_score < 7:
            st.warning(f"مؤشر الهائل الكلي: {avg_score:.2f} - المنظمة في مرحلة 'الهشاشة'. التكامل يحتاج إلى مأسسة.")
        else:
            st.success(f"مؤشر الهائل الكلي: {avg_score:.2f} - المنظمة في حالة 'تكامل صحي'.")

    with col_export:
        # تجميع البيانات للتصدير
        export_data = {
            "مؤشر": indicators[0]['label'] + "، " + indicators[1]['label'] + "، " + indicators[2]['label'] + "، " + indicators[3]['label'] + "، " + "مؤشر الهائل الكلي",
            "القيمة": [eri, vci, ssi, iii, avg_score]
        }
        export_df = pd.DataFrame(export_data)
        
        st.markdown("#### تصدير النتائج")
        st.download_button(
            label="📥 تحميل تقرير البيانات (CSV)",
            data=export_df.to_csv(index=False).encode('utf-8-sig'),
            file_name='h_sim_results.csv',
            mime='text/csv'
        )

# ملاحظة: يمكنك تعليق هذا الجزء في حالة الرفع على GitHub لتجنب رسائل التشغيل
st.sidebar.markdown("---")
st.sidebar.success("✅ بيانات شركة ألفا محملة افتراضياً للتشخيص.")
