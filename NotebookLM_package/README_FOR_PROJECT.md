# Wine Quality Multiple Linear Regression

本專案用 Kaggle 的 Red Wine Quality 資料集完成多元線性回歸作業，依照 CRISP-DM 流程進行資料理解、資料準備、特徵選擇、建模、模型評估與結果呈現。

## 選定資料集

- Kaggle 資料集：Red Wine Quality
- 來源：https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009
- 原始研究資料：UCI Machine Learning Repository / Cortez et al.
- 預測目標：`quality`
- 特徵數：11 個
- 任務類型：回歸預測

## 為什麼選這個資料集

Wine Quality 資料集包含紅酒的化學檢測數值，例如酸度、糖分、氯化物、密度、pH、硫酸鹽與酒精濃度，目標是預測紅酒品質分數。它的輸入特徵共有 11 個，符合本作業要求的 10 至 20 個 features，也很適合展示特徵選擇與線性回歸模型評估。

## 專案檔案

```text
.
├── ASSIGNMENT_REQUIREMENTS.md  # 作業要求整理
├── README.md                   # 專案說明與執行步驟
├── chat.md                     # 與 ChatGPT 的聊天紀錄整理
├── requirements.txt            # Python 套件需求
├── 4112056012_hw2.py           # 分析主程式
├── data/                       # 資料集放置位置
└── outputs/                    # 程式產生的圖表與結果
```

## 執行環境

建議使用 Python 3.10 以上版本。

安裝套件：

```bash
pip install -r requirements.txt
```

執行分析：

```bash
python 4112056012_hw2.py
```

程式會優先讀取：

```text
data/winequality-red.csv
```

如果本機沒有該檔案，程式會嘗試從公開 UCI 資料來源下載相同資料。正式報告仍請標示 Kaggle 連結作為本作業資料集來源。

## 作業完成步驟

1. 到 Kaggle 下載 Red Wine Quality 資料集。
2. 將 `winequality-red.csv` 放到 `data/` 資料夾。
3. 確認主程式檔名為 `4112056012_hw2.py`。
4. 執行 `pip install -r requirements.txt`。
5. 執行 `python 4112056012_hw2.py`。
6. 檢查 `outputs/` 中的模型評估結果與圖片。
7. 依照 CRISP-DM 架構撰寫 PDF 報告。
8. 使用 NotebookLM 研究同主題解法，整理 100 字以上摘要放入報告。
9. 將 `chat.md` 或聊天頁面匯出為 PDF，放入繳交檔案。
10. 將程式、報告 PDF、GPT 對話 PDF、圖片與資料夾壓縮為 `4112056012_hw2.zip`。

## CRISP-DM 報告可寫方向

### Business Understanding

本分析目標是根據紅酒的化學成分預測品質分數，協助了解哪些化學指標可能與品質評分較相關。此任務可協助酒品製造或品質管理人員用量化資料輔助品質判斷。

### Data Understanding

資料集中每筆資料代表一款紅酒樣本，包含 11 個化學特徵與 1 個品質分數。可先檢查資料筆數、欄位型態、遺漏值、敘述統計與特徵相關係數。

### Data Preparation

資料準備包含讀取資料、確認缺失值、切分訓練與測試資料、標準化特徵，以及將 `quality` 作為預測目標。

### Modeling

使用 Linear Regression 建立基準模型，並透過 SelectKBest 挑選與目標較相關的特徵後建立第二個模型，比較特徵選擇前後的效果。

### Evaluation

使用 MAE、RMSE、R2 評估模型表現，並繪製實際值與預測值比較圖。圖中加入預測區間，用來呈現模型預測的不確定性。

### Deployment

本作業的部署方式可設計為簡單的品質預測流程：輸入紅酒化學檢測數值，模型輸出預測品質分數，並提供重要特徵與模型誤差作為決策參考。

## NotebookLM 摘要撰寫提醒

可將 Kaggle 頁面、UCI 資料說明、相關教學文章或論文摘要加入 NotebookLM，請它比較常見解法。報告中需放入 100 字以上摘要，並明確標示「NotebookLM 摘要」。

## GPT 輔助內容

本專案已建立 `chat.md` 用來整理與 ChatGPT 的對話紀錄。最後請將聊天紀錄匯出為 PDF，並在報告中標示「GPT 輔助內容」。
