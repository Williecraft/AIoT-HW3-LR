# AIoT HW3 / HW2 Linear Regression 作業要求整理

## 1. 作業目標

本次作業要使用實際資料集完成「多元線性回歸 (Multiple Linear Regression)」分析，並依照 CRISP-DM 流程整理從資料理解、資料準備、建模到評估的完整過程。

## 2. 資料集要求

- 來源：Kaggle 公開資料集
- 特徵數：10 至 20 個 features
- 類型不限，可選房價、醫療、車輛效能、品質預測等主題
- 報告中必須明確標示：
  - 資料集名稱
  - Kaggle 來源
  - 資料集連結
  - 預測目標欄位

## 3. 分析任務要求

- 使用 Linear Regression 進行預測
- 可使用：
  - Simple Linear Regression
  - Multiple Linear Regression
  - Auto Regression
- 必須包含：
  - Feature Selection
  - Model Evaluation
  - 預測結果圖
  - 信賴區間或預測區間

## 4. CRISP-DM 報告架構

報告需依照以下六個階段撰寫：

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

## 5. AI 協助要求

- 所有與 ChatGPT 的對話需匯出成 PDF，可使用 pdfCrowd 或其他工具
- 必須使用 NotebookLM 研究網路上同主題解法
- 報告中需包含 100 字以上的 NotebookLM 摘要
- 報告中需明確標示：
  - GPT 輔助內容
  - NotebookLM 摘要

## 6. 繳交內容

建議繳交壓縮檔名稱：

```text
4112056012_hw2.zip
```

壓縮檔中建議包含：

- `4112056012_hw2.py` 或 `4112056012_hw2.ipynb`
- PDF 報告
- GPT 對話 PDF
- NotebookLM 摘要
- 分析輸出圖片與模型評估結果
- 若使用 GitHub 或 Colab，需附連結與 `README.md`

## 7. 評分標準

### 文件說明 50%

- CRISP-DM 流程完整且邏輯清楚：25%
- 包含 GPT 對話與 NotebookLM 摘要：15%
- 有明確說明資料集來源與研究脈絡：10%

### 結果呈現 50%

- 模型正確可執行，具特徵選擇與評估：25%
- 結果合理、美觀且具有說服力：15%
- 呈現 Kaggle 名次或預測結果評估，例如預測圖、評估指標：10%

## 8. 本專案選定資料集

- 資料集：Red Wine Quality
- 類型：回歸分析
- 特徵數：11 個輸入特徵
- 預測目標：`quality`
- Kaggle 連結：https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009
- 選擇理由：特徵數符合 10 至 20 個 features 的要求，目標欄位可作為連續數值進行線性回歸，且資料欄位清楚，適合用 CRISP-DM 流程完整說明。
