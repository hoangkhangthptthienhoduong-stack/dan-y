import streamlit as st
import google.generativeai as genai

# 1. Cấu hình trang - Bỏ Sidebar mặc định bằng cách để layout wide và không dùng sidebar
st.set_page_config(
    page_title="Văn Học Trẻ - Lập Dàn Ý",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed" # Tự động thu gọn thanh bên
)

# 2. CSS Tinh chỉnh giao diện khung trắng, chữ đậm rõ nét
st.markdown("""
    <style>
    /* Ẩn hoàn toàn nút mở Sidebar để giao diện chỉ còn khung trắng */
    [data-testid="stSidebarNav"] {display: none;}
    [data-testid="collapsedControl"] {display: none;}
    
    /* Nền hồng cực nhạt gần như trắng cho trang nhã */
    .stApp {
        background-color: #fffafb;
    }
    
    /* Tiêu đề chính màu mận chín */
    .main-title {
        color: #880e4f;
        text-align: center;
        font-family: 'Lexend', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        margin-top: -50px;
    }

    /* Chữ tiêu đề mục (Nhập đề bài, Ngữ liệu) */
    h3 {
        color: #4a001f !important;
        font-weight: bold !important;
        font-size: 1.6rem !important;
    }
    
    /* Chữ hướng dẫn màu xám đậm */
    p, span, label {
        color: #2d2d2d !important;
        font-weight: 500 !important;
    }

    /* Ô nhập liệu nền trắng viền hồng đậm */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 15px !important;
        border: 2px solid #ad1457 !important;
        background-color: #ffffff !important;
        color: #000000 !important;
        font-size: 1.1rem !important;
    }

    /* Nút bấm Gradient hồng đậm */
    .stButton>button {
        background: linear-gradient(90deg, #d81b60, #ad1457) !important;
        color: white !important;
        border-radius: 30px !important;
        border: none !important;
        padding: 0.8rem !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(173, 20, 87, 0.2);
    }
    
    /* Khung kết quả dàn ý */
    .result-card {
        background-color: white;
        padding: 35px;
        border-radius: 25px;
        border-top: 8px solid #ad1457;
        box-shadow: 0 15px 35px rgba(0,0,0,0.08);
        color: #1a1a1a;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Tiêu đề trang
st.markdown('<h1 class="main-title">🌸 TRÌNH LẬP DÀN Ý VĂN HỌC 🌸</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; margin-bottom: 40px;'>Nơi biến ngữ liệu thành những ý tưởng tuyệt vời</p>", unsafe_allow_html=True)

try:
    if "GEMINI_API_KEY" not in st.secrets:
        st.error("Lỗi: Chưa tìm thấy API Key trong mục Secrets!")
    else:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-2.5-flash')

        # Chia 2 cột cân đối
        col1, col2 = st.columns([1, 1], gap="large")

        with col1:
            st.markdown("### 🖋️ Nhập Đề Bài")
            topic = st.text_input("", placeholder="Nhập đề bài văn tại đây...", label_visibility="collapsed")
            
            st.markdown("### 📖 Cung Cấp Ngữ Liệu")
            context = st.text_area("", height=350, placeholder="Dán đoạn văn hoặc bài thơ vào đây...", label_visibility="collapsed")

        with col2:
            st.markdown("### 🚀 Phân Tích & Lập Dàn Ý")
            st.write("Nhấn nút để AI bắt đầu xây dựng khung bài viết chi tiết cho bạn.")
            
            if st.button("💝 Bắt Đầu Lập Dàn Ý"):
                if topic and context:
                    with st.spinner('💖 AI đang tập trung phân tích...'):
                        prompt = f"""
                        Bạn là giáo viên dạy văn giỏi. Hãy lập dàn ý chi tiết cho đề bài sau dựa trên ngữ liệu được cung cấp.
                        Đề bài: {topic}
                        Ngữ liệu: {context}
                        
                        Dàn ý bao gồm: Mở bài, Thân bài (các luận điểm + dẫn chứng), Nghệ thuật, Kết bài.
                        Sử dụng emoji phù hợp.
                        """
                        response = model.generate_content(prompt)
                        # ĐỔI CÂU THÔNG BÁO THEO Ý KHANG
                        st.success("✅ Đã hoàn tất dàn ý!") 
                        st.markdown(f'<div class="result-card">{response.text}</div>', unsafe_allow_html=True)
                        st.balloons()
                else:
                    st.warning("Khang ơi, nhớ điền đủ thông tin vào 2 ô bên trái nhé! 🌸")

except Exception as e:
    st.error(f"Hệ thống đang bận: {e}")
