# PDF 번역 및 OCR 처리 프로젝트

이 프로젝트는 PDF 파일을 읽고, 텍스트를 추출하여 번역 후 새로운 PDF 파일로 저장하는 Python 스크립트입니다. 텍스트 추출에 실패할 경우, 이미지에서 텍스트를 추출하기 위해 OCR(Optical Character Recognition) 기능을 사용합니다.

## 기능

- PDF 파일에서 텍스트 추출
- 텍스트가 없을 경우 OCR을 사용하여 이미지에서 텍스트 추출
- 추출한 텍스트를 Google Translate API를 이용해 한국어로 번역
- 번역된 텍스트를 원본 PDF에 삽입
- 번역된 PDF 파일 저장

## 요구 사항

이 프로젝트를 실행하려면 다음의 Python 라이브러리를 설치해야 합니다.

- **PyMuPDF**: PDF 파일을 읽고 수정하기 위해 사용됩니다.
- **Pillow**: 이미지 처리 및 OCR을 위한 라이브러리입니다.
- **pytesseract**: OCR 기능을 제공하는 Tesseract를 Python에서 사용할 수 있도록 하는 라이브러리입니다.
- **googletrans**: Google Translate API를 사용하여 텍스트를 번역합니다.

## 설치

프로젝트를 실행하려면 Python 3.x와 함께 필요한 라이브러리를 설치해야 합니다.

### 1. Tesseract OCR 설치

Tesseract OCR은 이미지에서 텍스트를 추출하기 위한 도구입니다. [여기](https://github.com/tesseract-ocr/tesseract)에서 Tesseract OCR을 다운로드하고 설치하십시오. 설치 후, Tesseract 실행 파일의 경로를 `pytesseract.pytesseract.tesseract_cmd`에 설정해야 합니다.

예시:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

필요한 라이브러리 설치
다음 명령어를 사용하여 필요한 라이브러리를 설치하십시오.

bash
코드 복사
pip install PyMuPDF pytesseract googletrans Pillow
사용 방법
Python 스크립트에 필요한 PDF 파일 경로와 저장 경로를 설정합니다.
스크립트를 실행하면 PDF 파일에서 텍스트를 추출하고, 텍스트가 없으면 OCR을 사용하여 텍스트를 추출합니다.
추출한 텍스트를 Google Translate API를 사용해 번역한 후, 번역된 텍스트를 새로운 PDF로 저장합니다.


결과
번역된 PDF 파일은 설정한 output_pdf_path에 저장됩니다.
각 페이지에서 텍스트를 추출하고 번역한 후, 새로운 PDF로 저장됩니다.
주의 사항
PDF 파일이 텍스트로 되어 있지 않고 이미지로 되어 있을 경우, OCR을 사용하여 텍스트를 추출합니다. 이 경우 OCR의 정확도는 이미지의 품질에 따라 달라질 수 있습니다.
번역된 텍스트는 기존 PDF 텍스트와 겹쳐서 삽입됩니다. 페이지 레이아웃에 따라 텍스트가 잘리거나 위치가 이상할 수 있습니다. 이를 개선하려면 텍스트 크기 및 위치 조정을 추가해야 할 수 있습니다.
라이센스
이 프로젝트는 MIT 라이센스 하에 제공됩니다.

go
코드 복사

이 `README.md` 파일은 프로젝트 설명, 설치 방법, 사용 방법 등을 잘 담고 있으며, GitHub 리포지토리에서 쉽게 사용할 수 있습니다.





