# 4112056012 多元線性回歸分析報告草稿

正式版報告已整理於 `4112056012_report.md`。

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

根據 NotebookLM 對於 Kaggle 上的 Red Wine Quality 資料集與相關分析資料的研究整理，本資料集的研究目的在於透過紅酒的化學檢測數值來預測其品質分數，以協助理解哪些化學指標與品質評分最為相關。在特徵重要性的分析中，常見的關鍵特徵包含了酒精濃度 (alcohol)、揮發性酸度 (volatile acidity) 以及硫酸鹽 (sulphates) 等數值。本分析選用線性回歸 (Linear Regression) 作為基準模型，主要是因為其具備高度的可解釋性，能透過相關係數與模型係數直觀地解釋各種化學檢測數值對品質的影響。然而，這類模型在該資料集上的解釋力（R2 值）通常不會太高，主要是因為紅酒品質的分數帶有主觀評分的成分，且可能受到化學數值以外的其他因素影響。雖然單純線性回歸的解釋能力有限，但它為後續應用可能會有更好表現的複雜模型奠定了極佳的評估基礎。

## 五、網路主流或更優解法比較

在 NotebookLM 針對網路上常見的 Wine Quality 類型問題解法整理中，除了線性回歸，資料科學社群最常使用的進階解法包含了 Random Forest、Gradient Boosting 與 XGBoost 等模型。此外，也有許多解法會將原本的數值預測轉換為分類模型，將品質直接區分為低、中、高等級來進行分析。

比較這些方法與線性回歸的差異，線性回歸的優點在於模型極為簡單且可解釋性強，因此非常適合作為預測任務的 baseline。不過，線性回歸的限制在於它難以有效捕捉變數之間複雜的非線性關係。相對地，Tree-based models 的優點就是能妥善處理非線性與特徵之間的交互作用，通常在預測表現上會更為優異。儘管進階模型的準確率可能較高，但考量到本作業的核心重點在於演練多元線性回歸分析並完整落實 CRISP-DM 流程，因此本專案仍維持以 Linear Regression 作為主要模型，並透過特徵選擇與加入預測區間來強化整體分析的完整性與說服力。

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
