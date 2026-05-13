# 模型結果整理

## 資料集基本資訊

```text
Dataset shape: 1599 rows, 12 columns
Missing values: 0
Input features: 11
Target: quality
```

## 使用的模型

本作業使用 `scikit-learn` 建立 Linear Regression 模型，並比較兩種設定：

1. 使用全部 11 個 features
2. 使用 SelectKBest 選出前 8 個 features

## 模型評估指標

| Model | MAE | RMSE | R2 |
|---|---:|---:|---:|
| Linear Regression - all features | 0.5035 | 0.6245 | 0.4032 |
| Linear Regression - top 8 selected features | 0.5062 | 0.6265 | 0.3993 |

## 特徵選擇結果

SelectKBest 選出的 8 個 features：

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

## 初步解讀

使用全部特徵的 Linear Regression 模型表現略優於特徵選擇後的模型。全部特徵模型的 R2 約為 0.4032，代表模型可以解釋約四成的品質分數變異。由於紅酒品質分數具有主觀評分成分，而且可能受到化學數值以外的因素影響，因此單純線性回歸的解釋能力有限是合理的。

特徵選擇後的模型 R2 約為 0.3993，與全部特徵模型差距很小，表示前 8 個特徵已保留多數預測資訊。這可以在報告中用來說明特徵選擇能讓模型更簡潔，但不一定會提升預測表現。
