# 4112056012 多元線性回歸分析報告草稿

## 一、資料集來源

本作業選用 Kaggle 上的 Red Wine Quality 資料集。

- 資料集名稱：Red Wine Quality
- Kaggle 來源：https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009
- 分析任務：使用紅酒的化學檢測數值預測品質分數 `quality`
- 特徵數：11 個
- 目標欄位：`quality`
- 模型類型：多元線性回歸

選擇此資料集的原因是它具有 11 個輸入特徵，符合本作業要求的 10 至 20 個 features，且目標欄位 `quality` 可以作為數值型預測目標，適合使用線性回歸進行分析。

## 二、CRISP-DM 分析流程

### 1. Business Understanding

本分析的目標是根據紅酒的化學成分預測品質分數。紅酒品質通常受到酸度、酒精濃度、硫酸鹽、密度等因素影響，若能透過模型找出與品質較相關的特徵，便可協助品質管理人員進行初步判斷。此分析不取代專業品酒評分，而是提供一個以數據為基礎的輔助評估方式。

### 2. Data Understanding

資料集共有 1599 筆資料與 12 個欄位，其中 11 個欄位為輸入特徵，1 個欄位為預測目標 `quality`。輸入特徵包含固定酸度、揮發性酸度、檸檬酸、殘糖、氯化物、游離二氧化硫、總二氧化硫、密度、pH、硫酸鹽與酒精濃度。

程式檢查後發現各欄位沒有缺失值，因此不需要額外進行遺漏值補值。另透過相關係數熱圖觀察各特徵與品質分數之間的關係，作為後續特徵選擇的參考。

### 3. Data Preparation

資料準備包含以下步驟：

1. 讀取 `winequality-red.csv`
2. 確認資料欄位與缺失值
3. 將 `quality` 設為預測目標
4. 將其餘 11 個欄位設為輸入特徵
5. 使用 train-test split 切分訓練集與測試集
6. 使用 StandardScaler 進行特徵標準化

資料切分使用 80% 作為訓練資料，20% 作為測試資料，並設定固定 random state 以確保結果可重現。

### 4. Modeling

本作業建立兩個線性回歸模型進行比較：

第一個模型使用全部 11 個特徵建立 Linear Regression，作為基準模型。

第二個模型使用 SelectKBest 搭配 `f_regression` 進行特徵選擇，挑選前 8 個與目標變數較相關的特徵，再建立 Linear Regression 模型。

SelectKBest 選出的 8 個特徵如下：

```text
fixed acidity
volatile acidity
citric acid
chlorides
total sulfur dioxide
density
sulphates
alcohol
```

### 5. Evaluation

本作業使用 MAE、RMSE 與 R2 評估模型表現。

| Model | MAE | RMSE | R2 |
|---|---:|---:|---:|
| Linear Regression - all features | 0.5035 | 0.6245 | 0.4032 |
| Linear Regression - top 8 selected features | 0.5062 | 0.6265 | 0.3993 |

從結果可以看出，使用全部特徵的模型 R2 約為 0.4032，略高於特徵選擇後的模型。這表示在本次資料切分與模型設定下，全部特徵模型的解釋能力稍好。不過兩者差距不大，代表特徵選擇後仍能保留大部分預測能力，且模型更簡潔。

本作業也輸出實際值與預測值比較圖，並加入約 95% 預測區間，用來呈現模型預測的不確定性。相關圖片位於 `outputs/` 資料夾。

### 6. Deployment

若要將此模型應用於實際情境，可設計為一個紅酒品質預測流程。使用者輸入紅酒的化學檢測數值後，模型輸出預測品質分數，並搭配模型誤差與預測區間提供參考。實務上仍建議搭配人工品評與更多非化學特徵，例如產地、年份、釀造方式等資料，以提升判斷準確度。

## 三、GPT 輔助內容

本作業使用 ChatGPT / Codex 協助閱讀作業說明、整理作業需求、建立 README、建立 Python 分析程式、選擇 Kaggle 資料集，以及產生初步報告草稿。

聊天紀錄已整理於 `chat.md`。正式繳交前需將聊天紀錄匯出成 PDF，並與報告一同繳交。

## 四、NotebookLM 摘要

此段需由使用者將 Kaggle 資料集頁面、UCI 資料說明、相關 Wine Quality 線性回歸教學或研究文章加入 NotebookLM 後，整理 100 字以上摘要。

可參考撰寫方向：

```text
NotebookLM 摘要：
透過 NotebookLM 整理 Wine Quality 資料集相關資料後，可以發現多數解法會先進行資料探索、相關係數分析與特徵標準化，再使用線性回歸、決策樹、隨機森林或其他機器學習方法預測品質分數。由於 wine quality 的評分帶有主觀性，單純線性模型通常只能解釋部分變異，因此 R2 不會特別高。常見重要特徵包含 alcohol、volatile acidity、sulphates 與 citric acid，其中 alcohol 通常與品質呈正相關，而 volatile acidity 通常與品質呈負相關。相較於複雜模型，線性回歸的優點是容易解釋，適合用來理解各化學特徵與品質之間的基本關係。
```

正式繳交時，請將上方內容改成你自己用 NotebookLM 產生與整理後的摘要。

## 五、網路主流或更優解法比較

Wine Quality 資料集在網路上的常見解法除了 Linear Regression，也常使用 Random Forest、Gradient Boosting、XGBoost 或分類模型。若將 `quality` 視為連續數值，適合使用回歸模型；若將品質分成低、中、高等級，也可轉為分類問題。

相較於線性回歸，Random Forest 或 Gradient Boosting 通常能捕捉非線性關係，因此預測表現可能更好。不過本作業重點是多元線性回歸與 CRISP-DM 流程，因此選擇 Linear Regression 作為主要模型，並用特徵選擇與預測區間強化分析完整性。

## 六、輸出檔案

程式執行後產生以下輸出：

```text
outputs/model_metrics.csv
outputs/selected_features.csv
outputs/correlation_heatmap.png
outputs/selected_features.png
outputs/prediction_interval_all_features.png
outputs/prediction_interval_selected_features.png
```

這些結果可放入 PDF 報告中作為圖表與模型評估依據。
