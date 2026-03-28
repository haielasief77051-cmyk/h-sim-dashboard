import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(page_title="H-SIM Digital Lab", layout="wide", initial_sidebar_state="expanded")

# تخصيص المظهر عبر CSS بسيط
st.markdown("""
    <style>
    .main { background-color: #fdfdfd; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_type=True)

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
        """)
    
    with col2:
        st.info("**مبدأ الهائل:** التكامل ليس خياراً، بل هو قانون البقاء في عصر التحول الرقمي.")
        # 
    
    st.success("👈 انتقل الآن إلى تبويب 'لوحة المؤشرات الذكية' للبدء في تشخيص منظمتك.")

# --- التبويب الثاني: لوحة المؤشرات (المحرك الرقمي) ---
with tabs[1]:
    st.title("📊 لوحة القيادة الرقمية (Digital Dashboard)")
    
    # القائمة الجانبية (Sidebar) للمدخلات
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
    fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'indicator'}]*2]*2, vertical_spacing=0.15)
    for i, ind in enumerate(indicators):
        row, col = (i // 2) + 1, (i % 2) + 1
        fig.add_trace(go.Indicator(
            mode = "gauge+number", value = ind["value"],
            title = {'text': f"<b>{ind['label']}</b><br><span style='font-size:0.8em;color:gray'>{ind['info']}</span>"},
            gauge = {'axis': {'range': [0, 10]}, 'bar': {'color': "black"},
                     'steps': [{'range': [0, 3], 'color': "#ff4d4d"}, {'range': [3, 6], 'color': "#ffa64d"}, {'range': [6, 10], 'color': "#4dff4d"}]}
        ), row=row, col=col)
    
    fig.update_layout(height=600, margin=dict(t=50, b=50))
    st.plotly_chart(fig, use_container_width=True)