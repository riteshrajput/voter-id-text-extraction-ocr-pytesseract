# voter-id-text-extraction

* An implementation to extract info from VoterID image and automatically fetching details from electorial website.
* Electoral website : https://electoralsearch.in/##resultArea

## Getting Started

* Run "TextExtractVoterId.py" to extract information from the Voters ID photo.

* Run "TextProcessing.py" to extract Voter ID information from textfile and obtain json file.

* You will obtain "TextExtract.txt" and "Result.json" from running above two programs.

* Before running the below file, edit the path of tesseract and chromedriver according to your system.

* Run the "ScrapeVoterDetails.py" to scrape the data from website automatically.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.

```bash
pip install numpy
pip install Pillow
pip install selenium
pip install pytesseract
pip install beautifulsoup4
pip install opencv-python
```

## Environment

* Python 3.6

* If you receive an error - "TesseractNotFoundError: tesseract is not installed or it's not in your path"

```
1) Download tesseract and install it. Windows version is available here: "https://github.com/UB-Mannheim/tesseract/wiki"
2) Copy the path of the tesseract install and paste it line of code exact as below.
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## Captcha Solver

* The captcha is solved using [Pytesseract](https://pypi.org/project/pytesseract/). 

<p align="center">
  <img src="README_gif.gif">
</p>

## Contributing
Please open an issue if you have any trouble or to discuss what you would like to change.

## Authors

* [RiteshRajput](https://github.com/riteshrajput/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
