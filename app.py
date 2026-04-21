import streamlit as st
import google.generativeai as genai



st.set_page_config(
    page_title="Văn Học Trẻ - Lập Dàn Ý Pro",
    page_icon="🌸",
    layout="wide"
)

# 2. CSS Tinh chỉnh độ tương phản (Hết chá mắt)
st.markdown("""
    <style>
    /* Nền hồng nhạt dịu mắt */
    .stApp {
        background-color: #fff0f3;
    }
    
    /* Tiêu đề chính đậm đà */
    .main-title {
        color: #880e4f;
        text-align: center;
        font-family: 'Lexend', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.05);
    }

    /* Chỉnh chữ tiêu đề phụ (Nhập đề bài, Ngữ liệu) thành màu đậm hẳn */
    h3 {
        color: #4a001f !important; /* Màu mận cực đậm */
        font-weight: bold !important;
        font-size: 1.5rem !important;
        margin-bottom: 5px !important;
    }
    
    /* Chỉnh màu chữ hướng dẫn */
    p, span, label {
        color: #2d2d2d !important; /* Màu xám đen than, cực kỳ rõ */
        font-weight: 500 !important;
    }

    /* Làm nổi bật ô nhập liệu */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 15px !important;
        border: 2px solid #ad1457 !important;
        background-color: #ffffff !important;
        color: #000000 !important;
        font-size: 1.1rem !important;
    }

    /* Nút bấm Gradient Hồng Đậm */
    .stButton>button {
        background: linear-gradient(90deg, #d81b60, #ad1457) !important;
        color: white !important;
        border-radius: 30px !important;
        border: none !important;
        padding: 1rem !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(173, 20, 87, 0.3);
    }
    
    /* Khung kết quả */
    .result-card {
        background-color: white;
        padding: 30px;
        border-radius: 25px;
        border-left: 10px solid #ad1457;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        color: #1a1a1a;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #880e4f;'>📚 Góc Sáng Tạo</h2>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/5903/5903939.png", width=120)
    st.divider()
    st.markdown("✨ **Thành viên:** Khang - Sư phạm Ngữ văn")
    # Khang có thể đổi tên model ở đây nếu muốn hiện trên giao diện cho đúng
    st.markdown("🖍️ **Công cụ:** Gemini AI")
    st.image("https://cdn-icons-png.flaticon.com/512/2641/2641409.png", width=80)

# 4. Giao diện chính
st.markdown('<h1 class="main-title">🌸 TRÌNH LẬP DÀN Ý VĂN HỌC 🌸</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1rem; margin-bottom: 30px;'>Nơi biến ngữ liệu thành những ý tưởng tuyệt vời</p>", unsafe_allow_html=True)

try:
    if "GEMINI_API_KEY" not in st.secrets:
        st.error("Khang ơi, bạn quên dán API Key vào Secrets rồi!")
    else:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        
        # MẸO: Nếu bản 2.5 hết lượt, hãy sửa dòng dưới thành 'gemini-1.5-flash'
        model = genai.GenerativeModel('gemini-2.5-flash')

        col1, col2 = st.columns([1, 1], gap="large")

        with col1:
            st.markdown("### 🖋️ Nhập Đề Bài")
            topic = st.text_input("Đề bài văn:", placeholder="Ví dụ: Phân tích khổ thơ đầu bài Tràng Giang...", label_visibility="collapsed")
            
            st.markdown("### 📖 Cung Cấp Ngữ Liệu")
            context = st.text_area("Đoạn trích/Ngữ liệu:", height=300, placeholder="Dán đoạn văn hoặc bài thơ vào đây...", label_visibility="collapsed")

        with col2:
            st.markdown("### 🚀 Phân Tích & Lập Dàn Ý")
            st.write("Dàn ý chi tiết sẽ giúp bạn viết bài mạch lạc và sâu sắc hơn.")
            
            if st.button("💝 Bắt Đầu Lập Dàn Ý"):
                if topic and context:
                    with st.spinner('💖 AI đang tập trung đọc hiểu ngữ liệu...'):
                        prompt = f"""
                        Bạn là một giáo viên dạy văn giỏi. Hãy phân tích ngữ liệu sau và lập dàn ý chi tiết cho đề bài.
                        Đề bài: {topic}
                        Ngữ liệu: {context}
                        
                        Yêu cầu trình bày dàn ý:
                        1. Mở bài: Dẫn dắt hấp dẫn.
                        2. Thân bài: Chia luận điểm rõ ràng, trích dẫn đúng ngữ liệu.
                        3. Đánh giá nghệ thuật đặc sắc.
                        4. Kết bài: Tổng kết ý nghĩa.
                        Hãy dùng emoji sinh động.
                        """
                        response = model.generate_content(prompt)
                        st.success("Xong rồi nè Khang ơi! ✨")
                        st.markdown(f'<div class="result-card">{response.text}</div>', unsafe_allow_html=True)
                        st.balloons()
                else:
                    st.warning("Bạn điền thiếu thông tin kìa, kiểm tra lại nhé! 🌸")

except Exception as e:
    st.error(f"Hệ thống đang bảo trì hoặc hết lượt dùng: {e}")
