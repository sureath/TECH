import streamlit as st
import os

# إعداد الصفحة
st.set_page_config(page_title="تحوّل ذكي... بخطوة وعي", layout="wide")

# بيانات الجلسة
if "scores" not in st.session_state:
    st.session_state.scores = {"before": [], "after": []}

# ==============================
# واجهة البداية
# ==============================
st.title("تحوّل ذكي... بخطوة وعي")

st.markdown("""
مرحبًا بك في تجربة الفرق بعينك 💡  
من خلال استفتاء أجريناه، اكتشفنا أن أغلب الناس يعتمدون على الذكاء الاصطناعي في مهامهم اليومية.
تحديدا :

CHATGPT  
ومن هنا انطلقت مبادرتنا: تحوّل ذكي... بخطوة وعي.  
جرّب بنفسك الفرق بين الطريقة التقليدية والطريقة الذكية، وشوف بنفسك كيف التقنية تغيّر تجربتك! 👇
""")

st.markdown("---")

# اختيار المهمة
task = st.selectbox("اختر المجال الذي ترغب بتجربته:",
                    ["🎨 التصميم", "✈ الحجز الذكي", "💻 البرمجة والتعليم"])

# ==============================
# 🎨 التصميم
# ==============================
if task == "🎨 التصميم":
    st.subheader("🎨 التصميم الذكي")

    st.markdown("""
    🎬 السيناريو قبل التقنية:  
    كم مرة كانت عندك فكرة تصميم، لكن ضيّعت وقتك في تنسيق الألوان أو ترتيب العناصر؟ 😩  
    يلا، صمّم بوستر بسيط بالطريقة التقليدية — اختر الألوان والنصوص بنفسك.
    """)

    before_time = st.slider("⏱ كم أخذ منك وقت التصميم؟", 1, 5, 3)
    before_diff = st.slider("😓 ما مدى الصعوبة؟", 1, 5, 3)
    st.session_state.scores["before"] = [before_time, before_diff]

    st.markdown("---")
    st.markdown("### 🤖 *الطريقة الذكية:*")
    st.markdown("""
    استخدم أدوات الذكاء الاصطناعي داخل 
     CHATGPT
    Canva Magic Design أو *Figma AI*،  
    واكتشف كيف تقدر تنشئ تصميم احترافي خلال دقائق فقط!
    """)

    video_file = st.file_uploader("🎥 الفيديو التعريفي للطريقة الذكية:", type=["mp4", "mov", "avi"])
    if video_file:
        st.video(video_file)

    st.markdown("""
    🔗 المصادر الموثوقة:  
    """)

    after_time = st.slider("⏱ كم أخذ منك وقتك بعد استخدام التقنية؟", 1, 5, 2)
    after_diff = st.slider("😄 ما مدى السهولة؟", 1, 5, 2)
    st.session_state.scores["after"] = [after_time, after_diff]

    st.success("💬 الحكمة: التقنية ما تصمم عنك، لكنها توسّع لك أفق الإبداع.")

# ==============================
# ✈ الحجز الذكي
# ==============================
elif task == "✈ الحجز الذكي":
    st.subheader("✈ الحجز الذكي")

    st.markdown("""
    🎬 السيناريو قبل التقنية:  
    جاك إشعار لاجتماع طارئ في الرياض 😱  
    تبدأ تدور بين مواقع الطيران والفنادق... وتضيع وقتك بين الأسعار والخيارات.  
    """)

    before_time = st.slider("⏱ كم استغرق منك البحث؟", 1, 5, 4)
    before_diff = st.slider("😩 ما مدى صعوبته؟", 1, 5, 4)
    st.session_state.scores["before"] = [before_time, before_diff]

    st.markdown("---")
    st.markdown("### 🤖 *الطريقة الذكية:*")
    st.markdown("""
    مع
     ChatGPT Booking & *AI Agent Mode*،  
    تقدر تحجز الرحلة والفندق بخطوة وحدة ✈🏨  
    بس اكتب طلبك وخل الذكاء الاصطناعي يسوي الباقي!
    """)

    video_file = st.file_uploader("🎥الفيديو التعريفي للطريقة الذكية:", type=["mp4", "mov", "avi"])
    if video_file:
        st.video(video_file)

    st.write("🔗 *المصادر الموثوقة:*")
    after_time = st.slider("⏱ كم أخذ منك وقتك بعد التقنية؟", 1, 5, 1)
    after_diff = st.slider("😄 ما مدى السهولة؟", 1, 5, 1)
    st.session_state.scores["after"] = [after_time, after_diff]

    st.warning("🚨 تذكير: لا تدخل بياناتك الشخصية أثناء التجربة.")
    st.success("💭 الحكمة: التقنية تختصر وقتك، لكن وعيك يحافظ على أمانك.")

# ==============================
# 💻 البرمجة والتعليم
# ==============================
else:
    st.subheader("💻 البرمجة والتعليم")

    st.markdown("""
    🎬 السيناريو قبل التقنية:  
    تحاول تكتب كود بسيط، وتواجه أخطاء غريبة، وتبدأ رحلة البحث في المراجع واليوتيوب 😩  
    جرّب تكتب كود بايثون يطبع الأرقام الزوجية من 1 إلى 20:""")

    st.code("""for i in range(1, 21):\n    if i % 2 == 0:\n        print(i)""", language="python")
    before_time = st.slider("⏱ كم أخذ منك كتابة الكود؟", 1, 5, 4)
    before_diff = st.slider("😓 مدى الصعوبة؟", 1, 5, 4)
    st.session_state.scores["before"] = [before_time, before_diff]

    st.markdown("---")
    st.markdown("### 🤖 *الطريقة الذكية:*")
    st.markdown("""
    الآن مع
     *ChatGPT + Codex*،
      تقدر تتعلم المفهوم  
    وتشوف الخطوات، وتكتب الكود مع الذكاء الاصطناعي،  
    بل وترفعه مباشرة على
     GitHub 
     وتشوف تطورك 👩🏻‍💻✨
    """)

    video_file = st.file_uploader("🎥الفيديو التعريفي للطريقة الذكية:", type=["mp4", "mov", "avi"])
    if video_file:
        st.video(video_file)

    st.success("""
    🚀 أعطيناك الآن الانطلاقة... والبقية عليك!
    تعلم، جرّب، ووسّع أفقك —  
    باقي المشوار بين يديك 👇  
    كمل سلسلة التعلم من هذه المصادر الموثوقة وابدأ رحلتك التقنية بثقة ووعي 🌟
    """)
    st.write("من OpenAI – شرح CodeX")
    st.write("https://youtube.com/playlist?list=PLOXw6I10VTv-IwPfAPgK9F2YQOcgr1N8s&si=b15TV70Wst9Cvzx0")
    st.write("https://youtube.com/playlist?list=PLOXw6I10VTv-ZkTjAFQx8P3i4QurANKyG&si=lyimisjtpGnzF7-q")
    after_time = st.slider("⏱ كم أخذ منك وقتك بعد التقنية؟", 1, 5, 2)
    after_diff = st.slider("😄 مدى السهولة؟", 1, 5, 2)
    st.session_state.scores["after"] = [after_time, after_diff]

    st.success("💎 الحكمة: الكود الجاهز يعلمك، لكن الكود اللي تكتبه بنفسك يثبتك.")

# ==============================
# 👁 المقارنة النهائية
# ==============================
st.markdown("---")
if st.button("👁 شوف الفرق بعينك"):
    before = st.session_state.scores["before"]
    after = st.session_state.scores["after"]

    if before and after:
        time_diff = before[0] - after[0]
        diff_diff = before[1] - after[1]
        improve_t = (time_diff / before[0]) * 100 if before[0] else 0
        improve_d = (diff_diff / before[1]) * 100 if before[1] else 0

        st.subheader("📊 تقرير المقارنة:")
        st.write(f"⏱ الوقت: قبل {before[0]} / بعد {after[0]}")
        st.write(f"⚙ الصعوبة: قبل {before[1]} / بعد {after[1]}")
        st.success(f"🚀 قللت وقتك بنسبة {improve_t:.0f}% وزادت سهولتك بنسبة {improve_d:.0f}% ✨")
        st.markdown("> 👁 التقنية بيدك، لكن الوعي قرارك. شفت الفرق بعينك؟ 💡")
    else:
        st.warning("🔹 أكمل التقييم أولاً قبل عرض المقارنة.")

st.caption("⚠ تجربة توعوية فقط — لا تدخل بيانات حساسة أو خاصة.")
st.caption( "اثير العتيبي  - شيماء الخماش - اميره عبدالله")