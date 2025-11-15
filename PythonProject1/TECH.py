from pathlib import Path
import streamlit as st

# =========================
# إعداد المسارات
# =========================
BASE = Path(__file__).parent

def img(name: str) -> str:
    return str(BASE / "images" / name)

def vid(name: str) -> str:
    return str(BASE / "videos" / name)


# =========================
# إعداد الصفحة العامة
# =========================
st.set_page_config(
    page_title="تحوّل ذكي... بخطوة وعي 💡",
    layout="wide",
    page_icon="💡"
)

if "scores" not in st.session_state:
    st.session_state.scores = {"before": [], "after": []}


# =========================
# الصفحة الافتتاحية
# =========================
st.title("تحوّل ذكي... بخطوة وعي 💡")

st.markdown("""
أجرينا *استبيانًا* لمعرفة مدى اعتماد الناس على الذكاء الاصطناعي في مهامهم اليومية،  
واكتشفنا أن الغالبية يستخدمون أداة:

*ChatGPT* 🤖  

ومن هنا انطلقت مبادرتنا:  
### "تحوّل ذكي... بخطوة وعي"  
لرفع الوعي التقني وتعزيز الاستخدام المسؤول للذكاء الاصطناعي،  
حتى نطوّر مهاراتنا ونحافظ على *خصوصيتنا وأماننا الرقمي*. 🔐
""")

st.markdown("---")

st.markdown("""
كثير من الناس يتفاجؤون بأن معلومات تخصّهم ظهرت على الإنترنت،  
أو حتى في نماذج ذكاء اصطناعي *لكن بهوية مختلفة!* 😯  

> الذكاء الاصطناعي لا يتعمد كشف أسرارك،  
> لكنه يتعلّم من البيانات التي تزوده بها.  

وهنا تأتي أهمية الوعي بكيفية استخدام التقنية بذكاء ومسؤولية. 🌱
""")

st.info("""
🔒 *ابدأ بالخطوة الأهم: الحفاظ على خصوصيتك.*

📌 اتبع هذه الخطوات داخل ChatGPT:

1. افتح  
   *Settings ⚙*
2. اختر  
   *Data Controls*
3. فعّل الخيار  
   *Turn off training on your data*
4. واحذف المحادثات القديمة إن احتوت على بيانات خاصة.

💭 التقنية تساعدك، لكنها لا تحميك إن لم تكن واعيًا.  
*الوعي مسؤوليتك. ✨*
""")

st.markdown("""
<div style="
    background-color:#fff3cd;
    padding:25px;
    border-radius:15px;
    border:2px solid #ffc107;
    font-size:18px;
    line-height:1.9;
    text-align:justify;
    color:#1a1a1a;
">
<b>⚠ البيانات ليست نصوصًا فقط…</b><br><br>

هي صور، ووجوه، وتعبيرات، ومشاعر، ولحظات نشاركها دون أن نشعر بقيمتها.<br>
النماذج الذكية قد تتعلّم من أي محتوى بصري ترفعه — سواء كان صورة شخصية، أو تعبير وجه، أو حتى لقطة عابرة.<br><br>

<b>❗ ما ترفعه اليوم… قد يُعاد تشكيله غدًا.</b><br><br>

ولهذا نؤكد دائمًا:<br>
• دقّق قبل رفع أي صورة.<br>
• تأكد من مصدر الأداة قبل مشاركتك لأي محتوى بصري.<br>
• واعلم أن الوعي هو خط الدفاع الأول قبل التقنية نفسها.
</div>
""", unsafe_allow_html=True)

# فيديو التحذير
st.video(vid("waarr.mp4"))



st.markdown("---")

# =========================
# من تكون؟
# =========================
st.title("من تكون؟ 🤔")
st.markdown("اختر من يمثلك وتعرّف على دورك في عالم التقنية 👇")

col1, col2 = st.columns(2)

with col1:
    st.image(img("home.png"), caption="الرئيسية")
    st.image(img("who.png"), caption="من تكون؟")

with col2:
    st.image(img("teacher.png"), caption="معلم")
    st.markdown("""
    💡 *لو كنت معلمًا* وتبغى تطبّق مفهوم Prompt Engineering  
    فهنا نماذج أسئلة تساعدك تبني محادثات تعليمية فعّالة مع طلابك. 👩🏻‍🏫
    """)
    st.image(img("parental.png"), caption="الرقابة الأبوية")
    st.markdown("""
    🧠 *وإذا كنت أبًا*، فـ ChatGPT قريبًا بيقدّم ميزة  
    Parental Controls لحماية أبنائك وضمان تجربة تعليمية آمنة 🤍
    """)

st.markdown("---")
st.markdown("🌟 *التقنية تصنع الفرق، لكن وعيك هو اللي يصنع الأمان.*")
st.markdown("---")

st.markdown("""
🌐 [زر موقع OpenAI الرسمي للتعرّف أكثر على التحكم بالبيانات](https://openai.com)

🎯 *خلك واعٍ، خلك مطّلع، وابدأ تجربتك التقنية بخطوة وعي.*
""")

# =========================
# زر الانتقال للتجربة
# =========================
if st.button("ابدأ تجربتك الآن 🚀"):
    st.session_state.page = "main"


# =========================
# التجربة التفاعلية
# =========================
if "page" in st.session_state and st.session_state.page == "main":

    st.markdown("---")
    st.title("👁 الفرق بعينك – التقنية بوعي")

    st.markdown("""
    من هنا تبدأ التجربة 👇  
    كل مهمة بتوضح الفرق بين الطريقة *التقليدية* والطريقة *الذكية* باستخدام الذكاء الاصطناعي.
    """)

    task = st.selectbox("اختر المجال الذي ترغب بتجربته:",
                        ["🎨 التصميم", "✈️ الحجز الذكي", "💻 البرمجة والتعليم"])

    # =====================================
    # 🎨 التصميم
    # =====================================
    if task == "🎨 التصميم":
        st.subheader("🎨 التصميم الذكي")
        st.markdown("""
        🎬 *السيناريو قبل التقنية:*  
        كم مرة كانت عندك فكرة تصميم، لكن ضيّعت وقتك في تنسيق الألوان أو ترتيب العناصر؟ 😩  
        """)

        before_time = st.slider("⏱ كم أخذ منك وقت التصميم؟", 1, 5, 3)
        before_diff = st.slider("😓 ما مدى الصعوبة؟", 1, 5, 3)
        st.session_state.scores["before"] = [before_time, before_diff]

        st.markdown("---")
        st.markdown("### 🤖 الطريقة الذكية:")

        st.markdown("""
        استخدم أدوات مثل  
        *Canva Magic Design* و *Figma AI* داخل *ChatGPT*  
    و شوف كيف تقدر تسوي تصميم احترافي خلال دقائق فقط! 🎨✨
        """)

        st.video(vid("DESIGN.mp4"))

        st.markdown("""
        🔗 *المصادر الموثوقة:*  
        - [Canva Magic Design](https://chatgpt.com/apps/canva/)  
        - [Figma AI Overview](https://youtu.be/4bItdPD4c90?si=fiEJ4muSyVsBEOJh)  
        - [Canva Official Video](https://youtu.be/aqeZ2uTIaDQ?si=Rw4pK6zSxNxEC1hr)
        """)

        st.markdown("""
        <div style="background-color:#fff3cd;padding:25px;border-radius:15px;
        border:2px solid #ffc107;font-size:18px;line-height:1.8;text-align:justify;
        color:#000000;font-weight:600;">
        ⚠️ <b>التقنية تساعدك على الإبداع، لكنها لا تصنع بصمتك.</b><br>
        التصميم الواعي هو انعكاس لهويتك وقيمك. ✨
        </div>
        """, unsafe_allow_html=True)


    # =====================================
    # ✈️ الحجز الذكي
    # =====================================
    elif task == "✈️ الحجز الذكي":
        st.subheader("✈️ الحجز الذكي")
        st.markdown("""
        🎬 *السيناريو قبل التقنية:*  
        جاك إشعار لاجتماع طارئ في الرياض 😱  
        تبدأ تدور بين مواقع الطيران والفنادق... وتضيع وقتك بين الأسعار والخيارات.
        """)

        before_time = st.slider("⏱ كم أخذ منك وقت البحث؟", 1, 5, 4)
        before_diff = st.slider("😩 ما مدى الصعوبة؟", 1, 5, 4)
        st.session_state.scores["before"] = [before_time, before_diff]

        st.markdown("---")
        st.markdown("### 🤖 الطريقة الذكية:")

        st.markdown("""
        مع *ChatGPT Booking* و *AI Agent Mode*  
        تقدر تحجز رحلتك وفندقك بخطوة وحدة ✈️🏨  
        فقط اكتب وجهتك والتواريخ وشاهد النتائج فوراً.
        """)

        st.video(vid("TRAVEL.mp4"))

        st.markdown("""
        🔗 *المصادر الموثوقة:*  
        - [OpenAI Travel Use Cases](https://chatgpt.com/features/agent/)  
        - [AI Agent Demo Playlist](https://www.youtube.com/playlist?list=PLOXw6I10VTv_9xLWUFMRDL6DWwVRg0Ts7)
        """)

        st.markdown("""
        <div style="background-color:#fde2e2;padding:25px;border-radius:15px;
        border:2px solid #dc3545;font-size:18px;line-height:1.8;text-align:justify;
        color:#000000;font-weight:600;">
        🚨 <b>التقنية تختصر وقتك، لكنها لا تعفيك من الوعي.</b><br>
        لا تدخل بياناتك الشخصية أو البنكية أثناء استخدام أدوات الذكاء الاصطناعي. 🔒
        </div>
        """, unsafe_allow_html=True)


    # =====================================
    # 💻 البرمجة والتعليم
    # =====================================
    else:
        st.subheader("💻 البرمجة والتعليم")
        st.markdown("""
        🎬 *السيناريو قبل التقنية:*  
        تحاول تكتب كود بسيط وتواجه أخطاء كثيرة،  
        وتبدأ رحلة البحث في المصادر واليوتيوب 😩  
        """)

        st.code("""for i in range(1, 21):\n    if i % 2 == 0:\n        print(i)""", language="python")
        before_time = st.slider("⏱ كم أخذ منك وقت كتابة الكود؟", 1, 5, 4)
        before_diff = st.slider("😓 مدى الصعوبة؟", 1, 5, 4)
        st.session_state.scores["before"] = [before_time, before_diff]

        st.markdown("---")
        st.markdown("### 🤖 الطريقة الذكية:")

        st.markdown("""
        مع *ChatGPT + Codex*  
        تتعلّم المفهوم خطوة بخطوة وتكتب الكود مع الذكاء الاصطناعي،  
        بل وترفعه مباشرة على *GitHub* وتشوف تطوّرك 👩🏻‍💻✨
        """)

        st.video(vid("CODE.mp4"))

        st.subheader(" طالب مدرسة؟")

        st.markdown("""
                🎬 *السيناريو قبل التقنية:*  
                طالب أو طالبة ما يعرف من وين يبدأ في المهارات الرقمية،  
                محتار بين كثرة المصادر وما يدري وش الطريق الصح! 😕
                """)

        st.video(vid("STUDENT.mp4"))

        st.markdown("""
                💡 *الفكرة:*  
                هذا الفيديو يوضح أول خطوة لبناء أساس قوي في المهارات الرقمية،  
                وكيف تبدأ طريقك بثقة ووعي بعيد عن التشتت.  
                """)

        st.markdown("""
        🔗 *المصادر الموثوقة:*  
        - [OpenAI Codex](https://openai.com/codex/)  
        - [Codex Playlist 1](https://youtube.com/playlist?list=PLOXw6I10VTv-ZkTjAFQx8P3i4QurANKyG)  
        - [Codex Playlist 2](https://youtube.com/playlist?list=PLOXw6I10VTv-IwPfAPgK9F2YQOcgr1N8s)
        """)

        st.markdown("""
        <div style="background-color:#dbeafe;padding:25px;border-radius:15px;
        border:2px solid #0d6efd;font-size:18px;line-height:1.8;text-align:justify;
        color:#000000;font-weight:600;">
        💡 <b>التقنية تعلّمك، لكنها لا تفكّر عنك.</b><br>
        االبرمجه الصحيحه هي تكتب الكود بفهمك، ليس ان تنسخه بلا فهم. 👨🏻‍💻
        </div>
        """, unsafe_allow_html=True)

    # =========================
    # رابط الاستبيان
    # =========================
    st.markdown("---")
    st.markdown("""
    📝 **ساعدنا في تطوير التجربة!**  
    نرغب نعرف رأيك واقتراحاتك لتحسين المبادرة عبر هذا الاستبيان:  
    👉 [اضغط هنا لتعبئة الاستبيان](https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=S6tr4uaXVEexY2D4I36FMeRI3aQNAKZEovDgiCxBCUJUOTBEVzBUUVFLUVNNWFNJREo1NjdUTk1UMy4u)
    """)


    # =========================
    # نهاية التجربة 💬
    # =========================
    st.markdown("---")
    st.subheader("🌟 انتهت تجربتك التوعوية!")

    st.markdown("""
    👏 لقد خضت تجربة "تحوّل ذكي بخطوة وعي"،  
    وشاهدت بنفسك كيف يمكن للذكاء الاصطناعي أن يسهل الحياة...  
    لكن التميّز الحقيقي يبدأ عندما تستخدم التقنية بوعي ومسؤولية. 💭  
    """)

    st.markdown("""
    تذكّر دائمًا أن:
    > التقنية وُجدت لتخدم الإنسان،  
    > لكنها لا تُغني عن وعيه، ولا تحلّ محلّ قيمه. 🤍  
    """)

    st.markdown("""
    أكمل رحلتك، وتعلّم أكثر، وكن جزءًا من المستقبل الواعي.  
    وشارِكنا رأيك وساعدنا نطوّر التجربة أكثر 💡👇
    """)

    # زر استبيان جميل منسق
    st.markdown("""
    <div style="text-align:center; margin-top:25px;">
        <a href="https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=S6tr4uaXVEexY2D4I36FMeRI3aQNAKZEovDgiCxBCUJUOTBEVzBUUVFLUVNNWFNJREo1NjdUTk1UMy4u"
        target="_blank"
        style="background-color:#6f42c1;color:white;padding:14px 40px;border-radius:12px;
        text-decoration:none;font-size:18px;font-weight:bold;box-shadow:0px 4px 12px rgba(111,66,193,0.4);">
        ✨ شاركنا رأيك في الاستبيان ✨
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.caption("شكراً لوقتك... ووعيك التقني يصنع الفرق دائمًا 💜")


    st.caption("⚠ تجربة توعوية فقط — لا تدخل بيانات حساسة أو شخصية.")
    st.caption(" أثير العتيبي – شيماء الخماش – أميره عبدالله.")
