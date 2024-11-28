import fitz  # PyMuPDF
import pytesseract
from googletrans import Translator
from PIL import Image
import io

# Tesseract OCR 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# PDF 경로
input_pdf_path = r"C:\Users\dwegw\Documents\stm32\stm32_1.pdf"   ##당신의 pdf 경로로 바꿔야함 
output_pdf_path = r"C:\Users\dwegw\Documents\stm32\stm32_1_translated.pdf" ##번역 후 생성할 pdf 파일의 위치와 이름 지정 

# 번역기 초기화
translator = Translator()

# 원본 PDF 열기
pdf_document = fitz.open(input_pdf_path)

# PDF의 각 페이지 처리
for page_num in range(len(pdf_document)):
    page = pdf_document[page_num]
    
    # 텍스트 추출 시도
    text = page.get_text("text")
    
    if not text.strip():  # 텍스트가 없으면 OCR 사용
        pix = page.get_pixmap()
        img_data = pix.tobytes("png")
        img = Image.open(io.BytesIO(img_data))
        text = pytesseract.image_to_string(img)
    
    if text.strip():
        print(f"Page {page_num + 1} 텍스트 추출 완료: {text[:100]}...")  # 텍스트 확인용 로그
        translated_text = translator.translate(text, src='en', dest='ko').text
        print(f"Page {page_num + 1} 번역 완료: {translated_text[:100]}...")  # 번역 텍스트 확인용 로그
        page.insert_text((72, 72), translated_text, fontsize=11)

# 결과 저장
try:
    pdf_document.save(output_pdf_path)
    print(f"번역된 PDF가 {output_pdf_path}에 저장되었습니다.")
except Exception as e:
    print(f"PDF 저장 오류: {e}")

pdf_document.close()

