
import streamlit as st
from datetime import date

import database
from content_agent import build_post_prompt

st.set_page_config(
    page_title="BuildMate 🎀",
    page_icon="🎀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# BUILD MATE - DREAMY PINK DESIGN THEME
# ==========================================

st.markdown("""
<style>

/* Dreamy Fairy Decorations — No Castle 🎀 */

.stApp::before {
    content: "♡  ✧  ☁  ⋆  🎀  ✦  ♡";
    position: fixed;
    top: 105px;
    right: 35px;
    font-size: 23px;
    letter-spacing: 12px;
    color: #e8a6c5;
    opacity: 0.55;
    pointer-events: none;
    z-index: 0;
}

.stApp::after {
    content: "✧  ♡  ☁  ⋆  ✨  ♡";
    position: fixed;
    bottom: 35px;
    left: 350px;
    font-size: 21px;
    letter-spacing: 10px;
    color: #d99bc1;
    opacity: 0.45;
    pointer-events: none;
    z-index: 0;
}

/* Soft dreamy cards */
div[data-testid="stMetric"],
div[data-testid="stExpander"] {
    background: rgba(255, 250, 253, 0.88);
    border: 1px solid #f3d5e5;
    border-radius: 20px;
    box-shadow: 0 5px 18px rgba(210, 145, 180, 0.08);
}

/* Cute buttons */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(120deg, #edb0cd, #dba9e5);
    color: #713d60;
    border: 1px solid #edc5dd;
    border-radius: 15px;
    font-weight: 600;
    transition: 0.25s ease;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: linear-gradient(120deg, #e99fc3, #d49be0);
    color: white;
    border-color: #e7b3d2;
    transform: translateY(-2px);
}
/* Main application background */

/* Decorative floating background elements */



/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #fce5ef 0%,
        #f9eaf5 55%,
        #f5e8f8 100%
    );
    border-right: 1px solid #f2d5e3;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: #70445e;
}

/* Headings */
h1, h2, h3 {
    color: #925575 !important;
    font-weight: 700 !important;
}

/* Paragraphs */
p, label, .stMarkdown {
    color: #60495a;
}

/* Metric cards */

/* Buttons */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(
        135deg,
        #df91b3,
        #c77da4
    );
    color: white !important;
    border: none;
    border-radius: 14px;
    padding: 10px 22px;
    font-weight: 600;
    transition: all 0.2s ease;
    box-shadow: 0 4px 10px rgba(190, 116, 155, 0.16);
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: linear-gradient(
        135deg,
        #cc7fa5,
        #b96b94
    );
    transform: translateY(-2px);
    border: none;
    color: white !important;
}

/* Text inputs */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    background-color: #fffafd;
    border: 1px solid #edccdc;
    border-radius: 12px;
    color: #493744;
}

/* Expanders */
div[data-testid="stExpander"] {
    background: rgba(255, 255, 255, 0.78);
    border: 1px solid #f0d5e2;
    border-radius: 15px;
    margin-bottom: 10px;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
}

.stTabs [data-baseweb="tab"] {
    color: #925575;
    border-radius: 10px;
}

.stTabs [aria-selected="true"] {
    background: #f9dfeb;
    color: #925575 !important;
}

/* Alerts */
div[data-testid="stAlert"] {
    border-radius: 14px;
}
    /* Footer */
.buildmate-footer {
    text-align: center;
    color: #a47b91;
    padding: 20px;
    font-size: 13px;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}
/* Cute BuildMate touches */

.stApp {
    background: linear-gradient(
        135deg,
        #fff7fb 0%,
        #fffafd 45%,
        #f7f1ff 100%
    );
}

/* Soft pastel cards */
div[data-testid="stMetric"],
div[data-testid="stExpander"],
div[data-testid="stForm"] {
    background: rgba(255, 255, 255, 0.82);
    border: 1px solid #f5dce9;
    border-radius: 20px;
    box-shadow: 0 5px 18px rgba(205, 145, 180, 0.10);
    padding: 12px;
}

/* Cute pink buttons */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(110deg, #f5b8d2, #d9b8f4);
    color: #603d58;
    border: none;
    border-radius: 18px;
    font-weight: 600;
    transition: all 0.25s ease;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(204, 135, 180, 0.25);
}


/* Pretty section headings */
h1, h2, h3 {
    color: #925575;
}

/* Dreamy pastel dashboard metric cards */
div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #ffffff, #fff0f7);
    border: 1px solid #f3cde0;
    border-radius: 22px;
    padding: 22px 18px;
    box-shadow: 0 7px 20px rgba(203, 143, 179, 0.13);
    transition: all 0.25s ease;
    min-height: 110px;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 25px rgba(203, 143, 179, 0.22);
}

div[data-testid="stMetricLabel"] {
    color: #a16d8c;
    font-weight: 600;
}

div[data-testid="stMetricValue"] {
    color: #925575;
    font-weight: 700;
}

/* Soft dashboard dividers */
hr {
    border-color: #f2d9e8;
    margin-top: 20px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# Cute application heading
st.markdown("""
<div style="
    background: linear-gradient(120deg, #f8dce9, #fff0f6, #f3e4f5);
    padding: 25px;
    border-radius: 22px;
    border: 1px solid #f1d3e2;
    margin-bottom: 20px;
">
    <h1 style="color:#925575; margin-bottom:5px;">
        🎀 BuildMate ✨
    </h1>
    <p style="color:#946a81; font-size:16px; margin:0;">
        Your little creative corner ☁️ ♡
    </p>
</div>
""", unsafe_allow_html=True)
database.create_tables()

st.sidebar.markdown("""
<div style="text-align:center; padding:15px 5px;">
    <h2 style="color:#925575;">🎀 BuildMate</h2>
    <p style="color:#a47b91;">♡ Your creative workspace ♡</p>
    <p style="color:#c58bb0;">☁️ ✧ ⋆ ୨୧ ⋆ ✧ ☁️</p>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "♡ Choose a section ♡",
    [
        "🏡 Dashboard",
        "☁️ Trending Topics",
        "✨ AI Content Studio",
        "🎀 Create Post",
        "💌 Reply Assistant",
        "📖 Content History"
    ],
    index=[
        "🏡 Dashboard",
        "☁️ Trending Topics",
        "✨ AI Content Studio",
        "🎀 Create Post",
        "💌 Reply Assistant",
        "📖 Content History"
    ].index(st.session_state.get("selected_page", "🏡 Dashboard"))
)
if page == "🏡 Dashboard":
    posts = database.get_posts()
    replies = database.get_replies()

    col1, col2, col3 = st.columns(3)

    col1.metric("Saved Posts", len(posts))
    col2.metric("Saved Replies", len(replies))
    col3.metric("Approval", "Required")

    st.divider()

    st.markdown("""
<div style="
    background: linear-gradient(120deg, #ffe4f0, #f2e5ff, #fff5fa);
    border: 1px solid #f5d2e5;
    border-radius: 25px;
    padding: 28px;
    margin-bottom: 25px;
    box-shadow: 0 6px 20px rgba(200, 140, 180, 0.12);
">
    <div style="font-size: 14px; color: #a56c91;">
        ♡ WELCOME TO YOUR LITTLE CREATIVE WORLD ♡
    </div>
    <h1 style="color: #925575; margin: 12px 0 5px 0;">
        Hello, Shreya! 🎀
    </h1>
    <p style="color: #98758e; font-size: 16px; margin-bottom: 8px;">
        Your ideas deserve a little magic. ✨
    </p>
    <div style="color: #bd8eae; font-size: 19px;">
        ☁️  ♡  ⋆  ✧  ୨୧  ✧  ⋆  ♡
    </div>
</div>
""", unsafe_allow_html=True)
    st.success("Your content workspace is connected to SQLite.")
    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #fff0f7, #f3eaff, #fff8fc);
        border: 1px solid #f1d4e7;
        border-radius: 22px;
        padding: 20px 24px;
        margin: 15px 0 25px 0;
        box-shadow: 0 5px 16px rgba(190, 135, 175, 0.10);
    ">
        <div style="color:#b17b9c; font-size:13px;">
            ✧ YOUR LITTLE DAILY REMINDER ✧
        </div>
        <h3 style="color:#925575; margin:10px 0;">
            Small steps create beautiful things. ♡
        </h3>
        <p style="color:#98758e; margin-bottom:0;">
            Keep learning, keep building, and let your creativity bloom. 🌷
        </p>
    </div>
    """, unsafe_allow_html=True) 
    st.subheader("♡ Quick Actions")

    action1, action2, action3 = st.columns(3)

    with action1:
        if st.button("🎀 Create a Post", use_container_width=True):
            st.session_state["selected_page"] = "🎀 Create Post"
            st.rerun()

    with action2:
        if st.button("💌 Write a Reply", use_container_width=True):
            st.session_state["selected_page"] = "💌 Reply Assistant"
            st.rerun()

    with action3:
        if st.button("☁️ Explore Trends", use_container_width=True):
            st.session_state["selected_page"] = "☁️ Trending Topics"
            st.rerun()
    st.subheader("Today's Content Plan")
    st.write("Date:", date.today())
    st.write("Daily target: 1 post")
    st.write("Platforms: LinkedIn and AWS Builder Center")

    st.info("Every post requires your approval.")
   
elif page == "☁️ Trending Topics":

    st.header("🔥 Trending Technical Topics")

    st.write(
        "BuildMate discovers technical topics from live news feeds."
    )

    if st.button("Discover Latest Topics"):

        with st.spinner("Searching for trending topics..."):

            from trend_agent import discover_trends

            topics = discover_trends(limit=10)

            new_count = sum(
                database.save_topic(topic)
                for topic in topics
            )

        st.success(f"Discovery complete! {new_count} new topics saved.")

    topics = database.get_topics()

    st.subheader("Your Discovered Topics")

    if topics:

        for topic in topics:

            with st.expander(
                f"{topic[2]} | {topic[1]}"
            ):

                st.write("**Headline:**", topic[1])
                st.write("**Category:**", topic[2])
                st.write("**Source:**", topic[3])
                st.write("**Published:**", topic[7])
                st.write("**Relevance score:**", topic[6])

                if topic[5]:
                    st.write("**Summary:**", topic[5])

                if topic[4]:
                    st.markdown(f"[Read original article]({topic[4]})")

    else:
        st.info("No topics found yet. Click Discover Latest Topics.")
  

elif page == "✨ AI Content Studio":

    from content_agent import prepare_content
    from gemini_agent import generate_content

    st.header("🤖 AI Content Studio")

    st.write(
        "BuildMate discovers technical topics and uses "
        "Gemini to create original content."
    )

    topics = database.get_topics()

    if not topics:
        st.warning(
            "No discovered topics available. "
            "Visit Trending Topics first."
        )

    else:
        selected = st.selectbox(
            "♡ Choose a trending topic",
            topics,
            format_func=lambda topic: f"{topic[2]} | {topic[1]}"
        )

        topic_data = {
            "title": selected[1],
            "category": selected[2],
            "source": selected[3],
            "link": selected[4],
            "summary": selected[5]
        }

        plan = prepare_content(topic_data)

        st.subheader("Selected Trending Topic")
        st.write(plan["topic"])

        col1, col2 = st.columns(2)

        col1.metric("Content Format", plan["format"])
        col2.metric("Suggested Platform", plan["platform"])

        if st.button(
            "✨ Generate AI Content",
            type="primary"
        ):
            with st.spinner("Gemini is creating your content..."):
                try:
                    result = generate_content(
                        topic_data,
                        plan["format"],
                        plan["platform"]
                    )

                    st.session_state["generated_content"] = result
                    st.success("Content generated successfully!")

                except Exception as error:
                    st.error(f"Content generation failed: {error}")

        if "generated_content" in st.session_state:

            result = st.session_state["generated_content"]

            st.markdown("""
            <div style="
                background: linear-gradient(120deg, #fff0f7, #f3eaff, #fffafd);
                border: 1px solid #f0d2e5;
                border-radius: 22px;
                padding: 20px 24px;
                margin: 20px 0;
                box-shadow: 0 6px 18px rgba(190, 135, 175, 0.12);
            ">
                <div style="color:#b17b9c; font-size:13px;">
                    ✧ YOUR CREATIVE SPACE ✧
                </div>
                <h3 style="color:#925575; margin:10px 0 5px 0;">
                    Your content is ready! ♡
                </h3>
                <p style="color:#98758e; margin:0;">
                    Review, edit and make it yours before saving.
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.subheader("♡ Generated Content Preview")

            edited_title = st.text_input(
                "Content Title",
                value=result["title"],
                key="generated_title"
            )

            edited_body = st.text_area(
                "Edit Your Content",
                value=result["body"],
                height=350,
                key="generated_body"
            )

            if result["format"] == "Poll":
                st.subheader("Poll Options")

                for index, option in enumerate(
                    result.get("poll_options", []), 1
                ):
                    st.write(f"{index}. {option}")

            st.caption(
                f"Platform: {result['platform']} | "
                f"Format: {result['format']}"
            )

            st.write("Source:", result["source_link"])

            if st.button("Save for Approval", type="primary"):

                final_content = (
                    f"{edited_title}\n\n{edited_body}"
                )

                if result["format"] == "Poll":
                    final_content += "\n\nPoll Options:\n"

                    for index, option in enumerate(
                        result.get("poll_options", []), 1
                    ):
                        final_content += f"{index}. {option}\n"

                database.save_post(
                    result["platform"],
                    topic_data["title"],
                    final_content
                )

                st.success(
                    "Saved successfully! Check Content History "
                    "for your pending content."
                )

                del st.session_state["generated_content"]


elif page == "🎀 Create Post":

    st.header("✍️ AI Post Generator")

    st.write("Prepare your post and save your final draft.")

    with st.form("post_form"):

        platform = st.selectbox(
            "Select platform",
            ["LinkedIn", "AWS Builder Center"]
        )

        topic = st.text_input("What is your post about?")

        tone = st.selectbox(
            "Choose writing tone",
            [
                "Professional and natural",
                "Friendly and conversational",
                "Educational",
                "Thought-provoking"
            ]
        )

        key_points = st.text_area(
            "Important points to include",
            height=100
        )

        call_to_action = st.text_input(
            "Call to action (optional)"
        )

        generate = st.form_submit_button(
            "Prepare Post Instructions"
        )

    if generate:
        if topic.strip():
            st.session_state["post_prompt"] = build_post_prompt(
                platform, topic, tone, key_points, call_to_action
            )
            st.session_state["post_platform"] = platform
            st.session_state["post_topic"] = topic
        else:
            st.warning("Please enter a topic.")

    if "post_prompt" in st.session_state:

        st.subheader("Your Post Instructions")

        st.code(
            st.session_state["post_prompt"],
            language="text"
        )

        st.divider()

        st.subheader("📝 Post Preview")

        post_content = st.text_area(
            "Write or paste your post here",
            height=250,
            key="post_content"
        )

        if st.button("Save Post"):

            if post_content.strip():

                database.save_post(
                    st.session_state["post_platform"],
                    st.session_state["post_topic"],
                    post_content
                )

                st.success("Your post has been saved!")

            else:
                st.warning("Please enter your post first.")


elif page == "💌 Reply Assistant":

    from reply_agent import generate_reply

    st.header("💬 Comment Reply Assistant")

    platform = st.selectbox(
        "Select platform",
        ["LinkedIn", "AWS Builder Center"]
    )

    comment = st.text_area(
        "Paste the original comment",
        height=130
    )

    tone = st.selectbox(
        "Choose reply tone",
        ["Professional", "Friendly", "Appreciative", "Technical"]
    )

    if st.button("✨ Generate AI Reply", type="primary"):

        if comment.strip():

            with st.spinner("Gemini is writing your reply..."):

                try:
                    result = generate_reply(
                        comment,
                        platform,
                        tone
                    )

                    st.session_state["reply_text"] = result
                    st.success("Your AI reply is ready!")

                except Exception as error:
                    st.error(f"Reply generation failed: {error}")

        else:
            st.warning("Please paste the original comment.")

    reply = st.text_area(
        "Review or edit your suggested reply",
        height=150,
        key="reply_text"
    )

    if st.button("💌 Save Reply"):

        if comment.strip() and reply.strip():

            database.save_reply(platform, comment, reply)

            st.success("Your reply has been saved!")

        else:
            st.warning("Please enter both the comment and reply.")

elif page == "📖 Content History":

    st.header("📚 Content History")

    tab1, tab2 = st.tabs(["Posts", "Replies"])

    with tab1:

        posts = database.get_posts()

        if posts:

            for post in posts:

                with st.expander(
                    f"{post[1]} | {post[2]} | {post[4]}"
                ):

                    st.write(post[3])
                    st.caption("Created: " + post[5])

                    if post[4] == "Pending":

                        if st.button(
                            "Approve Post",
                            key=f"approve_{post[0]}"
                        ):

                            database.update_post_status(
                                post[0], "Approved"
                            )

                            st.rerun()

        else:
            st.info("No saved posts yet.")

    with tab2:

        replies = database.get_replies()

        if replies:

            for reply in replies:

                with st.expander(
                    f"{reply[1]} | Reply #{reply[0]}"
                ):

                    st.write("Original comment:")
                    st.write(reply[2])

                    st.write("Suggested reply:")
                    st.write(reply[3])

                    st.caption("Created: " + reply[5])

        else:
            st.info("No saved replies yet.")

st.divider()
st.caption("BuildMate | Built with Python and Streamlit")

# Creator Section 🎀

st.markdown("""
<div style="
    background: linear-gradient(135deg, #fff0f6, #fce4ef, #f5e9fa);
    padding: 25px;
    border-radius: 24px;
    border: 1px solid #f1cddd;
    margin-top: 35px;
    margin-bottom: 20px;
    text-align: center;
">
    <h2 style="color:#925575;">♡ A Little About the Creator ♡</h2>
<p style="color:#a47b91;">
    The creative mind behind BuildMate ✨
</p>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1, 2])

with left:
    st.image(
        "assets/shreya.jpg",
        width=250
    )

with right:
    st.markdown("""
    <div style="
        background: #fffafd;
        padding: 25px;
        border-radius: 22px;
        border: 1px solid #f2d5e3;
    ">
        <h2 style="color:#925575;">Shreya Patel 🎀</h2>
        <h4 style="color:#c27fa1;">Founder & Creator of BuildMate</h4>
        <p style="color:#80677a;">Computer Engineering Student</p>
        <p style="color:#80677a;">
            I built BuildMate as a personal project to explore
            AI, automation, and content creation.
            It's a little space where technology meets creativity.
        </p>
        <p style="color:#d18bad; font-size:25px;">
            ♡ ✧ ୨୧ ☁️ ⋆ ✨ ♡
        </p>
        <p style="color:#a47b91;">
            Dream it. Build it. Keep growing. 💗
        </p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("""
<div style="
    text-align:center;
    padding:18px;
    color:#a47b91;
    font-size:13px;
">
    Made with ♡ and a little magic ✨
    <br>
    BuildMate | Your AI-powered creative workspace ☁️
    <br>
    ♡ ⋆ ✧ ୨୧ ✧ ⋆ ♡
</div>
""", unsafe_allow_html=True)
