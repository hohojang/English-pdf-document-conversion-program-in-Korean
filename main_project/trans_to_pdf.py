##import fitz  # PyMuPDF
##import pytesseract
##from googletrans import Translator
##from PIL import Image
##import io
##
### Tesseract OCR 경로 설정 (Tesseract 설치 경로를 정확히 설정)
##pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
##
### PDF 경로
##input_pdf_path = r"C:\Users\dwegw\Documents\stm32\stm32_1.pdf"
##output_pdf_path = r"C:\Users\dwegw\Documents\stm32\stm32_1_translated.pdf"
##
### 번역기 초기화
##translator = Translator()
##
### 원본 PDF 열기
##pdf_document = fitz.open(input_pdf_path)
##
### 번역된 내용을 새 PDF로 저장
##for page_num in range(len(pdf_document)):
##    page = pdf_document[page_num]
##    
##    # 텍스트 추출 시도
##    text = page.get_text("text")  # 페이지의 텍스트 추출
##    
##    if not text.strip():  # 텍스트가 없으면 이미지에서 텍스트 추출 (OCR 사용)
##        # 페이지의 이미지 추출
##        pix = page.get_pixmap()
##        img_data = pix.tobytes("png")  # 이미지를 PNG 형식으로 변환
##        img = Image.open(io.BytesIO(img_data))  # 이미지를 Pillow로 열기
##        text = pytesseract.image_to_string(img)  # OCR로 텍스트 추출
##    
##    if text.strip():  # 텍스트가 있으면 번역 시작
##        translated_text = translator.translate(text, src='en', dest='ko').text
##        # 새로운 텍스트 삽입
##        page.insert_text((72, 72), translated_text, fontsize=11)  # 번역된 텍스트 삽입
##
### 결과 저장
##pdf_document.save(output_pdf_path)
##pdf_document.close()
##
##print(f"번역된 PDF가 {output_pdf_path}에 저장되었습니다.")

import fitz  # PyMuPDF
import pytesseract
from googletrans import Translator
from PIL import Image
import io

# Tesseract OCR 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# PDF 경로
input_pdf_path = r"C:\Users\dwegw\Documents\stm32\stm32_1.pdf"
output_pdf_path = r"C:\Users\dwegw\Documents\stm32\stm32_1_translated.pdf"

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

