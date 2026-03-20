# 📚 Kitapyurdu Weekly Best Sellers Scraper
A high-performance Python web scraper designed to extract weekly best-selling book data from Kitapyurdu. It automates the data collection process and formats it for business analysis or personal tracking.

## 🚀 Key Features
* **Multi-page Scraping:** Automatically crawls through multiple pages of best-seller lists (e.g., Pages 1 to 5).
* **Data Cleansing:** Uses advanced string processing to ensure clean, whitespace-free data.
* **Excel-Ready Output:** Generates a professional `.csv` file with `utf-8-sig` encoding for perfect character display in Excel.
* **Bot Protection Awareness:** Includes custom `User-Agent` headers to ensure stable and reliable requests.

## 📸 Visual Demo (Terminal Output)
The scraper processes pages in real-time, extracting titles and prices as shown below:

| Page 1 Extraction Progress | Page 5 Extraction Progress |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/5b3e04ce-f63b-45cf-959b-f875b51804db" width="400" /> | <img src="https://github.com/user-attachments/assets/da812795-f972-422e-b222-e66079e1d830" width="400" /> |

## 🛠️ Installation & Usage
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/casper3773/Python-book-scraping.git](https://github.com/casper3773/Python-book-scraping.git)
    cd Python-book-scraping
    ```
2.  **Install dependencies:**
    ```bash
    pip install requests beautifulsoup4
    ```
3.  **Run the script:**
    ```bash
    python Python-book-scraping.py
    ```

## 📜 License
This project is licensed under the MIT License.
